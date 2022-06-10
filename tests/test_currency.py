import unittest
from credmark.cmf.engine.model_unittest import ModelTestCase

from credmark.cmf.types import Currency, FiatCurrency, Address
from credmark.cmf.types.token import NativeToken, Token
from credmark.cmf.types.data.fiat_currency_data import FIAT_CURRENCY_DATA


class TestCurrency(ModelTestCase):
    def test_run(self):
        for symbol, fiat_entry in FIAT_CURRENCY_DATA.items():
            fc = Currency(symbol=symbol)
            self.assertTrue(isinstance(fc, FiatCurrency))
            self.assertEqual(fc.symbol, symbol)
            self.assertEqual(fc.name, fiat_entry['name'])
            self.assertEqual(fc.address, Address(fiat_entry['address']))
            self.assertTrue(fc.fiat)

            fc = FiatCurrency(symbol=symbol)
            self.assertTrue(isinstance(fc, FiatCurrency))
            self.assertEqual(fc.symbol, symbol)
            self.assertEqual(fc.name, fiat_entry['name'])
            self.assertEqual(fc.address, Address(fiat_entry['address']))
            self.assertTrue(fc.fiat)

            fc = Currency(address=Address(fiat_entry['address']))
            self.assertTrue(isinstance(fc, FiatCurrency))
            self.assertEqual(fc.symbol, symbol)
            self.assertEqual(fc.name, fiat_entry['name'])
            self.assertEqual(fc.address, Address(fiat_entry['address']))
            self.assertTrue(fc.fiat)

            fc = FiatCurrency(address=Address(fiat_entry['address']))
            self.assertTrue(isinstance(fc, FiatCurrency))
            self.assertEqual(fc.symbol, symbol)
            self.assertEqual(fc.name, fiat_entry['name'])
            self.assertEqual(fc.address, Address(fiat_entry['address']))
            self.assertTrue(fc.fiat)

        token = Currency(symbol="CMK")
        self.assertTrue(isinstance(token, Token))
        self.assertFalse(isinstance(token, NativeToken))
        self.assertEqual(token.symbol, "CMK")
        self.assertEqual(token.address, "0x68CFb82Eacb9f198d508B514d898a403c449533E")
        self.assertEqual(token.name, 'Credmark')
        self.assertFalse(token.fiat)

        btc_token = Currency(symbol='BTC')
        self.assertTrue(isinstance(btc_token, Token))
        self.assertFalse(isinstance(btc_token, NativeToken))
        self.assertEqual(btc_token.symbol, "BTC")
        self.assertEqual(btc_token.address, Address("0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"))
        self.assertEqual(btc_token.name, "Bitcoin")
        self.assertFalse(btc_token.fiat)

        native_token = Currency(symbol='ETH')
        self.assertTrue(isinstance(native_token, NativeToken))
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.name, "Ethereum")
        self.assertEqual(native_token.address, Address(
            '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'))
        self.assertFalse(native_token.fiat)

        native_token = NativeToken(symbol='ETH')
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
