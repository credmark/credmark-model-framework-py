import logging
from typing import Union
from unittest import TestCase

from credmark.cmf.engine.context import EngineModelContext
from credmark.cmf.engine.model_api import ModelApi
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.cmf.engine.web3 import Web3Registry
from credmark.cmf.model.context import ModelContext
from dotenv import find_dotenv, load_dotenv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level='INFO')


class ContextTestCase(TestCase):
    """
    Test Case with Model Context.

    You can set block_number and chain id for context by overriding
    `context` and `context_chain_id` class methods

    ```
    @classmethod
    def context_block_number(cls) -> Union[None, int]:
        return 12345678

    @classmethod
    def context_chain_id(cls) -> int:
        return 1
    ```

    Some configuration is done with environment variables. They can be set
    in your shell or a `.env.test` file, which can be created at the root folder
    of the cloned repository.

    The `CREDMARK_WEB3_PROVIDER_CHAIN_ID_{N}` is a JSON object where the keys are
    chain ids (as strings) and the values are URLs to HTTP providers.

    Set {N} with a chain id, for example `CREDMARK_WEB3_PROVIDER_CHAIN_ID_1` and
    set the value as the URL of the HTTP provider.

    For example, a `.env` file can contain the following:

    ```
    CREDMARK_WEB3_PROVIDER_CHAIN_ID_1=https://eth-mainnet.alchemyapi.io/v2/ABC123
    CREDMARK_WEB3_PROVIDER_CHAIN_ID_137=https://polygon-mainnet.g.alchemy.com/v2/ABC123
    ```

    ALTERNATIVELY you may set all your providers in a single env var:

    For example, a `.env.test` file can contain the following:

    ```
    CREDMARK_WEB3_PROVIDERS='{1:"https://eth-mainnet.alchemyapi.io/v2/ABC123"}'
    ```

    This variable is used to run tests which require web3. It can be ignored
    for those tests which do not require web3.

    Use self.logger to access logger.
    """

    _context: EngineModelContext
    logger: logging.Logger

    @classmethod
    def context_block_number(cls) -> Union[None, int]:
        return None

    @classmethod
    def context_chain_id(cls) -> int:
        return 1

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(__name__)

        load_dotenv(find_dotenv('.env.test', usecwd=True))
        chain_to_provider_url = Web3Registry.load_providers_from_env()

        model_loader = ModelLoader(['tests'], load_dev_models=True)
        api = ModelApi.api_for_url(None)
        web3_registry = Web3Registry(chain_to_provider_url)

        chain_id = cls.context_chain_id()
        depth = 1
        run_id = 'test-run'
        block_number = cls.context_block_number()
        if block_number is None:
            block_number = EngineModelContext.get_latest_block_number(api, chain_id)
        logging.info(f'Using latest block number {block_number}')

        context = EngineModelContext(
            chain_id, block_number, web3_registry,
            run_id, depth, model_loader, api, True)
        context.dev_mode = True
        #pylint: disable=protected-access
        ModelContext._current_context = context
        cls._context = context
        cls._context.is_active = True

    @classmethod
    def tearDownClass(cls):
        if cls._context is not None:
            cls._context.is_active = False
            #pylint: disable=protected-access
            ModelContext._current_context = None
