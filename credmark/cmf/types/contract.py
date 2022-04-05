
from typing import (
    Any,
    Union,
    List,
)

from web3.contract import Contract as Web3Contract
import json
import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError
from .account import Account
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField, DTO


class Contract(Account):

    class ContractMetaData(DTO):
        contract_name: Union[str, None] = None
        deploy_tx_hash: Union[str, None] = None
        constructor_args: Union[str, None] = None
        abi_hash: Union[str, None] = None
        abi: Union[List[dict], str, None] = None
        is_transparent_proxy: Union[bool, None] = None
        proxy_implementation: Union[Any, None] = None

    _meta: ContractMetaData = PrivateAttr(
        default_factory=lambda: Contract.ContractMetaData())  # pylint: disable=unnecessary-lambda
    _instance: Union[Web3Contract, None] = PrivateAttr(default=None)
    _proxy_implementation = PrivateAttr(default=None)
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

        meta = data.get('meta', None)
        if meta is not None:
            if isinstance(meta, dict):
                self._meta = type(self._meta)(**meta)
            if isinstance(meta, type(self._meta)):
                self._meta = meta

        if isinstance(data.get('abi'), str):
            self._meta.abi = json.loads(data['abi'])
        self._instance = None
        self._proxy_implementation = None

    def _load(self):
        if self._loaded:
            return
        context = credmark.cmf.model.ModelContext.current_context()

        contract_q_results = context.run_model(
            'contract.metadata', {'contractAddress': self.address})

        if len(contract_q_results['contracts']) > 0:
            res = contract_q_results['contracts'][0]
            self._meta.contract_name = res.get('contract_name')
            self._meta.constructor_args = res.get('constructor_args')
            self._meta.abi = res.get('abi')
            self._meta.is_transparent_proxy = res.get('proxy', 0) == "1"
            # TODO: Implementation needs to be validated on the db
            if self._meta.is_transparent_proxy:
                self._meta.proxy_implementation = Contract(address=res.get('implementation'))
            self._loaded = True
        else:
            if self._meta.abi is None:
                raise ModelDataError(f'abi not available for address {self.address}')
        self._loaded = True

    @property
    def instance(self):
        if self._instance is None:
            context = credmark.cmf.model.ModelContext.current_context()
            if self.abi is None:
                self._load()
            self._instance = context.web3.eth.contract(
                address=context.web3.toChecksumAddress(self.address),
                abi=self.abi
            )
        return self._instance

    @property
    def proxy_for(self):
        if not self._loaded:
            self._load()
        return self._meta.proxy_implementation

    @ property
    def functions(self):
        if isinstance(self.proxy_for, Contract):
            return self.proxy_for.functions
        return self.instance.functions

    @ property
    def events(self):
        if isinstance(self.proxy_for, Contract):
            return self.proxy_for.events
        return self.instance.events

    @ property
    def info(self):
        if isinstance(self, ContractInfo):
            return self
        self._load()
        return ContractInfo(**self.dict(), meta=self._meta)

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
        if not self._loaded:
            self._load()
        return self._meta.is_transparent_proxy


class ContractInfo(Contract):
    meta: Contract.ContractMetaData


class Contracts(IterableListGenericDTO[Contract]):
    contracts: List[Contract] = DTOField(default=[], description="A List of Contracts")
    _iterator: str = PrivateAttr('contracts')
