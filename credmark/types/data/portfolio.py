from typing import List
from ..dto import DTOField, PrivateAttr, IterableListGenericDTO
from .position import Position


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField([], description='List of positions')
    _iterator = PrivateAttr('positions')
