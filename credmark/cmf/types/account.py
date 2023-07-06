from typing import List

import credmark.cmf.model
from credmark.cmf.model.models import Models
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

    _models = PrivateAttr(None)

    @classmethod
    def validate(cls, value):
        if isinstance(value, str):
            return cls(value)
        if isinstance(value, dict):
            return cls(**value)
        if isinstance(value, cls):
            return value
        raise TypeError(
            f'{cls.__name__} must be deserialized with an str or dict')

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

    @property
    def models(self):
        if self._models is None:
            # The models instance can be used to run models like a method
            # We don't pass the block_number so it uses the default
            # (our context) block number.
            context = credmark.cmf.model.ModelContext.current_context()
            self._models = Models(context, input=self)
        return self._models

    def to_accounts(self):
        return Accounts(accounts=[self.address])  # type: ignore


class Accounts(IterableListGenericDTO[Account]):
    accounts: List[Account] = DTOField(
        default=[], description="A list of Accounts")
    _iterator: str = PrivateAttr('accounts')

    def to_address(self) -> List[Address]:
        # pylint: disable=not-an-iterable
        return [acc.address for acc in self.accounts]

    class Config:
        schema_extra = {
            'examples': [
                {"accounts": ["0x388c818ca8b9251b393131c08a736a67ccb19297",
                              "0xf9cbBA7BF1b10E045691dDECa48182dB213E8F8B"]},
                {"accounts": [{"address": "0x388c818ca8b9251b393131c08a736a67ccb19297"},
                              {"address": "0xf9cbBA7BF1b10E045691dDECa48182dB213E8F8B"}]},
            ]
        }
