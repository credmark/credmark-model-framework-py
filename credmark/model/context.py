from abc import abstractmethod
from functools import partial
from typing import Any, ClassVar, Protocol, Type, TypeVar, Union, overload
from .ledger import Ledger
from .web3 import Web3Registry
import credmark.types
from credmark.dto import DTO, EmptyInput
from credmark.model.utils.contract_util import ContractUtil
from credmark.model.utils.historical_util import HistoricalUtil

DTOT = TypeVar('DTOT')


class RunModelProtocol(Protocol):
    # These are partials of the context.run_model() calls
    # The overloads match the run_model calls in ModelContext
    @overload
    def __call__(self,
                 input: Union[dict, DTO],
                 return_type: Type[DTOT],
                 block_number: Union[int, None] = None,
                 version: Union[str, None] = None,
                 ) -> DTOT:
        ...

    @overload
    def __call__(self,
                 input: Union[dict, DTO] = EmptyInput(),
                 return_type: Union[Type[dict], None] = None,
                 block_number: Union[int, None] = None,
                 version: Union[str, None] = None) -> dict:
        ...

    def __call__(self,  # type: ignore
                 input=EmptyInput(),
                 return_type=None,
                 block_number=None,
                 version=None,
                 ) -> Any:
        ...


class RunModelMethod:
    """
    A run model method is callable (where the prefix is the actual
    model name) or called with a method name (where prefix is the dot prefix
    of the model name.)
    """

    def __init__(self, context, prefix=None):
        self.__context = context
        self.__prefix = prefix

    # The __call__ overloads match the run_model calls in ModelContext
    # __call__ is used for model names that have no dot prefix
    @overload
    def __call__(self,
                 input: Union[dict, DTO],
                 return_type: Type[DTOT],
                 block_number: Union[int, None] = None,
                 version: Union[str, None] = None,
                 ) -> DTOT:
        ...

    @overload
    def __call__(self,
                 input: Union[dict, DTO] = EmptyInput(),
                 return_type: Union[Type[dict], None] = None,
                 block_number: Union[int, None] = None,
                 version: Union[str, None] = None) -> dict:
        ...

    def __call__(self, input=EmptyInput(),  # type: ignore
                 return_type=None,
                 block_number=None,
                 version=None,
                 ) -> Any:
        return self.__context.run_model(
            f"{self.__prefix.replace('_', '-')}",
            input, return_type, block_number, version)

    # Handle method calls where the prefix is the dot prefix of a model name
    def __getattr__(self, __name: str) -> RunModelProtocol:
        return partial(self.__context.run_model,
                       f"{self.__prefix}.{__name.replace('_', '-')}")


class ModelContext:
    """
    Model context class

    Instance attributes:
        chain_id (int): chain ID, ex 1
        block_number (int): default block number
        web3 (Web3): a configured web3 instance for RPC calls
        models: an object that has a virtual method for every model

    Methods:
        run_model(...) - run the specified model and return the results

    Running a model:

    The context.models instance can be used to run models with a method
    call, with any "-" in the model name replaced with "_".

    For example:
    - context.run_model('example.echo') becomes context.models.example.echo()
    - context.run_model('example.ledger-blocks') becomes context.models.example.ledger_blocks()
    - context.run_model('var-model') becomes context.models.var_model()

    The other args that you can pass to context.run_model() (besides slug) can
    passed to the method call, for example:
      context.models.rpc.get_blocknumber(input=dict(timestamp=1438270017))

    """
    current_context: ClassVar = None

    class Models:
        """
        An instance that can run any model by accessing it as a
        method with any "." or "-" in the model name replaced with "_".
        """

        def __init__(self, context):
            self.__context = context

        def __getattr__(self, __name: str) -> RunModelMethod:
            return RunModelMethod(self.__context, __name)

    def __init__(self, chain_id: int, block_number: int,
                 web3_registry: Web3Registry):
        # type hint
        ModelContext.current_context: Union[ModelContext, None]

        self.chain_id = chain_id
        self._block_number = credmark.types.BlockNumber(block_number)
        self._web3 = None
        self._web3_registry = web3_registry
        self._ledger = None
        self._contract_util = None
        self._historical_util = None

        # The models instance can be used to run models like a method
        self.models = ModelContext.Models(self)

    @property
    def block_number(self):
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: int):
        self._block_number = credmark.types.BlockNumber(block_number)

    @property
    def web3(self):
        if self._web3 is None:
            self._web3 = self._web3_registry.web3_for_chain_id(self.chain_id)
            self._web3.eth.default_block = self.block_number if \
                self.block_number is not None else 'latest'
        return self._web3

    @property
    def ledger(self) -> Ledger:
        if self._ledger is None:
            self._ledger = Ledger(self)
        return self._ledger

    @property
    def contracts(self) -> ContractUtil:
        if self._contract_util is None:
            self._contract_util = ContractUtil(self)
        return self._contract_util

    @property
    def historical(self) -> HistoricalUtil:
        if self._historical_util is None:
            self._historical_util = HistoricalUtil(self)
        return self._historical_util

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTO],
                  return_type: Type[DTOT],
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  ) -> DTOT: ...

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTO] = EmptyInput(),
                  return_type: Union[Type[dict], None] = None,
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  ) -> dict: ...

    @abstractmethod
    def run_model(self,  # type: ignore
                  slug,
                  input=EmptyInput(),
                  return_type=None,
                  block_number=None,
                  version=None,
                  ) -> Any:
        """Run a model by slug and optional version.

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
            ModelDataError, ModelRunError, ModelNotFoundError
            and various other sublasses of ModelBaseError.

            In order for models to be consistently deterministic,
            the ONLY type of error a model should catch and handle
            from a call to run_model() is a ModelDataError, which is
            considered a permanent error for the given conext.
            All other errors are considered transient, coding errors,
            or conditions that may change in the future.
        """
