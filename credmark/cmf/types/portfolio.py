from typing import List

from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr

from .position import Position


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(default=[], description='List of positions')
    _iterator: str = PrivateAttr('positions')

    def get_value(self, price_model='price.quote', block_number=None, quote=None):
        """
        Returns:
            The value of the portfolio using the price_model.

        Raises:
            ModelDataError: if no pools available for a position's price data.
        """
        if len(self.positions) > 0:
            return sum(pos.get_value(price_model, block_number=block_number, quote=quote)
                       for pos in self.positions)  # pylint:disable=not-an-iterable
        return 0

    class Config:
        schema_extra: dict = {
            'examples': [{'positions': [exp]} for exp in Position.Config.schema_extra['examples']]
        }
