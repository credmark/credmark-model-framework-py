from typing import List
from .address import Address, NULL_ADDRESS
from ..dto import DTO, PrivateAttr, IterableListDto


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


class Accounts(IterableListDto):
    accounts: List[Account]
    _iterator: str = PrivateAttr('accounts')

