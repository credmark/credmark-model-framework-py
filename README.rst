===============================
credmark-model-sdk
===============================

Credmark SDK for developing models in python

Install
-------

.. code-block:: bash

    $ pip install credmark-model-sdk


Configuration
-------------

Some configuration is done with environment variables.
They can be set in your shell or a ``.env`` file.

Environment variables:

```CREDMARK_WEB3_PROVIDERS`` [OPTIONAL] is a JSON object where the keys are chain ids
(as strings) and the values are URLs to HTTP providers. You must use your own
provider URLs. This is not required if your model does not use web3.

For example, a ``.env`` file can contain the following:

.. code-block:: bash

    CREDMARK_WEB3_PROVIDERS={"1":"https://eth-mainnet.alchemyapi.io/v2/ABC123","137":"https://polygon-mainnet.g.alchemy.com/v2/ABC123"}

