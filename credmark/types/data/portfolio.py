from typing import List
from ..dto import DTOField, PrivateAttr, IterableListDto
from .position import Position


class Portfolio(IterableListDto):
    positions: List[Position] = DTOField([], description='List of positions')
    _iterator = PrivateAttr('positions')
