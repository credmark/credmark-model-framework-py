from typing import List
from ..dto import DTOField, IterableListDto
from .position import Position


class Portfolio(IterableListDto):
    positions: List[Position] = DTOField([], description='List of positions')
    iterator = 'positions'
