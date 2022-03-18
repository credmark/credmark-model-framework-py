from typing import Union
from credmark.model.errors import ModelBaseErrorDTO, ModelEngineError


class ModelNotFoundErrorDTO(ModelBaseErrorDTO):
    """
    A model requested to run was not found.

    The detail contains the fields:
    - slug: Slug of model not found
    - version: Version of model not found
    """


class ModelNotFoundError(ModelEngineError):
    dto_class = ModelNotFoundErrorDTO

    def __init__(self,
                 slug: Union[str, None] = None,
                 version: Union[str, None] = None,
                 message: Union[str, None] = None,
                 **kwargs):
        if message is None:
            message = 'Missing model {0}{1} {2}'.format(
                slug if slug else '<empty-slug>',
                ' version ' + version if version is not None else '',
                message if message is not None else '')
        if 'detail' not in kwargs:
            detail = {'slug': slug, 'version': version}
            super().__init__(message=message, detail=detail, **kwargs)
        else:
            super().__init__(message=message, **kwargs)


class ModelRunRequestErrorDTO(ModelBaseErrorDTO):
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
