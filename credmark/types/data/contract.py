import re

from credmark.types.data.address import Address
from credmark.types.data.json_dto import JsonList
from credmark.types.dto import DTO, DTOExtra,PrivateAttr

from typing import (
    Dict,
    Any,
    Union,
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


class ContractDTO(DTO):
    name: Union[str, None] = None
    address: Union[Address, None] = None
    deploy_tx_hash: Union[str, None] = None
    constructor_args: Union[str, None] = None
    abi_hash: Union[str, None] = None
    abi: JsonList = []


class Contract(ContractDTO):
    _context: Any = PrivateAttr()
    _instance: Any = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True

    @property
    def instance(self) -> Web3Contract:
        if self._instance is None:
            if self.info.address is not None:
                self._instance = self._context.web3.eth.contract(
                    address=self._context.web3.toChecksumAddress(self.info.address),
                    abi=self.info.abi
                )
            else:
                raise ValueError(f'address is None. Unable to create contract')
        return self._instance

    @property
    def functions(self):
        return self.instance.functions

    def __dict__(self):
        return self.info.__dict__