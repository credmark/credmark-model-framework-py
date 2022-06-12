import unittest
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.model.errors import ModelBaseError

from credmark.cmf.types import Token, Address
from credmark.cmf.types.token import NativeToken
from credmark.cmf.types.data.fungible_token_data import (
    FUNGIBLE_TOKEN_DATA_BY_SYMBOL,
    FUNGIBLE_TOKEN_DATA_BY_ADDRESS
)


class TestToken(ModelTestCase):
    def test_run(self):
        with self.assertRaises(ModelBaseError):
            Token()

        with self.assertRaises(ModelBaseError):
            Token(symbol="INVALID_SYMBOL")

        for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items():
            chain_has_native_token = False
            symbols_set = set()
            addresses_set = set()
            names_set = set()

            for token_symbol, token_meta in chain_tokens.items():
                if 'is_native_token' in token_meta and token_meta['is_native_token']:
                    if chain_has_native_token:
                        raise Exception(f'There are >1 native token on {chain_id=}')

                    chain_has_native_token = True
                try:
                    self.assertEqual(token_symbol, token_meta['symbol'])
                    self.assertTrue('symbol' in token_meta)
                    self.assertTrue('decimals' in token_meta)
                    self.assertTrue('name' in token_meta)
                    self.assertTrue('address' in token_meta)
                    self.assertTrue(token_meta['address'] == Address(
                        token_meta['address']).checksum)

                    self.assertTrue(token_meta['symbol'] not in symbols_set)
                    self.assertTrue(token_meta['name'] not in names_set)
                    self.assertTrue(token_meta['address'] not in addresses_set)
                    addresses_set.add(token_meta['address'])
                    names_set.add(token_meta['name'])
                    symbols_set.add(token_meta['symbol'])
                except:
                    print(token_meta)
                    raise

            if not chain_has_native_token:
                raise Exception('There is no native token on {chain_id}')

        for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_ADDRESS.items():
            chain_has_native_token = False
            symbols_set = set()
            addresses_set = set()
            names_set = set()
            for token_address, token_meta in chain_tokens.items():
                if 'is_native_token' in token_meta and token_meta['is_native_token']:
                    if chain_has_native_token:
                        raise Exception(f'There are >1 native token on {chain_id=}')

                    chain_has_native_token = True
                try:
                    self.assertEqual(token_address, token_meta['address'])
                    self.assertTrue('symbol' in token_meta)
                    self.assertTrue('decimals' in token_meta)
                    self.assertTrue('name' in token_meta)
                    self.assertTrue('address' in token_meta)
                    self.assertTrue(token_meta['address'] == Address(
                        token_meta['address']).checksum)

                    self.assertTrue(token_meta['symbol'] not in symbols_set)
                    self.assertTrue(token_meta['name'] not in names_set)
                    self.assertTrue(token_meta['address'] not in addresses_set)
                    addresses_set.add(token_meta['address'])
                    names_set.add(token_meta['name'])
                    symbols_set.add(token_meta['symbol'])
                except:
                    print(token_meta)
                    raise

            if not chain_has_native_token:
                raise Exception('There is no native token on {chain_id}')

        chain_tokens = FUNGIBLE_TOKEN_DATA_BY_SYMBOL['1']
        for token_n, (token_symbol, token_meta) in enumerate(chain_tokens.items()):
            print(f'{token_n+1}/{len(chain_tokens)}: {token_symbol}')
            token = Token(symbol=token_symbol)
            self.assertEqual(token.symbol, token_meta['symbol'])
            self.assertEqual(token.name, token_meta['name'])
            self.assertEqual(token.address, token_meta['address'])
            self.assertEqual(token.decimals, token_meta['decimals'])

        token = Token(symbol="CMK")
        self.assertEqual(token.symbol, "CMK")
        self.assertEqual(token.address, "0x68CFb82Eacb9f198d508B514d898a403c449533E")
        self.assertEqual(token.decimals, 18)
        self.assertEqual(token.total_supply, 100_000_000 * 10**18)

        for native_token in (
            NativeToken(),
            NativeToken(symbol='ETH'),
            NativeToken(symbol='ETH', address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'),
            NativeToken(symbol='ETH', address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeee'),
            NativeToken(address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeEeeee'),
            NativeToken(address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'),
            Token(symbol="ETH", address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeeeeee'),
            Token(symbol="ETH"),
            Token(address='0xeeeeeeeeeeeeeeeeeeeeeeeeeeEeeeeeeeeeeeee')
        ):
            self.assertEqual(native_token.symbol, "ETH")
            self.assertEqual(native_token.name, "Ethereum")
            self.assertEqual(native_token.decimals, 18)


if __name__ == '__main__':
    unittest.main()
