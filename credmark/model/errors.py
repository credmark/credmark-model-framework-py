from typing import Union
from pydantic import BaseModel as DTO, Field as DTOField


# If you subclass this, you MUST add a doc string to your subclass
# or it will reuse this one.
class ModelBaseErrorDTO(DTO):
    """
    The base error type that other errors inherit from.

    The main error types are:
     - ModelDataError: An error that occurs during the lookup, generation,
       or processing of data. It is not an error in the code but an
       but an unexpected situation with the data. For example, a request
       for a contract at an address that does not exist will return a
       ModelDataError. This error is considered deterministic and permanent,
       in the sense that for the given context, the same error will always occur.

     - ModelRunError: An error that occurs during the running of a model.
       This error is usually related to a model coding error or
       not properly handling exceptions from web3, math libraries etc.
       These errors are considered transient because it is expected
       they could give a different result if run again, for example
       if the code was fixed or a web3 connection issue was resolved etc.

     - ModelEngineError: An error occurred in the model running engine.
       These errors are considered transient because they usually
       relate to network or resource issues.
    """
    type: str = DTOField(..., description='Error type')
    message: str = DTOField(..., description='Error message')


class ModelBaseError(Exception):
    """
    Base error class for Credmark model errors.
    You should not create instances of this class directly.

    Subclasses can create a custom DTO class and set the
    dto_class property. They should override the __init__
    method with extra params (as needed) and **kwargs
    (for safety) and call super() with the extra args defined
    in the dto. See ModelDataError for an example.
    """
    class_map = {}

    dto_set = set()

    # subclasses can set this to add more data to the error
    dto_class = ModelBaseErrorDTO

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.class_map[cls.__name__] = cls
        cls.dto_set.add(cls.dto_class)

    @classmethod
    def class_for_name(cls, name: str):
        return cls.class_map.get(name)

    @classmethod
    def error_schemas(cls):
        schemas = []
        for dto in cls.dto_set:
            s = dto.schema()
            # Remove DTO from the titles
            # so they match the error types/classnames
            title: str = s['title']
            if title.endswith('DTO'):
                s = s.copy()
                title = title[:-3]
                s['title'] = title
            schemas.append(s)
        return schemas

    def __init__(self, message: str, **data):
        super().__init__(message)
        self.data = self.dto_class(type=self.__class__.__name__,
                                   message=message, **data)

    def dict(self):
        return self.data.dict()

    def json(self):
        return self.data.dict()


class ModelDataErrorDTO(ModelBaseErrorDTO):
    """
    An error that occurs during the lookup, generation, or
    processing of data this is considered deterministic and
    permanent, in the sense that for the given context, the
    same error will always occur.

    A model may raise a ModelDataError in situations such as:
     - the requested data does not exist or is not available for
       the current context block number.
     - the input data is incomplete, references non-existent
       items, or cannot be processed

    A model may (and often should) catch and handle ModelDataErrors
    raised from running a model.
    """
    code: str = DTOField(..., description='Short identifier for the type of error')
    data: Union[dict, None] = DTOField(
        None, description='Arbitrary data related to the error')
    chainId: int = DTOField(1, description='Context chain id')
    blockNumber: int = DTOField(..., description='Context block number')


class ModelDataError(ModelBaseError):
    """
    An error that occurs during the lookup, generation, or
    processing of data this is considered deterministic and
    permanent, in the sense that for the given context, the
    same error will always occur.

    A model may raise a ModelDataError in situations such as:
     - the requested data does not exist or is not available for
       the current context block number.
     - the input data is incomplete, references non-existent
       items, or cannot be processed

    A model may (and often should) catch and handle ModelDataErrors
    raised from calls to context.run_model().

    An easy way to raise from a model is: self.raise_data_error()
    """
    dto_class = ModelDataErrorDTO

    class ErrorCodes:
        GENERAL = 'general'
        NO_DATA = 'no_data'
        CONFLICT = 'conflict'
        INVALID_INPUT = 'invalid_input'

    # If adding parameters, give them default values for
    # backwards compatibility.
    def __init__(self,
                 message: str,
                 code: str,
                 chain_id: int,
                 block_number: int,
                 data: Union[dict, list, str, int, float, None] = None,
                 **_kwargs):
        super().__init__(message,
                         code=code,
                         chainId=chain_id,
                         blockNumber=block_number,
                         data=data)


class ModelRunError(ModelBaseError):
    """
    An error that occurs during the running of a model.
    If a model raises any unknown exception, it is automatically
    converted to a ModelRunError.

    This error is usually related to a model coding error or
    not properly handling exceptions from web3, math libraries etc.

    A ModelRunError will terminate the model run of a parent model.
    In most circumstances it is NOT recommended to catch these
    errors.

    These errors are considered transient because it is expected
    they could give a different result if run again, for example
    if the code was fixed or a web3 connection issue was resolved
    etc.
    """


class ModelInvalidStateError(ModelRunError):
    """
    A request was made that conflicts with the current context,
    for example context.run_model() was called with a block number higher
    than the block number of the current context.

    Although these errors are permanent for a given context,
    these are considered a logic or coding error.
    """


class ModelNoContextError(ModelRunError):
    """
    An attempt was made to use a core data object outside
    the context of a model run.
    """


class MaxModelRunDepthError(ModelRunError):
    """
    Models successively calling context.run_model() with nesting too deep.
    """


class ModelDefinitionError(ModelBaseError):
    """
    An error related to the definition of model code.
    These errors occur when a model is being loaded, not
    during model run requests.
    """


class ModelEngineError(ModelBaseError):
    """
    An error occurred before, during, or after a model run
    relating to the runner engine and not the model code itself.

    These errors are considered transient.
    """
