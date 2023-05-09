from typing import List

from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr

from .position import Position, PositionWithPrice


class Portfolio(IterableListGenericDTO[Position]):
    positions: List[Position] = DTOField(
        default=[], description='List of positions')
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


class PortfolioWithPrice(IterableListGenericDTO[PositionWithPrice]):
    positions: List[PositionWithPrice] = DTOField(
        default=[], description='List of positions')
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
            'examples': [{'positions': [exp]}
                         for exp in PositionWithPrice.Config.schema_extra['examples']]
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
