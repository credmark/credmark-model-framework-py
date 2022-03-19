
import credmark.model
from credmark.model.errors import ModelNoContextError, ModelRunError
import credmark.types
from .token_wei import TokenWei
from .contract import Contract
from .address import Address
from .data_content.fungible_token_data import FUNGIBLE_TOKEN_DATA
from .data_content.erc_standard_data import ERC20_BASE_ABI
from typing import List, Union
from credmark.dto import PrivateAttr, IterableListGenericDTO, DTOField
from ..models.core import CoreModels


def get_fungible_token_from_configuration(
        chain_id: str,
        symbol: Union[str, None] = None,
        address: Union[Address, None] = None,
        is_native_token: bool = False):
    token_datas = [
        t for t in FUNGIBLE_TOKEN_DATA.get(chain_id, [])
        if (t.get('is_native_token', False) == is_native_token and
            (t.get('address', None) == address or
             t.get('symbol', None) == symbol))
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
    Token represents a fungible Token that is either an ERC20 or
    a Native Token (such as ETH or MATIC)

    It will load a standard simplified ERC20 ABI in the case of
    one not existing. It allows for None addresses, in the case
    of it being a native token.
    """
    address: Union[Address, None] = None
    symbol: Union[str, None] = None
    name: Union[str, None] = None
    is_native_token: bool = False
    decimals: int

    class Config:
        schema_extra = {
            'examples': [{'symbol': 'USDC'},
                         {'symbol': 'USDC', 'decimals': 6}
                         ] + Contract.Config.schema_extra['examples']
        }

    @classmethod
    def native_token(cls):
        return Token(is_native_token=True)

    def __init__(self, **data):

        if not ('symbol' in data and
                'decimals' in data and
                'address' in data and
                'name' in data):
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ModelNoContextError(
                    f'No current context to look up missing token data {data}')
            token_address = None
            if data.get('address', None) is not None:
                token_address = Address(str(data.get('address')))

            token_data = get_fungible_token_from_configuration(
                chain_id=str(context.chain_id),
                is_native_token=data.get('is_native_token', False),
                symbol=data.get('symbol', None),
                address=token_address)

            if token_data is not None:
                data['is_native_token'] = token_data.get('is_native_token', False)
                data['symbol'] = token_data.get('symbol', None)
                data['address'] = token_data.get('address', None)
                data['name'] = token_data.get('name', None)
                data['decimals'] = token_data.get('decimals', None)
                data['protocol'] = token_data.get('protocol', None)
                data['product'] = token_data.get('product', None)

            if data.get('address', None) is not None:
                erc20 = Contract(address=data.get('address'), abi=ERC20_BASE_ABI)
                if data.get('symbol', None) is None:
                    data['symbol'] = erc20.functions.symbol().call()
                if data.get('name', None) is None:
                    data['name'] = erc20.functions.name().call()
                if data.get('decimals', None) is None:
                    data['decimals'] = erc20.functions.decimals().call()
                # TODO: Handle the Error that this isn't an ERC20

        super().__init__(**data)

    @ property
    def price_usd(self):
        context = credmark.model.ModelContext.current_context
        if context is None:
            raise ModelNoContextError(f'No current context to get price of token {self.symbol}')
        if self.is_native_token:
            wrapped_native = [t for t in FUNGIBLE_TOKEN_DATA.get(
                str(context.chain_id), []) if t.get('wraps') == self.symbol][0]
            return context.run_model(CoreModels.token_price, Token(**wrapped_native),
                                     return_type=credmark.types.Price).price
        return context.run_model(CoreModels.token_price, self,
                                 return_type=credmark.types.Price).price

    @ property
    def instance(self):
        try:
            return super().instance
        except Exception:
            if self.abi is None:
                self.abi = ERC20_BASE_ABI
        return super().instance

    def total_supply(self) -> TokenWei:
        if self.is_native_token:
            return TokenWei(0, self.decimals)
        return TokenWei(self.functions.totalSupply().call(), self.decimals)

    def balance_of(self, address: Address) -> TokenWei:
        if self.is_native_token:
            context = credmark.model.ModelContext.current_context
            if context is None:
                raise ModelNoContextError(f'No current context to get price of token {self.symbol}')
            return TokenWei(context.web3.eth.get_balance(address), self.decimals)
        return TokenWei(self.functions.balanceOf(address).call(), self.decimals)

    def allowance(self, owner: Address, spender: Address) -> TokenWei:
        if self.is_native_token:
            return TokenWei(0, self.decimals)
        return TokenWei(self.functions.allowance(owner, spender).call(), self.decimals)


class Tokens(IterableListGenericDTO[Token]):
    tokens: List[Token] = DTOField(
        default=[], description="An iterable list of Token Objects")
    _iterator: str = PrivateAttr('tokens')
