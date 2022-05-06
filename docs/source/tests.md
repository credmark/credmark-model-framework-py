# Testing Models

## Unit Testing

The Credmark Model Framework testing is based on the standard Python unittest module.

### Creating Tests

Create unit tests in python files with a specific naming pattern,
the default being `test*.py`, for example `test_model.py`. Typically they should be in the same folder as the model they test.

The unit tests must be implemented as subclasses of {class}`credmark.cmf.engine.model_unittest.ModelTestCase` and implement `test_*` methods to implement specific tests.

```{eval-rst}
.. autoclass:: credmark.cmf.engine.model_unittest.ModelTestCase
   :members:
```

You can use the {func}`credmark.cmf.engine.model_unittest.model_context` decorator on your test methods to configure a
specific context and [mocks](mocks_section) for the test:

```{eval-rst}
.. autofunction:: credmark.cmf.engine.model_unittest.model_context
```

See an [Example Unit Test](example_test_section)

### Running Tests

You can run tests using:

```
credmark-dev test
```

By default, it will run all tests in the `models` folder. To limit tests to a specific folder, you can pass a folder argument:

```
credmark-dev test models/contrib/mymodels
```

You can also use the `--pattern` argument to change the file matching pattern used for test discovery. The default is `test*.py`.

(mocks_section)=

## Mocks

When testing a model that calls other models, you can use mock models to generate predictable output. Mock models are simply configured static model outputs for a specified model slug (and optionally some partial input properties to match.)

For example, if you're developing a model that queries some data (by calling a ledger model for example) and then does some processing on it, you can mock the ledger model to return a set
of test data.

### Mock Configuration

Model mocks are defined using the {class}`credmark.cmf.engine.mocks.ModelMock` and {class}`credmark.cmf.engine.mocks.ModelMockConfig` classes. You can put your mocks in the same file as the model that uses them or another file in your models folder under `models/contrib`.

{class}`credmark.cmf.engine.mocks.ModelMockConfig` defines a full configuration of (multiple) mocks that can be used when running `credmark-dev`. It contains a `models` property that is a dictionary where the keys are model slugs and the values are a single or list of {class}`credmark.cmf.engine.mocks.ModelMock` instances.

```{eval-rst}
.. autoclass:: credmark.cmf.engine.mocks.ModelMockConfig
   :members:
```

A {class}`credmark.cmf.engine.mocks.ModelMock` instance contains the output for the model (which can be a dict or DTO instance, a `ModelBaseError` subclass instance, a string, another `ModelMock` instance or a list containing any of these types.) It also has a property `repeat` which specifies how many times the mock output can be used. The default is `0` which means the output can be used an unlimited number of times.

```{eval-rst}
.. autoclass:: credmark.cmf.engine.mocks.ModelMock
   :members:
```

### Testing with Mocks

To use mocks for a test, you can pass a configured `ModelMockConfig` instance to the {func}`credmark.cmf.engine.model_unittest.model_context` test method decorator.

```py
model_mocks_config = ModelMockConfig(
    models={
        'price': [
            ModelMock(Price(price=42.0, src='mock.price'),
                      input={'address': '0x68cfb82eacb9f198d508b514d898a403c449533e'}),
        ]
    })

    @model_context(chain_id=1,
                   block_number=140000,
                   mocks=model_mocks_config)
    def test_price(self):
        ...
```

### Running with Mocks

You can also run your model using mocks. To do that, you simply pass a parameter to `credmark-dev` telling it the location of the `ModelMockConfig` instance you want to use using the module name (dot notation) followed by a dot and the variable name.

For example, if you have a `ModelMockConfig` defined in the file `models/contrib/my_models/my_model.py` with the variable name `my_mocks`, the model mock config is specified with `models.contrib.my_models.my_model.my_mocks`. You can run the model `contrib.my-model` with the mocks using:

```
credmark-dev run contrib.my-model --model_mocks models.contrib.my_models.my_model.my_mocks
```

### Example Using Mocks

Here is an example of a model file that defines a mock for the model slug `price`. In this case there is one result for requests with partial input containing an `address` of `'0x68cfb82eacb9f198d508b514d898a403c449533e'`. To extend this, more `ModelMock`s could be added to the list or a single `ModelMock` with no `input` to match specified could be used
(whose output would be returned for any request for the `price` model.)

```python
from credmark.cmf.model import Model
from credmark.cmf.engine.mocks import ModelMockConfig, ModelMock
from credmark.cmf.types import Price, Token

model_mocks_config = ModelMockConfig(
    models={
        'price': [
            ModelMock(Price(price=42.0, src='mock.price'),
                      input={'address': '0x68cfb82eacb9f198d508b514d898a403c449533e'}),
        ]
    })


@Model.describe(slug='contrib.cmk-price',
                version='1.0',
                display_name='CMK Price',
                description='CMK Price test model',
                output=Price)
class CMKPriceModel(Model):

    def run(self, input: dict) -> Price:
        token = Token(symbol='CMK')
        price = Price(**self.context.models.price(token))
        return price
```

If this model was in the file `models/contrib/my_models/cmk_price.py`, you could run it with:

```
credmark-dev run contrib.cmk-price -m models.contrib.my_models.cmk_price.model_mocks_config
```

and the output will be something like:

```json
{
  "slug": "contrib.cmk-price",
  "version": "1.0",
  "output": {
    "price": 42.0,
    "src": "mock.price"
  },
  "dependencies": {
    "price": {
      "0.0": 1
    },
    "contrib.cmk-price": {
      "1.0": 1
    }
  }
}
```

(example_test_section)=

#### Example Unit Test

You can use mocks in a unit test by decorating your test method:

```py
from credmark.cmf.engine.mocks import ModelMock, ModelMockConfig
from credmark.cmf.engine.model_unittest import ModelTestCase, model_context
from credmark.cmf.types import Price

model_mocks_config = ModelMockConfig(
    models={
        'price': [
            ModelMock(Price(price=42.0, src='mock.price'),
                      input={'address': '0x68cfb82eacb9f198d508b514d898a403c449533e'}),
        ]
    })

class ModelTest(ModelTestCase):

    @model_context(chain_id=1,
                   block_number=140000,
                   mocks=model_mocks_config)
    def test_price(self):

        output = self.context.models.contrib.cmk-price()

        self.assertEqual(output['price'], 42.0)
```
