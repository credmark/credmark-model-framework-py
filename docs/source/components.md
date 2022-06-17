# Model Framework Core Components

This document describes the key components and concepts of the Credmark Model Framework.

## Model Class

A Credmark model inherits from a simple base class called {class}`~credmark.cmf.model.Model`. The actual code can be found [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/model/__init__.py).

All Models should import this class `from credmark.cmf.model import Model`, subclass it, and override the run() method. See examples [here](https://github.com/credmark/credmark-models-py/tree/main/models/examples).

The {meth}`credmark.cmf.model.Model.describe` decorator `@Model.describe()` provides a simple interface to define the model properties such as slug, version, display_name, description, developer, input, output etc so that it can be used easily by consumers and other models.

If description is not specified, the `__doc__` string of the model's class is used for the model description.

See example [here](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_01_model.py).

## Data Transfer Object (DTO)

Input and output data for models are json-serializable objects of arbitrary depth and complexity. Objects can have 0 or more keys whose values can be null, number, string, array, or another object.

Although you can use dictionaries for model input and output data in your python code, we strongly encourage the use of DTOs (Data Transfer Objects.)

DTOs are classes with typed properties which will serialize and deserialize to and from JSON. They also automatically produce a JSON-schema that is used to document the input and output of a model. Each model may have their own DTOs or may share or inherit a DTO from another model that you have developed.

To create a DTO, simply subclass the DTO base class and use DTOFields to annotate your properties. Under the hood, the Credmark Model Framework uses the pydantic python module (DTO is simply an alias for pydantic BaseModel and DTOField an alias for Field) so almost anything that works with pydantic will work for your DTO.

Please see the [pydantic docs](https://pydantic-docs.helpmanual.io/usage/models/) for more information.

### Model Error Detail DTO [Advanced Topic]

Besides input and output, subclasses of {class}`~credmark.cmf.model.errors.ModelBaseError` can use a DTO for the `data.detail` object instead of a dict. You can simply pass a DTO as the `detail` arg in a model constructor:

```py
address = Address(some_address_string)
e = ModelDataError(message='Address is not a contract',
                   code=ModelDataError.Codes.CONFLICT,
                   detail=address)
```

If your detail object has many properties and you want to document the error and details, you can create a custom DTO and error class:

- Create a DTO subclass that defines the data you want to store in the detail.

For example:

```py
class TokenAddressNotFoundDetailDTO(DTO):
    address: Address = DTOField(...,description='Address for token not found')
```

- Create a DTO subclass that defines the new error DTO. (This step is not strictly necessary but it lets you document the error.) The trick is to use the generic properties of the `ModelErrorDTO` to specify the detail's DTO class: `ModelErrorDTO[TokenAddressNotFoundDetailDTO]`

```py
class TokenAddressNotFoundDTO(ModelErrorDTO[TokenAddressNotFoundDetailDTO]):
  """
  This error occurs when there is no token at the specified address.
  The detail contains the address.
  """
```

- Then create a `ModelDataError` (or `ModelRunError`) subclass and set the class property `dto_class` to your new error DTO class:

```py
class TokenAddressNotFoundError(ModelDataError):
    dto_class = TokenAddressNotFoundDTO
```

- You can now create an error instance with:

```py
# bad_address is set to an Address instance
error = TokenAddressNotFoundError(message='Bad address',
                                detail=TokenAddressNotFoundDetailDTO(address=bad_address))
# You can now access: error.data.detail.address
```

## Data Classes

We have some built-in reusable data type classes available under [Credmark.cmf.types](https://github.com/credmark/credmark-model-framework-py/tree/main/credmark/cmf/types).

We have created and grouped together different classes to manage input and output data types (DTOs) to be used by models. These types include some standard blockchain and financial data structures as well as some standard input and output objects for Credmark models.

**1. Address:** this class is a subclass of string and holds a blockchain address.

{class}`~credmark.cmf.types.address.Address` class is inherited from `str` to help with web3 address conversion. It's highly recommended to use it instead of a string.

✔️: Address("0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9").checksum # checksum version to be used

❌: Address("0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9") # lower case version

❌:"0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9" # lower case version

Example:

```py
from credmark.cmf.types import Address, Contract

contract = Contract(
    # lending pool address
    address=Address("0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9").checksum,
    abi=AAVE_V2_TOKEN_CONTRACT_ABI
)
```

The address can be provided in lower case, upper case or checksum hex format. This class will normalize the address into lower case. Note that It can be used as a normal string but it also has a "checksum" property which returns a web3 ChecksumAddress.

See [e_03_address.py](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_03_address.py) on how to use this class.

**2. Account(s):** {class}`~credmark.cmf.types.account.Account` simply holds an address. Accounts is a list of account instances which allows iteration through each account.

See [e_04_account.py](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_04_account.py) on how to use this class.

**3. Contract:** a {class}`~credmark.cmf.types.contract.Contract` is a subclass of {class}`~credmark.cmf.types.account.Account` which has a name, deployed transaction hash, abi, protocol name etc.

Object instantiation of this class will load all information available for the contract (against contract address provided as input) in our database and you can access whatever information you want from the object.

See the [Contract](contract_section) section for more details. See [e_05_contract.py](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_05_contract.py) for examples of how to use this class.

**4. Token:** {class}`~credmark.cmf.types.token.Token` is a specific kind of contract; hence the Token class inherits from {class}`~credmark.cmf.types.contract.Contract` class.

This class allows you to load token information with an address or symbol as well as get its price in USD Currently this class supports data load for erc20 token but we will support erc721 as well soon.

See [e_06_token.py](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_06_token.py) on how to use this class. Token_data.py lists all erc20 tokens currently supported.

**5. Price:** The {class}`~credmark.cmf.types.price.Price` classes can be used to hold a price.

**6. Position:** A {class}`~credmark.cmf.types.position.Position` class holds a {class}`~credmark.cmf.types.token.Token` and an amount. It can calculate its value based on the token price in USD. You can also access the scaled amount property if you need the scaled amount of the erc20 token.

Token_data.py lists all erc20 tokens currently supported.

**7. Portfolio:** A {class}`~credmark.cmf.types.portfolio.Portfolio` class holds a list of {class}`~credmark.cmf.types.position.Position` instances. So, it can be used to calculate all positions within a wallet.

## Model Context

Each model runs with a particular context, including the block chain id, block number, and a configured web3 instance (among other things). The context’s web3 instance can be used to make RPC calls. It also enforces deterministic behavior for Models.

The {class}`~credmark.cmf.model.context.ModelContext` class is the context for the model and can be accessed from a model as `self.context`.
The base code can be found [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/model/context.py). It provides an interface for models to run other models, call contracts, get ledger data, use a web3 instance etc.

The key utilities in `ModelContext` are

- [Web3](web3_section)
- [Contract](contract_section)
- [Ledger](ledger_section)
- [Block number](block_number_section)
- [Historical Utility](historical_section)

### Calling Other Models

A model can call other models and use their results. You can pass the input as an input arg and the model output is returned as a dict (or DTO if `return_type` is specified.)

If an error occurs during a call to run a model, an exception is raised. See {doc}`errors`

There are 2 ways to call another model:

- Using `context.models` (Recommended)
- Calling `context.run_model()`

#### `context.models`

Models are exposed on `context.models` by their slug (with any "-" (hyphens) in the slug replaced with "\_" (underscores)) and can be called like a function, passing the input as a DTO or dict or as standard keyword args (kwargs).

For example, here we use keyword args:

```py
# Returns a dict with output of the model
result = self.context.models.example.model(message='Hello world')
```

You can use a DTO for the output by initializing it with the output dict.

Here we use a DTO instance as the input and convert the output to another DTO instance:

```py
class ExampleEchoInput(DTO):
    message: str = DTOField('Hello', description='A message')


class ExampleEchoOutput(DTO):
    echo: str

input = ExampleEchoInput(message='Hello world')
output = ExampleEchoOutput(**self.context.models.example.model(input))

output.echo # will equal 'Hello world from block: 14661701'
```

You can run a model at a different block number by using the `context.models(block_number=12345)` syntax, for example:

```py
# Runs the model with a context of block number 12345
result = self.context.models(block_number=12345).example.model(message='Hello world')
```

#### `context.run_model()`

Alternatively you can run a model by slug string using the `context.run_model` method:

```py
def run_model(name: str,
              input: Union[dict, DTO] = EmptyInput(),
              return_type: Union[Type[dict], Type[DTO], None],
              block_number: Union[int, None] = None,
              version: Union[str, None] = None)
```

If `return_type` is None or dict, then the method returns the model output as a dict. If it's a DTO class, the method returns a DTO instance. As above, you can use a dict result with `**` to initialize a DTO instance yourself.

For example:

```py
# token = Token( ) instance

price = Price(**self.context.run_model('price', token))

# has the same effect as:

price = self.context.run_model('price', token, return_type=credmark.cmf.types.Price)
```

(web3_section)=

### Web3

`context.web3` will return a configured web3 instance with the default block set to the block number of context.

The web3 providers are determined from the environment variables as described in the [credmark_dev](credmark_dev) docs. Currently, during development, model developers will need to use their own alchemy account (or other web3 provider) to access web3 functionality. When a model is deployed, it automatically uses a Credmark web3 provider.

(contract_section)=

### Contract

Credmark simplifies the process of getting web3 instances of any contract from any chain. So you don't need to find and hardcode chain specific attributes and functions within these chains to run your models.

The model context exposes the `context.contracts` property which can be used to get contracts by metadata or address. The contracts are instances of the {class}`~credmark.cmf.types.contract.Contract` class which are configured and use the web3 instance at specified block number and specified chain id along with additional data based on `constructor_args`.

Example code for contact class can be found [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/types/contract.py).

Currently below parameters as argument are supported to fetched using Contracts:

- name: name of the contract
- address: address of the contract
- deploy_tx_hash: transaction hash at which contract was deployed
- Constructor_args
- protocol: protocol name
- product: product name
- abi_hash
- abi

Contract functions are accessible using the `contract.functions` property.

Tip: the contract object returned from contract class can be used to fetch any specific web3 attributes of the contract and call contract functions. As well it can be used as a DTO (see details below) so it can be returned as part of the output of a model.

(ledger_section)=

### Ledger

Credmark allows access to in-house blockchain ledger data via ledger interface (`context.ledger`), so that any model can fetch/use ledger data if required. This is done via {class}`~credmark.cmf.model.ledger.Ledger` class which currently supports below functions:

- get_transactions
- get_traces
- get_logs
- get_contracts
- get_blocks
- get_receipts
- get_erc20_tokens
- get_erc20_transfers

Please refer [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/model/ledger/__init__.py) for the code of the `Ledger` class.

(block_number_section)=

### Block number

The `context.block_number` holds the block number for which a model is running. Models only have access to data at (by default) or before this block number (by instantiating a new context). In other words models cannot see into the future and ledger queries etc. will restrict access to data by this block number.
As a subclass of `int`, the {class}`~credmark.cmf.types.block_number.BlockNumber` class allows the provided block numbers to be treated as integers and hence enables arithmetic operations on block numbers. It also allows you to fetch the corresponding datetime and timestamp properties for the block number. This can be super useful in case we want to run any model iteratively for a certain block-interval or time-interval backwards from the block number provided in the context.

Example code for the block-number class can be found [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/types/block_number.py).

**Block number, Timestamp and Python datetime**

In blockchain, every block is created with a timestamp (in Unix epoch). In Python there are two types for date, date and datetime, with datetime can be with tzinfo or without. To provide convienent tools to query between the three and resolve the confusion around time, we have a few tools with {class}`~credmark.cmf.types.block_number.BlockNumber` class.

1. property, `block_number.timestamp_datetime`: Return the Python datetime with UTC of the block.

2. property, `block_number.timestamp`: Return the Unix epoch of the block.

3. class method: `from_datetime(cls, timestamp: int)`: Return a {class}`~credmark.cmf.types.block_number.BlockNumber` instance to be less or equal to the input timestamp.

   Be cautious when we obtain a timestamp from a Python datetime, we should attach a tzinfo (e.g. timezone.utc) to the datetime. Otherwise, Python take account of the local timezone when converting to a timestamp. See the model [`example.block-time`](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_08_blocknumber.py).

4. Use a {class}`~credmark.cmf.types.block_number.BlockNumber` instance: Obtain a Python datetime with UTC of the block. The block number should be less or equal to the context block.

   ```py
   from credmark.types import BlockNumber

   dt = BlockNumber(14234904).timestamp_datetime
   ```

More example code for the block-number class can be found in [here](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_08_blocknumber.py)

(historical_section)=

### Historical Utility

The historical utility {class}`~credmark.cmf.model.utils.historical_util.HistoricalUtil`, available at `context.historical` (see code [here](https://github.com/credmark/credmark-model-framework-py/blob/main/credmark/cmf/model/utils/historical_util.py)), allows you to run a model over a series of blocks for any defined range and interval.

Block ranges can be specified by blocks (either a window from current block or a start and end block) with {meth}`~credmark.cmf.model.utils.historical_util.HistoricalUtil.run_model_historical_blocks` or by time (a window from the current block’s time or start and end time) with {meth}`~credmark.cmf.model.utils.historical_util.HistoricalUtil.run_model_historical`. Times can be specified different units, i.e. year, month, week, day, hour, minute and second.

See [e_11_historical.py](https://github.com/credmark/credmark-models-py/blob/main/models/examples/e_11_historical.py) on how to use this class.
