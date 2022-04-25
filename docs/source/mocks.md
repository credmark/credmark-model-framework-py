# Testing a Model With Mocks

When developing a model that calls other models, you can test your model by using mock models. Mock models are simply configured static model outputs for a specified model slug (and optionally some partial input properties to match.)

For example, if you're developing a model that queries some data (by calling a ledger model for example) and then does some processing on it, you can mock the ledger model to return a set
of test data.

## Mock Configuration

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

## Running with Mocks

To run your model using mocks, you simply pass a parameter to `credmark-dev` telling it the location of the `ModelMockConfig` instance you want to use using the module name (dot notation) followed by a dot and the variable name.

For example, if you have a `ModelMockConfig` defined in the file `models/contrib/my_models/my_model.py` with the variable name `my_mocks`, the model mock config is specified with `models.contrib.my_models.my_model.my_mocks`. You can run the model `contrib.my-model` with the mocks using:

```
credmark-dev run contrib.my-model --model_mocks models.contrib.my_models.my_model.my_mocks
```

## Example Using Mocks

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

```
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
