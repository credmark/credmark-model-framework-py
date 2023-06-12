# pylint: disable=line-too-long, pointless-string-statement

import credmark.cmf.model
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.types import BlockNumber, Contract

"""
with events
"0x0297e37f1873d2dab4487aa67cd56b58e2f27875"
"0x22126f95b1cde15182fe6a816765beb6a3096dc3"
"0x775d4d8c4751bae18ebdba4ebaa46a1ff54d0c9d"
"0x0bffc5692960bb043d3216839bdd6e5e64ff1b4e"
"0xde1df189259dd9ea1686ed939bdfc03a97621423"
"0x6286a9e6f7e745a6d884561d88f94542d6715698"
"0x8b397084699cc64e429f610f81fac13bf061ef55"
"0x3dec619dc529363767dee9e71d8dd1a5bc270d76"
"0x371b97c779e8c5197426215225de0eeac7dd13af"
"0x55b1a124c04a54eefdefe5fa2ef5f852fb5f2f26"
"0x5b45b414c6cd2a3341be70ba22be786b0124003f"
"0x5cf21a9899e679448284427c0baca807fad6bb8f"
"0xe8af04ad759ad790aa5592f587d3cfb3ecc6a9da"
"0x3b7335f3f1771122cd0107416b1da1b2fb7e94dd"
"0x4e5e55baeef3bc747d22123ce4ade3661c916a3e"
"0xf17a03a7f6db32441614ac0022e57d4e185530bb"
"0x7c621229fb0293ef8a4f5caa79a8bb4d60bf5ca4"
"0x58c1bbb508e96cfec1787acf6afe1c7008a5b064"
"0x1c57a5ee9c5a90c9a5e31b5265175e0642b943b1"
"0x33c6eec1723b12c46732f7ab41398de45641fa42"
"0x0000000000004946c0e9f43f4dee607b0ef1fa1c"
"""


class TestPolygon(ModelTestCase):
    def test_metadata(self):
        context = credmark.cmf.model.ModelContext.current_context()
        with context.fork(chain_id=137):
            cc = Contract("0xefe9c015cff1e9bd1d7cc1782b13571ea77cf63b")
            _ = cc.abi
            self.assertTrue(cc.abi is not None)

            cc = Contract("0xb6f53428b2e9a7875844299b2d3f80bfd696678e")
            _ = cc.abi
            self.assertTrue(cc.proxy_for is not None)

    def test_contract(self):
        context = credmark.cmf.model.ModelContext.current_context()
        with context.fork(chain_id=137):
            block_number = BlockNumber.from_ymd(2022, 1, 1, 12, 3)
            block_number_ts = block_number.timestamp
            block_number2 = BlockNumber.from_timestamp(block_number_ts)
            self.assertEqual(block_number, block_number2)

    def test_ledger(self):
        context = credmark.cmf.model.ModelContext.current_context()
        with context.fork(chain_id=137, block_number=43464962) as context_poly:
            context_poly.__dict__['original_input'] = {}
            context_poly.__dict__['slug'] = 'test'

            block_number = context_poly.block_number
            with context_poly.ledger.Block as q:
                df = q.select(q.columns, where=q.NUMBER.eq(block_number)).to_dataframe()
                self.assertTrue(df.shape[0] == 1)

            with context_poly.ledger.Contract as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.between_(block_number-1000, block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.Token as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.between_(block_number-1000, block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.Trace as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.eq(block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.Log as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.eq(38683710)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.Transaction as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.eq(block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.Receipt as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.eq(block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.TokenTransfer as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.eq(block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            with context_poly.ledger.TokenBalance as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.eq(block_number)).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

            cc = Contract('0xde1df189259dd9ea1686ed939bdfc03a97621423')

            with cc.ledger.events.Transfer as q:
                df = q.select(q.columns, where=q.BLOCK_NUMBER.between_(43451034, 43464962)).to_dataframe()
                self.assertTrue(df.shape[0] == 2)
