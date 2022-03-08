from typing import List
from .address import Address
from ..dto import DTO, PrivateAttr, IterableListDto


class Account(DTO):
    address: Address


class Accounts(IterableListDto):
    accounts: List[Account]
    _iterator: str = PrivateAttr('accounts')
