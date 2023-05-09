import credmark.cmf.model
from credmark.cmf.model.errors import ModelDataError
from credmark.dto import DTO, DTOField, cross_examples

from .price import PriceWithQuote
from .token_erc20 import NativeToken, Token


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    asset: Token

    def get_value(self, price_model='price.quote', block_number=None, quote=None) -> float:
        """
        Returns:
            The value of the position using the price_model.

        Raises:
            ModelDataError: if no pools available for price data.
        """
        context = credmark.cmf.model.ModelContext.current_context()
        if block_number is None:
            block_number = context.block_number
        if quote is not None:
            quote_dict = {'quote': quote}
        else:
            quote_dict = {}

        try:
            token_price = context.run_model(
                price_model,
                input={'base': self.asset} | quote_dict,
                block_number=block_number)['price']
        except ModelDataError:
            token_price = 0
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


class PositionWithPrice(Position):
    fiat_quote: PriceWithQuote

    class Config:
        schema_extra = {
            'examples': cross_examples(Position.Config.schema_extra['examples'],
                                       PriceWithQuote.Config.schema_extra['examples'],
                                       limit=10)
        }
