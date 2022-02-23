from credmark.types.dto import DTO, DTOField


class Price(DTO):
    value_usd: float = DTOField(0.0, description='Value in US dollars')
    token: str = DTOField('', description='Token symbol')
