# credmark-model-framework-py

This repo contains the code for the `credmark-model-framework` python package.

For information on how to build models, see the [credmark-models-py repo](https://github.com/credmark/credmark-models-py)

## Install

```
pip install git+https://github.com/credmark/credmark-model-framework-py.git@main
```

## Build During Development

```
python setup.py sdist
```


## SDK Core Components 

### Model Components

In the following you will find the key components of every model.

#### Model Class

Credmark uses a simple base class called ‘Model’ class to set up a model. The actual code can be found [here](https://github.com/credmark/credmark-model-sdk-py/blob/main/credmark/model/base.py).

All Models should import this class ```import credmark.model``` and can override the run() method. See examples [here](https://github.com/credmark/credmark-models-py/tree/main/models/examples).

This class provides a simple interface to define model properties (decorator) such as slug, version, display_name, description, developer, input, output etc so that it can be used easily by other models and is immediately accessible via the api.

Simply use ```@credmark.model.describe()``` to define these decorative properties. See example [here](https://github.com/credmark/credmark-models-py/blob/main/models/examples/address_examples.py).

#### Model Context Class

This class sets up the context for the model to run. The base code can be found [here](https://github.com/credmark/credmark-model-sdk-py/blob/main/credmark/model/context.py).

This enables any model to be composable and run for any context. This also enforces deterministic behavior for Models. 
The key utilities in  Model-Context are below.

##### Contract

Credmark simplified the process of getting web3 instances of any contract from any chain. So you don't need to find and hardcode chain specific attributes and functions within these chains to run your models. 
To get the web3 instance, ‘ModelContext’ class simply uses ‘Contract’ class to return an object (based on input parameters provided)  which includes data of the web3 instance at specified block number and specified chain id along with additional data based on ```constructor_args```.

Code for contact class can be found [here](https://github.com/credmark/credmark-model-sdk-py/blob/main/credmark/types/data/contract.py).

Currently below parameters as argument are supported to fetched using Contracts:
- name: name of the contract
- address: address of the contract
- deploy_tx_hash: transaction hash at which contract was deployed
- Constructor_args
- protocol: protocol name
- product: product name
- abi_hash
- abi

Tip: the contract object returned from contract class can be reused to fetch any specific web3 attributes of the contract and to develop a model on top of that.

##### Ledger

Credmark allows access to in-house blockchain ledger data via ledger interface so that any model can fetch/use ledger data if required. This is done via ‘Ledger’ class which currently supports below functions:
- get_transactions
- get_traces
- get_logs
- get_contracts
- get_blocks
- get_receipts
- get_erc20_tokens
- get_erc20_transfers

Please refer [here](https://github.com/credmark/credmark-model-sdk-py/blob/main/credmark/model/ledger/ledger.py) for the code of the ledger class.

##### Web3

Web3Registry class is used to read the web3 provided parameter from .env file and allow contract class to fetch the data from the web3 provider. Code for web3 can be found [here](https://github.com/credmark/credmark-model-sdk-py/blob/main/credmark/model/web3/registry.py).

Currently users will need to use their own alchemy account (or other web3 provider) to access web3 functionality.

##### Block Number

block_number class allows the provided block numbers to be treated as integer and hence enables arithmetic operations on block number. This class also allows to fetch datetime and timestamp properties of the blocknumber. This can be super useful in case we want to run any model iteratively for a certain block-interval or time-interval backwards to the block number provided in the original argument in ```-b``` while running the model.

The Code for block-number class can be found [here](https://github.com/credmark/credmark-model-sdk-py/blob/main/credmark/types/data/block_number.py).

#### DTO

Input and output for the model are defined in DTOs. DTOs decipher the input parameters (json objects) for the model to run. Each model may have their own DTOs or may inherit DTO from another model.
Note that Input to a model is a json-serializable object of arbitrary depth and complexity. Objects can have 0 or more keys whose values can be null, number, string, array, or another object.

## SDK CLI

All commands accept ```-h``` parameter for help, e.g.:

```
credmark-dev -h
```

