from .address import Address
from ..dto import DTO


class Wallet(DTO):
    address: Address
