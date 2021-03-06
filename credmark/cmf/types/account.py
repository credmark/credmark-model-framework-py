from typing import List

from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr

from .address import Address, evm_address_regex


class Account(DTO):
    """
    Accounts are a way to pass addresses between models.
    They act as a base class to any type that requires an address object.
    (e.g. Contracts, Token, etc.)

        a = Account(address='0xad529dabbd6201545ce9aac300b868f2443382b9')

        a = Account('0xad529dabbd6201545ce9aac300b868f2443382b9')

    """

    address: Address

    @classmethod
    def validate(cls, obj):
        if isinstance(obj, str):
            return cls(obj)
        if isinstance(obj, dict):
            return cls(**obj)
        if isinstance(obj, cls):
            return obj
        raise TypeError(f'{cls.__name__} must be deserialized with an str or dict')

    def __init__(self, *args, **data):
        if len(args) > 0:
            if isinstance(args[0], str) and evm_address_regex.match(args[0]) is not None:
                super().__init__(address=args[0])
                return
            elif isinstance(args[0], dict):
                data = args[0]

        super().__init__(**data)

    class Config:
        schema_extra = {
            'examples': [{'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984', }]
        }


class Accounts(IterableListGenericDTO[Account]):
    accounts: List[Account] = DTOField(
        default=[], description="A list of Accounts")
    _iterator: str = PrivateAttr('accounts')
