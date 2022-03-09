from typing import List
from ..dto import DTOField, PrivateAttr, IterableListGenericDTO
from .position import Position


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(default=[], description='List of positions')
    _iterator = PrivateAttr('positions')
