import re
from typing import (
    List,
    Union
)
from xml.sax.handler import property_declaration_handler
from .address import AddressStr, Address
from .json import JsonList
from ..dto import DTO, Extra

from typing import (
    Dict,
    Any,
)

from web3.contract import Contract as Web3Contract


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


class Contract(dict):

    def __init__(self, context, **kwargs) -> None:
        self.context = context
        self._instance = None
        self._dto = ContractDTO(**kwargs)

    @property
    def info(self):
        return self._dto

    @property
    def instance(self):
        if self._instance is None:
            self._instance = self.context.web3.eth.contract(
                address=self.context.web3.toChecksumAddress(self.info.address),
                abi=self.info.abi
            )
        return self._instance

    @property
    def functions(self):
        return self.instance.functions

    def __dict__(self):
        return self.info.__dict__


class ContractDTO(DTO):
    name: Union[str, None] = None
    address: Union[str, None] = None
    deploy_tx_hash: Union[str, None] = None
    constructor_args: Union[str, None] = None
    abi_hash: Union[str, None] = None
    abi: JsonList = []
