# All address in the field shall be checksum address

NATIVE_TOKEN = {
    "137": {
        "symbol": "MATIC",
        'address': '0x0000000000000000000000000000000000001010',
        "decimals": 18,
        "name": "polygon",
        "is_native_token": True,
    },
    "1": {
        "symbol": "ETH",
        "address": '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        "decimals": 18,
        "name": "Ethereum",
        "is_native_token": True,
        "wrapped": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    }
}

FUNGIBLE_TOKEN_DATA_BY_SYMBOL = {
    "137": {
        "MATIC": {
            "symbol": "MATIC",
            "decimals": 18,
            "name": "polygon",
            'address': '0x0000000000000000000000000000000000001010',
            "is_native_token": True,
        },
    },
    "1": {
        "ETH": {
            "symbol": "ETH",
            "decimals": 18,
            "name": "Ethereum",
            "address": '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
            "is_native_token": True
        },
        "BTC": {
            "symbol": "BTC",
            "decimals": 0,
            "name": "Bitcoin",
            "address": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB",
            "set_loaded_true": True,
        },
        "WETH": {
            "symbol": "WETH",
            "decimals": 18,
            "name": "Wrapped Ether",
            "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        },
        "CMK": {
            "symbol": "CMK",
            "decimals": 18,
            "name": "Credmark",
            "address": "0x68CFb82Eacb9f198d508B514d898a403c449533E",
            "protocol": "credmark"
        },
        "USDT": {
            "symbol": "USDT",
            "decimals": 6,
            "name": "Tether USD",
            "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7"
        },
        "BNB": {
            "symbol": "BNB",
            "decimals": 18,
            "name": "BNB",
            "address": "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"
        },
        "USDC": {
            "symbol": "USDC",
            "decimals": 6,
            "name": "USD Coin",
            "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
        },
        "EUROC": {
            "symbol": "EUROC",
            "decimals": 6,
            "name": "Euro Coin",
            "address": "0x1aBaEA1f7C830bD89Acc67eC4af516284b1bC33c"
        },
        "HEX": {
            "symbol": "HEX",
            "decimals": 8,
            "name": "HEX",
            "address": "0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39",
            "protocol": "hex"
        },
        "BUSD": {
            "symbol": "BUSD",
            "decimals": 18,
            "name": "Binance USD",
            "address": "0x4Fabb145d64652a948d72533023f6E7A623C7C53"
        },
        "UST": {
            "symbol": "UST",
            "decimals": 18,
            "name": "Wrapped UST Token",
            "address": "0xa47c8bf37f92aBed4A126BDA807A7b7498661acD",
            "protocol": "terra chain"
        },
        "SHIB": {
            "symbol": "SHIB",
            "decimals": 18,
            "name": "SHIBA INU",
            "address": "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"
        },
        "MATIC": {
            "symbol": "MATIC",
            "decimals": 18,
            "name": "Matic Token",
            "address": "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0",
            "protocol": "polygon"
        },
        "WBTC": {
            "symbol": "WBTC",
            "decimals": 8,
            "name": "Wrapped BTC",
            "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"
        },
        "CRO": {
            "symbol": "CRO",
            "decimals": 8,
            "name": "CRO",
            "address": "0xA0b73E1Ff0B80914AB6fe0444E65848C4C34450b",
            "protocol": "cronos chain"
        },
        "DAI": {
            "symbol": "DAI",
            "decimals": 18,
            "name": "Dai Stablecoin",
            "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
            "protocol": "maker"
        },
        "LINK": {
            "symbol": "LINK",
            "decimals": 18,
            "name": "ChainLink Token",
            "address": "0x514910771AF9Ca656af840dff83E8264EcF986CA",
            "protocol": "chainLink"
        },
        "TRX": {
            "symbol": "TRX",
            "decimals": 6,
            "name": "TRON",
            "address": "0xE1Be5D3f34e89dE342Ee97E6e90D405884dA6c67",
            "protocol": "tron chain"
        },
        "stETH": {
            "symbol": "stETH",
            "decimals": 18,
            "name": "Liquid staked Ether 2.0",
            "address": "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"
        },
        "wstETH": {
            "symbol": "wstETH",
            "decimals": 18,
            "name": "Wrapped liquid staked Ether 2.0",
            "address": "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0"
        },
        "THETA": {
            "symbol": "THETA",
            "decimals": 18,
            "name": "Theta Token",
            "address": "0x3883f5e181fccaF8410FA61e12b59BAd963fb645",
            "protocol": "theta chain"
        },
        "LEO": {
            "symbol": "LEO",
            "decimals": 18,
            "name": "Bitfinex LEO Token",
            "address": "0x2AF5D2aD76741191D15Dfe7bF6aC92d4Bd912Ca3"
        },
        "OKB": {
            "symbol": "OKB",
            "decimals": 18,
            "name": "OKB",
            "address": "0x75231F58b43240C9718Dd58B4967c5114342a86c"
        },
        "UNI": {
            "symbol": "UNI",
            "decimals": 18,
            "name": "Uniswap",
            "address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
            "protocol": "uniswap"
        },
        "wMANA": {
            "symbol": "wMANA",
            "decimals": 18,
            "name": "Wrapped Decentraland MANA",
            "address": "0xFd09Cf7cFffa9932e33668311C4777Cb9db3c9Be"
        },
        "FTM": {
            "symbol": "FTM",
            "decimals": 18,
            "name": "Fantom Token",
            "address": "0x4E15361FD6b4BB609Fa63C81A2be19d873717870",
            "protocol": "fantom"
        },
        "SAND": {
            "symbol": "SAND",
            "decimals": 18,
            "name": "SAND",
            "address": "0x3845badAde8e6dFF049820680d1F14bD3903a5d0"
        },
        "WFIL": {
            "symbol": "WFIL",
            "decimals": 18,
            "name": "Wrapped Filecoin",
            "address": "0x6e1A19F235bE7ED8E3369eF73b196C07257494DE",
            "protocol": "filecoin"
        },
        "VEN": {
            "symbol": "VEN",
            "decimals": 18,
            "name": "VeChain Token",
            "address": "0xD850942eF8811f2A866692A623011bDE52a462C1"
        },
        "FRAX": {
            "symbol": "FRAX",
            "decimals": 18,
            "name": "Frax",
            "address": "0x853d955aCEf822Db058eb8505911ED77F175b99e",
            "protocol": "frax"
        },
        "MIM": {
            "symbol": "MIM",
            "decimals": 18,
            "name": "Magic Internet Money",
            "address": "0x99D8a9C45b2ecA8864373A26D1459e3Dff1e17F3",
            "protocol": "abracadabra"
        },
        "GRT": {
            "symbol": "GRT",
            "decimals": 18,
            "name": "Graph Token",
            "address": "0xc944E90C64B2c07662A292be6244BDf05Cda44a7",
            "protocol": "the graph"
        },
        "BTT": {
            "symbol": "BTT",
            "decimals": 18,
            "name": "BitTorrent",
            "address": "0xC669928185DbCE49d2230CC9B0979BE6DC797957",
            "protocol": "bittorrent"
        },
        "GALA": {
            "symbol": "GALA",
            "decimals": 8,
            "name": "Gala",
            "address": "0x15D4c048F83bd7e37d49eA4C83a07267Ec4203dA"
        },
        "MKR": {
            "symbol": "MKR",
            "decimals": 18,
            "name": "Maker",
            "address": "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2",
            "protocol": "maker"
        },
        "ONE": {
            "symbol": "ONE",
            "decimals": 18,
            "name": "HarmonyOne",
            "address": "0x799a4202c12ca952cB311598a024C80eD371a41e",
            "protocol": "harmony chain"
        },
        "QNT": {
            "symbol": "QNT",
            "decimals": 18,
            "name": "Quant",
            "address": "0x4a220E6096B25EADb88358cb44068A3248254675"
        },
        "HBTC": {
            "symbol": "HBTC",
            "decimals": 18,
            "name": "Huobi BTC",
            "address": "0x0316EB71485b0Ab14103307bf65a021042c6d380"
        },
        "KCS": {
            "symbol": "KCS",
            "decimals": 6,
            "name": "KuCoin Token",
            "address": "0xf34960d9d60be18cC1D5Afc1A6F012A723a28811"
        },
        "TUSD": {
            "symbol": "TUSD",
            "decimals": 18,
            "name": "TrueUSD",
            "address": "0x0000000000085d4780B73119b644AE5ecd22b376"
        },
        "HT": {
            "symbol": "HT",
            "decimals": 18,
            "name": "HuobiToken",
            "address": "0x6f259637dcD74C767781E37Bc6133cd6A68aa161"
        },
        "ENJ": {
            "symbol": "ENJ",
            "decimals": 18,
            "name": "Enjin Coin",
            "address": "0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c"
        },
        "AMP": {
            "symbol": "AMP",
            "decimals": 18,
            "name": "Amp",
            "address": "0xfF20817765cB7f73d4bde2e66e067E58D11095C2"
        },
        "CEL": {
            "symbol": "CEL",
            "decimals": 4,
            "name": "Celsius",
            "address": "0xaaAEBE6Fe48E54f431b0C390CfaF0b017d09D42d"
        },
        "FXS": {
            "symbol": "FXS",
            "decimals": 18,
            "name": "Frax Share",
            "address": "0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0"
        },
        "CHZ": {
            "symbol": "CHZ",
            "decimals": 18,
            "name": "chiliZ",
            "address": "0x3506424F91fD33084466F402d5D97f05F8e3b4AF"
        },
        "wCELO": {
            "symbol": "wCELO",
            "decimals": 18,
            "name": "Wrapped Celo",
            "address": "0xE452E6Ea2dDeB012e20dB73bf5d3863A3Ac8d77a"
        },
        "NEXO": {
            "symbol": "NEXO",
            "decimals": 18,
            "name": "Nexo",
            "address": "0xB62132e35a6c13ee1EE0f84dC5d40bad8d815206"
        },
        "BAT": {
            "symbol": "BAT",
            "decimals": 18,
            "name": "Basic Attention Token",
            "address": "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
        },
        "USDP": {
            "symbol": "USDP",
            "decimals": 18,
            "name": "Pax Dollar",
            "address": "0x8E870D67F660D95d5be530380D0eC0bd388289E1"
        },
        "BIT": {
            "symbol": "BIT",
            "decimals": 18,
            "name": "BitDAO",
            "address": "0x1A4b46696b2bB4794Eb3D4c26f1c55F9170fa4C5"
        },
        "LRC": {
            "symbol": "LRC",
            "decimals": 18,
            "name": "LoopringCoin V2",
            "address": "0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD"
        },
        "aCRV": {
            "symbol": "aCRV",
            "decimals": 18,
            "name": "Aave interest bearing CRV",
            "address": "0x8dAE6Cb04688C62d939ed9B68d32Bc62e49970b1",
            "protocol": "aave"
        },
        "AAVE": {
            "symbol": "AAVE",
            "decimals": 18,
            "name": "Aave Token",
            "address": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
        },
        "SNX": {
            "symbol": "SNX",
            "decimals": 18,
            "name": "Synthetix Network Token",
            "address": "0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F"
        },
        "HOT": {
            "symbol": "HOT",
            "decimals": 18,
            "name": "HoloToken",
            "address": "0x6c6EE5e31d828De241282B9606C8e98Ea48526E2"
        }
    }
}

FUNGIBLE_TOKEN_DATA_BY_ADDRESS = {
    chain_id: {
        chain_meta['address']: chain_meta
        for chain_meta in chain_tokens.values()
    }
    for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items()
}
