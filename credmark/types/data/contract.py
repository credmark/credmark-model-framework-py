import json
from typing import (
    Union,
    List,
)

from web3.contract import Contract as Web3Contract

import credmark.model
from credmark.model.errors import ModelRunError, ModelNoContextError
from credmark.types.data.account import Account
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField


class Contract(Account):
    contract_name: Union[str, None] = None
    deploy_tx_hash: Union[str, None] = None
    constructor_args: Union[str, None] = None
    protocol: Union[str, None] = None
    product: Union[str, None] = None
    abi_hash: Union[str, None] = None
    abi: Union[List[dict], str, None] = None
    _instance: Union[Web3Contract, None] = PrivateAttr(default=None)

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True
        schema_extra = {
            'examples': Account.Config.schema_extra['examples'] +
            [{'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984',
              'abi': '(Optional) contract abi JSON string'
              }]
        }

    def __init__(self, **data):
        if isinstance(data.get('abi'), str):
            data['abi'] = json.loads(data['abi'])
        super().__init__(**data)
        self._instance = None

    @property
    def instance(self):
        if self._instance is None:
            if self.address is not None:
                context = credmark.model.ModelContext.current_context
                if context is not None:
                    if self.abi is None:
                        self.load()
                    self._instance = context.web3.eth.contract(
                        address=context.web3.toChecksumAddress(self.address),
                        abi=self.abi
                    )
                else:
                    raise ModelNoContextError(
                        'No current context. Unable to create contract instance.')
            else:
                # This should never actually happen so we consider it a coding error
                raise ModelRunError(
                    'Contract address is None. Unable to create contract instance.')
        return self._instance

    def load(self):
        context = credmark.model.ModelContext.current_context
        if context is not None:
            contract_q_results = context.run_model(
                'contract.metadata', {'contractAddress': self.address})
            if len(contract_q_results['contracts']) > 0:
                res = contract_q_results['contracts'][0]
                self.contract_name = res.get('contract_name')
                self.constructor_args = res.get('constructor_args')
                self.protocol = res.get('protocol')
                self.product = res.get('product')
                self.abi = res.get('abi')

    @property
    def functions(self):
        return self.instance.functions


class Contracts(IterableListGenericDTO[Contract]):
    contracts: List[Contract] = DTOField(default=[], description="A List of Contracts")
    _iterator: str = PrivateAttr('contracts')
