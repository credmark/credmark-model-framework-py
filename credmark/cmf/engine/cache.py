# pylint:disable=too-many-arguments
import hashlib
import logging
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple

from sqlitedict import SqliteDict
from sqlitedict import logger as sqlitedict_logger

sqlitedict_logger.setLevel(logging.ERROR)

import json
import sqlite3
import zlib

from credmark.dto.encoder import json_dumps


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
    return sqlite3.Binary(zlib.compress(json_dumps(obj).encode()))


def my_decode(obj):
    return json.loads(zlib.decompress(bytes(obj)))


class SqliteDB:
    # non-deterministic model results
    exclude_slugs = [
        'rpc.get-latest-blocknumber',
        'chain.get-latest-block',
        'dex.pool-volume-historical',
        'dex.pool-volume',
        'console',
    ]

    _trace = False
    _stats = {'total': 0, 'hit': 0, 'miss': 0, 'exclude': 0, 'new': 0}
    _enabled = True

    def __init__(self, db_uri, tablename, flag='c',
                 db_base_uris: Optional[List[str]] = None, outer_stack=True):
        self._db = SqliteDict(db_uri, outer_stack=outer_stack, flag=flag,
                              autocommit=True, tablename=tablename,
                              encode=my_encode, decode=my_decode)

        if db_base_uris is not None:
            self._db_base = [SqliteDict(db_base_uri, outer_stack=outer_stack, flag='r',
                                        tablename=tablename,
                                        encode=my_encode, decode=my_decode)
                             for db_base_uri in db_base_uris]
        else:
            self._db_base = None

        self._logger = logging.getLogger(self.__class__.__name__)

    def close(self):
        self._db.commit(blocking=False)
        self._db.close()

    def commit(self):
        self._db.commit(blocking=False)

    def __del__(self):
        if self._db.filename != ':memory:':
            self.commit()

    def encode(self, key):
        return hashlib.sha256(key.encode('utf-8')).hexdigest()

    def cache_exclude(self):
        self._stats['exclude'] += 1
        self._stats['total'] += 1

    def cache_hit(self):
        self._stats['hit'] += 1
        self._stats['total'] += 1

    def cache_miss(self):
        self._stats['miss'] += 1
        self._stats['total'] += 1

    def cache_new(self):
        self._stats['new'] += 1
        self._stats['total'] += 1

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    @property
    def enabled(self):
        return self._enabled


class ModelRunCache(SqliteDB):
    def __init__(self, db_uri=':memory:', flag='c',
                 db_base_uris: Optional[List[str]] = None, enabled=True):
        super().__init__(db_uri=db_uri, tablename='model_run_cache',
                         flag=flag, db_base_uris=db_base_uris)
        self._enabled = enabled

    @property
    def stats(self):
        return self._stats

    def __getitem__(self, key):
        try:
            return self._db.__getitem__(key)
        except Exception as _err:
            if self._db_base is None:
                raise _err

            for d in self._db_base:
                try:
                    return d.__getitem__(key)
                except Exception as _err2:
                    pass
            raise _err

    def __setitem__(self, key, value):
        return self._db.__setitem__(key, value)

    def __delitem__(self, key):
        return self._db.__delitem__(key)

    def log_on(self):
        self._trace = True
        self._logger.setLevel(logging.INFO)

    def log_off(self):
        self._trace = False
        self._logger.setLevel(logging.INFO)

    def clear(self, do_clear):
        if do_clear:
            self._db.clear()

    def keys(self):
        yield from self._db.keys()
        if self._db_base is not None:
            for d in self._db_base:
                yield from d.keys()

    def items(self):
        yield from self._db.items()
        if self._db_base is not None:
            for d in self._db_base:
                yield from d.items()

    def __iter__(self):
        yield from self._db.iterkeys()
        if self._db_base is not None:
            for d in self._db_base:
                yield from d.iterkeys()

    def values(self):
        yield from self._db.values()
        if self._db_base is not None:
            for d in self._db_base:
                yield from d.values()

    def __len__(self):
        return (self._db.__len__() +
                (0 if self._db_base is None
                else sum(len(d) for d in self._db_base)))

    def slugs(self,
              is_v: Callable[[Any], bool] = (lambda _: True)
              ) -> Generator[Tuple[str, str, int, str], None, None]:
        for k, v in self._db.items():
            if is_v(v):
                yield (v['slug'], v['version'], v['block_number'], k)

        if self._db_base is not None:
            for d in self._db_base:
                for k, v in d.items():
                    if is_v(v):
                        yield (v['slug'], v['version'], v['block_number'], k)

    def block_numbers(self):
        block_numbers = set()
        for v in self._db.values():
            if v['block_number'] not in block_numbers:
                block_numbers.add(v['block_number'])
                yield v['block_number']

    def slugs_by_block(self, block_numbers: List[int]):
        return self.slugs(is_v=lambda v, block_numbers=block_numbers:
                          v['block_number'] in block_numbers)

    def slugs_by_name(self, slugs: List[str]):
        return self.slugs(is_v=lambda v, slugs=slugs:
                          v['slug'] in slugs)

    def slugs_by_name_block(self, slugs: List[str], block_numbers: List[int]):
        return self.slugs(is_v=lambda v, slugs=slugs, block_numbers=block_numbers:
                          v['slug'] in slugs and v['block_number'] in block_numbers)

    def encode_run_key(self, chain_id, block_number, slug, version, input):
        return super().encode(repr((slug, version, chain_id, block_number, input)))

    def get(self, chain_id, block_number,
            slug, version, input) -> Tuple[Optional[str], Tuple[Dict, Any, Dict]]:
        if not self._enabled:
            return None, ({}, None, {})

        if slug in self.exclude_slugs:
            self.cache_exclude()
            return None, ({}, None, {})

        key = self.encode_run_key(chain_id, block_number, slug, version, input)
        needle = self._db.get(key, None)
        if needle is None:
            if self._db_base is not None:
                for d in self._db_base:
                    needle = d.get(key, None)
                    if needle is not None:
                        break

            if needle is None:
                if self._trace:
                    self._logger.info(f'[{self.__class__.__name__}] Not found: '
                                      f'{chain_id}/{block_number}/{(slug, version)}/[{input}]')
                self.cache_miss()
                return None, ({}, None, {})

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

        return key, (needle['output'],
                     needle.get('errors', None),
                     needle.get('dependencies', {}))

    def put(self, chain_id, block_number, slug, version, input, output, dependencies, errors=None):
        if not self._enabled or slug in self.exclude_slugs:
            return

        key = self.encode_run_key(chain_id, block_number, slug, version, input)
        if key in self._db:
            if self._trace:
                self._logger.info('No case for overwriting cache: '
                                  f'{chain_id}/{block_number}/{(slug, version)}/{input}/'
                                  f'{self._db.filename=}')

        if self._db_base is not None:
            for d in self._db_base:
                if key in d:
                    if self._trace:
                        self._logger.info('No case for overwriting cache: '
                                          f'{chain_id}/{block_number}/{(slug, version)}/{input}/'
                                          f'{self._db.filename=}')

        result = {'chain_id': chain_id, 'block_number': block_number,
                  'slug': slug, 'version': version, 'input': input, 'output': output,
                  'dependencies': dependencies, 'errors': errors}

        if slug != 'contract.metadata':
            if self._trace:
                self._logger.info(result)

        self.cache_new()
        self._db[key] = result

    def get_contract(self, address, chain_id=0):
        return self.get(chain_id, 0,
                        'contract.metadata',
                        None,
                        {"contractAddress": address.lower()})[1][2]
