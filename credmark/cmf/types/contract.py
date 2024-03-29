# pylint: disable=line-too-long

from typing import List, Optional, Sequence, Union, cast

from web3 import Web3
from web3.contract.contract import Contract as Web3Contract

import credmark.cmf.model
from credmark.cmf.engine.cache import ContractMetaCache
from credmark.cmf.model.errors import (ModelDataError, ModelEngineError,
                                       ModelRunError)
from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr

from .abi import ABI
from .account import Account
from .address import Address
from .block_number import BlockNumber, BlockNumberOutOfRangeError
from .contract_web3 import fetch_events
from .ledger_contract import ContractLedger

SLOT_TRUEUSD = Web3.keccak(text="trueUSD.proxy.implementation").hex()
SLOT_ZEPPELINOS = Web3.keccak(text='org.zeppelinos.proxy.implementation').hex()
SLOT_EIP1967 = hex(
    int(Web3.keccak(text='eip1967.proxy.implementation').hex(), 16) - 1)
SLOT_BEACON = hex(int(Web3.keccak(text='eip1967.proxy.beacon').hex(), 16) - 1)
SLOT_PPROXY = hex(int(Web3.keccak(text='IMPLEMENTATION_SLOT').hex(), 16))
SLOT_PROXYMANYTOONE = hex(
    int(Web3.keccak(text='IMPLEMENTATION_ADDRESS').hex(), 16) + 1)
SLOT_ARA = hex(int(Web3.keccak(text='io.ara.proxy.implementation').hex(), 16))

# pylint:disable=too-many-branches


def get_slot_proxy_address(context, contract_address,
                           contract_name, contract_abi) -> Optional[Address]:
    slot_proxy_address = None
    if context.chain_id == 1:
        if contract_name == 'Unitroller':
            if contract_address == Address('0x3d9819210A31b4961b30EF54bE2aeD79B9c9Cd3B'):
                cc = context.web3.eth.contract(address=Address(
                    contract_address).checksum, abi=contract_abi)
                slot_proxy_address = Address(
                    cc.functions.comptrollerImplementation().call())
        elif contract_name in ['DelegateCallProxyManyToOne']:
            slot_proxy_address = Address(context.web3.eth.get_storage_at(
                contract_address, SLOT_PROXYMANYTOONE))
        elif contract_name in ['AraProxy']:
            slot_proxy_address = Address(
                context.web3.eth.get_storage_at(contract_address, SLOT_ARA))
        elif contract_name in ['YAMDelegator',
                               'CErc20Delegator',
                               'AppProxyUpgradeable',
                               'ZoraProxy',
                               'TokenProxy',
                               'MeterGovProxy',
                               'InstaToken']:
            # EIP-897
            cc = context.web3.eth.contract(address=Address(
                contract_address).checksum, abi=contract_abi)
            if cc.abi is not None and 'implementation' in cc.abi.functions:
                slot_proxy_address = Address(
                    cc.functions.implementation().call())
        elif (contract_name == 'Delegator' and
                contract_address == Address('0x1985365e9f78359a9B6AD760e32412f4a445E862')):
            cc = context.web3.eth.contract(address=Address(
                contract_address).checksum, abi=contract_abi)
            controller = Contract(address=Address(
                cc.functions.getController().call()))
            lookupName = cc.functions.controllerLookupName().call()
            slot_proxy_address = Address(
                cast(str, controller.functions.lookup(lookupName).call()))
        elif contract_name in ['OwnedUpgradeabilityProxy']:
            if contract_address == Address('0x0000000000085d4780B73119b644AE5ecd22b376'):
                slot_proxy_address = Address(
                    context.web3.eth.get_storage_at(contract_address, SLOT_TRUEUSD))
        elif contract_name in ['FiatTokenProxy',
                               'AdminUpgradeabilityProxy',
                               'InitializeGovernedUpgradeabilityProxy']:
            slot_proxy_address = Address(
                context.web3.eth.get_storage_at(contract_address, SLOT_EIP1967))
            if slot_proxy_address.is_null():
                slot_proxy_address = Address(
                    context.web3.eth.get_storage_at(contract_address, SLOT_ZEPPELINOS))
        elif contract_name in ['BeaconProxy', 'UpgradeBeaconProxy', ]:
            # TODO: BEACON has a special design. The actual contract could be two-levels down
            # From token -> beacon -> beacon's implementation
            # context.web3.eth.contract(address='0x5A235C0b4cB8d0e80a5c3bF4d2faD5c32E440884',
            #       abi=Contract('0x612447E8d0BDB922059cE048bb5a7CeF9e017812').abi)
            #           .functions.childImplementation().call()
            # context.web3.eth.contract(
            #       address=Address('0xBE86f647b167567525cCAAfcd6f881F1Ee558216').checksum,
            #       abi=Contract('0x612447E8d0BDB922059cE048bb5a7CeF9e017812').abi)
            #           .functions.childImplementation().call()
            # cc = Contract('0xd31a59c85ae9d8edefec411d448f90841571b89c');
            # pd.DataFrame(cc.fetch_events(cc.instance.events.BeaconUpgraded,
            # from_block=0, to_block=self.context.block_number))
            slot_proxy_address = Address(
                context.web3.eth.get_storage_at(contract_address, SLOT_BEACON))
        elif contract_name in ['InitializedProxy']:
            cc = context.web3.eth.contract(address=Address(
                contract_address).checksum, abi=contract_abi)
            if cc.abi is not None and 'logic' in cc.abi.functions:
                slot_proxy_address = Address(cc.functions.logic().call())
        elif contract_name in ['PProxyPausable', 'PProxy']:
            slot_proxy_address = Address(
                context.web3.eth.get_storage_at(contract_address, SLOT_PPROXY))
            cc = context.web3.eth.contract(address=Address(
                contract_address).checksum, abi=contract_abi)
            if cc.abi is not None and 'getImplementation' in cc.abi.functions:
                slot_proxy_address = Address(
                    cc.functions.getImplementation().call())
        elif contract_name in ['RenERC20Proxy',
                               'RenBTC',
                               'TransparentUpgradeableProxy',
                               'InitializableAdminUpgradeabilityProxy',
                               'InitializableImmutableAdminUpgradeabilityProxy',
                               'BridgeToken',
                               'ERC1967Proxy']:
            # if eip-1967 compliant, https://eips.ethereum.org/EIPS/eip-1967
            slot_proxy_address = Address(
                context.web3.eth.get_storage_at(contract_address, SLOT_EIP1967))
        # else:
        #    slot_proxy_address = Address(context.web3.eth.get_storage_at(contract_address, SLOT_EIP1967))

    if slot_proxy_address is None or slot_proxy_address.is_null():
        return None

    return slot_proxy_address


class Contract(Account):
    """
    Contract object to make web3 call smart contract functions.
    You could create a contract with the following

        c = Contract(address='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

        c = Contract('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

    """

    class ContractMetaData(DTO):
        contract_name: Optional[str] = None
        deploy_tx_hash: Optional[str] = None
        constructor_args: Optional[str] = None
        abi_hash: Optional[str] = None
        abi: Optional[ABI] = None
        is_transparent_proxy: Optional[bool] = None
        proxy_implementation: Optional['Contract'] = None
        deployed_block_number: Optional[BlockNumber] = None

    _meta: ContractMetaData = PrivateAttr(
        default_factory=lambda: Contract.ContractMetaData())  # pylint: disable=unnecessary-lambda
    _instance: Web3Contract | None = PrivateAttr(default=None)
    _loaded: bool = PrivateAttr(default=False)
    _ledger: Optional[ContractLedger] = PrivateAttr(default=None)
    _custom_abi: Optional[ABI] = PrivateAttr(default=None)

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True
        schema_extra = {
            'examples': Account.Config.schema_extra['examples'] +
            [{'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984',
              'abi': '(Optional) contract abi JSON string or list'
              }]
        }

    def __init__(self, *args, **data):
        super().__init__(*args, **data)

        meta = data.get('meta', None)
        if meta is not None:
            if isinstance(meta, dict):
                self._meta = type(self._meta)(**meta)
            if isinstance(meta, type(self._meta)):
                self._meta = meta

        if isinstance(data.get('abi'), (str, list)):
            self._meta.abi = ABI(data['abi'])
            self._custom_abi = self._meta.abi
        self._instance = None
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
            try:
                # fix block number when looking up contract
                contract_q_results = context.run_model('contract.metadata',
                                                       {'contractAddress': self.address},
                                                       block_number=0)
                ContractMetaCache().put(context.chain_id,
                                        self.address,
                                        contract_q_results)
            except ModelEngineError:
                contract_q_results = {"contracts": []}

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

            implementation_address = None
            if self._meta.contract_name in ['BeaconProxy', 'BridgeToken'] and self._meta.is_transparent_proxy:
                # TODO: Special case for BeaconProxy, proxy address may not up to date
                implementation_address = res.get('implementation')
            else:
                slot_proxy_address = get_slot_proxy_address(
                    context, self.address, self._meta.contract_name, self._meta.abi)

                if slot_proxy_address is not None and not slot_proxy_address.is_null():
                    # TODO: as we only store the latest implementation in DB but not for the history.
                    implementation_address = slot_proxy_address
                elif self._meta.is_transparent_proxy:
                    implementation_address = res.get('implementation')

            if implementation_address is not None:
                self._meta.proxy_implementation = Contract(
                    address=implementation_address,
                    # If a custom ABI is provided, we pass it on to
                    # the implementation contract to use as fallback
                    abi=self._custom_abi)
            self._loaded = True
        else:
            if self._meta.abi is None:
                raise ModelDataError(
                    f'abi not available for address {self.address}')
        self._loaded = True

    @property
    def instance(self) -> Web3Contract:
        """
        A web3 Web3Contract instance or raises a
        ``ModelDataError`` if no ABI is available.
        """
        context = credmark.cmf.model.ModelContext.current_context()
        if self._instance is not None:
            if (self._instance.w3.eth.chain_id != context.chain_id
                    or self._instance.w3.eth.default_block != context.block_number):
                self._instance = None

        if self._instance is None:
            if self.abi is not None:
                self._instance = context.web3.eth.contract(
                    address=context.web3.to_checksum_address(self.address),
                    abi=self.abi
                )
                return self._instance
            else:
                raise ModelDataError('Unable to load the ABI of the contract')
        else:
            return self._instance

    @property
    def proxy_for(self):
        """
        A proxy implementation if available
        """
        if not self._loaded:
            self._load()
        return self._meta.proxy_implementation

    @property
    def functions(self):
        """
        A web3 ContractFunctions instance for the contract.
        """
        if self.proxy_for is not None:
            context = credmark.cmf.model.ModelContext.current_context()
            return context.web3.eth.contract(
                address=context.web3.to_checksum_address(self.address),
                abi=self.proxy_for.abi).functions
        else:
            return self.instance.functions

    @property
    def events(self):
        """
        A web3 ContractEvents instance for the contract.

        """
        if isinstance(self.proxy_for, Contract):
            return self.proxy_for.events
        return self.instance.events

    @property
    def info(self):
        """
        A :class:`credmark.cmf.types.contract.ContractInfo` instance for the contract.
        """
        if isinstance(self, ContractInfo):
            return self
        self._load()
        return ContractInfo(**self.dict(), meta=self._meta)

    @property
    def deploy_tx_hash(self):
        """
        The deploy transaction hash, if available, otherwise None.
        """
        if not self._loaded:
            self._load()
        return self._meta.deploy_tx_hash

    @property
    def contract_name(self):
        """
        Name of the contract, if available, otherwise None.
        """
        if not self._loaded:
            self._load()
        return self._meta.contract_name

    @property
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

    def set_abi(self, abi: Union[List, str], set_loaded=False):
        """
        Set the ABI for the contract
        """
        if set_loaded:
            self._loaded = True
        else:
            if not self._loaded:
                try:
                    self._load()
                except ModelDataError as err:
                    # pylint: disable=unsupported-membership-test
                    if 'abi not available for address' not in err.data.message:
                        raise
        self._meta.abi = ABI(abi)
        return self

    @property
    def is_transparent_proxy(self):
        """
        True if is a transparent proxy. Otherwise False or None.
        """
        if not self._loaded:
            self._load()
        return self._meta.is_transparent_proxy

    @property
    def ledger(self) -> ContractLedger:
        """
        A :class:`~credmark.cmf.types.ledger.ContractLedger` instance which can be
        used to query the ledger for a contract's functions or events.

        To run a query, call a property of ``contract.ledger.functions.{NameOfFunction}``
        or ``contract.ledger.events.{NameOfEvent}``. The name of the function or event
        can be auto-completed by pressing TAB after the ``.``. Alternatively, you could
        looked up from ``contract.abi.functions`` or ``contract.abi.events``.

        Functions example::

            contract = Contract(address='0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04')
            with contract.ledger.functions.approve as q:
                ret = q.select(
                        columns=[q.spender')],
                        aggregates=[(f'MAX({q.value})', 'max_value')],
                        group_by=q.spender,
                        order_by='"max_value" desc',
                        limit=5)

                top_approvals = []
                for row in ret.data:
                    top_approvals.append({
                        "spender": row[q.spender],
                        "value": row['max_value']
                    })

        Events example::

            with contract.ledger.events.Transfer as q:
                ret = q.select(
                    columns=[q.EVT_BLOCK_NUMBER,
                             q.from,
                             q.to,
                             q.value],
                    order_by=q.EVT_BLOCK_NUMBER.desc(),
                    limit=4)

        See :class:`~credmark.cmf.types.ledger.ContractLedger.LedgerQueryContractFunctions` or
        :class:`~credmark.cmf.types.ledger.ContractLedger.LedgerQueryContractEvents`
        for more details.
        """
        if not self._loaded:
            self._load()

        if self._ledger is None:
            if self.proxy_for is not None and self.proxy_for.abi is not None:
                # TODO: Need to stitch all past proxied tables to become one table
                self._ledger = ContractLedger(address=self.address,
                                              proxy_address=self.proxy_for.address,
                                              abi=self.proxy_for.abi)
            elif self.abi is not None:
                self._ledger = ContractLedger(address=str(self.address),
                                              proxy_address=None,
                                              abi=self.abi)
            else:
                raise ModelRunError('Unable to obtain abi for the contract')
        return self._ledger

    # pylint: disable=too-many-arguments
    def fetch_events(self,
                     event,
                     argument_filters=None,
                     from_block=None,
                     to_block=None,
                     address=None,
                     topics=None,
                     contract_address=None,
                     argument_names: Optional[Sequence[str]] = None,
                     by_range: Optional[int] = None,
                     use_async: Optional[bool] = False,
                     async_worker: int = 10):
        """
        contract_address is by default set to the event's address.

        For proxy contract, the event could be from the proxy contract and
        contract_address could be overridden with the contract's address.

        For example,

            tok = Token('AAVE')
            list(tok.fetch_events(
                    tok.proxy_for.events.Transfer,
                    from_block=16_000_000,
                    to_block=16_010_000,
                    contract_address=tok.address))

        For non-proxy contract, we may use as following

            tok = Token('CRV')
            df = pd.DataFrame(tok.fetch_events(
                    tok.events.Transfer,
                    from_block=16_000_000,
                    to_block=16_001_000,
                    topics=['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef']))
            df.loc[:, ['blockNumber', '_from', '_to', '_value']]

        """
        context = credmark.cmf.model.ModelContext.current_context()
        if to_block is None:
            to_block = context.block_number
        elif to_block > context.block_number:
            raise ModelRunError(
                f'{to_block=} can not be later than current block {context.block_number}')
        return fetch_events(event,
                            argument_filters,
                            from_block,
                            to_block,
                            address=address,
                            topics=topics,
                            contract_address=contract_address,
                            argument_names=argument_names,
                            by_range=by_range,
                            async_web3=context.web3_async if use_async else None,
                            async_worker=async_worker)


class ContractInfo(Contract):
    meta: Contract.ContractMetaData

    @property
    def ledger(self) -> None:
        return None


class Contracts(IterableListGenericDTO[Contract]):
    contracts: List[Contract] = DTOField(
        default=[], description="A List of Contracts")
    _iterator: str = PrivateAttr('contracts')

    @classmethod
    def from_addresses(cls, addresses: List[Address]) -> 'Contracts':
        """
        Create a Contracts instance from a list of addresses.
        """
        return cls(contracts=[Contract(address=address) for address in addresses])

    @classmethod
    def empty(cls) -> 'Contracts':
        """
        Create a Contracts instance with no contracts.
        """
        return cls(contracts=[])
