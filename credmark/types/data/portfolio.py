from typing import List
from credmark.dto import (
    DTO,
    DTOField,
    PrivateAttr,
    IterableListGenericDTO,
)

from .address import Address

from .position import Position


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(default=[], description='List of positions')
    _iterator: str = PrivateAttr('positions')

    class Config:
        schema_extra: dict = {
            'examples': [{'positions': [exp]} for exp in Position.Config.schema_extra['examples']]
        }


class PriceList(DTO):
    prices: List[float]
    tokenAddress: Address

    class Config:
        schema_extra: dict = {
            'examples': [{'prices': [4.2, 2.3],
                          'tokenAddress': '0x6B175474E89094C44Da98b954EedeAC495271d0F'}]
        }
