from credmark.dto import DTO, DTOField, cross_examples
from .token import Token, NativeToken


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    asset: Token

    class Config:
        schema_extra = {
            'examples': cross_examples([{'amount': '4.2', }],
                                       [{'token': v}
                                           for v in Token.Config.schema_extra['examples']],
                                       limit=10)
        }


class TokenPosition(Position):
    asset: Token


class NativePosition(Position):
    asset: NativeToken
