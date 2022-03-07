from typing import List
from .address import Address
from ..dto import DTO, IterableListDto


class Account(DTO):
    address: Address


class Accounts(IterableListDto):
    accounts: List[Account]
    iterator: str = 'accounts'
