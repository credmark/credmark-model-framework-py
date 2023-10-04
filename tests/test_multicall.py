# pylint: disable=line-too-long

import unittest

import credmark.cmf.model
from credmark.cmf.engine.model_unittest import ModelTestCase, model_context
from credmark.cmf.types.address import Address
from credmark.cmf.types.token_erc20 import Token


class TestModel(ModelTestCase):

    @model_context(chain_id=1, block_number=17_000_000)
    def test_try_aggregate(self):
        t = Token('USDC')

        batch = credmark.cmf.model.ModelContext.current_context().web3_batch
        [symbol_result, decimals_result] = batch.call([t.functions.symbol(), t.functions.decimals()])
        self.assertEqual(symbol_result.success, True)
        self.assertEqual(symbol_result.return_data_decoded, 'USDC')

        self.assertEqual(decimals_result.success, True)
        self.assertEqual(decimals_result.return_data_decoded, 6)

        [symbol_result2, decimals_result2] = batch.call([t.functions.symbol(), t.functions.decimals()], unwrap=True)

        self.assertEqual(symbol_result2, symbol_result.return_data_decoded)
        self.assertEqual(decimals_result2, decimals_result.return_data_decoded)

    @model_context(chain_id=1, block_number=17_000_000)
    def test_try_aggregate_same_function(self):
        address = "0x8df175aba312ce90aa03f636573ca99c29fbb9d0"
        t1 = Token('USDC')
        t2 = Token('WETH')

        batch = credmark.cmf.model.ModelContext.current_context().web3_batch
        results = batch.call_same_function(t1.functions.balanceOf(Address(address).checksum),
                                           [t1.address.checksum, t2.address.checksum])

        b1 = results[0]
        b2 = results[1]

        self.assertEqual(b1.success, True)
        self.assertEqual(b1.return_data_decoded, 879377)

        self.assertEqual(b2.success, True)
        self.assertEqual(b2.return_data_decoded, 0)

        results2 = batch.call_same_function(
            t1.functions.balanceOf(Address(address).checksum),
            [t1.address.checksum, t2.address.checksum],
            unwrap=True)

        self.assertEqual(results2[0], b1.return_data_decoded)
        self.assertEqual(results2[1], b2.return_data_decoded)

    @model_context(chain_id=1, block_number=17_000_000)
    def test_try_aggregate_same_function_failure(self):
        t1 = Token('USDC').as_erc20(True)
        t2 = Token('WETH').as_erc20(True)

        batch = credmark.cmf.model.ModelContext.current_context().web3_batch
        [b1, b2] = batch.call_same_function(t1.functions.DECIMALS(),
                                            [t1.address.checksum, t2.address.checksum])

        self.assertEqual(b1.success, False)
        self.assertEqual(b1.return_data_decoded, b"")

        self.assertEqual(b2.success, False)
        self.assertEqual(b2.return_data_decoded, b"")


if __name__ == '__main__':
    unittest.main()
