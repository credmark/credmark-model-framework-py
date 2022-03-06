from ..dto import DTO, DTOField
from ..data.token import Token


class Price(DTO):
    value_usd: float = DTOField(0.0, description='Value in US dollars')
    token: Token = DTOField('', description='Token symbol')
