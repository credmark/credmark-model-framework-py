# Quickstart

(Quickstart)=

## Prerequisites

- [Python 3.9+](https://www.python.org/downloads/) or [Miniconda 4.10+](https://docs.conda.io/en/latest/miniconda.html) installed
- Personal web3 provider url ([Alchemy](https://docs.alchemy.com/alchemy/introduction/getting-started) or other) if you need to use your own web3 provider instance to run any model
- [Visual studio 2019+](https://visualstudio.microsoft.com/de/downloads/) installed for Windows users

## Fork Repository

Fork [credmark-models-py](https://github.com/credmark/credmark-models-py) repository

## Virtual Env

Create a virtual env (if you want):

```
python3 -m venv venv
source venv/bin/activate
```

If you wish, you can run it on miniconda. Simply install the miniconda version mentioned in the prerequisite, open Anaconda prompt, navigate to the repo folder and continue with steps (commands) as mentioned below.

## Install Dependencies

Then run:

```
pip install -r requirements.txt
```

For development, you can also run:

```
pip install -r requirements-dev.txt
```

## Configure environment variables

Some configuration is done with environment variables. They can be set in your shell or a `.env` file, which can be created at the root folder of the cloned repository.

**Environment variables**

The `CREDMARK_WEB3_PROVIDER_CHAIN_ID_{N}` is a JSON object where the keys are chain ids (as strings) and the values are URLs to HTTP providers.

Set {N} with a chain id, for example `CREDMARK_WEB3_PROVIDER_CHAIN_ID_1` and set the value as the URL of the HTTP provider.

For example, a `.env` file can contain the following:

```
CREDMARK_WEB3_PROVIDER_CHAIN_ID_1=https://eth-mainnet.alchemyapi.io/v2/ABC123
CREDMARK_WEB3_PROVIDER_CHAIN_ID_137=https://polygon-mainnet.g.alchemy.com/v2/ABC123
```

**ALTERNATIVELY** you may set all your providers in a single env var:

For example, a `.env` file can contain the following:

```
CREDMARK_WEB3_PROVIDERS='{1:"https://eth-mainnet.alchemyapi.io/v2/ABC123","137":"https://polygon-mainnet.g.alchemy.com/v2/ABC123"}'
```

This variable is used to run models which require web3. It can be ignored for those models which do not require web3.

**_NOTE_**: The web3 providers are used during local development. When a model is deployed it automatically uses Credmark's provider node.
