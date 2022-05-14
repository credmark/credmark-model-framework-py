from typing import List
from credmark.dto import (
    DTOField,
    PrivateAttr,
    IterableListGenericDTO,
)

from .position import Position


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(default=[], description='List of positions')
    _iterator: str = PrivateAttr('positions')

    def get_value(self, price_model='token.price'):
        return sum([pos.get_value(price_model) for pos in self.positions])

    class Config:
        schema_extra: dict = {
            'examples': [{'positions': [exp]} for exp in Position.Config.schema_extra['examples']]
        }
