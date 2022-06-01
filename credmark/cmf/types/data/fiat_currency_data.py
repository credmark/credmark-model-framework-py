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
        "name": "ndonesian Rupiah"},
    'INR': {
        "currency_code": to_currency_code(356),
        "name": "Indian Rupee"},
    'NGN': {
        "currency_code": to_currency_code(566)},
    'NZD': {
        "currency_code": to_currency_code(554)},
    'PHP': {
        "currency_code": to_currency_code(608)},
    'SGD': {
        "currency_code": to_currency_code(702)},
    'TRY': {
        "currency_code": to_currency_code(949)},
    'ZAR': {
        "currency_code": to_currency_code(710)},
    'XDR': {
        "currency_code": to_currency_code(960)}
})
