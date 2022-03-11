# pylint: disable=locally-disabled, unused-import

import re
from typing import Any, Dict, Generic, Iterator, List, TypeVar
from pydantic import (
    BaseModel as DTO,
    Field as DTOField,
    constr,
    confloat,
    conint,
    validator,
    Json as DTOJson,
    Extra as DTOExtra,
    PrivateAttr,
)
# A GenericDTO is a kind of DTO: isintance(g, DTO) == True
from pydantic.generics import GenericModel as GenericDTO

from abc import abstractproperty

from .dto_schema import (
    cross_examples,
    dto_schema_viz,
    print_tree,
    print_example,
)


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
