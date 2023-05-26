# pylint: disable=line-too-long, protected-access, too-many-branches

from typing import Any, List, Union

from eth_typing.evm import ChecksumAddress
from web3.exceptions import ABIFunctionNotFound, BadFunctionCallOutput

import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError, ModelRunError
from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr

from .abi import ABI
from .address import Address, evm_address_regex
from .block_number import BlockNumberOutOfRangeError
from .contract import Contract
from .data.erc_standard_data import ERC20_BASE_ABI
from .data.fungible_token_data import FUNGIBLE_TOKEN_DATA_BY_ADDRESS, FUNGIBLE_TOKEN_DATA_BY_SYMBOL, NATIVE_TOKEN


def get_token_from_configuration(
        chain_id: int,
        symbol: Union[str, None] = None,
        address: Union[Address, None] = None,
        is_native_token: bool = False) -> Union[dict, None]:

    if is_native_token:
        native_token_meta = NATIVE_TOKEN[chain_id]
        if ((symbol is None or native_token_meta['symbol'] == symbol) and
                (address is None or native_token_meta['address'] == Address(address))):
            return native_token_meta
        else:
            return None

    chain_tokens_by_symbol = FUNGIBLE_TOKEN_DATA_BY_SYMBOL.get(chain_id, {})
    chain_tokens_by_address = FUNGIBLE_TOKEN_DATA_BY_ADDRESS.get(chain_id, {})

    if symbol is not None:
        token_meta = chain_tokens_by_symbol.get(symbol, None)
        if ((token_meta is not None) and
                (address is None or token_meta['address'] == Address(address))):
            return token_meta
        else:
            return None
    else:
        return chain_tokens_by_address.get(address, None)


class Token(Contract):
    """
    Fungible Token that conforms to ERC20 standards.
    You could create a token with the following

        t = Token(symbol='CMK')

        t = Token(address='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')

        t = Token('CMK')

        t = Token('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')

    """

    class TokenMetadata(Contract.ContractMetaData):
        symbol: Union[str, None] = None
        name: Union[str, None] = None
        decimals: Union[int, None] = None
        total_supply: Union[int, None] = None
        wrapped: Union[Address, None] = None
        set_loaded: bool = False
        _cache: dict[str, dict[int, dict[int, Any]]] = PrivateAttr(default={})

        def get_cache(self, field, chain_id, block_number):
            return self._cache.get(field, {}).get(chain_id, {}).get(block_number)

        def update_cache(self, field, chain_id, block_number, value):
            if field not in self._cache:
                self._cache[field] = {}
            if chain_id not in self._cache[field]:
                self._cache[field][chain_id] = {}
            self._cache[field][chain_id][block_number] = value

    _meta: TokenMetadata = PrivateAttr(
        default_factory=lambda: Token.TokenMetadata())  # pylint: disable=unnecessary-lambda

    class Config:
        schema_extra = {
            'examples': [{'address': '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'},
                         {'symbol': 'AAVE'}
                         ] + Contract.Config.schema_extra['examples']
        }

    @classmethod
    def validate(cls, value):
        if isinstance(value, str):
            return cls(value)
        if isinstance(value, dict):
            return cls(**value)
        if isinstance(value, NativeToken):
            return value
        if isinstance(value, Token):
            return value
        raise TypeError(
            f'{cls.__name__} must be deserialized with an str or dict')

    def __new__(cls, *args, **data):
        if cls == NativeToken:
            return super().__new__(cls)

        if len(args) > 0:
            if isinstance(args[0], str):
                if evm_address_regex.match(args[0]) is not None:
                    if 'address' not in data:
                        data['address'] = args[0]
                else:
                    if 'symbol' not in data:
                        data['symbol'] = args[0]
            elif isinstance(args[0], dict):
                data = args[0] | data

        context = credmark.cmf.model.ModelContext.current_context()
        symbol = data.get('symbol', None)
        address = data.get('address', None)

        if symbol is None and address is None:
            return super().__new__(cls)

        token_data = get_token_from_configuration(
            chain_id=context.chain_id,
            symbol=symbol,
            address=address,
            is_native_token=True)

        if token_data is not None:
            return super().__new__(NativeToken)

        return super().__new__(cls)

    def __init__(self, *args, **data):
        if len(args) > 0:
            if isinstance(args[0], str):
                if evm_address_regex.match(args[0]) is not None:
                    if 'address' not in data:
                        data['address'] = args[0]
                else:
                    if 'symbol' not in data:
                        data['symbol'] = args[0]
            elif isinstance(args[0], dict):
                data = args[0] | data

        if 'address' not in data and 'symbol' not in data:
            raise ModelDataError('One of address or symbol is required')

        if 'address' not in data and 'symbol' in data:
            context = credmark.cmf.model.ModelContext.current_context()

            token_data = get_token_from_configuration(
                chain_id=context.chain_id, symbol=data['symbol'])

            if token_data is None:
                raise ModelDataError(f'Unsupported symbol: {data["symbol"]}')

            data['address'] = token_data['address']
            if 'meta' not in data:
                data['meta'] = {}
            data['meta']['symbol'] = token_data['symbol']
            data['meta']['name'] = token_data['name']
            data['meta']['decimals'] = token_data['decimals']
            data['meta']['wrapped'] = (Address(token_data['wrapped'])
                                       if 'wrapped' in token_data else None)

            if token_data.get('set_loaded', False):  # Special case for BTC
                self._loaded = True
                data['meta']['set_loaded'] = True
            else:
                data['meta']['set_loaded'] = False

        if data['address'] == Address.null():
            raise ModelDataError(
                f'NULL address ({Address.null()}) is not a valid Token Address')

        super().__init__(**data)

    def _load(self):
        if self._loaded:
            return

        if self._meta.abi is None:
            self._meta.abi = ABI(ERC20_BASE_ABI)

        super()._load()

    def as_erc20(self, set_loaded=False):
        if set_loaded:
            self.set_abi(ABI(ERC20_BASE_ABI), set_loaded=True)
            return self

        try:
            _ = self.abi
        except ModelDataError:
            self._meta.abi = ABI(ERC20_BASE_ABI)

        if self.proxy_for is not None:
            try:
                _ = self.proxy_for.abi
            except BlockNumberOutOfRangeError as err:
                raise BlockNumberOutOfRangeError(
                    err.data.message + f' for contract {self.address}') from err
            except ModelDataError:
                self.proxy_for.set_abi(ERC20_BASE_ABI, set_loaded=True)

        return self

    @property
    def info(self):
        _ = self.symbol, self.name, self.decimals, self.total_supply
        if isinstance(self, TokenInfo):
            return self
        self._load()

        return TokenInfo(**self.dict(), meta=self._meta)

    def try_erc20_property(self, prop_name):
        try:
            prop_value = self.functions[prop_name]().call()  # type: ignore
        except (BadFunctionCallOutput, ABIFunctionNotFound) as err:
            raise ModelDataError(
                f'No {prop_name} function on token {self.address}, non ERC20 Compliant'
                f' proxied by {self.proxy_for.address}' if self.proxy_for is not None else ''
            ) from err
        if prop_value is None:
            raise ModelDataError(f"Token.{prop_name} is None")
        return prop_value

    @property
    def symbol(self) -> str:
        self._load()
        current_block = int(credmark.cmf.model.ModelContext.current_context().web3.eth.default_block)
        current_chain_id = credmark.cmf.model.ModelContext.current_context().chain_id

        if not self._meta.set_loaded:
            self._meta.symbol = self._meta.get_cache('symbol', current_chain_id, current_block)

        if self._meta.symbol is None:
            try:
                symbol_tmp = self.try_erc20_property('symbol')
            except ModelDataError:
                symbol_tmp = self.try_erc20_property('SYMBOL')
            if isinstance(symbol_tmp, bytes):
                symbol_tmp = symbol_tmp.decode(
                    'utf-8', errors='strict').replace('\x00', '')
            elif isinstance(symbol_tmp, str):
                symbol_tmp = symbol_tmp.replace('\x00', '')
            elif not isinstance(symbol_tmp, str):
                raise ModelDataError(f'Unknown value for symbol {symbol_tmp}')
            self._meta.symbol = symbol_tmp
            self._meta.update_cache('symbol', current_chain_id, current_block, self._meta.symbol)
        return self._meta.symbol

    @property
    def decimals(self) -> int:
        self._load()
        current_block = int(credmark.cmf.model.ModelContext.current_context().web3.eth.default_block)
        current_chain_id = credmark.cmf.model.ModelContext.current_context().chain_id

        if not self._meta.set_loaded:
            self._meta.decimals = self._meta.get_cache('decimals', current_chain_id, current_block)

        if self._meta.decimals is None:
            try:
                self._meta.decimals = self.try_erc20_property('decimals')
            except ModelDataError:
                self._meta.decimals = self.try_erc20_property('DECIMALS')
            self._meta.update_cache('decimals', current_block, current_chain_id, self._meta.decimals)

        return self._meta.decimals

    @property
    def name(self) -> str:
        self._load()
        current_block = int(credmark.cmf.model.ModelContext.current_context().web3.eth.default_block)
        current_chain_id = credmark.cmf.model.ModelContext.current_context().chain_id
        if not self._meta.set_loaded:
            self._meta.name = self._meta.get_cache('name', current_chain_id, current_block)

        if self._meta.name is None:
            try:
                name_tmp = self.try_erc20_property('name')
            except ModelDataError:
                name_tmp = self.try_erc20_property('NAME')
            if isinstance(name_tmp, bytes):
                name_tmp = name_tmp.decode(
                    'utf-8', errors='strict').replace('\x00', '')
            elif isinstance(name_tmp, str):
                name_tmp = name_tmp.replace('\x00', '')
            elif not isinstance(name_tmp, str):
                raise ModelDataError(f'Unknown value for name {name_tmp}')
            self._meta.name = name_tmp
            self._meta.update_cache('name', current_chain_id, current_block, self._meta.name)
        return self._meta.name

    @property
    def total_supply(self) -> int:
        self._load()
        current_block = int(credmark.cmf.model.ModelContext.current_context().web3.eth.default_block)
        current_chain_id = credmark.cmf.model.ModelContext.current_context().chain_id
        if not self._meta.set_loaded:
            self._meta.total_supply = self._meta.get_cache('total_supply', current_chain_id, current_block)

        if self._meta.total_supply is None:
            self._meta.total_supply = self.try_erc20_property('totalSupply')
            self._meta.update_cache('total_supply', current_chain_id, current_block, self._meta.total_supply)
        return self._meta.total_supply

    @property
    def total_supply_scaled(self) -> float:
        return self.scaled(self.total_supply)

    def scaled(self, value) -> float:
        return value / (10 ** self.decimals)

    def balance_of(self, address: ChecksumAddress) -> int:
        balance = self.functions.balanceOf(address).call()
        return balance

    def balance_of_scaled(self, address: ChecksumAddress) -> float:
        return self.scaled(self.balance_of(address))

    @property
    def fiat(self) -> bool:
        return False


class TokenInfo(Token):
    """
    Subclass of Token containing its related metadata.
    """
    meta: Token.TokenMetadata

    @property
    def ledger(self) -> None:
        return None


class NativeToken(Token):
    """
    Native token for a chain, such as "ETH" or "MATIC".
    """

    def __init__(self, *args, **kwargs) -> None:
        context = credmark.cmf.model.ModelContext.current_context()
        token_data = NATIVE_TOKEN[context.chain_id]
        if token_data is None:
            raise ModelRunError(
                f'No native token specified for chain id: {context.chain_id}')

        if len(args) > 0:
            if isinstance(args[0], str):
                if evm_address_regex.match(args[0]) is not None:
                    if 'address' not in kwargs:
                        kwargs['address'] = args[0]
                else:
                    if 'symbol' not in kwargs:
                        kwargs['symbol'] = args[0]
            elif isinstance(args[0], dict):
                kwargs = args[0] | kwargs

        symbol = kwargs.get('symbol', None)
        address = kwargs.get('address', None)
        if symbol is not None and token_data['symbol'] != symbol:
            raise ModelRunError(
                f'Wrong symbol {symbol} specified for {token_data["symbol"]} '
                f'for chain id: {context.chain_id}')
        if address is not None and token_data['address'] != Address(address):
            raise ModelRunError(
                f'Wrong address {address} specified for {token_data["address"]} '
                f'for chain id: {context.chain_id}')
        super().__init__(**({'address': token_data['address']}))

        self._meta.abi = ABI([])
        self._meta.symbol = token_data['symbol']
        self._meta.name = token_data['name']
        self._meta.decimals = token_data['decimals']
        self._meta.wrapped = Address(token_data['wrapped'])
        self._meta.total_supply = 0
        self._loaded = True

    def balance_of(self, address: ChecksumAddress) -> int:
        context = credmark.cmf.model.ModelContext.current_context()
        balance = context.web3.eth.get_balance(address)
        return balance

    def balance_of_scaled(self, address: ChecksumAddress) -> float:
        context = credmark.cmf.model.ModelContext.current_context()
        balance = self.balance_of(address)
        return float(context.web3.fromWei(balance, 'ether'))

    @property
    def symbol(self):
        if self._meta.symbol is not None:
            return self._meta.symbol
        raise ModelRunError(f'No symbol found for {self}')

    @property
    def name(self):
        if self._meta.name is not None:
            return self._meta.name
        raise ModelRunError(f'No name found for {self}')

    @property
    def decimals(self):
        if self._meta.decimals is not None:
            return self._meta.decimals
        raise ModelRunError(f'No decimals found for {self}')

    @property
    def ledger(self) -> None:
        return None

    def wrapped(self) -> Token:
        if self._meta.wrapped is not None:
            return Token(address=self._meta.wrapped)
        raise ValueError('No wrapper Token found')


class Tokens(IterableListGenericDTO[Token]):
    """
    Iterable list of Token instances.
    """

    tokens: List[Token] = DTOField(
        default=[], description="An iterable list of Token Objects")
    _iterator: str = PrivateAttr('tokens')

    class Config:
        schema_extra = {
            "examples": [{"tokens": ['0x6B175474E89094C44Da98b954EedeAC495271d0F',  # DAI
                                     '0x514910771AF9Ca656af840dff83E8264EcF986CA']}]  # LINK
        }

    @classmethod
    def from_addresses(cls, addresses: List[Address]) -> 'Tokens':
        """
        Returns a Tokens instance from a list of addresses.
        """
        return cls(tokens=[Token(address=address) for address in addresses])

    @classmethod
    def empty(cls) -> 'Tokens':
        """
        Returns an empty Tokens instance.
        """
        return cls(tokens=[])
