import re
from typing import Any, Dict, Union

from eth_typing.evm import ChecksumAddress
from web3 import Web3
from web3._utils.validation import validate_address as eth_utils_validate_address

from credmark.cmf.model.errors import ModelTypeError


def validate_address(addr: str) -> ChecksumAddress:
    try:
        checksum_addr = Web3.toChecksumAddress(addr)
        eth_utils_validate_address(checksum_addr)
        return checksum_addr
    except Exception as e:
        raise ModelTypeError(f'Address validation error: {str(e)}')


evm_address_regex = re.compile(r'^0x[a-fA-F0-9]{40}$')


MAX_ADDRESS_VALUE = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


class Address(str):
    """
    An EVM address which is a lowercase hex string.

    It can be created with a lowercase, uppercase, or checksum hex string
    and will be converted to lowercase.

    It can be used as a normal string but it also has
    a "checksum" property which returns a web3 ChecksumAddress.

    It compares with other strings/Addresses in a case-insensitive way.
    """
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string',
                            pattern='^0x[a-fA-F0-9]{40}$',
                            format='evm-address')

    @classmethod
    def null(cls):
        return NULL_ADDRESS

    def is_null(self):
        return self == NULL_ADDRESS

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, addr: str):
        if not isinstance(addr, str):
            raise ModelTypeError('Address must be a string')
        m = evm_address_regex.fullmatch(addr)
        if not m:
            raise ModelTypeError(f"Invalid address string '{addr}'")

        return cls(addr)

    def __new__(cls, addr):
        if isinstance(addr, int):
            if addr > MAX_ADDRESS_VALUE:
                raise ValueError(
                    f'Address {hex(addr)} has exceeded maximum value {MAX_ADDRESS_VALUE}')
            addr = f'{addr:#042x}'
        elif isinstance(addr, str):
            try:
                if len(addr) != 42:
                    addr = f'{int(addr, 16):#042x}'
            except Exception as e:
                raise ModelTypeError(f'Address validation error: {str(e)}')
        elif isinstance(addr, bytes):
            addr = addr.hex()
            if len(addr) != 42:
                addr = f'{int(addr, 16):#042x}'
        else:
            raise ModelTypeError(
                f'Address instance must be created with a string, int or bytes {addr}')
        return str.__new__(cls, addr.lower())

    def __init__(self, _addr: Union[str, int]):
        super().__init__()
        self._checksum = validate_address(self)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other.lower()
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, str):
            return str(self) < other.lower()
        return NotImplemented

    def __ge__(self, other):
        return not self < other

    def __gt__(self, other):
        if isinstance(other, str):
            return str(self) > other.lower()
        return NotImplemented

    def __le__(self, other):
        return not self > other

    @classmethod
    def valid(cls, addr):
        try:
            validate_address(addr)
        except Exception:
            return False
        return True

    def to_int(self):
        return int(self, 16)

    @property
    def checksum(self):
        return self._checksum


NULL_ADDRESS = Address("0x0000000000000000000000000000000000000000")
