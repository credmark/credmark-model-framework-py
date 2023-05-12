# pylint: disable=line-too-long

import unittest

import credmark.cmf.model
from credmark.cmf.engine.dev_models.console import get_dt
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.types import Contract


class TestLedgerGeneric(ModelTestCase):

    def test_ledger_contract_events(self):
        # pylint: disable=protected-access
        contract = Contract(
            address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')

        with contract.ledger.events.BalanceTransfer as q:
            df = q.select(
                columns=q.columns,
                order_by=q.CONTRACT_ADDRESS,
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

            df = q.select(
                columns=q.columns,
                order_by=q.CONTRACT_ADDRESS.comma_(q.EVT__FROMINDEX),
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

            df = q.select(
                columns=[q.TXN_HASH, q.CONTRACT_ADDRESS],
                order_by=q.CONTRACT_ADDRESS.comma_(q.EVT__FROMINDEX),
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        # Operations with integer number will convert it to float and losses precision
        with contract.ledger.events.BalanceTransfer as q:
            df = q.select(
                aggregates=[
                    (q.EVT__VALUE.max_().as_text(), 'max_value'),
                    (q.EVT__VALUE.as_numeric().max_().plus_(
                        q.EVT__VALUE.as_numeric().max_()).as_text(), 'max_valuex2'),
                    (q.EVT__VALUE.max_(), 'max_value2')],
                order_by=q.field('max_value').dquote().desc(),
                bigint_cols=['max_value', 'max_valuex2']).to_dataframe()

    def test_ledger_contract_functions(self):
        """
        select distinct name from ETHEREUM.DECODED.FUNCTIONS
            where to_address = '0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04';
        """

        contract = Contract(
            address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')

        with contract.ledger.functions.transfer as q:
            df = q.select(
                columns=q.columns,
                order_by=q.FROM_ADDRESS,
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

        with contract.ledger.functions.transfer as q:
            df = q.select(
                columns=[q.BLOCK_NUMBER],
                order_by=q.FROM_ADDRESS,
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

        with contract.ledger.functions.transfer as q:
            df = q.select(
                aggregates=[(q.FN_AMOUNT.max_(), 'max_amount')],
                group_by=[q.FN_RECIPIENT],
                order_by=q.field('max_amount').dquote().desc(),
                where=q.FN_AMOUNT.is_not_null(),
                limit=5).to_dataframe()

        # with self.assertRaises(ModelEngineError):

    def test_aggregate(self):
        context = credmark.cmf.model.ModelContext.current_context()

        print('test_aggregate: Transactions')
        with context.ledger.Transaction as oo:
            df = oo.select(
                aggregates=[(oo.MAX_FEE_PER_GAS.sum_(), 'sum_gas')],
                limit=5,
                where=oo.BLOCK_TIMESTAMP.gt(
                    oo.field(int(get_dt(2022, 3, 1).timestamp())).to_timestamp()),
                group_by=[oo.BLOCK_TIMESTAMP],
                order_by=oo.BLOCK_TIMESTAMP).to_dataframe()
            print(df)
            self.assertTrue(df.shape[0] == 5)

    def test_group_by(self):
        context = credmark.cmf.model.ModelContext.current_context()

        print('test_group_by')
        with context.ledger.Transaction as oo:
            # tx on block 6949017
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.eq('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                    oo.BLOCK_NUMBER.lt(12407891)
                ),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            # pylint:disable=line-too-long
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.gt('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                    oo.BLOCK_NUMBER.ge(5407891)),
                group_by=[oo.HASH, oo.BLOCK_NUMBER],
                having=(
                    oo.HASH.eq('0xb42b73e2b4dd8ce98604b1cd89ce3547642b6dd6ad85de4cf70ca164c195e636').or_(
                        oo.HASH.eq('0xd220614b63795c5e43868010c70359dca12ad1e918efa687d143d21b90c0a72a')
                    ))).to_dataframe()
            self.assertTrue(df.shape[0] >= 2)

            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.gt(
                    '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                        oo.BLOCK_NUMBER.ge(5407891)),
                group_by=[oo.HASH, oo.BLOCK_NUMBER],
                having=oo.HASH.in_([
                    '0xb42b73e2b4dd8ce98604b1cd89ce3547642b6dd6ad85de4cf70ca164c195e636',
                    '0xd220614b63795c5e43868010c70359dca12ad1e918efa687d143d21b90c0a72a']),
                offset=1).to_dataframe()
            self.assertTrue(df.shape[0] >= 1)


if __name__ == '__main__':
    unittest.main()
