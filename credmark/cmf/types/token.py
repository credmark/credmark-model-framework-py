from typing import List, Union
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField
import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError, ModelRunError
from credmark.cmf.types.currency import Currency

from .abi import ABI
from .contract import Contract
from .address import NATIVE_TOKEN_ADDRESS, Address
from .data.fungible_token_data import FUNGIBLE_TOKEN_DATA, ERC20_GENERIC_ABI
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
            (t.get('address', None) == address or
             t.get('symbol', None) == symbol) or
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


class Token(Contract, Currency):
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
            self._meta.abi = ABI(ERC20_GENERIC_ABI)

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

    def scaled(self, value) -> float:
        return value / (10 ** self.decimals)


class TokenInfo(Token):
    meta: Token.TokenMetadata


class NativeToken(Token):

    def __init__(self, **data) -> None:
        context = credmark.cmf.model.ModelContext.current_context()
        data = {"address": NATIVE_TOKEN_ADDRESS}
        super().__init__(**data)
        if context.chain_id == 1:
            self._meta.abi = ABI([])
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
