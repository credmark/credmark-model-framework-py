from ..dto import DTO, DTOField
from ..data.token import Token


class Price(DTO):
    price: float = DTOField(0.0, description='Value of one Token')

    class Config:
        schema_extra: dict = {
            'examples': [{'price': 4.2}]
        }


class TokenPairPrice(Price):
    token: Token = DTOField(..., description='Token')
    reference_token: Token = DTOField(
        default_factory=lambda: Token(symbol="USDC"),
        description='The token as the reference price (Defaults to USDC)')

    class Config:
        schema_extra: dict = {
            'examples': [{'token': Token.Config.schema_extra['examples']}]
        }
