from typing import List
from ..dto import DTO, DTOField
from .position import Position


class Portfolio(DTO):
    positions: List[Position] = DTOField([], description='List of positions')
