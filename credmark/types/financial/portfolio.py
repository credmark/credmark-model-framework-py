from typing import List
from credmark.types.dto import DTO, DTOField
from credmark.types.financial.position import Position


class Portfolio(DTO):
    positions: List[Position] = DTOField([], description='List of positions')
