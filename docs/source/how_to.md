# Run a Model

To see a list of all models available, use the command:

```
credmark-dev list
```

You can then pick a model name (slug) and run the model by using the command:

```
credmark-dev run <Specify Slug> -b <Specify block number>  -i <Specify Input>
```

so for example

```
credmark-dev run cmk.circulating-supply -b 14000000  -i “{}”
```

Tip: you can run the command

```
credmark-dev list --manifests
```

to see the input data format required for each model. It will also show the output formats.

# Develop a Model

A model is essentially a python code file which implements the model class by subclassing from a base class. See some examples [here](https://github.com/credmark/credmark-models-py/tree/main/models/examples).

**Steps**

1. Create a folder in the [models/contrib folder](https://github.com/credmark/credmark-models-py/tree/main/models) that will hold all of your models, for example `models/contrib/my_models`. You can add models directly there or create subfolders as desired. Do not work in another contributer's folder.
2. Create a python file, for example `model_foo.py` (again it can have any name as long as it ends in .py) in the folder you created in step 1.
3. Ensure your model class inherits from the base Model class `credmark.cmf.model.Model`. Also, use decorator `@Model.describe` to define the metadata for your model.
   Example:

```py
from credmark.cmf.model import Model

@Model.describe(slug='contrib.echo',
                   version='1.0',
                   display_name='Echo',
                   description="A test model to echo the message property sent in input.",
                   developer='Credmark',
                   input=EchoDto,
                   output=EchoDto)
class EchoModel(Model):
    def run(self, input: EchoDto) -> EchoDto:
        return input
```

The model class implements a `run(self, input)` method, which takes input data (as a dict or DTO (Data Transfer Object)) and returns a result dict or DTO (see later section DTO), with various properties and values, potentially nested with other JSON-compatible data structures.

A special DTO `EmptyInput`, which is an empty DTO, is created for model with no input required. The model input is EmptyInput by default if `input` is not specified in the decorator `@Model.describe`. If the model takes non-empty input, modeller can specify `input=dict` or create a DTO for more structured data.

A model can optionally implement a `init(self)` method which will be called when the instance is initialized and the `self.context` is available.

Models can call other python code, in imported python files (in your models folder or below) or from packages, as needed. You may not import code from other model folders. One thing to keep in mind is that different instances of a model may or may not be run in the same python execution so do not make use of global or class variables unless they are meant to be shared across model instances.

A model instance has access to the following instance variables:

- `self.context` - A context which holds state and provides functionality. Details on the [Model Context](#model-context) are below.
- `self.logger` - Python logger instance for logging to stderr(optional) A model should never write/print to stdout.

Please find more detailed examples [here](https://github.com/credmark/credmark-models-py/blob/main/models/examples/address_examples.py).

**Constraints**

- Model slugs MUST start with `"contrib."` and the rest of the string can contain letters (upper and lowercase), numbers, and hyphens. In general, use a hyphen between words. Slugs must be unique in a case-insensitive manner across all models running within Credmark.
- Input variables and Output data fields should use camel-cased names.

**DTO**

For the DTOs (Data Transfer Objects) we use the python module `pydantic` to define and validate the data. We have aliased `pydantic`'s `BaseModel` as DTO and `Field` as `DTOField` to avoid confusion with Credmark models but all the functionality of `pydantic` is available.

The DTO used in the example above, for both the input and output, looks like this:

```py
from credmark.dto import DTO, DTOField

class EchoDto(DTO):
    message: str = DTOField('Hello', description='A message')
```

The `credmark-model-framework` defines many common data objects as DTOs and fields such as Address, Contract, Token, Position, Portfolio etc. They can be found [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/types)

- Example 1: Use Address in input/ouput DTOs

The input data, e.g. `{"poolAddress":"0x..."}`, is converted to `Address` type. The property `.checksum` to get its checksum address.

```py
from credmark.cmf.model import Model
from credmark.cmf.types import Address

class PoolAddress(DTO):
    poolAddress: Address = DTOField(..., description='Address of Pool')

@Model.describe(...
                         input=PoolAddress)
class AModel(Model):
  def run(self, input: PoolAddress):
    address = input.poolAddress.checksum
```

- Example 2: Use Address to auto-convert to checksum address.

```py
from credmark.cmf.types import Address

def run(self, input):
    address = Address(wallet_adress)
    address.checksum
```

- Example 3: Pre-defined financial DTO to define input. Use it as object in the `run(self, input)`

```py
from credmark.cmf.model import Model
from credmark.cmf.types import Portfolio

"""
# Portfolio is defined in the framework
# class Portfolio(DTO):
#    positions: List[Position] = DTOField([], description='List of positions')

class PortfolioSummary(DTO):
    num_tokens: int = DTOField(..., description='Number of different tokens')
"""

@Model.describe(slug='contrib.type-test-1',
                         version='1.0',
                         display_name='Test Model',
                         description='A Test Model',
                         input=Portfolio,
                         output=PortfolioSummary)
class TestModel(Model):

    def run(self, input: Portfolio) -> PortfolioSummary:
        return PortfolioSummary(num_tokens=len(input.positions))

```

We strongly encourage you to create DTOs and/or make use of the common objects, either as your top-level DTO or as sub-objects and in lists etc. as needed.

You may use `credmark-dev describe {model_slug}` to show the input/output schema and examples for specific model(s). For example

```
credmark-dev describe aave.token-asset-historical

(...omit the output header)

Loaded models:

 - slug: aave.token-asset-historical
 - version: 1.0
 - tags: None
 - display_name: Aave V2 token liquidity
 - description: Aave V2 token liquidity at a given block number
 - developer:
 - input schema:
   Token(object)
     └─address(string)
 - input example:
   #01: {'symbol': 'USDC'}
   #02: {'symbol': 'USDC', 'decimals': 6}
   #03: {'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984'}
   #04: {'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984', 'abi': '(Optional) contract abi JSON string'}
 - output schema:
   BlockSeries(object)
     └─series(List[BlockSeriesRow])
         └─blockNumber(integer)
         └─blockTimestamp(integer)
         └─sampleTimestamp(integer)
         └─output(object)
 - output example:
   #01: {'series': [{'blockNumber': 'integer', 'blockTimestamp': 'integer', 'sampleTimestamp': 'integer', 'output': 'object'}]}
 - class: models.credmark.protocols.aave.aave_v2.AaveV2GetTokenAssetHistorical
```

# Submit a Model

If you are a contributor external to credmark, you should create your folder in [credmark-models-py/models/contrib].

You should create and keep your models under this folder. Note that we have applied additional conditions for model slug names under this folder. Slug name must start with `contrib.<model-name>`, so for example: `Slug = ‘contrib.sample-model`.

If you are a contributor external to credmark, you should create your folder in [credmark-models-py/models/contrib].

You should create and keep your models under this folder. Note that we have applied additional conditions for model slug names under this folder. Slug name must start with `contrib.<model-name>`, so for example: `Slug = ‘contrib.sample-model`.

Once your model is ready to submit, simply create a pull request on the github repo and let us know in our [Discord](https://discord.com/invite/BJbYSRDdtr).
