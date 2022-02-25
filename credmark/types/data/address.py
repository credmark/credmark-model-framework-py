from typing import (
    Union,
)

from eth_utils import (
    is_integer,
    is_checksum_address
)

from web3._utils.validation import (
    validate_address as eth_utils_validate_address,
)

from typing import (
    Dict,
    Any,
)

from web3 import Web3

from ..dto import DTO, DTOField

import functools


def validate_address(addr: Union[str, int]) -> str:
    if not is_checksum_address(addr):
        _addr = Web3.toChecksumAddress(addr)
    else:
        _addr = addr
    eth_utils_validate_address(_addr)
    return _addr


class AddressStr(str):
    @ classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(type='string', format='address')

    @ classmethod
    def __get_validators__(cls):
        yield cls.validate

    @ classmethod
    def validate(cls, addr: Union[str, int]) -> str:
        return validate_address(addr)


class Address(str):
    class DTOAddress(DTO):
        addr: AddressStr = DTOField(..., description='address')

    def __init__(self, addr):
        if is_integer(addr):
            addr = Web3.toChecksumAddress(addr)
        self._addr = self.__class__.DTOAddress(addr=addr)

    def __hash__(self):
        return super().__hash__()

    def __str__(self):
        return self._addr.addr

    def __repr__(self):
        return self.__str__()

    def str(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._addr == other._addr
        if isinstance(other, str):
            return self._addr.addr == other
        return self.__str__() == self.__class__(other).__str__()

    @ property
    def addr(self):
        return self._addr.addr

    @ classmethod
    def valid(cls, addr):
        try:
            validate_address(addr)
        except Exception:
            return False
        return True


if __name__ == '__main__':
    def expect_exception(func):
        got_exception = False
        try:
            func()
        except Exception:
            got_exception = True
        if not got_exception:
            raise ValueError

    class PoolAddress(DTO):
        poolAddress: AddressStr = DTOField(..., description='Address of Pool')

    pa = PoolAddress(poolAddress='0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    expect_exception(
        functools.partial(PoolAddress, {'poolAddress': '0xD905e2eaeBe188fc92179b6350'})
    )

    Address(0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8)
    Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
    Address('0xd533a949740bb3306d119cc777fa900ba034cd52')
    Address('0x' + (bytes.fromhex('0xddf252ad1be2c89b69c2b068fc378daa952ba7f1'[2:])).hex())
    Address('0xddf252ad1be2c89b69c2b068fc378daa952ba7f1'[2:])

    assert Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8') == Address(
        '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    assert not Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D9') == Address(
        '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    assert Address.valid(addr='0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')

    assert not Address.valid('0xD905e2eaeBe')

    a1 = Address('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
    assert a1 == '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'

    expect_exception(
        functools.partial(Address, 123)
    )

    expect_exception(
        functools.partial(
            Address, '0x' + bytes.fromhex('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'[2:]).hex())
    )

    addr = '0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8'
    assert hash(Address(addr)) == hash(addr)

    print('all passed')
