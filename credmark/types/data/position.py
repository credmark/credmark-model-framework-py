from credmark.model.errors import ModelRunError
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

    @ property
    def scaled_amount(self):
        decimals = self.asset.decimals
        if decimals is None:
            # Not clear if this is a ModelRunError or ModelDataError
            # TODO: Until we have definitive token lookup, we'll consider
            # it transient as a ModelRunError.
            raise ModelRunError(
                f'No position scaled_amount for token {self.token.symbol} missing decimals value')
        return self.amount / (10 ** decimals)


class TokenPosition(Position):
    asset: Token


class NativePosition(Position):
    asset: NativeToken
