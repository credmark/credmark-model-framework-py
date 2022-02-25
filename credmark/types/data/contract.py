import re
from typing import (
    List
)
from .address import AddressStr
from .json import JsonList
from ..dto import DTO

from typing import (
    Dict,
    Any,
)


class Hex0xStr(str):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string', format='json-string')

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, hex_0x_str: str) -> str:
        Hex0xStr
        # (?:0x?)?[\p{XDigit}]+$
        '^0x[0-9a-fA-F]+$'

        r_hex_short = r'\s*(?:#|0x)?([0-9a-f])([0-9a-f])([0-9a-f])([0-9a-f])?\s*'
        r_hex_long = r'\s*(?:#|0x)?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})?\s*'

        m = re.fullmatch(r_hex_long, hex_0x_str)
        if not m:
            raise ValueError('Unkwown no-0x-prefix hex: {hex_0x_str}')
        return hex_0x_str


class Contract(DTO):
    name: str
    address: AddressStr
    deploy_tx_hash: str  # hexstr
    constructor_args: str  # hexstr
    abi_hash: str  # hexstr
    abi: JsonList  # json-list


class Contracts(DTO):
    contracts: List[Contract]
