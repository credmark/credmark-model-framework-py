from typing import (
    Union,
    List,
)

from web3.contract import Contract as Web3Contract
from web3._utils.filters import construct_event_filter_params
from web3._utils.events import get_event_data
from urllib3.exceptions import ReadTimeoutError
from requests.exceptions import ReadTimeout

import json
import credmark.model
from credmark.model.errors import ModelDataError
from credmark.types.data.account import Account, Address
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField, DTO
from credmark.types.data.data_content.transparent_proxy_data import UPGRADEABLE_CONTRACT_ABI


class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class ContractMetaCache(Singleton):
    cache = {}


class Contract(Account):

    class ContractMetaData(DTO):
        contract_name: Union[str, None] = None
        deploy_tx_hash: Union[str, None] = None
        constructor_args: Union[str, None] = None
        abi_hash: Union[str, None] = None
        abi: Union[List[dict], str, None] = None
        proxy_for: Union[Account, None] = None

    _meta: ContractMetaData = PrivateAttr(
        default_factory=lambda: Contract.ContractMetaData())  # pylint: disable=unnecessary-lambda
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

        meta = data.get('meta', None)
        if meta is not None:
            if isinstance(meta, dict):
                self._meta = type(self._meta)(**meta)
            if isinstance(meta, type(self._meta)):
                self._meta = meta

        if isinstance(data.get('abi'), str):
            self._meta.abi = json.loads(data['abi'])
        self._instance = None
        self._proxy_for = None

    def _load(self):
        if self._loaded:
            return
        context = credmark.model.ModelContext.current_context()

        if self.address not in ContractMetaCache().cache:
            contract_q_results = context.run_model('contract.metadata',
                                                   {'contractAddress': self.address})
            ContractMetaCache().cache[self.address] = contract_q_results
        else:
            contract_q_results = ContractMetaCache().cache[self.address]

        if len(contract_q_results['contracts']) > 0:
            res = contract_q_results['contracts'][0]
            self._meta.contract_name = res.get('contract_name')
            self._meta.constructor_args = res.get('constructor_args')
            self._meta.abi = res.get('abi')
            self._loaded = True
            if self.is_transparent_proxy:
                if self.proxy_for is not None:
                    self._meta.proxy_for = Account(address=self.proxy_for.address)
        else:
            if self._meta.abi is None:
                raise ModelDataError(f'abi not available for address {self.address}')
        self._loaded = True

    @property
    def instance(self):
        if self._instance is None:
            context = credmark.model.ModelContext.current_context()
            if self.abi is not None:
                self._instance = context.web3.eth.contract(
                    address=context.web3.toChecksumAddress(self.address),
                    abi=self.abi
                )
        return self._instance

    @ property
    def proxy_for(self):
        if not self._loaded:
            self._load()

        if self._proxy_for is None and self.is_transparent_proxy and self.instance is not None:
            context = credmark.model.ModelContext.current_context()

            # TODO: Get this from the database, Not the RPC
            try:
                events = self.instance.events.Upgraded.createFilter(
                    fromBlock=0, toBlock=context.block_number).get_all_entries()

                if len(events) > 0:
                    self._proxy_for = Contract(address=events[len(events) - 1].args.implementation)
                elif self.constructor_args is not None and len(self.constructor_args) >= 40:
                    self._proxy_for = Contract(address=Address('0x' + self.constructor_args[-40:]))

            except ValueError:
                # Some node server does not support the newer eth_newFilter method
                # Alternatively, use the protected method.
                # self.instance.events.Upgraded._get_event_abi()
                try:
                    event_abi = [x for x in self.instance.events.abi
                                 if 'name' in x and x['name'] == 'Upgraded' and
                                 'type' in x and x['type'] == 'event'][0]

                    __data_filter_set, event_filter_params = construct_event_filter_params(
                        abi_codec=context.web3.codec,
                        event_abi=event_abi,
                        address=self.address.checksum,
                        fromBlock=0,
                        toBlock=context.block_number
                    )
                    events = context.web3.eth.get_logs(event_filter_params)
                    events = [get_event_data(context.web3.codec, event_abi, s) for s in events]

                    if len(events) > 0:
                        self._proxy_for = Contract(
                            address=events[-1]['args']['implementation'])
                    elif self.constructor_args is not None and len(self.constructor_args) >= 40:
                        self._proxy_for = Contract(address=Address(
                            '0x' + self.constructor_args[-40:]))
                except (ReadTimeoutError, ReadTimeout):
                    if self.constructor_args is not None and len(self.constructor_args) >= 40:
                        self._proxy_for = Contract(address=Address(
                            '0x' + self.constructor_args[-40:]))

        return self._proxy_for

    @ property
    def functions(self):
        if self.proxy_for is not None:
            context = credmark.model.ModelContext.current_context()
            return context.web3.eth.contract(
                address=context.web3.toChecksumAddress(self.address),
                abi=self.proxy_for.abi
            ).functions
        if self.instance is not None:
            return self.instance.functions

    @property
    def events(self):
        if self.proxy_for is not None:
            context = credmark.model.ModelContext.current_context()
            return context.web3.eth.contract(
                address=context.web3.toChecksumAddress(self.address),
                abi=self.proxy_for.abi
            ).events
        if self.instance is not None:
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

    @property
    def is_transparent_proxy(self):
        # TODO : Find a more definitive token proxy identification mechanism
        if self._meta.contract_name == "InitializableAdminUpgradeabilityProxy":
            return True
        if self._meta.contract_name == "AdminUpgradeabilityProxy":
            return True
        if self._meta.contract_name == "FiatTokenProxy":
            return True
        if self._meta.abi == UPGRADEABLE_CONTRACT_ABI:
            return True
        return False


class ContractInfo(Contract):
    meta: Contract.ContractMetaData


class Contracts(IterableListGenericDTO[Contract]):
    contracts: List[Contract] = DTOField(default=[], description="A List of Contracts")
    _iterator: str = PrivateAttr('contracts')
