from abc import abstractmethod
import io
from typing import Any, Type, TypeVar, Union, overload
from web3 import Web3

from .print import print_manifest_description
from .errors import ModelNoContextError
from .ledger import Ledger
import credmark.cmf.types
from credmark.dto import DTOType, DTOTypesTuple, EmptyInput
from .utils.historical_util import HistoricalUtil

DTOT = TypeVar('DTOT')


class RunModelMethod:
    # This class is used interally by the context.

    # A run model method is callable (where the prefix is the actual
    # model name) or called with a method name (where prefix is the
    # dot prefix of the model name.)

    # If this is set to true for the class, the doc string
    # for an instance will be set to the model schema doc
    interactive_docs = False

    def __init__(self, context, prefix: str, block_number: Union[int, None] = None):
        self.__context = context
        self.__prefix = prefix
        self.__block_number = block_number

        if self.interactive_docs:
            # In interactive mode, we set the docstring to the
            # manifest doc for the model
            manifest = self.__context._model_manifests(True).get(prefix)
            if manifest is not None:
                doc = io.StringIO()
                print_manifest_description(manifest, doc)
                self.__doc__ = doc.getvalue()
                doc.close()
            else:
                slugs = [s for s in self.__context._model_manifests(True).keys()
                         if s.startswith(prefix)]
                slugs.sort()
                self.__doc__ = f'Run a model.\n\nAvailable models: {", ".join(slugs)}'

    # run a model. args can be a positional DTO or dict or kwargs
    @overload
    def __call__(self,
                 input: Union[DTOType, dict, None] = None,
                 return_type: Union[dict, None] = None,
                 **kwargs) -> dict:
        ...

    @overload
    def __call__(self,
                 input: Union[DTOType, dict, None] = None,
                 return_type: Type[DTOType] = EmptyInput,
                 **kwargs) -> DTOType:
        ...

    def __call__(self,
                 input: Union[DTOType, dict, None] = None,
                 return_type: Union[dict, Type[DTOType], None] = None,
                 **kwargs) -> Union[dict, DTOType]:
        if isinstance(input, DTOTypesTuple):
            input = input.dict()
        elif input is None:
            input = kwargs

        return self.__context.run_model(
            f"{self.__prefix.replace('_', '-')}",
            input, block_number=self.__block_number,
            return_type=return_type)

    # Handle method calls where the prefix is the dot prefix of a model name

    def __getattr__(self, __name: str):
        if self.interactive_docs:
            model_manifests: dict = self.__context._model_manifests(True)
            # If prefix matches a complete slug we allow access to
            # manifest fields and model class properties.
            if self.__prefix in model_manifests:
                if __name in model_manifests[self.__prefix]:
                    return model_manifests[self.__prefix][__name]
                else:
                    mclass = self.__context._class_for_model(self.__prefix.replace('_', '-'))
                    if mclass is not None:
                        mclassdict = vars(mclass)
                        if __name in mclassdict:
                            return mclassdict[__name]

        return RunModelMethod(
            self.__context, f"{self.__prefix}.{__name}",
            block_number=self.__block_number)

    def __dir__(self):
        if self.interactive_docs:
            # For ipython tab-complete
            model_manifests: dict = self.__context._model_manifests(True)

            if self.__prefix in model_manifests:
                mclass = self.__context._class_for_model(self.__prefix.replace('_', '-'))
                fields = list(model_manifests[self.__prefix].keys())
                if mclass is not None:
                    # allow autocomplete for some model class properties
                    fields.extend(['inputDTO', 'outputDTO'])
                fields.sort()
                return fields

            prefix = self.__prefix + '.'
            prefix_len = len(prefix)
            slugs = [s[prefix_len:]
                     for s in self.__context._model_manifests(True).keys() if s.startswith(prefix)]
            slugs.sort()
            return slugs
        else:
            return super().__dir__()


class ModelContext:
    """
    Model context class. It holds the current context (chain id
    and block number) as well as helpers for getting ledger data,
    running other models both individually and historically over a
    series of blocks, looking up contracts, and accessing a web3
    node.

    You can access an instance of this class from a model
    as ``self.context``.
    """
    _current_context: Union['ModelContext', None] = None

    @classmethod
    def current_context(cls) -> 'ModelContext':
        """
        Get the current context and raise a ModelNoContextError
        exception if there is no current context.
        """
        context = cls._current_context
        if context is None:
            raise ModelNoContextError("No current ModelContext")
        return context

    @classmethod
    def get_current_context(cls) -> Union['ModelContext', None]:
        """
        Get the current context, which could be None.
        Normally you should use current_context() instead.
        """
        return cls._current_context

    @classmethod
    def set_current_context(cls, context: Union['ModelContext', None]):
        """
        Set the current context, which could be None.
        Normally you should not use this method.
        """
        cls._current_context = context

    class Models:
        """
        """

        def __init__(self, context, block_number: Union[int, None] = None):
            self.__context = context
            self.__block_number = block_number

        def __getattr__(self, __name: str) -> RunModelMethod:
            return RunModelMethod(self.__context, __name, block_number=self.__block_number)

        def __call__(self, block_number=None):
            return ModelContext.Models(self.__context, block_number=block_number)

        def __dir__(self):
            if RunModelMethod.interactive_docs:
                # For ipython tab-complete
                slugs = list(self.__context._model_manifests(True).keys())
                slugs.sort()
                return slugs
            else:
                return super().__dir__()

        def reload(self):
            if RunModelMethod.interactive_docs:
                self.__context._model_reload()  # pylint: disable=protected-access

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
            self._models = ModelContext.Models(self)
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
    def chain_id(self):
        """
        Context chain id as an integer
        """
        return self._chain_id

    @property
    def block_number(self):
        """
        Context block number. A credmark.cmf.types.BlockNumber instance.
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: int):
        self._block_number = credmark.cmf.types.BlockNumber(block_number)

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
            self._ledger = Ledger(self)
        return self._ledger

    @property
    def historical(self) -> HistoricalUtil:
        """
        A :class:`~credmark.cmf.model.utils.historical_util.HistoricalUtil`
        instance which can be used to run a model over a series of blocks based
        on time or block intervals.
        """
        if self._historical_util is None:
            self._historical_util = HistoricalUtil(self)
        return self._historical_util

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTOType],
                  return_type: Type[DTOT],
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None,
                  ) -> DTOT: ...

    @overload
    @abstractmethod
    def run_model(self,
                  slug: str,
                  input: Union[dict, DTOType] = EmptyInput(),
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
