
from credmark.dto import DTO, DTOField  # type: ignore


class Currency(DTO):
    """
    This is the base type for any Fungible Currency.
    """


class FiatCurrency(Currency):
    """
    This is Fiat Currency. It's used as inputs to pricing and currency models.
    """

    symbol: str
    name: str = DTOField('')
