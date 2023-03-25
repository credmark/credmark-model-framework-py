# pylint:disable=too-many-lines
# All address in the field shall be checksum address

from credmark.cmf.types.network import Network
from credmark.cmf.types.data.fungible_token_data_avalenche import AVALANCHE_TOKENS
from credmark.cmf.types.data.fungible_token_data_mainnet import MAINNET_TOKENS
from credmark.cmf.types.data.fungible_token_data_arbitrum_one import ARBITRUM_ONE_TOKENS
from credmark.cmf.types.data.fungible_token_data_optimism import OPTIMISM_TOKENS
from credmark.cmf.types.data.fungible_token_data_fantom import FANTOM_TOKENS


NATIVE_TOKEN = {
    int(Network.Mainnet): {
        "symbol": "ETH",
        "address": '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        "decimals": 18,
        "name": "Ethereum",
        "is_native_token": True,
        "wrapped": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    },
    int(Network.BSC): {
        "symbol": "BNB",
        "address": '0x0000000000000000010000100100111001000010',
        "decimals": 18,
        "name": "BSC",
        "is_native_token": True,
        "wrapped": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
    },
    int(Network.Polygon): {
        "symbol": "MATIC",
        'address': '0x0000000000000000000000000000000000001010',
        "decimals": 18,
        "name": "Matic Token",
        "is_native_token": True,
        "wrapped": "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270",
    },
    int(Network.ArbitrumOne): {
        "symbol": "ETH",
        "address": '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        "decimals": 18,
        "name": "Ethereum",
        "is_native_token": True,
        "wrapped": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    },
    int(Network.Optimism): {
        "symbol": "ETH",
        "address": '0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000',
        "decimals": 18,
        "name": "Ethereum",
        "is_native_token": True,
        "wrapped": "0x4200000000000000000000000000000000000006",
    },
    int(Network.Avalanche): {
        "symbol": "AVAX",
        "address": '0xaAaAaAaaAaAaAaaAaAAAAAAAAaaaAaAaAaaAaaAa',
        "decimals": 18,
        "name": "Avalanche",
        "is_native_token": True,
        "wrapped": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
    },
    int(Network.Fantom): {
        "symbol": "FTM",
        "address": '0xFFfFfFffFFfffFFfFFfFFFFFffFFFffffFfFFFfF',
        "decimals": 18,
        "name": "Fantom",
        "is_native_token": True,
        "wrapped": "0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83",
    }
}

FUNGIBLE_TOKEN_DATA_BY_SYMBOL = {
    int(Network.Polygon): {
        "MATIC": {
            "symbol": "MATIC",
            "decimals": 18,
            "name": "polygon",
            'address': '0x0000000000000000000000000000000000001010',
            "is_native_token": True,
        },
    },
    int(Network.Mainnet): MAINNET_TOKENS,
    int(Network.ArbitrumOne): ARBITRUM_ONE_TOKENS,
    int(Network.Optimism): OPTIMISM_TOKENS,
    int(Network.Avalanche): AVALANCHE_TOKENS,
    int(Network.Fantom): FANTOM_TOKENS,
}

FUNGIBLE_TOKEN_DATA_BY_ADDRESS = {
    chain_id: {
        chain_meta['address']: chain_meta
        for chain_meta in chain_tokens.values()
    }
    for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items()
}
