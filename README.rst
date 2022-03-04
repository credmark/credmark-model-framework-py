===============================
credmark-model-framework
===============================

Credmark Model Framework for developing models in python.

For information on how to build models, see the `credmark-models-py repo <https://github.com/credmark/credmark-models-py>`_

Install
-------

.. code-block:: bash

    $ pip install credmark-model-framework


Configuration
-------------

Some configuration is done with environment variables.
They can be set in your shell or a ``.env`` file.

Environment variables:

- Web3 Providers

If you are using web3 in your models, you can set environment variables
for the providers. You must use your own provider URLs. This is not required if your model does not use web3.

Set a variable for each Chain Id you wish to use:

```CREDMARK_WEB3_PROVIDER_CHAIN_ID_{N}`` [OPTIONAL] Set {N} with a chain id, for example
CREDMARK_WEB3_PROVIDER_CHAIN_ID_1 and set the value as the URL of the HTTP provider.

For example, a ``.env`` file can contain the following:

.. code-block:: bash

    CREDMARK_WEB3_PROVIDER_CHAIN_ID_1=https://eth-mainnet.alchemyapi.io/v2/ABC123
    CREDMARK_WEB3_PROVIDER_CHAIN_ID_137=https://polygon-mainnet.g.alchemy.com/v2/ABC123


ALTERNATIVELY you may set all your providers in a single env var:

```CREDMARK_WEB3_PROVIDERS`` [OPTIONAL] is a JSON object where the keys are chain ids
(as strings) and the values are URLs to HTTP providers.

For example, a ``.env`` file can contain the following:

.. code-block:: bash

    CREDMARK_WEB3_PROVIDERS={"1":"https://eth-mainnet.alchemyapi.io/v2/ABC123","137":"https://polygon-mainnet.g.alchemy.com/v2/ABC123"}

