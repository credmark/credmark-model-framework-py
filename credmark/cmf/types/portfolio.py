import math
from typing import List

import credmark.cmf.model
from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr

from .adt import Maybe, Some
from .position import Position
from .price import PriceWithQuote


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(
        default=[], description='List of positions')
    _iterator: str = PrivateAttr('positions')

    def get_value(self, block_number=None, quote=None):
        """
        Returns:
            The value of the portfolio using the price_model.

        Raises:
            ModelDataError: if no pools available for a position's price data.
        """
        non_zero_positions = [position for position in self.positions
                              if not math.isclose(position.amount, 0)]

        if len(non_zero_positions) == 0:
            return 0

        total = 0
        context = credmark.cmf.model.ModelContext.current_context()
        if block_number is None:
            block_number = context.block_number

        pqs_maybe = context.run_model(
            slug='price.quote-multiple-maybe',
            input=Some(some=[
                {'base': p.asset.address} if quote is None
                else {'base': p.asset.address, 'quote': quote}
                for p in non_zero_positions
            ]),
            block_number=block_number,
            return_type=Some[Maybe[PriceWithQuote]],
        )
        for price_maybe, position in zip(pqs_maybe.some, non_zero_positions):
            if price_maybe.just is not None:
                total += position.amount * price_maybe.just.price

        return total

    class Config:
        schema_extra: dict = {
            'examples': [{'positions': [exp]} for exp in Position.Config.schema_extra['examples']]
        }

    @classmethod
    def merge(cls, port1: "Portfolio", port2: "Portfolio"):
        positions = {}
        for pos in port1:
            pos_key = str(pos.asset.address)
            if positions.get(pos_key, None) is None:
                positions[pos_key] = pos.copy()
            else:
                positions[pos_key].amount += pos.amount

        for pos in port2:
            pos_key = str(pos.asset.address)
            if positions.get(pos_key, None) is None:
                positions[pos_key] = pos.copy()
            else:
                positions[pos_key].amount += pos.amount

        return cls(positions=list(positions.values()))
