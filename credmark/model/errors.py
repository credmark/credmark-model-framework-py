from typing import Union


class ModelBaseError(Exception):
    """
    Base error class for Credmark model errors.
    You should not create instances of this class directly.
    """

    def dict(self):
        obj = vars(self)
        obj['type'] = self.__class__.__name__
        obj['message'] = super().__str__()
        return obj


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

    class ErrorCodes:
        GENERAL = 'general'
        NO_DATA = 'no_data'
        CONFLICT = 'conflict'
        INVALID_INPUT = 'invalid_input'

    # If adding parameters, give them default values for
    # backwards compatibility.
    def __init__(self, message: str,
                 code: str,
                 chain_id: int,
                 block_number: int,
                 data: Union[dict, list, str, int, float, None] = None):
        self.code = code
        self.data = data
        self.chain_id = chain_id
        self.block_number = block_number
        super().__init__(message)


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
