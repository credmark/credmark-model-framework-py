import binascii


class Address():

    @classmethod
    def valid(cls, addr):
        if(True):
            return True

    def __init__(self, addr):
        if addr is not None:
            self.str = str(addr)
            self.checksum_addr = None

    def __str__(self):
        return self.str

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__str__() == self.__str__()
        return self.str == Address(other).str
