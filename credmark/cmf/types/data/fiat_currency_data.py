def to_currency_code(code):
    return '0x{:040x}'.format(code)


FIAT_CURRENCY_DATA = dict({
    'USD': {
        "currency_code": to_currency_code(840),
        "name": "United States Dollar"},
    'GBP': {
        "currency_code": to_currency_code(826),
        "name": "British Pound"},
    'EUR': {
        "currency_code": to_currency_code(978),
        "name": "Euro"},
    'JPY': {
        "currency_code": to_currency_code(392),
        "name": "Japanese Yen"},
    'CNY': {
        "currency_code": to_currency_code(156),
        "name": "Chinese Yuan"},
    'AUD': {
        "currency_code": to_currency_code(36),
        "name": "Australian Dollar"},
    'KRW': {
        "currency_code": to_currency_code(410),
        "name": "South Korean won"},
    'BRL': {
        "currency_code": to_currency_code(986),
        "name": "Brazilian Real"},
    'CAD': {
        "currency_code": to_currency_code(124),
        "name": "Canadian Dollar"},
    'CHF': {
        "currency_code": to_currency_code(756),
        "name": "Swiss Franc"},
    'IDR': {
        "currency_code": to_currency_code(360),
        "name": "Indonesian Rupiah"},
    'INR': {
        "currency_code": to_currency_code(356),
        "name": "Indian Rupee"},
    'NGN': {
        "currency_code": to_currency_code(566),
        "name": "Nigerian Naira"},
    'NZD': {
        "currency_code": to_currency_code(554),
        "name": "New Zealand Dollar"},
    'PHP': {
        "currency_code": to_currency_code(608),
        "name": "Philippine Peso"},
    'SGD': {
        "currency_code": to_currency_code(702),
        "name": "Singapore Dollar"},
    'TRY': {
        "currency_code": to_currency_code(949),
        "name": "Turkish Lira"},
    'ZAR': {
        "currency_code": to_currency_code(710),
        "name": "South African Rand"},
    'XDR': {
        "currency_code": to_currency_code(960),
        "name": "Special Drawing Rights"},
    'ARS': {
        "currency_code": to_currency_code(32),
        "name": "Argentine Peso"},
    'RUB': {
        "currency_code": to_currency_code(643),
        "name": "Russian Ruble"},
    'XAG': {
        "currency_code": to_currency_code(961),
        "name": "Silver (one troy ounce)"},
    'XAU': {
        "currency_code": to_currency_code(959),
        "name": "Gold (one troy ounce)"},
})
