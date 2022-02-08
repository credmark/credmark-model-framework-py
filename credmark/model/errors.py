from typing import Union


class MissingModelError(Exception):
    def __init__(self, name: str, version: Union[str, None], message: Union[str, None] = None):
        self.name = name
        self.version = version
        message = 'Missing model {0}{1}{2}'.format(
            name if name else '<empty-name>',
            ' version ' + version if version is not None else '',
            message if message is not None else '')
        super().__init__(message)


class ModelRunError(Exception):
    pass


class MaxModelRunDepthError(Exception):
    pass


class ModelRunRequestError(Exception):
    def __init__(self, message, result: dict):
        super().__init__(message)
        self.result = result
