from typing import List
from .address import Address
from ..dto import DTO, DTOField, PrivateAttr, IterableListGenericDTO


class Account(DTO):
    address: Address


class Accounts(IterableListGenericDTO[Account]):
    accounts: List[Account] = DTOField(
        default=[], description="An iterable list of Account objects")
    _iterator: str = PrivateAttr('accounts')
