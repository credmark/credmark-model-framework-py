
from typing import (
    Union,
    List,
)

from web3.contract import Contract as Web3Contract
import json
import credmark.model
from credmark.model.errors import ModelDataError, ModelNoContextError
from credmark.types.data.account import Account, Address
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField, DTO
from credmark.types.data.data_content.transparent_proxy_data import UPGRADEABLE_CONTRACT_ABI


class Contract(Account):

    class ContractMetaData(DTO):
        contract_name: Union[str, None] = None
        deploy_tx_hash: Union[str, None] = None
        constructor_args: Union[str, None] = None
        abi_hash: Union[str, None] = None
        abi: Union[List[dict], str, None] = None
        proxy_for: Union[Account, None] = None

    _meta: ContractMetaData = PrivateAttr(
        default_factory=lambda: Contract.ContractMetaData())
    _instance: Union[Web3Contract, None] = PrivateAttr(default=None)
    _proxy_for = PrivateAttr(default=None)
    _loaded = PrivateAttr(default=False)

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
        super().__init__(**data)

        if isinstance(data.get('abi'), str):
            self._meta.abi = json.loads(data['abi'])

        meta = data.get('meta', None)
        if meta is not None:
            if isinstance(meta, dict):
                self._meta = self.ContractMetaData(**meta)
            if isinstance(meta, self.ContractMetaData):
                self._meta = meta

        self._instance = None
        self._proxy_for = None

    def _load(self):
        if self._loaded:
            return
        context = credmark.model.ModelContext.current_context
        if context is not None:
            contract_q_results = context.run_model(
                'contract.metadata', {'contractAddress': self.address})

            if len(contract_q_results['contracts']) > 0:
                res = contract_q_results['contracts'][0]
                self._meta.contract_name = res.get('contract_name')
                self._meta.constructor_args = res.get('constructor_args')
                self._meta.abi = res.get('abi')
                self._loaded = True
                if self.is_transparent_proxy:
                    self._meta.proxy_for = Account(address=self.proxy_for.address)
            else:
                if self._meta.abi is None:
                    raise ModelDataError(f'abi not available for address {self.address}')
        self._loaded = True

    @property
    def instance(self):
        if self._instance is None:
            context = credmark.model.ModelContext.current_context
            if context is not None:
                if self._meta.abi is None:
                    self._load()
                self._instance = context.web3.eth.contract(
                    address=context.web3.toChecksumAddress(self.address),
                    abi=self._meta.abi
                )
            else:
                raise ModelNoContextError(
                    'No current context. Unable to create contract instance.')
        return self._instance

    @property
    def proxy_for(self):
        if not self._loaded:
            self._load()
        if self._proxy_for is None and self.is_transparent_proxy:
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ModelNoContextError(
                    'No current context. Unable to create contract instance.')
            # TODO: Get this from the database, Not the RPC
            events = self.instance.events.Upgraded.createFilter(
                fromBlock=0, toBlock=context.block_number).get_all_entries()
            if len(events) > 0:
                self._proxy_for = Contract(address=events[len(events) - 1].args.implementation)
            elif self.constructor_args is not None and len(self.constructor_args) >= 40:
                self._proxy_for = Contract(address=Address('0x' + self.constructor_args[-40:]))
        return self._proxy_for

    @ property
    def functions(self):
        if self.proxy_for is not None:
            return self.proxy_for.functions
        return self.instance.functions

    @ property
    def events(self):
        if self.proxy_for is not None:
            return self.proxy_for.events
        return self.instance.events

    @ property
    def info(self):
        if isinstance(self, ContractInfo):
            return self
        self._load()
        return ContractInfo(**self.dict(), meta=self._meta.dict())

    @ property
    def deploy_tx_hash(self):
        if not self._loaded:
            self._load()
        return self._meta.deploy_tx_hash

    @ property
    def contract_name(self):
        if not self._loaded:
            self._load()
        return self._meta.contract_name

    @ property
    def constructor_args(self):
        if not self._loaded:
            self._load()
        return self._meta.constructor_args

    @ property
    def abi(self):
        if not self._loaded:
            self._load()
        return self._meta.abi

    @ property
    def is_transparent_proxy(self):
        if self._meta.contract_name == "InitializableAdminUpgradeabilityProxy":
            return True
        if self._meta.contract_name == "AdminUpgradeabilityProxy":
            return True
        if self._meta.abi == UPGRADEABLE_CONTRACT_ABI:
            return True
        return False


class ContractInfo(Contract):
    meta: Contract.ContractMetaData


class Contracts(IterableListGenericDTO[Contract]):
    contracts: List[Contract] = DTOField(default=[], description="A List of Contracts")
    _iterator: str = PrivateAttr('contracts')
