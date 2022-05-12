import credmark.cmf.model
from credmark.dto import DTO, DTOField, cross_examples
from .token import Token, NativeToken
from .price import Price


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    asset: Token

    def get_value(self):
        context = credmark.cmf.model.ModelContext.current_context()
        try:
            token_price = Price(**context.models.token.price(self.asset)).price
        except Exception:
            token_price = 0.0

        if token_price is None:
            token_price = 0.0

        return token_price * self.amount

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
