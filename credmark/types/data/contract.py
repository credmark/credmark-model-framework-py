from typing import (
    Union,
    List,
)

from web3.contract import Contract as Web3Contract

import credmark.model
from credmark.types.data.address import Address
from credmark.types.dto import DTO, DTOField, IterableListDto, PrivateAttr


class Contract(DTO):
    name: Union[str, None] = None
    address: Address = DTOField(..., description='Contract address')
    deploy_tx_hash: Union[str, None] = None
    constructor_args: Union[str, None] = None
    protocol: Union[str, None] = None
    product: Union[str, None] = None
    abi_hash: Union[str, None] = None
    abi: Union[List[dict], None] = None
    _instance: Union[Web3Contract, None] = PrivateAttr(default=None)

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True

    def __init__(self, **data):
        super().__init__(**data)
        self._instance = None

    @property
    def instance(self):
        if self._instance is None:
            if self.address is not None:
                context = credmark.model.ModelContext.current_context
                if context is not None:
                    # TODO: Check if self.abi is None and fetch if necessary
                    self._instance = context.web3.eth.contract(
                        address=context.web3.toChecksumAddress(self.address),
                        abi=self.abi
                    )
                else:
                    raise ValueError('No current context. Unable to create contract instance.')
            else:
                raise ValueError('Contract address is None. Unable to create contract instance.')
        return self._instance

    @property
    def functions(self):
        return self.instance.functions


class Contracts(IterableListDto):
    list: List[Contract]
