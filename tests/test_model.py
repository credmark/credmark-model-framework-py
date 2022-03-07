import unittest
import logging
import credmark.model
from credmark.model.engine.context import EngineModelContext
from credmark.model.engine.model_loader import ModelLoader
from credmark.types.dto import DTO, DTOField

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level='DEBUG')


class Car(DTO):
    brand: str = DTOField(..., description='Brand of car')
    color: str = DTOField(..., description='Color of car')


@credmark.model.describe(slug='testmodel',
                         version='1.0',
                         display_name='Test Model',
                         description='SDK Test Model',
                         developer='Credmark',
                         input=Car,
                         output=Car)
class PIModel(credmark.model.Model):

    def run(self, input: Car) -> Car:
        return input


class TestStringMethods(unittest.TestCase):

    def test_run(self):
        model_loader = ModelLoader(['tests'])
        if model_loader.errors:
            logging.error(model_loader.errors)

        car = Car(brand="credmark", color="green")

        result = EngineModelContext.create_context_and_run_model(
            chain_id=1,
            block_number=1,
            model_slug='testmodel',
            input=car.dict(),
            model_loader=model_loader,
            chain_to_provider_url=None,
            api_url=None,
            run_id='test_run')

        self.assertEqual(result['slug'], 'testmodel')
        self.assertEqual(result['version'], '1.0')
        self.assertEqual(result['dependencies']['testmodel']['1.0'], 1)
        output = result['output']
        self.assertEqual(car.brand, output['brand'])
        self.assertEqual(car.color, output['color'])


if __name__ == '__main__':
    unittest.main()
