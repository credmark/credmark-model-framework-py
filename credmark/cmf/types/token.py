import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError, ModelRunError
from .address import NATIVE_TOKEN_ADDRESS, Address
from .account import Account
from .contract import Contract
from .data.fungible_token_data import FUNGIBLE_TOKEN_DATA, ERC20_GENERIC_ABI
from .data.fiat_currency_data import FIAT_CURRENCY_DATA, FIAT_CURRENCY_DATA_BY_ADDRESS
from typing import List, Union
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField, DTO
from web3.exceptions import (
    BadFunctionCallOutput,
    ABIFunctionNotFound
)


def get_token_from_configuration(
        chain_id: str,
        symbol: Union[str, None] = None,
        address: Union[Address, None] = None,
        is_native_token: bool = False,
        wraps: Union[str, None] = None) -> Union[dict, None]:
    token_datas = [
        t for t in FUNGIBLE_TOKEN_DATA.get(chain_id, [])
        if (t.get('is_native_token', False) == is_native_token and
            ((t.get('address', None) == address and address is not None) or
             (t.get('symbol', None) == symbol and symbol is not None)) or
            (t.get('wraps', None) == wraps and wraps is not None))
    ]

    if len(token_datas) > 1:
        # TODO: Until we have definitive token lookup, we'll
        # consider it transient as a ModelRunError.
        raise ModelRunError(
            'Missing fungible token data in lookup for '
            f'chain_id={chain_id} symbol={symbol} '
            f'address={address} is_native_token={is_native_token}')

    if len(token_datas) == 1:
        return token_datas[0]

    return None


class Token(Contract):
    """
    Token represents a fungible Token that conforms to ERC20
    standards
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
        context = credmark.cmf.model.ModelContext.current_context()

        token_data = None
        if 'symbol' in data:
            token_data = get_token_from_configuration(
                chain_id=str(context.chain_id), symbol=data['symbol'], is_native_token=True)

        if 'address' in data:
            token_data = get_token_from_configuration(
                chain_id=str(context.chain_id), address=data['address'], is_native_token=True)

        if token_data is not None:
            return NativeToken()
        else:
            obj = super().__new__(cls)
            obj.__init__(**data)
            return obj

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

        if data['address'] == Address.null():
            raise ModelDataError(f'NULL address ({Address.null()}) is not a valid Token Address')

        super().__init__(**data)

    def _load(self):
        if self._loaded:
            return

        if self._meta.abi is None:
            self._meta.abi = ERC20_GENERIC_ABI

        super()._load()

    @ property
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

    @ property
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

    @ property
    def decimals(self) -> int:
        self._load()
        if self._meta.decimals is None:
            self._meta.decimals = self.try_erc20_property('decimals')
        return self._meta.decimals

    @ property
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

    @ property
    def total_supply(self) -> int:
        self._load()
        if self._meta.total_supply is None:
            self._meta.total_supply = self.try_erc20_property('totalSupply')
        return self._meta.total_supply

    def scaled(self, value) -> float:
        return value / (10 ** self.decimals)

    @property
    def fiat(self) -> bool:
        return False


class TokenInfo(Token):
    meta: Token.TokenMetadata


class NativeToken(Token):

    def __init__(self, **data) -> None:
        context = credmark.cmf.model.ModelContext.current_context()
        data = {"address": NATIVE_TOKEN_ADDRESS[context.chain_id]}
        super().__init__(**data)
        if context.chain_id == 1:
            self._meta.abi = []
            self._meta.symbol = "ETH"
            self._meta.decimals = 18
            self._meta.name = "Ethereum"
            self._meta.total_supply = 0
            self._loaded = True

    def get_balance(self, address: Address) -> int:
        context = credmark.cmf.model.ModelContext.current_context()
        return context.web3.eth.get_balance(address)


class NonFungibleToken(Contract):
    def __init__(self, **data):
        super().__init__(**data)
        raise NotImplementedError()


class Tokens(IterableListGenericDTO[Token]):
    tokens: List[Token] = DTOField(
        default=[], description="An iterable list of Token Objects")
    _iterator: str = PrivateAttr('tokens')


class FiatCurrency(Account):
    """
    This is DTO for Fiat Currency.
    """

    class FiatCurrencyMeta:
        symbol: Union[str, None] = None
        name: Union[str, None] = None

    _meta: FiatCurrencyMeta = PrivateAttr(
        default_factory=lambda: FiatCurrency.FiatCurrencyMeta())  # pylint: disable=unnecessary-lambda

    def __init__(self, **data):
        addr = data.get('address', None)
        symbol = data.get("symbol", None)

        if symbol is None and addr is None:
            raise ModelDataError('Missing both symbol and address')

        if symbol is not None:
            fiat_entry = FIAT_CURRENCY_DATA.get(symbol)

            if fiat_entry is None:
                raise ModelDataError('{symbol} is not added for fiat currency.')

            fiat_address = Address(fiat_entry['address'])
            if addr is not None and Address(addr) != fiat_address:
                raise ModelDataError(
                    f'Different address ({addr}) specified for {symbol}/{fiat_address}')

            super().__init__(address=fiat_address)
            self._meta.symbol = symbol
            self._meta.name = fiat_entry['name']

        elif addr is not None:
            fiat_entry = FIAT_CURRENCY_DATA_BY_ADDRESS.get(addr)

            if fiat_entry is None:
                raise ModelDataError('{symbol} is not added for fiat currency.')

            fiat_symbol = fiat_entry['symbol']
            if symbol is not None and symbol != fiat_symbol:
                raise ModelDataError(
                    f'Different symbol ({fiat_symbol}) specified for {symbol}/{addr}')

            super().__init__(address=Address(addr))
            self._meta.symbol = fiat_symbol
            self._meta.name = fiat_entry['name']

    @ property
    def symbol(self):
        return self._meta.symbol

    @ property
    def name(self):
        return self._meta.name

    @ property
    def fiat(self):
        return True


class Currency(DTO):

    """
    This is a converter for any Fungible Token and FiatCurrency.
    It's used as inputs to price models.
    """

    address: Union[Address, None] = None
    symbol: Union[str, None] = None
    name: Union[str, None] = None
    fiat: Union[bool, None] = None

    def __new__(cls, **data) -> Union[NativeToken, Token, FiatCurrency]:
        addr = data.get("address", None)
        symbol = data.get("symbol", None)
        fiat = data.get("fiat", None)

        if addr is not None:
            if FIAT_CURRENCY_DATA_BY_ADDRESS.get(addr, None) is not None and (fiat or fiat is None):
                return FiatCurrency(**data)
            if fiat is None or not fiat:
                return Token(**data)

        if symbol is not None:
            if FIAT_CURRENCY_DATA.get(symbol, None) is not None and (fiat or fiat is None):
                return FiatCurrency(**data)
            if fiat is None or not fiat:
                return Token(**data)

        raise ModelDataError(
            "Could not identify specific currency. Currency "
            "must be of type Token, NativeToken or FiatCurrency")
