from typing import List, Type, Union, Generic, TypeVar
from pydantic import BaseModel as DTO, Field as DTOField
from pydantic.generics import GenericModel as GenericDTO
from .transform import transform_data_for_dto


class ModelCallStackEntry(DTO):
    """
    An item in an error's call stack.
    """
    slug: str = DTOField(..., description='Model slug')
    version: str = DTOField(..., description='Model version')
    chainId: Union[int, None] = DTOField(None, description='Context chain id')
    blockNumber: Union[int, None] = DTOField(None, description='Context block number')

# If you subclass ModelBaseErrorDTO, you MUST add a doc-string
# to your subclass or it will reuse the one below in the schema.


DetailDTOClass = TypeVar('DetailDTOClass')


class ModelErrorDTO(GenericDTO, Generic[DetailDTOClass]):
    """
    The base error type that other errors inherit from.

    The main error types are:
     - ModelDataError: An error that occurs during the lookup, generation,
       or processing of data. It is not an error in the code but an
       but an unexpected situation with the data. For example, a request
       for a contract at an address that does not exist will return a
       ModelDataError. This error is considered deterministic and permanent,
       in the sense that for the given context, the same error will always occur.

     - ModelInputError: An error that occurs when the input data for a
       model is being validated. Usually it is caused by missing fields,
       fields of the wrong type, or conficting data. In the returned error
       the last stack entry is the model whose input triggered the error.

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
    stack: List[ModelCallStackEntry] = DTOField(
        [], description='Model call stack. First element is the first '
        'called model and last element is the model that raised the error.')
    code: str = DTOField('generic', description='Short identifier for the type of error')
    detail: Union[DetailDTOClass, None] = DTOField(
        None, description='Arbitrary data related to the error. '
        'This can be a dict or a DTO instance')
    permanent: bool = DTOField(False, description='If true, the error is permanent and '
                               'will also give the same result for the same context.')


class ModelBaseError(Exception):
    """
    Base error class for Credmark model errors.
    You should not create instances of this class directly.

    Subclasses can create a custom DTO class and set the
    dto_class property. They should override the __init__
    method with extra params (as needed) and **kwargs
    (for safety) and call super() with the extra args defined
    in the dto. See ModelDataError for an example.

    Subclasses must be able to be initialized from a normally
    and with their full dto json as a **kwargs. If you set
    a custom message or other default values in your __init__,
    be sure not to have duplicate keys.

    The dto data object is accessible at error.data
    """

    """
    Map of class name to class
    """
    class_map = {}

    """
    A set of of all model error DTOs used by ModelBaseError subclasses
    """
    dto_set = set()

    """
    Subclasses can set dto_class to a subclass of ModelErrorDTO
    to add more fields to the error.data
    """
    dto_class = ModelErrorDTO

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.class_map[cls.__name__] = cls
        cls.dto_set.add(cls.dto_class)

    @ classmethod
    def class_for_name(cls, name: str):
        """
        Return a specific error class for a name.
        Must be a subclass of ModelBaseError.
        """
        return cls.class_map.get(name)

    @ classmethod
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

    def __init__(self, message: str,
                 **data):
        super().__init__(message)
        self.data = self.dto_class(type=self.__class__.__name__,
                                   message=message,
                                   **data)

    def dict(self):
        """
        Return a dict for the error DTO
        """
        return self.data.dict()

    def json(self):
        """
        Return JSON for the error DTO
        """
        return self.data.dict()

    def transform_data_detail(self, dto_class: Union[Type[DTO], None] = None):
        """
        Convert the data.detail (if any) to a specific DTO subclass or
        to a dict if dto_class is None.
        """
        if self.data.detail is not None:
            self.data.detail = transform_data_for_dto(
                self.data.detail, dto_class, self.data.type, 'detail')


class ModelDataErrorDTO(ModelErrorDTO):
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
    """
    dto_class = ModelDataErrorDTO

    class ErrorCodes:
        GENERIC = 'generic'
        NO_DATA = 'no_data'
        CONFLICT = 'conflict'

    # If adding parameters, give them default values for
    # backwards compatibility.
    def __init__(self,
                 message: str,
                 code: str = 'generic',
                 detail: Union[dict, None] = None,
                 **kwargs):
        if 'permanent' not in kwargs:
            kwargs = dict(kwargs, permanent=True)
        super().__init__(message=message,
                         code=code,
                         detail=detail,
                         **kwargs)


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


class ModelInputError(ModelBaseError):
    """
    An error that occurs when invalid input is sent to a model.
    The message describes the invalid or missing fields.

    The last model on the call stack is the model that received the
    invalid input.
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
