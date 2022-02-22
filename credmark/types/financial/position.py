from credmark.types.dto import DTO, DTOField


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    token: str = DTOField(..., description='Token symbol')
