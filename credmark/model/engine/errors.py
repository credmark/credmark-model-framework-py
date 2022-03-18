from typing import Union
from credmark.model.errors import ModelBaseErrorDTO, ModelEngineError, DTOField


class ModelNotFoundErrorDTO(ModelBaseErrorDTO):
    """
    A model requested to run was not found.
    """
    slug: str = DTOField(..., description='Slug of model not found')
    version: str = DTOField(..., description='Version of model not found')


class ModelNotFoundError(ModelEngineError):
    dto_class = ModelNotFoundErrorDTO

    def __init__(self,
                 slug: str,
                 version: Union[str, None],
                 message: Union[str, None] = None,
                 **_kwargs):
        message = 'Missing model {0}{1} {2}'.format(
            slug if slug else '<empty-slug>',
            ' version ' + version if version is not None else '',
            message if message is not None else '')
        super().__init__(message, slug=slug, version=version)


class ModelRunRequestErrorDTO(ModelBaseErrorDTO):
    """
    An HTTP-related error that occurred while making a
    request for a model to run.
    """
    code: int = DTOField(..., description='HTTP error code')
    error: str = DTOField(..., description='Error string')


class ModelRunRequestError(ModelEngineError):

    dto_class = ModelRunRequestErrorDTO

    def __init__(self,
                 message: str,
                 code: int,
                 error: str, **_kwargs):
        super().__init__(message, code=code, error=error)


class ModelManifestWriteError(ModelEngineError):
    pass
