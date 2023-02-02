from typing import List, Union

from credmark.dto import DTO, DTOField, IterableListGenericDTO, PrivateAttr, cross_examples

from .address import Address
from .fiat_currency import Currency

__all__ = ['Price', 'PriceList', 'PriceWithQuote']


class Price(DTO):
    price: float = DTOField(0.0, description='Value of one Token')
    src: Union[str, None] = DTOField(None, description='Source')

    class Config:
        schema_extra: dict = {
            'examples': [{'price': 4.2},
                         {'price': 4.2, 'src': 'uniswap-v3'}]
        }


class PriceWithQuote(Price):
    quoteAddress: Address = DTOField(description='The address of quoted currency')

    def cross(self, other: 'PriceWithQuote'):
        return PriceWithQuote(price=self.price * other.price,
                              src=f'({self.src},{other.src})',
                              quoteAddress=other.quoteAddress)

    def inverse(self, quoteAddress):  # pylint: disable=invalid-name
        return PriceWithQuote(price=1 / self.price,
                              src=f'{self.src}|Inv',
                              quoteAddress=quoteAddress)

    @classmethod
    def usd(cls, **data):
        if 'quoteAddress' in data:
            raise ValueError(
                f'quoteAddress is default to USD but specified {data["quoteAddress"]=}')
        return cls(**data, quoteAddress=Currency('USD').address)

    @classmethod
    def eth(cls, **data):
        if 'quoteAddress' in data:
            raise ValueError(
                f'quoteAddress is default to ETH but specified {data["quoteAddress"]=}')
        return cls(**data, quoteAddress=Currency('ETH').address)

    def to_price(self):
        return Price(price=self.price, src=self.src)

    class Config:
        schema_extra: dict = {
            'examples': cross_examples(Price.Config.schema_extra['examples'],
                                       [{'quoteAddress': Currency('USD').address}],
                                       limit=10)
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
