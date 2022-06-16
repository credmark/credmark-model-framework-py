from typing import List
import credmark.cmf.model
from credmark.dto import DTO, DTOField, cross_examples, PrivateAttr, IterableListGenericDTO
from .address import Address
from .token import Token
from .price import Price


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


class SpotPosition(Position):
    def get_value(self, price_model='price.quote'):
        """
        Returns:
            The value of the position using the price_model.

        Raises:
            ModelDataError: if no pools available for price data.
        """
        context = credmark.cmf.model.ModelContext.current_context()
        token_price = context.run_model(price_model, input=self.asset, return_type=Price).price
        return token_price * self.amount


class SpotPositions(IterableListGenericDTO[SpotPosition]):
    spot_positions: List[SpotPosition] = DTOField(
        default=[], description="A list of Spot Positions")
    _iterator: str = PrivateAttr('spot_positions')

    def get_value(self, price_model='price.quote'):
        total = 0
        for pos in self.spot_positions:
            total += pos.get_value()
        return total


class LPPosition(Position):
    pool_address: Address
    staked_positions: List[Position]


class SetPosition(Position):
    pool_address: Address
    set_positions: List[Position]


class YieldPosition(Position):
    ...
