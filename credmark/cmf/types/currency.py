
from credmark.dto import DTO  # type: ignore


class Currency(DTO):
    """
    This is the base type for any Fungible Currency.
    """


class FiatCurrency(Currency):
    """
    This is Fiat Currency. It's used as inputs to pricing and currency models.
    """

    symbol: str = 'USD'
    name: str = 'United States Dollar'
