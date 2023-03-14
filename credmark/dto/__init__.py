# pylint: disable=locally-disabled, unused-import

import re
from typing import Any, Dict, Generic, Iterator, List, TypeVar, Union
from pydantic import (
    BaseModel as DTO,
    Field as DTOField,
    ValidationError as DTOValidationError,
    constr,
    confloat,
    conint,
    validator,
    Json as DTOJson,
    Extra as DTOExtra,
    PrivateAttr,
)
# A GenericDTO is a kind of DTO: isinstance(g, DTO) == True
from pydantic.generics import GenericModel as GenericDTO


class DTOPretty:
    """
    A Mixin class to add pretty print to DTO
    """

    def _repr_pretty_(self, p, cycle):  # pylint:disable=invalid-name
        class_name = self.__class__.__name__
        if cycle:
            p.text(f'{class_name}(...)')
        else:
            with p.group(4, f'{class_name}(', ')'):
                for k in self.__fields__:  # type: ignore #pylint:disable=no-member
                    v = getattr(self, k)
                    p.break_()
                    p.pretty(k)
                    p.text(':')
                    p.pretty(v)


def fixstr(fixed_length):
    return constr(min_length=fixed_length,
                  max_length=fixed_length)


class HexStr(str):
    """
    Hex string DTO field
    """
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string', format='hex-string')

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, hex_str: str) -> str:
        r_hex = r'(0x)?[0-9a-fA-F]+'

        m = re.fullmatch(r_hex, hex_str)
        if not m:
            raise ValueError('Invalid hex string: {hex_str}')
        return hex_str


DTOCLS = TypeVar('DTOCLS')


class IterableListGenericDTO(GenericDTO, Generic[DTOCLS]):
    _iterator: str

    def __iter__(self) -> Iterator[DTOCLS]:
        return getattr(self, self._iterator).__iter__()

    def __getitem__(self, key) -> DTOCLS:
        return getattr(self, self._iterator).__getitem__(key)

    def append(self, obj):
        return getattr(self, self._iterator).append(obj)

    def extend(self, obj):
        return getattr(self, self._iterator).extend(obj)


class EmptyInput(DTO):
    """
    The model does not require any input. This is an empty object.
    """
    class Config:
        schema_extra: dict = {
            'examples': [{}]
        }


class IntDTO(int):
    """
    A DTO that can be used as an integer output (or input) to a model.
    When used as a top-level DTO it is serialized as a dict with a
    ``value`` field ``{"value": 12345}``, otherwise it is serialized
    as a number.

    It can be used in python code as a normal integer.
    """
    @classmethod
    def schema(cls):
        return {'title': cls.__name__,
                'description': 'DTO for an integer value.',
                'type': 'object',
                'properties': {
                    'value': {
                        'title': 'Value',
                        'description': 'An integer',
                        'type': 'integer'}
                },
                'required': ['value']}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # A pydantic validator so instances can be deserialized
    # from an int or a dict.
    @classmethod
    def validate(cls, i):
        if isinstance(i, int):
            return cls(i)
        if isinstance(i, dict):
            return cls(**i)
        raise TypeError(f'{cls.__name__} must be deserialized with an int or dict')

    def __new__(cls, value: int, **_kwargs):
        return super().__new__(cls, value)

    def dict(self):
        return {"value": self}


class FloatDTO(float):
    """
    A DTO that can be used as an float output (or input) to a model.
    When used as a top-level DTO it is serialized as a dict with a
    ``value`` field ``{"value": 123.45}``, otherwise it is serialized
    as a number.

    It can be used in python code as a normal float.
    """
    @classmethod
    def schema(cls):
        return {'title': cls.__name__,
                'description': 'DTO for a float value.',
                'type': 'object',
                'properties': {
                    'value': {
                        'title': 'Value',
                        'description': 'A floating-point number',
                        'type': 'number'}
                },
                'required': ['value']}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # A pydantic validator so instances can be deserialized
    # from an float or a dict.
    @classmethod
    def validate(cls, i):
        if isinstance(i, float):
            return cls(i)
        if isinstance(i, dict):
            return cls(**i)
        raise TypeError(f'{cls.__name__} must be deserialized with an float or dict')

    def __new__(cls, value: float, **_kwargs):
        return super().__new__(cls, value)

    def dict(self):
        return {"value": self}


class StrDTO(str):
    """
    A DTO that can be used as an string output (or input) to a model.
    When used as a top-level DTO it is serialized as a dict with a
    ``value`` field ``{"value": "foobar"}``, otherwise it is serialized
    as a string.

    It can be used in python code as a normal string.
    """
    @classmethod
    def schema(cls):
        return {'title': cls.__name__,
                'description': 'DTO for a string value.',
                'type': 'object',
                'properties': {
                    'value': {
                        'title': 'Value',
                        'description': 'A string',
                        'type': 'string'}
                },
                'required': ['value']}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # A pydantic validator so instances can be deserialized
    # from an str or a dict.
    @classmethod
    def validate(cls, i):
        if isinstance(i, str):
            return cls(i)
        if isinstance(i, dict):
            return cls(**i)
        raise TypeError(f'{cls.__name__} must be deserialized with a str or dict')

    def __new__(cls, value: str, **_kwargs):
        return super().__new__(cls, value)

    def dict(self):
        return {"value": self}


DTOType = Union[DTO, IntDTO, StrDTO, FloatDTO]

DTOTypesTuple = (DTO, IntDTO, StrDTO, FloatDTO)
"""
A tuple containing the DTO types superclasses.
This can be used when checking if an instance is a DTOType
subclass: ```isinstance(obj, DTOTypesTuple)```
"""


from .dto_schema import (
    cross_examples,
    dto_schema_viz,
    print_tree,
    print_example,
)

from .encoder import (
    json_dump,
    json_dumps
)


class MetadataDto():
    _meta: Union[dict, DTO] = PrivateAttr(
        default_factory=lambda: {})  # pylint: disable=unnecessary-lambda

    def __init__(self, **data):
        super().__init__(**data)
        meta = data.get('meta', None)
        if meta is not None:
            if isinstance(meta, dict):
                self._meta = type(self._meta)(**meta)
            if isinstance(meta, type(self._meta)):
                self._meta = meta

        for key, value in data.items():
            self._meta.__setattr__(key, value)
