import hashlib
import logging

from sqlitedict import SqliteDict, logger

logger.setLevel(logging.ERROR)

import json
import sqlite3
import zlib


class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class Cache(Singleton):
    _cache = {}
    _trace = False


class ContractMetaCache(Cache):
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        super().__init__()

    def get(self, chain_id, address):
        if chain_id not in self._cache:
            return False, {}

        needle = self._cache[chain_id].get(address, None)
        if needle is None:
            if self._trace:
                self._logger.info(f'[Cache] Not found meta: {chain_id=}/{address}')
            return False, {}

        if self._trace:
            self._logger.info(f'[Cache] Found meta: {chain_id=}/{address}')
        return True, needle

    def put(self, chain_id, address, meta):
        if chain_id not in self._cache:
            self._cache[chain_id] = {}

        if address not in self._cache[chain_id]:
            block_number = None
            if len(meta['contracts']) > 0:
                block_number = meta['contracts'][0]['block_number']
            self._cache[chain_id][address] = meta
            if self._trace:
                self._logger.info(f'[Cache] Save {chain_id=}/{address} '
                                  f'valid from {block_number}')


def my_encode(obj):
    return sqlite3.Binary(zlib.compress(json.dumps(obj).encode()))


def my_decode(obj):
    return json.loads(zlib.decompress(bytes(obj)))


class SqliteDB:
    def __init__(self, db_uri, tablename, outer_stack=False):
        self._db = SqliteDict(db_uri, outer_stack=outer_stack,
                              autocommit=False, tablename=tablename,
                              encode=my_encode, decode=my_decode)

    def __del__(self):
        self._db.commit()
        self._db.close()

    def encode(self, key):
        return hashlib.sha256(key.encode('utf-8')).hexdigest()


class ModelRunCache(SqliteDB):
    _cache = {}
    _trace = False
    _stats = {'total': 0, 'hit': 0, 'miss': 0, 'exclude': 0}
    _enabled = True
    _commit_freq = 1000

    exclude_slugs = ['rpc.get-latest-blocknumber']

    def __init__(self, db_uri=':memory:'):
        super().__init__(db_uri=db_uri, tablename='model_run_cache')
        self._logger = logging.getLogger(self.__class__.__name__)

    def stats(self):
        return self._stats

    def __del__(self):
        super().__del__()

    def __getitem__(self, key):
        return self._db.__getitem__(key)

    def __setitem__(self, key, value):
        return self._db.__setitem__(key, value)

    def cache_exclude(self):
        self._stats['exclude'] += 1
        self._stats['total'] += 1

    def cache_hit(self):
        self._stats['hit'] += 1
        self._stats['total'] += 1

    def cache_miss(self):
        self._stats['miss'] += 1
        self._stats['total'] += 1

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def keys(self):
        return self._db.keys()

    def items(self):
        return self._db.items()

    def values(self):
        return self._db.values()

    def __len__(self):
        return self._db.__len__()

    def __iter__(self):
        return self._db.iterkeys()

    def slugs(self):
        return [(x['slug'], x['version'], x['block_number'])
                for x in self._db.values()]

    def encode_runkey(self, chain_id, block_number, slug, version, input):
        return super().encode(repr((slug, version, chain_id, block_number, input)))

    def get(self, chain_id, block_number, slug, version, input):
        if not self._enabled:
            return False, {}

        if slug in self.exclude_slugs:
            self.cache_exclude()
            return False, {}

        key = self.encode_runkey(chain_id, block_number, slug, version, input)
        needle = self._db.get(key, None)
        if needle is None:
            if self._trace:
                self._logger.info(f'[{self.__class__.__name__}] Not found: '
                                  f'{chain_id}/{block_number}/{(slug, version)}/[{input}]')
            self.cache_miss()
            return False, {}

        self.cache_hit()
        if self._trace:
            self._logger.info(f'[{self.__class__.__name__}] Found: '
                              f'{chain_id}/{block_number}/{(slug, version)}/{input}'
                              f'={needle}')

        assert needle['chain_id'] == chain_id
        assert needle['block_number'] == block_number
        assert needle['slug'] == slug
        assert needle['version'] == version
        assert needle['input'] == input

        return True, needle['output']

    def put(self, chain_id, block_number, slug, version, input, output):
        if not self._enabled or slug in self.exclude_slugs:
            return

        key = self.encode_runkey(chain_id, block_number, slug, version, input)
        if self._trace and key in self._db:
            self._logger.info(f'[{self.__class__.__name__}] Overwriting existing '
                              f'{chain_id}/{block_number}/{(slug, version)}/{input}')

        result = dict(chain_id=chain_id, block_number=block_number,
                      slug=slug, version=version, input=input, output=output)

        if slug != 'contract.metadata':
            if self._trace:
                self._logger.info(result)

        self._db[key] = result

        if self._stats['miss'] // self._commit_freq == 0:
            self._db.commit()
