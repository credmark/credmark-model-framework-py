import unittest
from credmark.cmf.engine.model_unittest import ModelTestCase
from credmark.cmf.types import Some, Price


class TestModel(ModelTestCase):
    def test_many_plain(self):
        mm = Some[int](some=[1, 2, 3])
        df = mm.to_dataframe()
        self.assertTrue(df[0].shape[0] == 3)

    def test_many_dict(self):
        mm = Some[dict](some=[Price(price=1, src='a').dict(),
                              Price(price=2, src='b').dict()])
        df = mm.to_dataframe()
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(fields=[('x', lambda x: f'{x["price"]*100} {x["src"]*100}')])
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(fields=[('x', lambda x: f'{x["price"]*100} {x["src"]*10}'),
                                     ('y', lambda x: x["price"] - 100)])
        self.assertTrue(df.shape[0] == 2)

    def test_many_dto(self):
        mm = Some[Price](some=[Price(price=1, src='a'),
                               Price(price=2, src='b')])
        df = mm.to_dataframe()
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(fields=[('x', lambda x: f'{x.price} {x.src*100}')])
        self.assertTrue(df.shape[0] == 2)

        df = mm.to_dataframe(fields=[('x', lambda x: f'{x.price*100} {x.src*10}'),
                                     ('y', lambda x: x.price - 100)])
        self.assertTrue(df.shape[0] == 2)


if __name__ == '__main__':
    unittest.main()
