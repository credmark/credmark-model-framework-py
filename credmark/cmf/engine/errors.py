# pylint:disable=ungrouped-imports
from credmark.cmf.model.errors import ModelErrorDTO, ModelEngineError


class ModelRunRequestErrorDTO(ModelErrorDTO):
    """
    An HTTP-related error that occurred while making a
    request for a model to run.

    The code field is the HTTP error code.
    """


class ModelRunRequestError(ModelEngineError):

    dto_class = ModelRunRequestErrorDTO

    def __init__(self,
                 message: str,
                 code: str,
                 **kwargs):
        super().__init__(message=message, code=code, **kwargs)


class ModelManifestWriteError(ModelEngineError):
    pass
