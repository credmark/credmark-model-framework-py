from typing import List
from .address import Address
from ..dto import DTO, PrivateAttr, IterableListGenericDTO


class Account(DTO):
    address: Address


class Accounts(IterableListGenericDTO[Account]):
    accounts: List[Account]
    _iterator: str = PrivateAttr('accounts')
