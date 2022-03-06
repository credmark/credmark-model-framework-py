from ..dto import DTO, DTOField
from ..data.token import Token


class Position(DTO):
    amount: float = DTOField(0.0, description='Quantity of token held')
    token: Token = DTOField(..., description='Token')

    def value_usd(self):
        # TODO: Figure out for non-ERC20 Tokens
        return float(self.token.price_usd) * self.scaled_amount

    @property
    def scaled_amount(self):
        return self.amount / (10 ** self.token.decimals)
