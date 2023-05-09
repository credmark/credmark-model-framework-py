import unittest

from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.types import PriceWithQuote, Records, Some


class TestModel(ModelTestCase):
    def test_records(self):
        mm = Records(records=[(1, 2, 3), (1, 2, 3)],
                     fields=['c1', 'c2', 'c3'],
                     n_rows=2,
                     fix_int_columns=[])
        df = mm.to_dataframe()
        self.assertTrue(df.shape == (2, 3))
        self.assertTrue(df.loc[0].shape[0] == 3)

        nn = Records.from_dataframe(df)
        self.assertTrue(len(nn) == 2)
        self.assertEqual(nn, mm)

    def test_some_plain(self):
        mm = Some[int](some=[1, 2, 3])
        df = mm.to_dataframe()
        self.assertEqual(df.shape, (3, 1))

    def test_some_dict(self):
        mm = Some[dict](some=[PriceWithQuote.usd(price=1, src='a').dict(),
                              PriceWithQuote.usd(price=2, src='b').dict()])
        df = mm.to_dataframe()
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(
            fields=[('x', lambda x: f'{x["price"]*100} {x["src"]*100}')])
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(fields=[('x', lambda x: f'{x["price"]*100} {x["src"]*10}'),
                                     ('y', lambda x: x["price"] - 100)])
        self.assertTrue(df.shape[0] == 2)

    def test_some_dto(self):
        mm = Some[PriceWithQuote](some=[PriceWithQuote.usd(price=1, src='a'),
                                        PriceWithQuote.usd(price=2, src='b')])
        df = mm.to_dataframe()
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(
            fields=[('x', lambda x: f'{x.price} {x.src*100}')])
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(fields=[('x', lambda x: f'{x.price*100} {x.src*10}'),
                                     ('y', lambda x: x.price - 100)])
        self.assertTrue(df.shape[0] == 2)

        self.assertTrue(Some[int].empty().is_empty())


if __name__ == '__main__':
    unittest.main()
