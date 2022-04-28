import unittest
from credmark.cmf.model.errors import ModelBaseError

from credmark.cmf.types import Token
from credmark.cmf.types.token import NativeToken
from tests.context_test_case import ContextTestCase


class TestToken(ContextTestCase):
    def test_run(self):
        token = Token(symbol="CMK")
        self.assertEqual(token.symbol, "CMK")
        self.assertEqual(token.address, "0x68CFb82Eacb9f198d508B514d898a403c449533E")
        self.assertEqual(token.decimals, 18)
        self.assertEqual(token.total_supply, 100_000_000 * 10**18)

        with self.assertRaises(ModelBaseError):
            Token()

        with self.assertRaises(ModelBaseError):
            Token(symbol="INVALID_SYMBOL")

        native_token = NativeToken()
        self.assertEqual(native_token.symbol, "ETH")
        self.assertEqual(native_token.name, "ethereum")
        self.assertEqual(native_token.decimals, 18)


if __name__ == '__main__':
    unittest.main()
