from ..dto import DTO, DTOField
from ..data.token import Token


class Price(DTO):
    price: float = DTOField(0.0, description='Value of one Token')


class TokenPairPrice(Price):
    token: Token = DTOField(..., description='Token')
    reference_token: Token = DTOField(
        default_factory=lambda: Token(symbol="USDC"),
        description='The token as the reference price (Defaults to USDC)')
