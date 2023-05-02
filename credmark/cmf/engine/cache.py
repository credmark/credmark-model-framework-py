# pylint:disable=too-many-arguments

import hashlib
import json
import logging
import sqlite3
import zlib
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple

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
                self._logger.info(
                    f'[Cache] Not found meta: {chain_id=}/{address}')
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

    def __init__(self):
        self._db = {}
        self._logger = logging.getLogger(self.__class__.__name__)

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
    def __init__(self, enabled=True):
        super().__init__()
        self._enabled = enabled

    @property
    def stats(self):
        return self._stats

    def __getitem__(self, key):
        return self._db.__getitem__(key)

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

    def items(self):
        yield from self._db.items()

    def __iter__(self):
        yield from self._db.__iter__()

    def values(self):
        yield from self._db.values()

    def __len__(self):
        return self._db.__len__()

    def slugs(self,
              is_v: Callable[[Any], bool] = (lambda _: True)
              ) -> Generator[Tuple[str, str, int, str], None, None]:
        for k, v in self._db.items():
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
            slug, version, input) -> \
            Tuple[Optional[str], Tuple[Optional[Dict], Optional[Dict], Dict]]:
        if not self._enabled:
            return None, ({}, None, {})

        if slug in self.exclude_slugs:
            self.cache_exclude()
            return None, ({}, None, {})

        key = self.encode_run_key(chain_id, block_number, slug, version, input)
        needle = self._db.get(key, None)
        if needle is None:
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

        output = needle['output']
        errors = needle.get('errors')
        depends = needle.get('dependencies', {})
        return key, (output.copy() if output is not None else None,
                     errors.copy() if errors is not None else None,
                     depends.copy())

    def put(self, chain_id, block_number, slug, version, input, output, dependencies, errors=None):
        if not self._enabled or slug in self.exclude_slugs:
            return

        key = self.encode_run_key(chain_id, block_number, slug, version, input)
        if key in self._db:
            if self._trace:
                self._logger.info('No case for overwriting cache: '
                                  f'{chain_id}/{block_number}/{(slug, version)}/{input}/')

        result = dict(chain_id=chain_id,
                      block_number=block_number,
                      slug=slug,
                      version=version,
                      input=input.copy(),
                      output=output.copy() if output is not None else None,
                      dependencies=dependencies.copy(),
                      errors=errors.copy() if errors is not None else None)

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
