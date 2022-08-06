import unittest

import credmark.cmf.model
from credmark.cmf.engine.dev_models.console import get_block, get_dt
from credmark.cmf.engine.errors import ModelEngineError
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.types import Contract
from credmark.cmf.types.ledger_errors import InvalidQueryException


class TestLedger(ModelTestCase):

    def test_ledger_contract_events(self):
        # pylint: disable=protected-access
        contract = Contract(address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')

        with contract.ledger.events.BalanceTransfer as q:
            df = q.select(
                columns=q.columns,
                order_by=q.CONTRACT_ADDRESS,
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

            df = q.select(
                columns=q.columns,
                order_by=q.CONTRACT_ADDRESS.comma_(q._FROMINDEX),
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

            df = q.select(
                columns=[q.EVT_HASH, q.CONTRACT_ADDRESS],
                order_by=q.CONTRACT_ADDRESS.comma_(q._FROMINDEX),
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with contract.ledger.events.BalanceTransfer as q:
            df = q.select(
                aggregates=[
                    (q._VALUE.max_().to_char(), 'max_value'),
                    (q._VALUE.max_().plus_(q._VALUE.max_()).to_char(), 'max_valuex2'),
                    (q._VALUE.max_(), 'max_value2')],
                order_by=q.field('max_value').dquote().desc(),
                bigint_cols=['max_value', 'max_valuex2']).to_dataframe()

    def test_ledger_contract_functions(self):
        contract = Contract(address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')

        with contract.ledger.functions.approve as q:
            df = q.select(
                columns=q.columns,
                order_by=q.CONTRACT_ADDRESS,
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

        with contract.ledger.functions.approve as q:
            df = q.select(
                columns=[q.TXN_BLOCK_NUMBER],
                order_by=q.CONTRACT_ADDRESS,
                limit=5).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

        with contract.ledger.functions.approve as q:
            with self.assertRaises(ModelEngineError):
                df = q.select(
                    aggregates=[(q.VALUE.max_(), 'max_value')],
                    group_by=[q.SPENDER],
                    order_by=q.field('max_value').dquote().desc(),
                    limit=5).to_dataframe()

    def test_aggregate(self):
        context = credmark.cmf.model.ModelContext.current_context()

        with context.ledger.Transaction as oo:
            df = oo.select(
                aggregates=[(oo.MAX_FEE_PER_GAS.sum_(), 'sum_gas')],
                limit=5,
                where=oo.BLOCK_TIMESTAMP.gt(get_dt(2022, 3, 1).timestamp()),
                order_by=oo.BLOCK_TIMESTAMP,).to_dataframe()
            self.assertTrue(df.shape[0] == 1)

    def test_op(self):
        context = credmark.cmf.model.ModelContext.current_context()

        # force = True
        with context.ledger.Transaction as oo:

            # change the last e => E with force shall return 0 rows
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.eq(
                    '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261dE',
                    force=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] == 0)

            # restore the last E => e with force to return 1 row
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.eq(
                    '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de',
                    force=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] == 1)

            # in with force
            # Change the last e => E with force shall return 0 rows

            df = oo.select(
                where=oo.HASH.in_(
                    ['0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261dE'],
                    force=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] == 0)

            # in with force
            # restore the last E => e with force to return 1 row
            df = oo.select(
                where=oo.HASH.in_(
                    ['0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de'],
                    force=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            # in with number with force True/False
            df = oo.select(
                where=oo.BLOCK_NUMBER.in_([6949017, 13949017], force=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(6949017 in df.block_number.unique())
            self.assertTrue(13949017 in df.block_number.unique())

            df = oo.select(
                where=oo.BLOCK_NUMBER.in_([6949017, 13949017]),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(6949017 in df.block_number.unique())
            self.assertTrue(13949017 in df.block_number.unique())

            df = oo.select(
                where=oo.BLOCK_NUMBER.not_in_([6949017, 13949017]),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(6949017 not in df.block_number.unique())
            self.assertTrue(13949017 not in df.block_number.unique())

            # between with number with force True/False
            df = oo.select(
                where=oo.BLOCK_NUMBER.between_(6949017, 6949018, force=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(df.block_number.min() >= 6949017)
            self.assertTrue(df.block_number.max() <= 13949017)

            df = oo.select(
                where=oo.BLOCK_NUMBER.between_(6949017, 13949017),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(df.block_number.min() >= 6949017)
            self.assertTrue(df.block_number.max() <= 13949017)

            df = oo.select(
                where=oo.BLOCK_NUMBER.not_between_(6949017, 13949017),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(df.block_number.min() < 6949017)
            self.assertTrue(df.block_number.max() > 13949017)

    def test_group_by(self):
        context = credmark.cmf.model.ModelContext.current_context()

        with context.ledger.Transaction as oo:
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.gt(
                    '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                        oo.BLOCK_NUMBER.ge(12407891)
                ),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            # pylint:disable=line-too-long
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.gt(
                    '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
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

    def test_ledger_txn(self):
        context = credmark.cmf.model.ModelContext.current_context()

        with self.assertRaises(InvalidQueryException):
            with context.ledger.Transaction as oo:
                _ = oo.select(columns=oo.columns, limit=-5, order_by=oo.NONCE,
                              where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()

        with context.ledger.Transaction as oo:
            df = oo.select(
                columns=oo.columns,
                where=oo.HASH.gt(
                    '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                        oo.BLOCK_NUMBER.gt(13000000)
                ),
                order_by=oo.NONCE.desc().comma_(oo.TO_ADDRESS.asc())).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            df = oo.select(
                columns=oo.columns,
                where=(
                    oo.HASH.gt(
                        '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                            oo.BLOCK_NUMBER.gt(11586809)))).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            df = oo.select(
                columns=oo.columns,
                where=(
                    oo.HASH.gt(
                        '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
                    .and_(oo.BLOCK_NUMBER.le(13586809)).parentheses_()
                    .or_(oo.BLOCK_NUMBER.gt(10586809).parentheses_()))).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            df = oo.select(columns=oo.columns, where=oo.HASH.eq(
                '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
            ).to_dataframe()
            self.assertTrue(df.shape[0] == 1)

            df = oo.select(columns=oo.columns, where=oo.HASH.ge(
                '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
            ).to_dataframe()
            for x in df.hash.apply(lambda x: x[2]).unique():
                self.assertTrue(x in ['a', 'b', 'c', 'd', 'e', 'f'] or int(x) >= 9)

            df = oo.select(columns=oo.columns, where=oo.HASH.gt(
                '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
            ).to_dataframe()
            for x in df.hash.apply(lambda x: x[2]).unique():
                self.assertTrue(x in ['a', 'b', 'c', 'd', 'e', 'f'] or int(x) >= 9)

            df = oo.select(columns=oo.columns, where=oo.HASH.le(
                '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
            ).to_dataframe()
            for x in df.hash.apply(lambda x: x[2]).unique():
                self.assertTrue(int(x) <= 9)

            df = oo.select(columns=oo.columns, where=oo.HASH.lt(
                '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
            ).to_dataframe()
            for x in df.hash.apply(lambda x: x[2]).unique():
                self.assertTrue(int(x) <= 9)

    def test_ledger_tables(self):
        context = credmark.cmf.model.ModelContext.current_context()

        block_20220101 = get_block(get_dt(2022, 1, 1))

        with context.ledger.Transaction as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.NONCE,
                           where=oo.BLOCK_NUMBER.ge(block_20220101)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

            df = oo.select(columns=oo.columns, limit=5, order_by=oo.HASH.desc(),
                           where=oo.BLOCK_NUMBER.ge(block_20220101)).to_dataframe()
            self.assertTrue(df.hash[0].startswith('0xffff'))

            df = oo.select(columns=oo.columns, limit=5, order_by=oo.HASH.asc(),
                           where=oo.BLOCK_NUMBER.ge(block_20220101)).to_dataframe()
            self.assertTrue(df.hash[0].startswith('0x0000'))

        with context.ledger.Trace as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.GAS_USED,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Block as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.MINER,
                           where=oo.TIMESTAMP.gt(block_20220101)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Log as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.BLOCK_HASH,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Receipt as oo:
            df = oo.select(columns=oo.columns, limit=5,
                           order_by=oo.CUMULATIVE_GAS_USED,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.TokenTransfer as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.VALUE,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Token as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.TOTAL_SUPPLY,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Contract as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.BYTECODE,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.TokenBalance as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.TOKEN_ADDRESS,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)


if __name__ == '__main__':
    unittest.main()
