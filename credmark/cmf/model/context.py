from abc import abstractmethod
from contextvars import ContextVar, Token
from typing import Any, Type, TypeVar, Union, overload

import credmark.cmf.types
from credmark.dto import DTOType, EmptyInput
from web3 import Web3

from .errors import ModelNoContextError
from .ledger import Ledger
from .models import Models
from .utils.historical_util import HistoricalUtil

DTOT = TypeVar('DTOT')
MaybeModelContext = Union['ModelContext', None]


class ModelContext:
    """
    Model contexts class. It holds the current context (chain id
    and block number) as well as helpers for getting ledger data,
    running other models both individually and historically over a
    series of blocks, looking up contracts, and accessing a web3
    node.

    Current context uses contextvars to ensure setting and getting
    context is safe when using concurrent code. It can be used with
    either threads or asyncio.

    You can access an instance of this class from a model
    as ``self.context``.
    """

    __current_context: ContextVar[MaybeModelContext] = ContextVar('context', default=None)

    @classmethod
    def get_current_context(cls) -> MaybeModelContext:
        """
        Get the current context, which could be None.
        Normally you should use current_context() instead.
        """
        return cls.__current_context.get()

    @classmethod
    def set_current_context(cls, context: MaybeModelContext) -> Token[MaybeModelContext]:
        """
        Set the current context, which could be None.
        Normally you should not use this method.
        """
        return cls.__current_context.set(context)

    @classmethod
    def reset_current_context(cls, token: Token[MaybeModelContext]):
        """
        Reset the context to the value it had before
        `ModelContext.set_current_context` was called.

        Pass the token returned by `ModelContext.set_current_context`
        method
        """
        cls.__current_context.reset(token)

    @classmethod
    def current_context(cls) -> 'ModelContext':
        """
        Get the current context and raise a ModelNoContextError
        exception if there is no current context.
        """
        context = cls.get_current_context()
        if context is None:
            raise ModelNoContextError("No current ModelContext")
        return context

    def __init__(self, chain_id: int, block_number: int,
                 web3_registry):
        self._chain_id = chain_id
        self._block_number = credmark.cmf.types.BlockNumber(block_number)
        self._web3 = None
        self._web3_registry = web3_registry
        self._ledger = None
        self._historical_util = None
        self._models = None

    @property
    def models(self):
        """
        The ``context.models`` attribute can be used to run models with a method
        call, with any ``-`` in the model slug replaced with ``_``.

        For example:

        - ``context.run_model('example.model')`` becomes ``context.models.example.model()``
        - ``context.run_model('example.ledger-blocks')`` becomes
          ``context.models.example.ledger_blocks()``
        - ``context.run_model('var-model')`` becomes ``context.models.var_model()``

        The input that you pass to ``context.run_model()`` can be
        passed to the method call as keyword (named) args, for example::

            output = context.models.rpc.get_blocknumber(timestamp=1438270017)

        Or as an input ``DTO`` or dict::

            output = context.models.example.model(input_dto)

        You can use the run output to create an output DTO::

            output = EchoDto(**context.models.example.model(input_dto))

        You can run a model with a context of a block number (it must be lower than the
        block number of the current context) by calling the ``models`` instance with a
        ``block_number`` arg::

            output = context.models(block_number=123).example.model(input_dto)
        """
        if self._models is None:
            # The models instance can be used to run models like a method
            # We don't pass the block_number so it uses the default
            # (our context) block number.
            self._models = Models(self)
        return self._models

    @abstractmethod
    def _model_manifests(self, underscore_slugs=False) -> dict:
        # Context implementation will override this to return
        # a dict of slug to manifest dict containing available models.
        ...

    @abstractmethod
    def _class_for_model(self, slug: str, version: Union[str, None] = None):
        # Context implementation will override this to return
        # the model class for a slug. If the model is not available locally
        # it will return None.
        ...

    @property
    def chain_id(self) -> int:
        """
        Context chain id as an integer
        """
        return self._chain_id

    @property
    def network(self) -> credmark.cmf.types.Network:
        """
        Context chain id as an integer
        """
        return credmark.cmf.types.Network(self._chain_id)

    @property
    def block_number(self):
        """
        Context block number. A credmark.cmf.types.BlockNumber instance.
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: int):
        if block_number != self._block_number:
            self._block_number = credmark.cmf.types.BlockNumber(block_number)
            self._web3 = None
            self._ledger = None
            self._historical_util = None

    @property
    def web3(self) -> Web3:
        """
        A configured web3 instance
        """
        if self._web3 is None:
            self._web3 = self._web3_registry.web3_for_chain_id(self.chain_id)
            self._web3.eth.default_block = self.block_number if \
                self.block_number is not None else 'latest'
        return self._web3

    @property
    def ledger(self) -> Ledger:
        """
        A :class:`~credmark.cmf.model.ledger.Ledger` instance which can be
        used to query the ledger for data.
        """
        if self._ledger is None:
            self._ledger = Ledger()
        return self._ledger

    @property
    def historical(self) -> HistoricalUtil:
        """
        A :class:`~credmark.cmf.model.utils.historical_util.HistoricalUtil`
        instance which can be used to run a model over a series of blocks based
        on time or block intervals.
        """
        if self._historical_util is None:
            self._historical_util = HistoricalUtil()
        return self._historical_util

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTOType],
                  return_type: Type[DTOT],
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  local: bool = False
                  ) -> DTOT: ...

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTOType] = EmptyInput(),
                  return_type: Union[Type[dict], None] = None,
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  local: bool = False
                  ) -> dict: ...

    @abstractmethod
    def run_model(self,  # type: ignore
                  slug,
                  input=EmptyInput(),
                  return_type=None,
                  block_number=None,
                  version=None,
                  local: bool = False
                  ) -> Any:
        """
        Run a model by slug and optional version.

        In order for models to be consistently deterministic, the **ONLY** type
        of error a model should catch and handle from a call to ``run_model()``
        is a ``ModelDataError``, which is considered a permanent error for the
        given conext. All other errors are considered transient, coding errors,
        or conditions that may change in the future.

        Parameters:
            slug (str): the slug of the model
            input (dict | DTO): an optional dictionary or DTO instance of
                  input data that will be passed to the model when it is run.
            block_number (int | None): optional block number to use as context.
                  If None, the block_number of the current context will be used.
            version (str | None): optional version of the model.
                  If version is None, the latest version of
                  the model is used. Use of this paramater is NOT recommended.
            return_type (DTO Type | None): optional class to use for the
                  returned output data. If not specified, returned value is a dict.
                  If a DTO specified, the returned value will be an instance
                  of that class if the output data is compatible with it. If its not,
                  an exception will be raised.

        Returns:
            The output returned by the model's run() method as a dict
            or a DTO instance if return_type is specified.

        Raises:
            ModelDataError: A catchable permanent error.
            ModelRunError: A non-permanent run error. Should not be caught.
            ModelNotFoundError: Requested model was not found. Should not be caught.
            ModelBaseError: other subclasses of ``ModelBaseError`` that should not be caught.

        """
