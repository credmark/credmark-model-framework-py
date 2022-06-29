from typing import List, Union

import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError, ModelRunError
from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr
from web3.exceptions import ABIFunctionNotFound, BadFunctionCallOutput

from .abi import ABI
from .account import Account
from .address import Address, evm_address_regex
from .contract import Contract
from .data.erc_standard_data import ERC20_BASE_ABI
from .data.fiat_currency_data import (FIAT_CURRENCY_DATA_BY_ADDRESS,
                                      FIAT_CURRENCY_DATA_BY_SYMBOL)
from .data.fungible_token_data import (FUNGIBLE_TOKEN_DATA_BY_ADDRESS,
                                       FUNGIBLE_TOKEN_DATA_BY_SYMBOL,
                                       NATIVE_TOKEN)


def get_token_from_configuration(
        chain_id: str,
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
    """

    class TokenMetadata(Contract.ContractMetaData):
        symbol: Union[str, None] = None
        name: Union[str, None] = None
        decimals: Union[int, None] = None
        total_supply: Union[int, None] = None

    _meta: TokenMetadata = PrivateAttr(
        default_factory=lambda: Token.TokenMetadata())  # pylint: disable=unnecessary-lambda

    class Config:
        schema_extra = {
            'examples': [{'address': '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9'},
                         {'symbol': 'AAVE'}
                         ] + Contract.Config.schema_extra['examples']
        }

    def __new__(cls, **data):
        if cls == NativeToken:
            return super().__new__(cls)

        context = credmark.cmf.model.ModelContext.current_context()
        symbol = data.get('symbol', None)
        address = data.get('address', None)

        if symbol is None and address is None:
            return super().__new__(cls)

        token_data = get_token_from_configuration(
            chain_id=str(context.chain_id),
            symbol=symbol,
            address=address,
            is_native_token=True)

        if token_data is not None:
            return NativeToken()

        return super().__new__(cls)

    def __init__(self, **data):
        if 'address' not in data and 'symbol' not in data:
            raise ModelDataError('One of address or symbol is required')

        if 'address' not in data and 'symbol' in data:
            context = credmark.cmf.model.ModelContext.current_context()

            token_data = get_token_from_configuration(
                chain_id=str(context.chain_id), symbol=data['symbol'])

            if token_data is None:
                raise ModelDataError(f'Unsupported symbol: {data["symbol"]}')

            data['address'] = token_data['address']
            if 'meta' not in data:
                data['meta'] = {}
            data['meta']['symbol'] = token_data['symbol']
            data['meta']['name'] = token_data['name']
            data['meta']['decimals'] = token_data['decimals']

            if token_data.get('set_loaded_true', False):  # Special case for BTC
                self._loaded = True

        if data['address'] == Address.null():
            raise ModelDataError(f'NULL address ({Address.null()}) is not a valid Token Address')

        super().__init__(**data)

    def _load(self):
        if self._loaded:
            return

        if self._meta.abi is None:
            self._meta.abi = ABI(ERC20_BASE_ABI)

        super()._load()

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
        except (BadFunctionCallOutput, ABIFunctionNotFound):
            raise ModelDataError(
                f'No {prop_name} function on token {self.address}, non ERC20 Compliant'
                f' proxied by {self.proxy_for.address}' if self.proxy_for is not None else '')
        if prop_value is None:
            raise ModelDataError(f"Token.{prop_name} is None")
        return prop_value

    @property
    def symbol(self) -> str:
        self._load()
        if self._meta.symbol is None:
            symbol_tmp = self.try_erc20_property('symbol')
            if isinstance(symbol_tmp, bytes):
                symbol_tmp = symbol_tmp.decode('utf-8', errors='strict').replace('\x00', '')
            elif not isinstance(symbol_tmp, str):
                raise ModelDataError(f'Unknown value for symbol {symbol_tmp}')
            self._meta.symbol = symbol_tmp
        return self._meta.symbol

    @property
    def decimals(self) -> int:
        self._load()
        if self._meta.decimals is None:
            self._meta.decimals = self.try_erc20_property('decimals')
        return self._meta.decimals

    @property
    def name(self) -> str:
        self._load()
        if self._meta.name is None:
            name_tmp = self.try_erc20_property('name')
            if isinstance(name_tmp, bytes):
                name_tmp = name_tmp.decode('utf-8', errors='strict').replace('\x00', '')
            elif not isinstance(name_tmp, str):
                raise ModelDataError(f'Unknown value for name {name_tmp}')
            self._meta.name = name_tmp
        return self._meta.name

    @property
    def total_supply(self) -> int:
        self._load()
        if self._meta.total_supply is None:
            self._meta.total_supply = self.try_erc20_property('totalSupply')
        return self._meta.total_supply

    @property
    def total_supply_scaled(self) -> float:
        return self.scaled(self.total_supply)

    def scaled(self, value) -> float:
        return value / (10 ** self.decimals)

    def balance_of(self, address: Address) -> int:
        balance = self.functions.balanceOf(address).call()
        return balance

    def balance_of_scaled(self, address: Address) -> float:
        return self.scaled(self.balance_of(address))

    @property
    def fiat(self) -> bool:
        return False


class TokenInfo(Token):
    """
    Subclass of Token containing its related metadata.
    """
    meta: Token.TokenMetadata


class NativeToken(Token):
    """
    Native token for a chain, such as "ETH" or "MATIC".
    """

    def __init__(self, **kwargs) -> None:
        context = credmark.cmf.model.ModelContext.current_context()
        token_data = NATIVE_TOKEN[str(context.chain_id)]
        if token_data is None:
            raise ModelRunError(f'No native token specified for chain id: {context.chain_id}')

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
        super().__init__(address=token_data['address'])
        if context.chain_id == 1:
            self._meta.abi = ABI([])
            self._meta.symbol = token_data['symbol']
            self._meta.name = token_data['name']
            self._meta.decimals = token_data['decimals']
            self._meta.total_supply = 0
            self._loaded = True

    def balance_of(self, address: Address) -> int:
        context = credmark.cmf.model.ModelContext.current_context()
        if context.chain_id == 1:
            balance = context.web3.eth.get_balance(address)
            return balance
        else:
            raise ModelRunError(f'Not supported for chain id: {context.chain_id}')

    def balance_of_scaled(self, address: Address) -> float:
        context = credmark.cmf.model.ModelContext.current_context()
        if context.chain_id == 1:
            balance = self.balance_of(address)
            return float(context.web3.fromWei(balance, 'ether'))
        else:
            raise ModelRunError(f'Not supported for chain id: {context.chain_id}')


class NonFungibleToken(Contract):
    """
    Non-fungible token.

    `This class is not yet implemented`
    """

    def __init__(self, **data):
        super().__init__(**data)
        raise NotImplementedError()


class Tokens(IterableListGenericDTO[Token]):
    """
    Iterable list of Token instances.
    """

    tokens: List[Token] = DTOField(
        default=[], description="An iterable list of Token Objects")
    _iterator: str = PrivateAttr('tokens')


class FiatCurrency(Account):
    """
    Fiat currency.
    """

    class FiatCurrencyMeta:
        symbol: Union[str, None] = None
        name: Union[str, None] = None

    _meta: FiatCurrencyMeta = PrivateAttr(
        default_factory=lambda: FiatCurrency.FiatCurrencyMeta())  # pylint: disable=unnecessary-lambda

    def __init__(self, **data):
        address = data.get('address', None)
        symbol = data.get("symbol", None)

        if symbol is None and address is None:
            raise ModelDataError('Missing both symbol and address')

        if symbol is not None:
            fiat_meta = FIAT_CURRENCY_DATA_BY_SYMBOL.get(symbol, None)
            if fiat_meta is not None:
                if address is None or fiat_meta['address'] == address:
                    super().__init__(address=Address(fiat_meta["address"]))
                    self._meta.symbol = fiat_meta["symbol"]
                    self._meta.name = fiat_meta["name"]
                else:
                    raise ModelDataError(
                        f'Mismatch {symbol}/{address} for '
                        f'{fiat_meta["symbol"]}/{fiat_meta["address"]}')
            elif address is None:
                raise ModelDataError(f'{symbol} is not added for fiat currency.')

        if address is not None:
            fiat_meta = FIAT_CURRENCY_DATA_BY_ADDRESS.get(address, None)
            if fiat_meta is not None:
                if symbol is None or fiat_meta['symbol'] == symbol:
                    super().__init__(address=Address(fiat_meta["address"]))
                    self._meta.symbol = fiat_meta["symbol"]
                    self._meta.name = fiat_meta["name"]
                else:
                    raise ModelDataError(
                        f'Mismatch {symbol}/{address} for '
                        f'{fiat_meta["symbol"]}/{fiat_meta["address"]}')
            elif symbol is None:
                raise ModelDataError(f'{address} is not added for fiat currency.')
            else:
                raise ModelDataError(f'{symbol}/{address} is not added for fiat currency.')

    @property
    def symbol(self):
        return self._meta.symbol

    @property
    def name(self):
        return self._meta.name

    @property
    def fiat(self):
        return True


class Currency(Account):
    """
    Converter for any Fungible Token and FiatCurrency.
    It's used as inputs to price models.

    It can be constructed with a string (containing an address or symbol)
    or with kwargs ``address`` or ``symbol``::

        # The following constructions are equivalent:

        c = Currency('CMK')

        c = Currency('0x68cfb82eacb9f198d508b514d898a403c449533e')

        c = Currency(symbol='CMK')

        c = Currency(address='0x68cfb82eacb9f198d508b514d898a403c449533e')

    """

    symbol: Union[str, None] = None
    name: Union[str, None] = None
    fiat: Union[bool, None] = None

    class Config:
        schema_extra = {
            'examples': [
                {'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984'},
                {'symbol': 'CMK'},
            ]
        }

    @classmethod
    def validate(cls, d):
        if isinstance(d, str):
            return cls(d)
        if isinstance(d, dict):
            return cls(**d)
        raise TypeError(f'{cls.__name__} must be deserialized with an str or dict')

    def __new__(cls, *args, **data) -> Union[NativeToken, Token, FiatCurrency]:
        addr = data.get("address", None)
        symbol = data.get("symbol", None)
        fiat = data.get("fiat", None)

        if len(args) > 0:
            arg = args[0]
            if isinstance(arg, str):
                if evm_address_regex.match(arg) is not None:
                    return Token(address=arg)
                else:
                    return Token(symbol=arg)

        if addr is not None:
            if (FIAT_CURRENCY_DATA_BY_ADDRESS.get(addr, None) is not None and
                    (fiat or fiat is None)):
                return FiatCurrency(**data)
            if fiat is None or not fiat:
                return Token(**data)

        if symbol is not None:
            if (FIAT_CURRENCY_DATA_BY_SYMBOL.get(symbol, None) is not None and
                    (fiat or fiat is None)):
                return FiatCurrency(**data)
            if fiat is None or not fiat:
                return Token(**data)

        raise ModelDataError(
            "Could not identify specific currency. Currency "
            "must be of type Token, NativeToken or FiatCurrency")

    def __init__(self, *_args, **_data):
        super().__init__(**_data)
