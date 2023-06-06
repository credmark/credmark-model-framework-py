import logging
import unittest
from typing import Union

from dotenv import find_dotenv, load_dotenv

from credmark.cmf.engine.cache import ModelRunCache
from credmark.cmf.engine.context import EngineModelContext
from credmark.cmf.engine.mocks import ModelMockConfig, ModelMockRunner
from credmark.cmf.engine.model_api import ModelApi
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.cmf.engine.web3_registry import Web3Registry
from credmark.cmf.model.context import ModelContext


class ModelTestContextFactory:
    # Helps with configuring unittest mocks and contexts
    # A ModelTestContextFactory instance can be configured at startup
    # and set by calling use_factory().

    _factory: Union['ModelTestContextFactory', None] = None

    @classmethod
    def use_factory(cls, model_test_factory: 'ModelTestContextFactory'):
        cls._factory = model_test_factory

    @classmethod
    def factory(cls):
        if cls._factory is None:
            cls._factory = cls.create_default_factory()
        return cls._factory

    @classmethod
    def create_default_factory(cls):
        load_dotenv(find_dotenv('.env.test', usecwd=True))
        chain_to_provider_url = Web3Registry.load_providers_from_env()
        model_loader = ModelLoader(['models', 'tests'], load_dev_models=True)
        return ModelTestContextFactory(model_loader, chain_to_provider_url)

    def __init__(self,
                 model_loader: Union[ModelLoader, None] = None,
                 chain_to_provider_url: Union[dict[str, str], None] = None,
                 api_url: Union[str, None] = None):

        if model_loader is None:
            model_loader = ModelLoader(['.'])

        self.model_loader = model_loader
        self.api = ModelApi.api_for_url(api_url)

        self.web3_registry = Web3Registry(chain_to_provider_url)

        EngineModelContext.dev_mode = True
        EngineModelContext.test_mode = True

        EngineModelContext.use_local_models_slugs.update(
            model_loader.loaded_dev_model_slugs())

    def create_context(self,
                       chain_id: int = 1,
                       block_number: int = 16_960_851):
        # Clear the current context first
        ModelContext.set_current_context(None)

        model_cache = ModelRunCache(enabled=False)

        context = EngineModelContext(
            chain_id, block_number, self.web3_registry,
            'test', 0, self.model_loader, model_cache,
            self.api, is_top_level=True)

        context.__dict__['original_input'] = {}
        context.__dict__['slug'] = 'test'

        ModelContext.set_current_context(context)

        return context

    def clear_context(self):
        ModelContext.set_current_context(None)

    def use_mocks(self, mocks: Union[ModelMockConfig, None] = None):
        if mocks is not None:
            mock_runner = ModelMockRunner()
            mock_runner.add_mock_configuration(mocks)
            EngineModelContext.use_model_mock_runner(mock_runner)
        else:
            EngineModelContext.use_model_mock_runner(None)


def model_context(chain_id: int = 1,
                  block_number: int = 16_960_851,
                  mocks: Union[ModelMockConfig, None] = None):
    """
    A decorator that can be used on a test method in a
    ModelTestCase subclass to configure the context and
    mocks to use during the test.

    Example::

        @model_context(block_number=5000)
        def test_model(self):
            # self.context.block_number == 5000

    """
    def _deco(func):
        def _wrapper(self, *args, **kwargs):
            factory = ModelTestContextFactory.factory()
            factory.use_mocks(mocks)
            self.context = factory.create_context(chain_id, block_number)
            self.logger.debug('%s.%s using context chain_id=%d block_number=%d' %
                              (self.__class__.__name__, func.__name__, chain_id, block_number))
            return func(self, *args, **kwargs)
        return _wrapper
    return _deco


class ModelTestCase(unittest.TestCase):
    """
    A superclass for unittest TestCase instances that
    use framework classes and call other models.

    A ModelTestCase has a default context defined during
    the tests which is available at ``self.context``.

    To configure a specific context and mocks for a test,
    it is recommended to use the
    :func:`~credmark.cmf.engine.model_unittest.model_context`
    decorator on test_methods.

    Example::

        @model_context(block_number=5000)
        def test_model(self):
            # self.context.block_number == 5000

    Alternatively, a test method can use the ``self.create_model_context()``
    to create a new context and set mocks during a test.
    """

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

    def setUp(self):
        super().setUp()
        self.create_model_context()

    def tearDown(self) -> None:
        ModelTestContextFactory.factory().clear_context()
        return super().tearDown()

    def create_model_context(self,
                             chain_id: int = 1,
                             block_number: int = 16_960_851,
                             mocks: Union[ModelMockConfig, None] = None):
        """
        Create a new model context and set it as the current context.
        """
        factory = ModelTestContextFactory.factory()
        factory.use_mocks(mocks)
        self.context = factory.create_context(chain_id, block_number)
        self.logger.debug('%s using context chain_id=%d block_number=%d' %
                          (self.__class__.__name__, chain_id, block_number))

    @property
    def context(self):
        """
        Gets the context. If it doesn't exist, a default context will
        be created.
        Use the :func:`~credmark.cmf.engine.model_unittest.model_context`
        decorator or call ``self.create_model_context()`` to configure
        a context.
        """
        if self.__context is None:
            self.create_model_context()
        return self.__context

    @context.setter
    def context(self, value):
        self.__context = value
