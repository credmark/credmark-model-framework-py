import unittest

from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.model.errors import ModelDataError
from credmark.cmf.types import Address, Currency, FiatCurrency, NativeToken, Token
from credmark.cmf.types.data.fiat_currency_data import FIAT_CURRENCY_DATA_BY_ADDRESS, FIAT_CURRENCY_DATA_BY_SYMBOL


class TestCurrency(ModelTestCase):
    def test_run(self):
        names_set = set()
        symbols_set = set()
        addresses_set = set()
        for symbol, fiat_entry in FIAT_CURRENCY_DATA_BY_SYMBOL.items():
            self.assertEqual(symbol, fiat_entry['symbol'])

            self.assertTrue('symbol' in fiat_entry)
            self.assertTrue('name' in fiat_entry)
            self.assertTrue('address' in fiat_entry)

            self.assertTrue(fiat_entry['symbol'] not in symbols_set and
                            symbols_set.add(fiat_entry['symbol']) is None)
            self.assertTrue(fiat_entry['name'] not in names_set and
                            names_set.add(fiat_entry['name']) is None)
            self.assertTrue(fiat_entry['address'] not in addresses_set and
                            addresses_set.add(fiat_entry['address']) is None)

            for fc in (Currency(symbol=symbol),
                       FiatCurrency(symbol=symbol),
                       Currency(address=Address(fiat_entry['address'])),
                       FiatCurrency(address=Address(fiat_entry['address']))):
                self.assertTrue(isinstance(fc, FiatCurrency))
                self.assertEqual(fc.symbol, fiat_entry['symbol'])
                self.assertEqual(fc.name, fiat_entry['name'])
                self.assertEqual(fc.address, Address(fiat_entry['address']))
                self.assertTrue(fc.fiat)

        names_set = set()
        symbols_set = set()
        addresses_set = set()
        for fiat_addr, fiat_entry in FIAT_CURRENCY_DATA_BY_ADDRESS.items():
            self.assertEqual(fiat_addr, fiat_entry['address'])

            self.assertTrue('symbol' in fiat_entry)
            self.assertTrue('name' in fiat_entry)
            self.assertTrue('address' in fiat_entry)

            self.assertTrue(fiat_entry['symbol'] not in symbols_set and
                            symbols_set.add(fiat_entry['symbol']) is None)
            self.assertTrue(fiat_entry['name'] not in names_set and
                            names_set.add(fiat_entry['name']) is None)
            self.assertTrue(fiat_entry['address'] not in addresses_set and
                            addresses_set.add(fiat_entry['address']) is None)

            for fc in (Currency(address=Address(fiat_addr)),
                       FiatCurrency(address=Address(fiat_addr)),
                       Currency(symbol=fiat_entry['symbol']),
                       FiatCurrency(symbol=fiat_entry['symbol'])):
                self.assertTrue(isinstance(fc, FiatCurrency))
                self.assertEqual(fc.symbol, fiat_entry['symbol'])
                self.assertEqual(fc.name, fiat_entry['name'])
                self.assertEqual(fc.address, Address(fiat_entry['address']))
                self.assertTrue(fc.fiat)

        with self.assertRaises(ModelDataError):
            FiatCurrency(address=Address(
                '0x0000000000000000000000000000000000000349'))

        with self.assertRaises(ModelDataError):
            FiatCurrency(symbol='USE', address=Address(
                '0x0000000000000000000000000000000000000348'))

        with self.assertRaises(ModelDataError):
            FiatCurrency(symbol='USE')

        token = Currency(symbol="CMK")
        self.assertTrue(isinstance(token, Token))
        self.assertFalse(isinstance(token, NativeToken))
        self.assertEqual(token.symbol, "CMK")
        self.assertEqual(
            token.address, "0x68CFb82Eacb9f198d508B514d898a403c449533E")
        self.assertEqual(token.name, 'Credmark')
        self.assertFalse(token.fiat)

        btc_token = Currency(symbol='BTC')
        self.assertTrue(isinstance(btc_token, Token))
        self.assertFalse(isinstance(btc_token, NativeToken))
        self.assertEqual(btc_token.symbol, "BTC")
        self.assertEqual(btc_token.address, Address(
            "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"))
        self.assertEqual(btc_token.name, "Bitcoin")
        self.assertFalse(btc_token.fiat)

        native_token = Currency(symbol='ETH')
        self.assertTrue(isinstance(native_token, NativeToken))
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.name, "Ethereum")
        self.assertEqual(native_token.address, Address(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'))
        self.assertFalse(native_token.fiat)

        native_token = NativeToken()
        self.assertTrue(isinstance(native_token, NativeToken))
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.name, "Ethereum")
        self.assertEqual(native_token.address, Address(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'))
        self.assertFalse(native_token.fiat)

        native_token = NativeToken()
        self.assertTrue(isinstance(native_token, NativeToken))
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.name, "Ethereum")
        self.assertEqual(native_token.address, Address(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'))
        self.assertFalse(native_token.fiat)

        native_token = Token(symbol='ETH')
        self.assertTrue(isinstance(native_token, NativeToken))
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.name, "Ethereum")
        self.assertEqual(native_token.address, Address(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'))
        self.assertFalse(native_token.fiat)


if __name__ == '__main__':
    unittest.main()
