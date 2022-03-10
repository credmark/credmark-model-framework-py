from typing import List
from .address import Address, NULL_ADDRESS
from ..dto import DTO, DTOField, PrivateAttr, IterableListGenericDTO


class Account(DTO):
    address: Address

    class Config:
        schema_extra = {
            'example': [
                {
                    'address': NULL_ADDRESS,
                }
            ]
        }


class Accounts(IterableListGenericDTO[Account]):
    accounts: List[Account] = DTOField(
        default=[], description="A list of Accounts")
    _iterator: str = PrivateAttr('accounts')

