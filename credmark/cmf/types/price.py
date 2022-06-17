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

    def cross_price(self, other):
        return Price(price=self.price * other.price, src=f'{self.src},{other.src}')

    def inverse(self):
        return Price(price=1 / self.price, src=f'{self.src}|Inverse')


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
