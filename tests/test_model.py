import logging
import unittest

import credmark.cmf.model
from credmark.cmf.engine.context import EngineModelContext
from credmark.cmf.engine.model_unittest import ModelTestCase, model_context
from credmark.cmf.model import Model
from credmark.dto import DTO, DTOField

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level='DEBUG')


class Car(DTO):
    brand: str = DTOField(..., description='Brand of car')
    color: str = DTOField(..., description='Color of car')


@Model.describe(slug='testmodel',
                version='1.0',
                display_name='Test Model',
                description='SDK Test Model',
                developer='Credmark',
                input=Car,
                output=Car)
class AModel(Model):

    def run(self, input: Car) -> Car:
        return input


class TestModel(ModelTestCase):

    @model_context(chain_id=1, block_number=1)
    def test_run(self):

        car = Car(brand="credmark", color="green")

        output = self.context.run_model(
            slug='testmodel',
            input=car.dict())

        self.assertEqual(car.brand, output['brand'])
        self.assertEqual(car.color, output['color'])

    @model_context(chain_id=1, block_number=1)
    def test_run_top(self):

        car = Car(brand="credmark", color="green")

        result = EngineModelContext.run_model_with_context(
            self.context,
            model_slug='testmodel',
            model_version=None,
            input=car.dict(),
            transform_output_to_dict=True)

        self.assertEqual(result['slug'], 'testmodel')
        self.assertEqual(result['version'], '1.0')
        self.assertEqual(result['dependencies']['testmodel']['1.0'], 1)
        output = result['output']
        self.assertEqual(car.brand, output['brand'])
        self.assertEqual(car.color, output['color'])

    def test_context(self):
        context = credmark.cmf.model.ModelContext.current_context()

        current_block = context.block_number

        with context.enter(context.block_number - 10) as cc:
            self.assertEqual(credmark.cmf.model.ModelContext.current_context(),
                             cc)
            self.assertEqual(cc.block_number, context.block_number-10)

        self.assertEqual(
            credmark.cmf.model.ModelContext.current_context(), context)

        with context.enter(context.block_number - 10) as cc1:
            with cc1.enter(cc1.block_number - 10) as cc2:
                with cc2.enter(cc2.block_number - 10) as cc3:
                    self.assertEqual(credmark.cmf.model.ModelContext.current_context(),
                                     cc3)
                    self.assertEqual(cc3.block_number, context.block_number-30)
                    self.assertEqual(
                        cc3.web3.eth.default_block, cc3.block_number)

        self.assertEqual(
            credmark.cmf.model.ModelContext.current_context(), context)

        self.assertEqual(
            context.web3.eth.default_block, context.block_number)

        self.assertEqual(current_block, context.block_number)


if __name__ == '__main__':
    unittest.main()
