from typing import Union
from credmark.model.errors import ModelEngineError


class MissingModelError(ModelEngineError):
    def __init__(self, slug: str, version: Union[str, None], message: Union[str, None] = None):
        self.slug = slug
        self.version = version
        message = 'Missing model {0}{1} {2}'.format(
            slug if slug else '<empty-slug>',
            ' version ' + version if version is not None else '',
            message if message is not None else '')
        super().__init__(message)


class ModelRunRequestError(ModelEngineError):
    def __init__(self, message, result: dict):
        super().__init__(message)
        self.result = result


class WriteModelManifestError(ModelEngineError):
    pass
