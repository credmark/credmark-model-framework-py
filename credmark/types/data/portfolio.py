from typing import List
from ..dto import (
    DTO,
    DTOField,
    PrivateAttr,
    IterableListGenericDTO,
    cross_examples
)
from .account import Account
from .address import Address
from .price import Price

from .position import Position


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(default=[], description='List of positions')
    _iterator: str = PrivateAttr('positions')

    class Config:
        schema_extra: dict = {
            'examples': [{'positions': [exp]} for exp in Position.Config.schema_extra['examples']]
        }


class PriceList(DTO):
    price: Price
    token: Address

    class Config:
        schema_extra: dict = {
            'examples': cross_examples(Price.Config.schema_extra['examples'],
                                       Account.Config.schema_extra['examples'])
        }
