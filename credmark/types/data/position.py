from ..dto import DTO, DTOField, cross_examples
from ..data.token import Token


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    token: Token = DTOField(..., description='Token')

    class Config:
        schema_extra = {
            'examples': cross_examples([{'amount': '4.2', }],
                                       [{'token': v}
                                           for v in Token.Config.schema_extra['examples']],
                                       limit=10)
        }

    def value_usd(self):
        # TODO: Figure out for non-ERC20 Tokens
        return self.token.price_usd * self.scaled_amount

    @ property
    def scaled_amount(self):
        decimals = self.token.decimals
        if decimals is None:
            raise ValueError(
                f'No position scaled_amount for token {self.token.symbol} missing decimals value')
        return self.amount / (10 ** decimals)
