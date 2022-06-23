import json
import logging
from typing import Any, List, Union

import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError
from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr
from web3.contract import Contract as Web3Contract

from .abi import ABI
from .account import Account
from .address import Address
from .block_number import BlockNumber, BlockNumberOutOfRangeError
from .ledger import ContractLedger


class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class ContractMetaCache(Singleton):
    _cache = {}
    _trace = False

    def get(self, chain_id, address):
        if chain_id not in self._cache:
            return False, {}

        needle = self._cache[chain_id].get(address, None)
        if needle is None:
            if self._trace:
                logging.info(f'[Cache] Not found meta: {chain_id=}/{address}')
            return False, {}

        if self._trace:
            logging.info(f'[Cache] Return meta: {chain_id=}/{address}')
        return True, needle

    def put(self, chain_id, address, meta):
        if chain_id not in self._cache:
            self._cache[chain_id] = {}

        if address not in self._cache[chain_id]:
            block_number = None
            if len(meta['contracts']) > 0:
                block_number = meta['contracts'][0]['block_number']
            self._cache[chain_id][address] = meta
            if self._trace:
                logging.info(f'[Cache] Save {chain_id=}/{address} '
                             f'valid from {block_number}')


class Contract(Account):

    class ContractMetaData(DTO):
        contract_name: Union[str, None] = None
        deploy_tx_hash: Union[str, None] = None
        constructor_args: Union[str, None] = None
        abi_hash: Union[str, None] = None
        abi: Union[ABI, None] = None
        is_transparent_proxy: Union[bool, None] = None
        proxy_implementation: Union[Any, None] = None
        deployed_block_number: Union[BlockNumber, None] = None

    _meta: ContractMetaData = PrivateAttr(
        default_factory=lambda: Contract.ContractMetaData())  # pylint: disable=unnecessary-lambda
    _instance: Union[Web3Contract, None] = PrivateAttr(default=None)
    _proxy_implementation = PrivateAttr(default=None)
    _loaded = PrivateAttr(default=False)
    _ledger = PrivateAttr(default=None)

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
        self._ledger = None

    def _load(self):
        # pylint: disable=locally-disabled, line-too-long, too-many-branches, too-many-statements
        if self._loaded:
            return
        context = credmark.cmf.model.ModelContext.current_context()

        in_cache, cached_meta = ContractMetaCache().get(context.chain_id, self.address)

        if in_cache:
            contract_q_results = cached_meta
        else:
            contract_q_results = context.run_model('contract.metadata',
                                                   {'contractAddress': self.address})
            ContractMetaCache().put(context.chain_id,
                                    self.address,
                                    contract_q_results)

        if len(contract_q_results['contracts']) > 0:
            res = contract_q_results['contracts'][0]

            block_number = res.get('block_number', None)
            if block_number is not None:
                if block_number > context.block_number:
                    raise BlockNumberOutOfRangeError(
                        f'Contract {self.address} is initialized on the current block '
                        f'({context.block_number}) earlier than it was deployed '
                        f'({res.get("block_number", None)}).')
                self._meta.deployed_block_number = BlockNumber(block_number)
            else:
                self._meta.deployed_block_number = None

            self._meta.contract_name = res.get('contract_name')
            self._meta.constructor_args = res.get('constructor_args')
            self._meta.abi = ABI(res.get('abi'))
            self._meta.is_transparent_proxy = res.get('proxy', 0) == "1"

            if self._meta.is_transparent_proxy:
                # TODO: as we only store the latest implementation in DB but not in the past.
                proxy_address = res.get('implementation')
                if context.chain_id == 1:
                    # TODO: Implementation needs to be validated on the db
                    if self._meta.contract_name in ['OwnedUpgradeabilityProxy']:
                        if self.address == '0x0000000000085d4780B73119b644AE5ecd22b376':
                            proxy_address = context.web3.eth.get_storage_at(
                                self.address,
                                context.web3.keccak(text="trueUSD.proxy.implementation").hex()).hex()
                            proxy_address = '0x' + proxy_address[-40:]
                    elif self._meta.contract_name in ["AdminUpgradeabilityProxy", 'FiatTokenProxy']:
                        proxy_address = context.web3.eth.get_storage_at(
                            self.address,
                            context.web3.keccak(text='org.zeppelinos.proxy.implementation')).hex()
                        proxy_address = '0x' + proxy_address[-40:]
                        if proxy_address == Address.null():
                            storage_addr = hex(int(context.web3.keccak(
                                text='eip1967.proxy.implementation').hex(), 16) - 1)
                            proxy_address = context.web3.eth.get_storage_at(
                                self.address, storage_addr).hex()
                        proxy_address = '0x' + proxy_address[-40:]
                    elif (self._meta.contract_name == 'Unitroller' and
                          self.address == '0x3d9819210A31b4961b30EF54bE2aeD79B9c9Cd3B'):
                        cc = context.web3.eth.contract(address=Address(
                            self.address).checksum, abi=self._meta.abi)
                        proxy_address = cc.functions.comptrollerImplementation().call()
                    elif self._meta.contract_name in ["RenERC20Proxy",
                                                      "InitializableAdminUpgradeabilityProxy",
                                                      "InitializableImmutableAdminUpgradeabilityProxy"]:
                        # if eip-1967 compliant, https://eips.ethereum.org/EIPS/eip-1967
                        proxy_address = context.web3.eth.get_storage_at(
                            self.address,
                            '0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc').hex()
                        proxy_address = '0x' + proxy_address[-40:]
                    elif (self._meta.contract_name == 'Delegator' and
                          self.address == '0x1985365e9f78359a9B6AD760e32412f4a445E862'):
                        cc = context.web3.eth.contract(address=Address(
                            self.address).checksum, abi=self._meta.abi)
                        controller = Contract(address=Address(cc.functions.getController().call()))
                        lookupName = '0x' + cc.functions.controllerLookupName().call().hex()
                        proxy_address = controller.functions.lookup(lookupName).call()
                        proxy_address = '0x' + proxy_address[-40:]
                self._meta.proxy_implementation = Contract(address=proxy_address)
            self._loaded = True
        else:
            if self._meta.abi is None:
                raise ModelDataError(f'abi not available for address {self.address}')
        self._loaded = True

    @ property
    def instance(self) -> Web3Contract:
        """
        A web3 Web3Contract instance or raises a
        ``ModelDataError`` if no ABI is available.
        """
        if self._instance is None:
            if self.abi is not None:
                context = credmark.cmf.model.ModelContext.current_context()
                self._instance = context.web3.eth.contract(
                    address=context.web3.toChecksumAddress(self.address),
                    abi=self.abi
                )
                return self._instance
            else:
                raise ModelDataError('Unable to load the ABI of the contract')
        else:
            return self._instance

    @ property
    def proxy_for(self):
        """
        A proxy implementation if available
        """
        if not self._loaded:
            self._load()
        return self._meta.proxy_implementation

    @ property
    def functions(self):
        """
        A web3 ContractFunctions instance for the contract.
        """
        if self.proxy_for is not None:
            context = credmark.cmf.model.ModelContext.current_context()
            return context.web3.eth.contract(
                address=context.web3.toChecksumAddress(self.address),
                abi=self.proxy_for.abi
            ).functions
        else:
            return self.instance.functions

    @ property
    def events(self):
        """
        A web3 ContractEvents instance for the contract.

        """
        if isinstance(self.proxy_for, Contract):
            return self.proxy_for.events
        return self.instance.events

    @ property
    def info(self):
        """
        A :class:`credmark.cmf.types.contract.ContractInfo` instance for the contract.
        """
        if isinstance(self, ContractInfo):
            return self
        self._load()
        return ContractInfo(**self.dict(), meta=self._meta)

    @ property
    def deploy_tx_hash(self):
        """
        The deploy transaction hash, if available, otherwise None.
        """
        if not self._loaded:
            self._load()
        return self._meta.deploy_tx_hash

    @ property
    def contract_name(self):
        """
        Name of the contract, if available, otherwise None.
        """
        if not self._loaded:
            self._load()
        return self._meta.contract_name

    @ property
    def constructor_args(self):
        """
        Constructor args, if any, otherwise None.
        """
        if not self._loaded:
            self._load()
        return self._meta.constructor_args

    @property
    def abi(self):
        """
        The ABI for the contract, if it's available, otherwise None.
        """
        if not self._loaded:
            self._load()
        return self._meta.abi

    @property
    def deployed_block_number(self):
        if not self._loaded:
            self._load()
        return self._meta.deployed_block_number

    def set_abi(self, abi: Union[List, str]):
        """
        Set the ABI for the contract
        """
        if not self._loaded:
            self._load()
        self._meta.abi = ABI(abi)

    @ property
    def is_transparent_proxy(self):
        """
        True if is a transparent proxy. Otherwise False or None.
        """
        if not self._loaded:
            self._load()
        return self._meta.is_transparent_proxy

    @ property
    def ledger(self):
        """
        A :class:`~credmark.cmf.types.ledger.ContractLedger` instance which can be
        used to query the ledger for a contract's functions or events.

        To run a query, call a method ``contract.ledger.functions.contractFunctionName()``
        or ``contract.ledger.events.contractEventName()`` where ``contractFunctionName``
        and ``contractEventName`` are the actual names of functions and events
        of the contract.

        Functions example::

            contract = Contract(address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')
            ret = contract.ledger.functions.approve(
                    columns=[ContractLedger.Functions.InputCol('spender')],
                    aggregates=[
                        ContractLedger.Aggregate(
                            f'MAX({ContractLedger.Functions.InputCol("value")})', 'max_value')
                    ],
                    group_by=ContractLedger.Functions.InputCol('spender'),
                    order_by='"max_value" desc',
                    limit='5')

            top_approvals = []
            for row in ret.data:
                top_approvals.append({
                    "spender": row[ContractLedger.Functions.InputCol('spender')],
                    "value": row['max_value']
                })

        Events example::

            ret = contract.ledger.events.Transfer(
                    columns=[ContractLedger.Events.Columns.EVT_BLOCK_NUMBER,
                        ContractLedger.Events.InputCol('from'),
                        ContractLedger.Events.InputCol('to'),
                        ContractLedger.Events.InputCol('value')],
                    order_by=f'{ContractLedger.Events.Columns.EVT_BLOCK_NUMBER} desc',
                    limit='4')

        See :class:`~credmark.cmf.types.ledger.ContractLedger.ContractEntity` for more details.
        """
        if self._ledger is None:
            self._ledger = ContractLedger(str(self.address))
        return self._ledger


class ContractInfo(Contract):
    meta: Contract.ContractMetaData


class Contracts(IterableListGenericDTO[Contract]):
    contracts: List[Contract] = DTOField(default=[], description="A List of Contracts")
    _iterator: str = PrivateAttr('contracts')
