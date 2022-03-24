
import credmark.model
from credmark.model.errors import ModelNoContextError, ModelRunError
import credmark.types
from .token_wei import TokenWei
from .contract import Contract
from .address import Address
from .data_content.fungible_token_data import FUNGIBLE_TOKEN_DATA
from typing import List, Union
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField, DTO


def get_token_from_configuration(
        chain_id: str,
        symbol: Union[str, None] = None,
        address: Union[Address, None] = None,
        is_native_token: bool = False,
        wraps: Union[str, None] = None) -> dict:
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
        raise ModelRunError('Missing fungible token data in lookup for '
                            f'chain_id={chain_id} symbol={symbol} address={address} is_native_token={is_native_token}')

    if len(token_datas) == 1:
        return token_datas[0]


class Token(Contract):
    """
    Token represents a fungible Token that conforms to ERC20 
    standards
    """

    class TokenMetadata(Contract.ContractMetaData):
        symbol: Union[str, None] = None
        name: Union[str, None] = None
        decimals: Union[int, None] = None
        total_supply: Union[TokenWei, None] = None

    _meta: TokenMetadata = PrivateAttr(default=TokenMetadata())

    class Config:
        schema_extra = {
            'examples': [{'symbol': 'CMK'},
                         {'symbol': 'CMK', 'decimals': 18}
                         ] + Contract.Config.schema_extra['examples']
        }

    def __init__(self, **data):

        if 'address' not in data and 'symbol' in data:
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ModelNoContextError(
                    'No current context. Unable to create contract instance.')

            token_data = get_token_from_configuration(
                chain_id=str(context.chain_id), symbol=data['symbol'])
            if token_data is not None:
                data['address'] = token_data['address']
                if 'meta' not in data:
                    data['meta'] = {}
                data['meta']['symbol'] = token_data['symbol']
                data['meta']['name'] = token_data['name']
                data['meta']['decimals'] = token_data['decimals']

        if data.get('meta', None) is not None:
            if isinstance(data.get('meta'), dict):
                self._meta = self.TokenMetadata(**data.get('meta'))
            if isinstance(data.get('meta'), self.TokenMetadata):
                self._meta = data.get("meta")
        super().__init__(**data)

    def __load__(self):
        super().__load__()
        self._meta.symbol = self.functions.symbol().call()
        self._meta.name = self.functions.name().call()
        self._meta.decimals = self.functions.decimals().call()
        self._meta.total_supply = TokenWei(
            self.functions.totalSupply().call(), self._meta.decimals)

    @property
    def info(self):
        if not self._loaded:
            self.__load__()
        info = self.dict()
        info['meta'] = self._meta.dict()
        return TokenInfo(**info)

    @property
    def symbol(self):
        if not self._loaded:
            self.__load__()
        return self._meta.symbol

    @property
    def decimals(self):
        if not self._loaded:
            self.__load__()
        return self._meta.decimals

    @property
    def name(self):
        if not self._loaded:
            self.__load__()
        return self._meta.name

    @property
    def total_supply(self):
        if not self._loaded:
            self.__load__()
        return self._meta.total_supply

    def scaled(self, value):
        return value / (10 ** self.decimals)


class TokenInfo(Token):
    meta: Token.TokenMetadata


class NativeToken(DTO):
    symbol: str = 'ETH'
    name: str = 'ethereum'
    decimals: int = 18

    def __init__(self, **data) -> None:
        context = credmark.model.ModelContext.current_context
        if context is None:
            raise ModelNoContextError(
                'No current context. Unable to create contract instance.')

        token_data = get_token_from_configuration(
            chain_id=str(context.chain_id), is_native_token=True)

        data['symbol'] = token_data.get('symbol')
        data['decimals'] = token_data.get('decimals')
        data['name'] = token_data.get('name')
        super().__init__(**data)

    def scaled(self, value):
        return value / (10 ** self.decimals)

    def wrapped(self):
        context = credmark.model.ModelContext.current_context
        if context is None:
            raise ModelNoContextError(
                'No current context. Unable to create contract instance.')
        token_data = get_token_from_configuration(
            chain_id=str(context.chain_id), wraps=self.symbol)
        return Token(address=token_data['address'])


class NonFungibleToken(Contract):
    def __init__(self, **data):
        raise NotImplementedError()
        super().__init__(**data)


class Tokens(IterableListGenericDTO[Token]):
    tokens: List[Token] = DTOField(
        default=[], description="An iterable list of Token Objects")
    _iterator: str = PrivateAttr('tokens')
