import binascii
from typing import Union
from .address import Address


class Token():

    def __init__(self, address: Union[Address, None]):
        self.address = address

    def load(self):
        pass

    @classmethod
    def get(cls, id):
        if(Address.valid(id)):
            return Token(id)
        if("symbol is in the registry"):
            return Token("symbol.address")

    @property
    def decimals(self):
        if self.__decimals is None:
            self.load()
        return self.__decimals

    @property
    def symbol(self):
        if self.__symbol is None:
            self.load()
        return self.__symbol

    @property
    def name(self):
        if self.__name is None:
            self.load()
        return self.__name

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        return self.address == other.address
