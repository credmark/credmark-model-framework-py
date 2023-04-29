
from typing import Union

from credmark.cmf.model.errors import ModelDataError
from credmark.dto import PrivateAttr

from .account import Account
from .address import Address, evm_address_regex
from .data.fiat_currency_data import FIAT_CURRENCY_DATA_BY_ADDRESS, FIAT_CURRENCY_DATA_BY_SYMBOL
from .token_erc20 import NativeToken, Token


# pylint:disable=no-member, assigning-non-slot
class FiatCurrency(Account):
    """
    Fiat currency.
    """

    class FiatCurrencyMeta:
        symbol: Union[str, None] = None
        name: Union[str, None] = None

    _meta: FiatCurrencyMeta = PrivateAttr(
        default_factory=lambda: FiatCurrency.FiatCurrencyMeta())  # pylint: disable=unnecessary-lambda

    def __init__(self, **data):
        address = data.get('address', None)
        symbol = data.get("symbol", None)

        if symbol is None and address is None:
            raise ModelDataError('Missing both symbol and address')

        if symbol is not None:
            fiat_meta = FIAT_CURRENCY_DATA_BY_SYMBOL.get(symbol, None)
            if fiat_meta is not None:
                if address is None or fiat_meta['address'] == address:
                    super().__init__(address=Address(fiat_meta["address"]))
                    self._meta.symbol = fiat_meta["symbol"]
                    self._meta.name = fiat_meta["name"]
                else:
                    raise ModelDataError(
                        f'Mismatch {symbol}/{address} for '
                        f'{fiat_meta["symbol"]}/{fiat_meta["address"]}')
            elif address is None:
                raise ModelDataError(
                    f'{symbol} is not added for fiat currency.')

        if address is not None:
            fiat_meta = FIAT_CURRENCY_DATA_BY_ADDRESS.get(address, None)
            if fiat_meta is not None:
                if symbol is None or fiat_meta['symbol'] == symbol:
                    super().__init__(address=Address(fiat_meta["address"]))
                    self._meta.symbol = fiat_meta["symbol"]
                    self._meta.name = fiat_meta["name"]
                else:
                    raise ModelDataError(
                        f'Mismatch {symbol}/{address} for '
                        f'{fiat_meta["symbol"]}/{fiat_meta["address"]}')
            elif symbol is None:
                raise ModelDataError(
                    f'{address} is not added for fiat currency.')
            else:
                raise ModelDataError(
                    f'{symbol}/{address} is not added for fiat currency.')

    @property
    def symbol(self):
        return self._meta.symbol

    @property
    def name(self):
        return self._meta.name

    @property
    def fiat(self):
        return True


class Currency(Account):
    """
    Converter for any Fungible Token and FiatCurrency.
    It's used as inputs to price models.

    It can be constructed with a string (containing an address or symbol)
    or with kwargs ``address`` or ``symbol``::

        # The following constructions are equivalent:

        c = Currency('CMK')

        c = Currency('0x68cfb82eacb9f198d508b514d898a403c449533e')

        c = Currency(symbol='CMK')

        c = Currency(address='0x68cfb82eacb9f198d508b514d898a403c449533e')

    """

    symbol: Union[str, None] = None
    name: Union[str, None] = None
    fiat: Union[bool, None] = None

    class Config:
        schema_extra = {
            'examples': [
                {'address': '0x1F98431c8aD98523631AE4a59f267346ea31F984'},
                {'symbol': 'CMK'},
            ]
        }

    @classmethod
    def validate(cls, value):
        if isinstance(value, str):
            return cls(value)
        if isinstance(value, dict):
            return cls(**value)
        if isinstance(value, NativeToken):
            return value
        if isinstance(value, Token):
            return value
        if isinstance(value, FiatCurrency):
            return value
        raise TypeError(
            f'{cls.__name__} must be deserialized with an str or dict')

    def __new__(cls, *args, **data) -> Union[NativeToken, Token, FiatCurrency]:
        if len(args) > 0:
            arg = args[0]
            if isinstance(arg, str):
                if evm_address_regex.match(arg) is not None:
                    return cls.__new__(cls, address=arg)
                else:
                    return cls.__new__(cls, symbol=arg)

        addr = data.get("address", None)
        symbol = data.get("symbol", None)
        fiat = data.get("fiat", None)

        if addr is not None:
            if (FIAT_CURRENCY_DATA_BY_ADDRESS.get(addr, None) is not None and
                    (fiat or fiat is None)):
                return FiatCurrency(**data)
            if fiat is None or not fiat:
                return Token(**data)

        if symbol is not None:
            if (FIAT_CURRENCY_DATA_BY_SYMBOL.get(symbol, None) is not None and
                    (fiat or fiat is None)):
                return FiatCurrency(**data)
            if fiat is None or not fiat:
                return Token(**data)

        raise ModelDataError(
            "Could not identify specific currency. Currency "
            "must be of type Token, NativeToken or FiatCurrency")

    def __init__(self, *_args, **_data):
        super().__init__(**_data)
