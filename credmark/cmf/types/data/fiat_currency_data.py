def to_address(code: int) -> str:
    return '0x{:040x}'.format(code)


FIAT_CURRENCY_DATA = dict({
    'USD': {
        # 0x0000000000000000000000000000000000000348
        "address": to_address(840),
        "name": "United States Dollar"},
    'GBP': {
        "address": to_address(826),
        "name": "British Pound"},
    'EUR': {
        "address": to_address(978),
        "name": "Euro"},
    'JPY': {
        "address": to_address(392),
        "name": "Japanese Yen"},
    'CNY': {
        "address": to_address(156),
        "name": "Chinese Yuan"},
    'AUD': {
        "address": to_address(36),
        "name": "Australian Dollar"},
    'KRW': {
        "address": to_address(410),
        "name": "South Korean won"},
    'BRL': {
        "address": to_address(986),
        "name": "Brazilian Real"},
    'CAD': {
        "address": to_address(124),
        "name": "Canadian Dollar"},
    'CHF': {
        "address": to_address(756),
        "name": "Swiss Franc"},
    'IDR': {
        "address": to_address(360),
        "name": "Indonesian Rupiah"},
    'INR': {
        "address": to_address(356),
        "name": "Indian Rupee"},
    'NGN': {
        "address": to_address(566),
        "name": "Nigerian Naira"},
    'NZD': {
        "address": to_address(554),
        "name": "New Zealand Dollar"},
    'PHP': {
        "address": to_address(608),
        "name": "Philippine Peso"},
    'SGD': {
        "address": to_address(702),
        "name": "Singapore Dollar"},
    'TRY': {
        "address": to_address(949),
        "name": "Turkish Lira"},
    'ZAR': {
        "address": to_address(710),
        "name": "South African Rand"},
    'XDR': {
        "address": to_address(960),
        "name": "Special Drawing Rights"},
    'ARS': {
        "address": to_address(32),
        "name": "Argentine Peso"},
    'RUB': {
        "address": to_address(643),
        "name": "Russian Ruble"},
    'XAG': {
        "address": to_address(961),
        "name": "Silver (one troy ounce)"},
    'XAU': {
        "address": to_address(959),
        "name": "Gold (one troy ounce)"},
})

FIAT_CURRENCY_DATA_BY_ADDRESS = dict({
    v['address']: {'symbol': k} | v for k, v in FIAT_CURRENCY_DATA.items()
})
