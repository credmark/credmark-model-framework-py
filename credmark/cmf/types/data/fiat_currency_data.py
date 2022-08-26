def to_address(code: int) -> str:
    return '0x{:040x}'.format(code)


FIAT_CURRENCY_DATA_BY_SYMBOL = dict({
    'USD': {
        # 0x0000000000000000000000000000000000000348
        "symbol": "USD",
        "code": 840,
        "address": to_address(840),
        "name": "United States Dollar"},
    'GBP': {
        "symbol": "GBP",
        "code": 826,
        "address": to_address(826),
        "name": "British Pound"},
    'EUR': {
        "symbol": "EUR",
        "code": 978,
        "address": to_address(978),
        "name": "Euro"},
    'JPY': {
        "symbol": "JPY",
        "code": 392,
        "address": to_address(392),
        "name": "Japanese Yen"},
    'CNY': {
        "symbol": "CNY",
        "code": 156,
        "address": to_address(156),
        "name": "Chinese Yuan"},
    'AUD': {
        "symbol": "AUD",
        "code": 36,
        "address": to_address(36),
        "name": "Australian Dollar"},
    'KRW': {
        "symbol": "KRW",
        "code": 410,
        "address": to_address(410),
        "name": "South Korean won"},
    'BRL': {
        "symbol": "BRL",
        "code": 986,
        "address": to_address(986),
        "name": "Brazilian Real"},
    'CAD': {
        "symbol": "CAD",
        "code": 124,
        "address": to_address(124),
        "name": "Canadian Dollar"},
    'CHF': {
        "symbol": "CHF",
        "code": 756,
        "address": to_address(756),
        "name": "Swiss Franc"},
    'IDR': {
        "symbol": "IDR",
        "code": 360,
        "address": to_address(360),
        "name": "Indonesian Rupiah"},
    'INR': {
        "symbol": "INR",
        "code": 356,
        "address": to_address(356),
        "name": "Indian Rupee"},
    'NGN': {
        "symbol": "NGN",
        "code": 566,
        "address": to_address(566),
        "name": "Nigerian Naira"},
    'NZD': {
        "symbol": "NZD",
        "code": 554,
        "address": to_address(554),
        "name": "New Zealand Dollar"},
    'PHP': {
        "symbol": "PHP",
        "code": 608,
        "address": to_address(608),
        "name": "Philippine Peso"},
    'SGD': {
        "symbol": "SGD",
        "code": 702,
        "address": to_address(702),
        "name": "Singapore Dollar"},
    'TRY': {
        "symbol": "TRY",
        "code": 949,
        "address": to_address(949),
        "name": "Turkish Lira"},
    'ZAR': {
        "symbol": "ZAR",
        "code": 710,
        "address": to_address(710),
        "name": "South African Rand"},
    'XDR': {
        "symbol": "XDR",
        "code": 960,
        "address": to_address(960),
        "name": "Special Drawing Rights"},
    'ARS': {
        "symbol": "ARS",
        "code": 32,
        "address": to_address(32),
        "name": "Argentine Peso"},
    'RUB': {
        "symbol": "RUB",
        "code": 643,
        "address": to_address(643),
        "name": "Russian Ruble"},
    'XAG': {
        "symbol": "XAG",
        "code": 961,
        "address": to_address(961),
        "name": "Silver (one troy ounce)"},
    'XAU': {
        "symbol": "XAU",
        "code": 959,
        "address": to_address(959),
        "name": "Gold (one troy ounce)"},
})

FIAT_CURRENCY_DATA_BY_ADDRESS = dict({
    v['address']: v for k, v in FIAT_CURRENCY_DATA_BY_SYMBOL.items()
})
