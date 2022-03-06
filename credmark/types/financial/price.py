from ..dto import DTO, DTOField
from ..data.token import Token


class Price(DTO):
    price_usd: float = DTOField(0.0, description='Value of one Token in US dollars')
    token: Token = DTOField('', description='Token')
