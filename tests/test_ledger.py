# pylint: disable=line-too-long

import credmark.cmf.model
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.types import Address, BlockNumber, Contract, JoinType, Token
from credmark.cmf.types.ledger_errors import InvalidQueryException


class TestLedger(ModelTestCase):
    def no_test_ledger_contract_events(self):
        # pylint: disable=protected-access
        input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
        with input.ledger.events.Transfer as ts:
            df = ts.select(aggregates=[(ts.EVT_FROM, 'evt_from'),
                                       (ts.EVT_TO, 'evt_to'),
                                       (ts.BLOCK_NUMBER, 'block_number'),
                                       (ts.TXN_HASH, 'hash')],
                           order_by=ts.BLOCK_NUMBER,
                           where=ts.EVT_FROM.eq(Address.null()),
                           limit=10).to_dataframe()
            self.assertEqual(df.shape[0], 10)

        input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
        with input.ledger.events.Transfer.as_('ts') as ts:
            df = ts.select(aggregates=[(ts.EVT_FROM, 'evt_from'),
                                       (ts.EVT_TO, 'evt_to'),
                                       (f'{ts.BLOCK_NUMBER}+10', 'block_number'),
                                       (ts.TXN_HASH, 'hash')],
                           order_by=ts.BLOCK_NUMBER,
                           where=ts.EVT_FROM.eq(Address.null()),
                           limit=10).to_dataframe()
            self.assertEqual(df.shape[0], 10)

        input = Contract('0xED5AF388653567Af2F388E6224dC7C4b3241C544')
        with input.ledger.events.Transfer.as_('ts') as ts:
            with self.context.ledger.Transaction.as_('tx') as tx:
                df = ts.select(aggregates=[(tx.VALUE, 'value'),
                                           (ts.EVT_FROM, 'evt_from'),
                                           (ts.EVT_TO, 'evt_to'),
                                           (ts.BLOCK_NUMBER, 'block_number'),
                                           (ts.TXN_HASH, 'hash')],
                               order_by=ts.BLOCK_NUMBER,
                               where=ts.EVT_FROM.eq(Address.null()).and_(tx.TO_ADDRESS.eq(input.address)),
                               joins=[(JoinType.LEFT_OUTER, tx, tx.HASH.eq(ts.TXN_HASH))],
                               limit=10).to_dataframe()
                self.assertEqual(df.shape[0], 10)

    def test_transaction(self):
        with self.context.ledger.Transaction.as_('tx') as tx:
            df = tx.select([tx.BLOCK_NUMBER, tx.FROM_ADDRESS, tx.TO_ADDRESS, tx.VALUE],
                           order_by=tx.BLOCK_NUMBER,
                           where=tx.TO_ADDRESS.eq(Address.null()),
                           limit=10).to_dataframe()
            self.assertEqual(df.shape[0], 10)

    def test_op(self):
        # force = True
        with self.context.ledger.Transaction as oo:
            # change the last e => E with force shall return 0 rows
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.eq('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261dE',
                                 case_sensitive=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] == 0)

            # restore the last E => e with force to return 1 row
            df = oo.select(
                aggregates=[(oo.GAS_PRICE.sum_(), 'sum_gas_price')],
                where=oo.HASH.eq('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de',
                                 case_sensitive=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            print(df)
            self.assertTrue(df.shape[0] == 1)

            # in with str_lower
            # Change the last e => E with force shall return 0 rows
            df = oo.select(
                where=oo.HASH.in_(['0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261dE'],
                                  case_sensitive=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] == 0)

            # in with str_lower
            # restore the last E => e with force to return 1 row
            df = oo.select(
                where=oo.HASH.in_(['0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de'],
                                  case_sensitive=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER]).to_dataframe()
            print(df)
            self.assertTrue(df.shape[0] > 0)

            # in with number with str_lower True/False
            df = oo.select(
                where=oo.BLOCK_NUMBER.in_([6949017, 13949017], case_sensitive=True), group_by=[oo.HASH, oo.BLOCK_NUMBER],
                bigint_cols=[oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(6949017 in df.block_number.unique())
            self.assertTrue(13949017 in df.block_number.unique())

            df = oo.select(
                where=oo.BLOCK_NUMBER.in_([6949017, 13949017]),
                group_by=[oo.HASH, oo.BLOCK_NUMBER],
                bigint_cols=[oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(6949017 in df.block_number.unique())
            self.assertTrue(13949017 in df.block_number.unique())

            # Skip as it takes too long
            def _test_not_between1():
                print(f'Not between {(13919017, 13949018)}')
                df = oo.select(
                    where=oo.BLOCK_NUMBER.not_in_([6949017, 13949017]),
                    group_by=[oo.HASH, oo.BLOCK_NUMBER],
                    bigint_cols=[oo.BLOCK_NUMBER]).to_dataframe()
                self.assertTrue(df.shape[0] > 0)
                self.assertTrue(6949017 not in df.block_number.unique())
                self.assertTrue(13949017 not in df.block_number.unique())

            print(f'Between {(13919017, 13949018)}')
            df = oo.select(
                where=oo.BLOCK_NUMBER.between_(13919017, 13949018),
                group_by=[oo.HASH, oo.BLOCK_NUMBER],
                bigint_cols=[oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(df.block_number.min() >= 13919017)
            self.assertTrue(df.block_number.max() <= 13949017)

            # between with number with str_lower True/False: ineffective
            print(f'Between {(6949017, 6949018)}')
            df = oo.select(
                where=oo.BLOCK_NUMBER.between_(
                    6949017, 6949018, case_sensitive=True),
                group_by=[oo.HASH, oo.BLOCK_NUMBER],
                bigint_cols=[oo.BLOCK_NUMBER]).to_dataframe()
            self.assertTrue(df.shape[0] > 0)
            self.assertTrue(df.block_number.min() >= 6949017)
            self.assertTrue(df.block_number.max() <= 6949018)

            # Skip as it takes too long
            def _test_not_between2():
                print(f'Not between {(6949017, 6949018)}')
                df = oo.select(
                    aggregates=[(oo.BLOCK_NUMBER.max_(), 'max_block_number'),
                                (oo.BLOCK_NUMBER.min_(), 'min_block_number')],
                    where=oo.BLOCK_NUMBER.not_between_(6949017, 6949018),
                    group_by=[oo.HASH, oo.BLOCK_NUMBER],
                    bigint_cols=['max_block_number', 'min_block_number']
                ).to_dataframe()  # , oo.BLOCK_NUMBER
                self.assertTrue(df.shape[0] > 0)
                self.assertTrue(df.min_block_number.min() < 6949017)
                self.assertTrue(df.max_block_number.max() > 13949017)

    def test_ledger_tables(self):
        context = credmark.cmf.model.ModelContext.current_context()
        block_20220101 = BlockNumber.from_ymd(2022, 1, 1)

        with context.ledger.Contract as oo:
            df = oo.select(columns=oo.columns, limit=5,
                           order_by=oo.ADDRESS,
                           where=oo.BLOCK_NUMBER.gt(13000000)
                           ).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Transaction as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.TRANSACTION_INDEX,
                           where=oo.BLOCK_NUMBER.eq(block_20220101)).to_dataframe()
            self.assertTrue(df.shape[0] <= 5)

            df = oo.select(columns=oo.columns, limit=5, order_by=oo.HASH.desc(),
                           where=oo.BLOCK_NUMBER.eq(block_20220101)).to_dataframe()
            self.assertTrue(df.hash[0].startswith('0xf'))

            df = oo.select(columns=oo.columns, limit=5, order_by=oo.HASH.asc(),
                           where=oo.BLOCK_NUMBER.eq(block_20220101)).to_dataframe()
            self.assertTrue(df.hash[0].startswith('0x0'))

        with context.ledger.Trace as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.TRANSACTION_HASH,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Block as oo:
            df = oo.select(
                columns=oo.columns,
                limit=5,
                order_by=oo.MINER,
                where=oo.TIMESTAMP.eq(oo.field(block_20220101.timestamp).to_timestamp())).to_dataframe()
            self.assertTrue(df.shape[0] == 1)

        with context.ledger.Log as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.BLOCK_HASH,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Receipt as oo:
            df = oo.select(columns=oo.columns,
                           limit=5,
                           order_by=oo.CUMULATIVE_GAS_USED,
                           where=oo.BLOCK_NUMBER.eq(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.Token as oo:
            df = oo.select(columns=oo.columns, limit=5, order_by=oo.BLOCK_HASH,
                           where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.TokenBalance as q:
            df = q.select(q.columns,
                          where=q.TOKEN_ADDRESS.eq(Token("AAVE").address),
                          order_by=q.TOKEN_ADDRESS.desc(),
                          limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.TokenTransfer as q:
            df = q.select(q.columns, where=q.TOKEN_ADDRESS.eq(Token("AAVE").address),
                          order_by=q.TOKEN_ADDRESS.desc(),
                          limit=5).to_dataframe()
            self.assertTrue(df.shape[0] == 5)

        with context.ledger.TokenTransfer as q:
            df_txn = q.select(
                columns=q.columns,
                where=(q.TRANSACTION_HASH
                       .eq('0x4b37d2f343608457ca3322accdab2811c707acf3eb07a40dd8d9567093ea5b82')
                       .and_(q.BLOCK_NUMBER.eq(10861674)))).to_dataframe()
            self.assertTrue(df_txn.shape[0] == 1)

    def test_ledger_txn(self):
        context = credmark.cmf.model.ModelContext.current_context()

        # oo.NONCE
        with self.assertRaises(InvalidQueryException):
            with context.ledger.Transaction as oo:
                _ = oo.select(columns=oo.columns, limit=-5, order_by=oo.TRANSACTION_INDEX,
                              where=oo.BLOCK_NUMBER.gt(13000000)).to_dataframe()

        with context.ledger.Transaction as oo:
            # Tx 0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de is at 6949017
            df = oo.select(
                columns=oo.columns,
                where=oo.HASH.eq('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                    oo.BLOCK_NUMBER.lt(13000000)
                ),
                order_by=oo.TRANSACTION_INDEX.desc().comma_(oo.TO_ADDRESS.asc())).to_dataframe()
            self.assertTrue(df.shape[0] > 0)

            df = oo.select(
                columns=oo.columns,
                where=(
                    oo.HASH.eq('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de').and_(
                        oo.BLOCK_NUMBER.gt(11586809)))).to_dataframe()
            self.assertTrue(df.shape[0] == 0)

            df = oo.select(
                columns=oo.columns,
                where=oo.HASH.eq('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
            ).to_dataframe()
            self.assertTrue(df.shape[0] == 1)

            def _no_test_hash_op():
                df = oo.select(
                    columns=oo.columns,
                    where=(
                        oo.HASH.gt(
                            '0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
                        .and_(oo.BLOCK_NUMBER.le(13586809)).parentheses_()
                        .or_(oo.BLOCK_NUMBER.gt(10586809).parentheses_()))).to_dataframe()
                self.assertTrue(df.shape[0] > 0)

                df = oo.select(
                    columns=oo.columns,
                    where=oo.HASH.ge('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
                ).to_dataframe()
                for x in df.hash.apply(lambda x: x[2]).unique():
                    self.assertTrue(
                        x in ['a', 'b', 'c', 'd', 'e', 'f'] or int(x) >= 9)

                df = oo.select(
                    columns=oo.columns,
                    where=oo.HASH.gt('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
                ).to_dataframe()
                for x in df.hash.apply(lambda x: x[2]).unique():
                    self.assertTrue(
                        x in ['a', 'b', 'c', 'd', 'e', 'f'] or int(x) >= 9)

                df = oo.select(
                    columns=oo.columns,
                    where=oo.HASH.le('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
                ).to_dataframe()
                for x in df.hash.apply(lambda x: x[2]).unique():
                    self.assertTrue(int(x) <= 9)

                df = oo.select(
                    columns=oo.columns,
                    where=oo.HASH.lt('0x972a0eb7442f2d9393b0fa165eed419e3b9d142fab2d6803b8bcf45719d261de')
                ).to_dataframe()
                for x in df.hash.apply(lambda x: x[2]).unique():
                    self.assertTrue(int(x) <= 9)
