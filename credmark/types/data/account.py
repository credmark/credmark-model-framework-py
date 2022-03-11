from typing import List
from .address import Address
from ..dto import DTO, DTOField, PrivateAttr, IterableListGenericDTO


class Account(DTO):
    address: Address

    class Config:
        schema_extra = {
            'examples': [{'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984', }]
        }


class Accounts(IterableListGenericDTO[Account]):
    accounts: List[Account] = DTOField(
        default=[], description="A list of Accounts")
    _iterator: str = PrivateAttr('accounts')
