import credmark.cmf.model
from credmark.dto import DTO, DTOField, cross_examples

from .price import Price
from .token import NativeToken, Token


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    asset: Token

    def get_value(self, price_model='price.quote') -> float:
        """
        Returns:
            The value of the position using the price_model.

        Raises:
            ModelDataError: if no pools available for price data.
        """
        context = credmark.cmf.model.ModelContext.current_context()
        token_price = context.run_model(
            price_model, input={'base': self.asset}, return_type=Price).price
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
