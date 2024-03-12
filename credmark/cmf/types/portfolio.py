import math

import credmark.cmf.model
from credmark.dto import DTOField, IterableListGenericDTO, PrivateAttr

from .adt import Maybe, Some
from .fiat_currency import Currency, FiatCurrency
from .position import Position
from .price import PriceWithQuote
from .token_erc20 import Token


class Portfolio(IterableListGenericDTO[Position]):
    positions: list[Position] = DTOField(
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


class PortfolioBuilder:
    _positions: dict[str, Position] = {}
    _scale: bool = False
    _include_price = False
    _quote: Currency | None = None

    def append(self, pos: Position):
        return self.extend([pos])

    def extend(self, positions: list[Position]):
        for pos in positions:
            pos_key = str(pos.asset.address)
            if self._positions.get(pos_key, None) is None:
                self._positions[pos_key] = pos.copy()
            else:
                self._positions[pos_key].amount += pos.amount
        return self

    def scale(self, scale=True):
        self._scale = scale
        return self

    def include_price(self, include_price=True, quote: Currency | None = None):
        self._include_price = include_price
        if quote is not None:
            self._quote = quote
        return self

    @classmethod
    def _scale_by_token_decimals(cls, positions: list[Position]):
        if not positions:
            return positions

        context = credmark.cmf.model.ModelContext.current_context()

        token_addresses = map(lambda x: x.asset.address.checksum, positions)

        fn = Token('WETH').as_erc20(True).functions.decimals()
        fn_fallback = Token('WETH').as_erc20(True).functions.DECIMALS()
        decimals = context.web3_batch.call_same_function(
            fn,
            list(token_addresses),
            fallback_contract_function=fn_fallback,
            unwrap=True
        )

        scaled_positions: list[Position] = []
        for position, position_decimals in zip(positions, decimals):
            position_decimals = position_decimals if isinstance(position_decimals, int) else 0
            amount = position.amount / 10 ** position_decimals
            new_position = position.copy()
            new_position.amount = amount
            scaled_positions.append(new_position)

        return scaled_positions

    @classmethod
    def _price_by_quote(cls,
                        positions: list[Position],
                        quote: FiatCurrency | Currency | None = None):
        if not positions:
            return positions

        context = credmark.cmf.model.ModelContext.current_context()

        quote = FiatCurrency(symbol='USD') if quote is None else quote
        pqs_maybe = context.run_model(
            slug='price.quote-multiple-maybe',
            input=Some(some=[
                {'base': p.asset.address, 'quote': quote} for p in positions
            ]),
            return_type=Some[Maybe[PriceWithQuote]],
        )

        price_positions = []
        for price_maybe, position in zip(pqs_maybe.some, positions):
            price_quote = price_maybe.get_just(PriceWithQuote(price=0.0, src="none",
                                                              quoteAddress=quote.address))
            price_position = position.copy()
            price_position.price_quote = price_quote
            price_positions.append(price_position)

        return price_positions

    def build(self) -> Portfolio:
        positions = list(self._positions.values())
        if self._scale:
            positions = self._scale_by_token_decimals(positions)
        if self._include_price:
            positions = self._price_by_quote(positions)

        return Portfolio(positions=positions)
