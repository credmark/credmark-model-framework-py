# CLI credmark-dev

`credmark-dev` is a command-line tool installed with the `credmark-model-framework`. It can be used to run, list, and get docs for models. It also includes an [interactive python console](console_section).

## `help` command

```
$ credmark-dev --help

usage: credmark-dev [-h] [--log_level LOG_LEVEL] [--model_path MODEL_PATH]
                       [--manifest_file MANIFEST_FILE]
                       {version,list,list-models,models,deployed-models,describe,describe-models,man,run,run-model,test,run-tests,build,build-manifest,clean,remove-manifest}
                       ...

Credmark developer tool

optional arguments:
  -h, --help            show this help message and exit
  --log_level LOG_LEVEL
                        Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
  --model_path MODEL_PATH
                        Semicolon separated paths to the model folders (or parent) or model
                        python file. Defaults to models folder.
  --manifest_file MANIFEST_FILE
                        Name of the built manifest file. Defaults to models.json. [Not
                        required during development]

Commands:
  Supported commands

  {version,list,list-models,models,deployed-models,describe,describe-models,man,run,run-model,test,run-tests,build,build-manifest,clean,remove-manifest}
                        additional help
    version             Show version of the framework
    list (list-models)  List models in this repo
    models (deployed-models)
                        List models deployed on server
    describe (describe-models, man)
                        Show documentation for local and deployed models
    create (create-model)
                        Create a new model skeleton file
    run (run-model)     Run a model
    test (run-tests)    Run model tests
    build (build-manifest)
                        Build model manifest [Not required during development]
    clean (remove-manifest)
                        Clean model manifest
```

**_NOTE_**: `credmark-dev` will search for models under the folder `models` in the current folder. To change this location, use the `--model_path` argument.

## `create` command

Create a skeleton for a new model with the `create` command.

Below -h command shows the details of args:

```
$ credmark-dev create -h

usage: credmark-dev create [-h] model_folder filename

positional arguments:
  model_folder  The name of the folder under "models/contrib" in which to put the new model
                file. Ex. "my_models"
  filename      The name of the new model file. Ex. "model.py"

optional arguments:
  -h, --help    show this help message and exit

```

## `run` command

Below -h command shows the details of options available for run commands.

```
$ credmark-dev run -h

usage: credmark-dev run [-h] [-b BLOCK_NUMBER] [-c CHAIN_ID] [-i INPUT] [-o OUTPUT]
                       [-v MODEL_VERSION] [-j] [-d] [-l USE_LOCAL_MODELS] [-m MODEL_MOCKS]
                       [--generate_mocks GENERATE_MOCKS]
                       [--provider_url_map PROVIDER_URL_MAP] [--api_url API_URL]
                       model-slug

positional arguments:
  model-slug            Slug for the model to run or "console" for the interactive console.

optional arguments:
  -h, --help            show this help message and exit
  -b BLOCK_NUMBER, --block_number BLOCK_NUMBER
                        Block number used for the context of the model run. If not
                        specified, it is set to the latest block of the chain.
  -c CHAIN_ID, --chain_id CHAIN_ID
                        Chain ID. Defaults to 1.
  -i INPUT, --input INPUT
                        Input JSON or if value is "-" it will read input JSON from stdin.
  -o OUTPUT, --output OUTPUT
                        Output path to save model results as JSON file.
  -v MODEL_VERSION, --model_version MODEL_VERSION
                        Version of the model to run. Defaults to latest.
  -j, --format_json     Format output json to be more readable
  -d, --debug           Log debug info for model run input and output
  -l USE_LOCAL_MODELS, --use_local_models USE_LOCAL_MODELS
                        Comma-separated list of model slugs for models that should favor
                        use of the local version. This is only required when a model is
                        calling another model. Use "*" to use local versions of all models.
                        Use "-" to use no local models.
  -m MODEL_MOCKS, --model_mocks MODEL_MOCKS
                        Module path and symbol of model mocks config to use. For example,
                        models.contrib.mymodels.mymocks.mock_config
  --generate_mocks GENERATE_MOCKS
                        Generate model mocks and write them to the specified file. The
                        generated python file can be used with --model_mocks on another
                        run or in unit tests.
  --provider_url_map PROVIDER_URL_MAP
                        JSON object of chain id to Web3 provider HTTP URL. Overrides
                        settings in env vars.
  --api_url API_URL     Credmark API url. Defaults to the standard API
                        gateway. You do not normally need to set this.
```

To call any model we can specify the output by providing below parameters (they're not necessarily required):

- `-b` or `–block_number` : to define against which block number the model should run. If not specified, it uses the "latest" block from our ledger db.
- `-i` or `–input` : to provide input for a model in a predefined structure.(you can run command `credmark-dev list --manifests` to see the input format required for each model. See example below). If not provided it will default to “{}”.
  Model-slug: Name of the model (slug) to call the model.

Note: if chain ID is not mentioned explicitly in the parameter, it defaults to 1. If the model is using web 3 instance then chain id (and blockchain) will be picked from the .env file we defined during setup (refer to “configure environment variable” section). If the model is using Credmark database then, by default, it will refer to the Ethereum blockchain.

See the example below. Here, we are running the model “cmk.circulating-supply” at block_number 14000000.

```
$ credmark-dev run -b 14000000 cmk.circulating-supply -i "{}"

{"slug": "cmk.circulating-supply", "version": "1.0", "output": {"result": 28314402605762084044696668}, "dependencies": {"cmk.total-supply": {"1.0": 1}, "cmk.circulating-supply": {"1.0": 1}}}
```

## `list` command

Below `-h` command shows the details of options available for list commands.

```
$ credmark-dev list -h

usage: credmark-dev list [-h] [--manifests] [--json]

optional arguments:
  -h, --help   show this help message and exit
  --manifests
  --json
```

Note: You can also run `list-models` command alternatively.

Example below shows simple output (list of all models and their version) of list command:

```
$ credmark-dev list

Loaded models:

 - var: ['1.0']
 - cmk.total-supply: ['1.0']
 - cmk.circulating-supply: ['1.0']
 - xcmk.total-supply: ['1.0']
[...]
```

You can also get the list result in different formats using `--json` or `--manifest`.

## `describe` command

The describe command shows details on one or more models.

```
credmark-dev describe [model-slug]
```

The model-slug can be a slug or slug prefix string.

For example:

```shell
$ credmark-dev describe example.model

example.model
 - slug: example.model
 - version: 1.2
 - displayName: Example - Model
 - description: First example model to echo the message property sent in input.
 - developer: Credmark
 - tags: None
 - input schema (* for required field):
   ExampleEchoInput(ExampleEchoInput(*))
     └─message(string)
 - input example:
   #01: {"message": "string"}
 - output schema (* for required field):
   ExampleEchoOutput(ExampleEchoOutput(*))
     └─title(string)
     └─description(string)
     └─github_url(string)
     └─documentation_url(string)
     └─logs(List[Log])
         └─type(string)
         └─message(string)
         └─input(string)
         └─output(string)
         └─error(string)
     └─echo(string)
 - output example:
   #01: {"title": "string"}
 - errors:
   No defined errors
 - class: models.examples.e_01_model.ExampleEcho
```

## `test` command

Discover and run unit tests.

Below -h command shows the details of options available for the test command.

```
$ credmark-dev test -h

usage: credmark-dev test [-h] [-p PATTERN] [--api_url API_URL]
                            [--provider_url_map PROVIDER_URL_MAP]
                            [tests_folder]

positional arguments:
  tests_folder          Folder to start discovery for tests.
                        Defaults to "models".

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        Pattern to match test files (test*.py default).
  --api_url API_URL     Credmark API url. Defaults to the standard API gateway. You do not
                        normally need to set this.
  --provider_url_map PROVIDER_URL_MAP
                        JSON object of chain id to Web3 provider HTTP URL. Overrides
                        settings in env var or .env.test file.
```

To search for all tests under the `models` folder and run them use:

```
credmark-dev test
```

You can specify a start folder to search for tests by using an extra argument:

```
credmark-dev test models/contrib/mymodels
```

By default it searches for tests in files that match the pattern `test*.py`. You can specify an alternative pattern using the `--pattern` argument.

## `version` command

The version command shows the current version of the `credmark-model-framework`:

```
$ credmark-dev version
credmark-model-framework version 0.0.0
```

**Note:** the commands `build` and `clean` do not need to be used during model development.

(console_section)=

## Interactive Model Console

You can run an interactive python console with a model context using the command:

```
credmark-dev run console
```

This is useful to interactively develop and test models.

Within the console you can execute python commands interactively in the same environment as a model's `run()` method. The standard model properties are available such as `self.context` and `self.logger`, as well as some shortcuts and utility functions.

For more info on commands, enter `self.help()` in the console.

### Using the Console

The use the console to run small utilities or interactively test portions of model code.

The following are some examples:

#### Get current context block number

```
In [1]: block_number
Out[1]: 14000000

In [2]: block_number.timestamp_datetime
Out[2]: datetime.datetime(2022, 1, 13, 22, 59, 55, tzinfo=datetime.timezone.utc)
```

#### Get a block number for a timestamp

Get the {class}`~credmark.cmf.types.block_number.BlockNumber` for a timestamp at or before 2022-01-01 10:30:00 UTC

```
In [1]: bn = get_block(get_dt(2022,1,1,10,30,00))

In [2]: bn
Out[2]: 13919019

In [3]: bn.timestamp_datetime
Out[3]: datetime.datetime(2022, 1, 1, 10, 29, 56, tzinfo=datetime.timezone.utc)
```

#### Query the ledger

```
In [1]: ledger.get_blocks(columns=[BlockTable.Columns.NUMBER, BlockTable.Columns.TIMESTAMP], order_by=f'{BlockTable.Columns.NUMBER} desc', limit='5')

Out [1]: LedgerModelOutput(data=[{'number': 14000000, 'timestamp': 1642114795}, {'number': 13999999, 'timestamp': 1642114789}, {'number': 13999998, 'timestamp': 1642114786}, {'number': 13999997, 'timestamp': 1642114763}, {'number': 13999996, 'timestamp': 1642114759}])
```

#### Get info on a model

```
# Press tab for autocomplete list:
# In [1]: models.aave_v2

In [1]: models.aave_v2.get_lending_pool.description
Out[1]: 'Aave V2 - Get lending pool for main market'

# Get docs for model:

In [2]: models.aave_v2.get_lending_pool?
Out[2]: Call signature:
models.aave_v2.get_lending_pool(
    input: Union[pydantic.main.BaseModel, dict, NoneType] = None,
    return_type=None,
    **kwargs,
) -> dict
Type:           RunModelMethod
String form:    <credmark.cmf.model.context.RunModelMethod object at 0x12463f310>
File:           ~credmark/cmf/model/context.py
Docstring:
aave-v2.get-lending-pool
- slug: aave-v2.get-lending-pool
- displayName: aave-v2.get-lending-pool
- description: Aave V2 - Get lending pool for main market
- developer:
- input schema (* for required field):
  EmptyInput(object)
- input example:
  #01: {}
- output schema (* for required field):
  Contract(Contract(*))
    └─address(string)
- output example:
  #01: {"address": "0x1F98431c8aD98523631AE4a59f267346ea31F984"}
- errors:
  No defined errors

# If the model is local, you can get the input and output DTO classes:

In [3]: models.aave_v2.get_lending_pool.inputDTO
Out[3]: credmark.dto.EmptyInput

In [4]: models.aave_v2.get_lending_pool.outputDTO
Out[4]: credmark.cmf.types.contract.Contract

In [5]: models.token.price.inputDTO
Out[5]: credmark.cmf.types.token.Token

In [6]: models.token.price.inputDTO(symbol='CMK')
Out[6]: Token(address='0x68cfb82eacb9f198d508b514d898a403c449533e')

In [7]: models.token.price.outputDTO
Out[7]: credmark.cmf.types.price.Price
```

#### Run a model

```
In [1]: models.aave_v2.get_lending_pool()
Out[1]: {'address': '0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9'}
```

##### Run a model with parameters

```
In [1]: models.token.price(Token(symbol='CMK'))
Out[1]: {'price': 0.30365299879260643,
 'src': 'token.price:sushiswap.get-pool-price-info|uniswap-v3.get-pool-price-info'}

# Or use args to get the same result:
In [2]: models.token.price(symbol='CMK')
Out[2]: {'price': 0.30365299879260643,
 'src': 'token.price:sushiswap.get-pool-price-info|uniswap-v3.get-pool-price-info'}
```

##### Run a model and get a DTO result

```
In [2]: models.token.price(Token(symbol='CMK'), return_type=Price)
Out[2]: Price(price=0.30365299879260643, src='token.price:sushiswap.get-pool-price-info|uniswap-v3.get-pool-price-info')

# Or another way to get the same result:
In [2]: Price(**models.token.price(Token(symbol='CMK')))
Out[2]: Price(price=0.30365299879260643, src='token.price:sushiswap.get-pool-price-info|uniswap-v3.get-pool-price-info')
```

#### Switch context to an earlier block number

```
In [1]: self.goto_block(13000000)

Switching context to block 13000000.
Quit current context: quit()

In [2]: block_number
Out[2]: 13000000

In [3]: quit()

Exiting context at block 13000000.
Current context at block 14000000. Remaining block stack [].
```

### Console Configuration

You can configure the console to automatically import extra modules and classes by using a `credmark_dev_console.yaml` file in your working directory.

The yaml file can have an `imports` object that contains:

- `modules`: a list of objects containing:

  - `name`: full name of module to import) and optional
  - `as`: name to assign module to.

- `globals`: a list of strings containing the full module name followed by dot and the name of the symbol in the module. Ex. `models.credmark.protocols.lending.aave.aave_v2.AaveDebtInfo`

An example `credmark_dev_console.yaml` file:

```yaml
imports:
  modules:
    - name: numpy
      as: np
    - name: pandas
      as: pd
    - name: matplotlib.pyplot
      as: plt
  globals:
    - models.credmark.protocols.lending.aave.aave_v2.AaveDebtInfo
    - models.credmark.protocols.lending.aave.aave_v2.AaveDebtInfos
```
