from typing import (
    Union,
    List,
)
from credmark.dto import (
    DTO,
    DTOField,
    IterableListGenericDTO,
    PrivateAttr,
)
from .token import Token
from .address import Address


class Price(DTO):
    price: float = DTOField(0.0, description='Value of one Token')
    src: Union[str, None] = DTOField(None, description='Source')

    class Config:
        schema_extra: dict = {
            'examples': [{'price': 4.2},
                         {'price': 4.2, 'src': 'uniswap-v3'}]
        }


class TokenPairPrice(Price):
    token: Token = DTOField(..., description='Token')
    reference_token: Token = DTOField(
        default_factory=lambda: Token(symbol="USDC"),
        description='The token as the reference price (Defaults to USDC)')

    class Config:
        schema_extra: dict = {
            'examples': [{'token': Token.Config.schema_extra['examples']}]
        }


class PriceList(IterableListGenericDTO[float]):
    prices: List[float] = DTOField(default=[], description='List of prices')
    tokenAddress: Address
    src: Union[str, None] = DTOField(None, description='Source')
    _iterator: str = PrivateAttr('prices')

    class Config:
        schema_extra: dict = {
            'examples': [{'prices': [4.2, 2.3],
                          'tokenAddress': '0x6B175474E89094C44Da98b954EedeAC495271d0F'}]
        }
