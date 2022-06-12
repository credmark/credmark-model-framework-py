def to_address(code: int) -> str:
    return '0x{:040x}'.format(code)


FIAT_CURRENCY_DATA_BY_SYMBOL = dict({
    'USD': {
        # 0x0000000000000000000000000000000000000348
        "symbol": "USD",
        "address": to_address(840),
        "name": "United States Dollar"},
    'GBP': {
        "symbol": "GBP",
        "address": to_address(826),
        "name": "British Pound"},
    'EUR': {
        "symbol": "EUR",
        "address": to_address(978),
        "name": "Euro"},
    'JPY': {
        "symbol": "JPY",
        "address": to_address(392),
        "name": "Japanese Yen"},
    'CNY': {
        "symbol": "CNY",
        "address": to_address(156),
        "name": "Chinese Yuan"},
    'AUD': {
        "symbol": "AUD",
        "address": to_address(36),
        "name": "Australian Dollar"},
    'KRW': {
        "symbol": "KRW",
        "address": to_address(410),
        "name": "South Korean won"},
    'BRL': {
        "symbol": "BRL",
        "address": to_address(986),
        "name": "Brazilian Real"},
    'CAD': {
        "symbol": "CAD",
        "address": to_address(124),
        "name": "Canadian Dollar"},
    'CHF': {
        "symbol": "CHF",
        "address": to_address(756),
        "name": "Swiss Franc"},
    'IDR': {
        "symbol": "IDR",
        "address": to_address(360),
        "name": "Indonesian Rupiah"},
    'INR': {
        "symbol": "INR",
        "address": to_address(356),
        "name": "Indian Rupee"},
    'NGN': {
        "symbol": "NGN",
        "address": to_address(566),
        "name": "Nigerian Naira"},
    'NZD': {
        "symbol": "NZD",
        "address": to_address(554),
        "name": "New Zealand Dollar"},
    'PHP': {
        "symbol": "PHP",
        "address": to_address(608),
        "name": "Philippine Peso"},
    'SGD': {
        "symbol": "SGD",
        "address": to_address(702),
        "name": "Singapore Dollar"},
    'TRY': {
        "symbol": "TRY",
        "address": to_address(949),
        "name": "Turkish Lira"},
    'ZAR': {
        "symbol": "ZAR",
        "address": to_address(710),
        "name": "South African Rand"},
    'XDR': {
        "symbol": "XDR",
        "address": to_address(960),
        "name": "Special Drawing Rights"},
    'ARS': {
        "symbol": "ARS",
        "address": to_address(32),
        "name": "Argentine Peso"},
    'RUB': {
        "symbol": "RUB",
        "address": to_address(643),
        "name": "Russian Ruble"},
    'XAG': {
        "symbol": "XAG",
        "address": to_address(961),
        "name": "Silver (one troy ounce)"},
    'XAU': {
        "symbol": "XAU",
        "address": to_address(959),
        "name": "Gold (one troy ounce)"},
})

FIAT_CURRENCY_DATA_BY_ADDRESS = dict({
    v['address']: v for k, v in FIAT_CURRENCY_DATA_BY_SYMBOL.items()
})
