from typing import Union
from credmark.model.errors import ModelErrorDTO, ModelEngineError
from credmark.dto import DTO


class SlugAndVersionDTO(DTO):
    slug: str
    version: Union[str, None]


class ModelNotFoundErrorDTO(ModelErrorDTO[SlugAndVersionDTO]):
    """
    A model requested to run was not found.

    The detail contains the fields:
    - slug: Slug of model not found
    - version: Version of model not found
    """


class ModelNotFoundError(ModelEngineError):
    dto_class = ModelNotFoundErrorDTO

    @classmethod
    def create(cls, slug: str, version: Union[str, None], message: Union[str, None] = None):
        message = f'Missing model "{slug}" version {version if version is not None else "any"}' \
            + ('. ' + message if message is not None else '')
        return ModelNotFoundError(message=message,
                                  detail=SlugAndVersionDTO(slug=slug, version=version))


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
