from credmark.dto import DTO, DTOField, cross_examples
from .token import Token, NativeToken
from credmark.cmf.model import ModelContext


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    asset: Token

    def get_value(self):
        context = ModelContext.current_context()
        price = context.run_model('token.price', input=self.asset,
                                  block_number=context.block_number)['price']
        return price * self.amount

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
