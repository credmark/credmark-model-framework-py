import re
from typing import (
    Dict,
    Any,
)

from web3 import Web3
from web3._utils.validation import (
    validate_address as eth_utils_validate_address,
)
from credmark.types.dto import DTO, DTOField


def validate_address(addr: str):
    checksum_addr = Web3.toChecksumAddress(addr)
    eth_utils_validate_address(checksum_addr)
    return checksum_addr


evm_address_regex = re.compile(r'^0x[a-fA-F0-9]{40}$')


class Address(str):
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string',
                            pattern='^0x[a-fA-F0-9]{40}$',
                            format='evm-address')

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, addr: str):
        if not isinstance(addr, str):
            raise TypeError('Address must be a string')
        m = evm_address_regex.fullmatch(addr)
        if not m:
            raise ValueError(f"Invalid address string '{addr}'")

        return cls(addr)

    def __new__(cls, addr):
        if isinstance(addr, int):
            addr = hex(addr)
        elif not isinstance(addr, str):
            raise TypeError('Address instance must be created with a string or int')
        return str.__new__(cls, addr.lower())

    def __init__(self, _addr: str):
        super().__init__()
        self._checksum = validate_address(self)

    def __repr__(self):
        return f'Address({super().__repr__()})'

    @classmethod
    def valid(cls, addr):
        try:
            validate_address(addr)
        except Exception:
            return False
        return True

    @property
    def checksum(self):
        return self._checksum


if __name__ == '__main__':
    import functools

    def expect_exception(func):
        got_exception = False
        try:
            func()
        except Exception:
            got_exception = True
        if not got_exception:
            raise ValueError

    class PoolAddress(DTO):
        poolAddress: Address = DTOField(..., description='Address of Pool')

    # pa = PoolAddress(poolAddress='0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    expect_exception(
        functools.partial(PoolAddress, {'poolAddress': '0xD905e2eaeBe188fc92179b6350'})
    )

    Address(0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8)  # type: ignore
    Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
    Address('0xd533a949740bb3306d119cc777fa900ba034cd52')
    Address('0x' + (bytes.fromhex('0xddf252ad1be2c89b69c2b068fc378daa952ba7f1'[2:])).hex())
    Address('0xddf252ad1be2c89b69c2b068fc378daa952ba7f1'[2:])

    assert Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8') == Address(
        '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    assert Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D9') != Address(
        '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    assert Address.valid(addr='0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    assert not Address.valid('0xD905e2eaeBe')

    a1 = Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
    assert a1 == '0xd905e2eaebe188fc92179b6350807d8bd91db0d8'
    assert a1.checksum == '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'

    expect_exception(
        functools.partial(Address, 123)
    )

    expect_exception(
        functools.partial(
            Address, '0x' + bytes.fromhex(
                '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'[2:]).hex())
    )

    ADDR1 = '0xd905e2eaebe188fc92179b6350807d8bd91db0d8'
    assert hash(Address(ADDR1)) == hash(ADDR1)

    print('all passed')
