# pylint:disable=too-many-lines
# All address in the field shall be checksum address

from credmark.cmf.types.network import Network

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
        "WETH": {
            "symbol": "WETH",
            "decimals": 18,
            "name": "Wrapped Ether",
            'address': '0x7ceb23fd6bc0add59e62ac25578270cff1b9f619',
        },
        "USDC": {
            "symbol": "USDC",
            "decimals": 6,
            "name": "USDC Coin (PoS)",
            'address': '0x2791bca1f2de4661ed88a30c99a7a9449aa84174',
        },
        "DPI": {
            "symbol": "DPI",
            "decimals": 18,
            "name": "DefiPulse Index (PoS)",
            'address': '0x85955046DF4668e1DD369D2DE9f3AEB98DD2A369',
        },
        'GHST': {
            "symbol": "GHST",
            "decimals": 18,
            "name": "Aavegotchi GHST Token (PoS)",
            'address': '0x385Eeac5cB85A38A9a07A70c73e0a3271CfB54A7',
        },
        'LINK': {
            "symbol": "LINK",
            "decimals": 18,
            "name": "ChainLink Token",
            'address': '0x53E0bca35eC356BD5ddDFebbD1Fc0fD03FaBad39',
        },
        'WMATIC': {
            "symbol": "WMATIC",
            "decimals": 18,
            "name": "Wrapped Matic",
            'address': '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270',
        },
        'SUSHI': {
            "symbol": "SUSHI",
            "decimals": 18,
            "name": "SushiToken (PoS)",
            'address': '0x0b3F868E0BE5597D5DB7fEB59E1CADBb0fdDa50a',
        }
    },

    int(Network.Mainnet): {
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
            "set_loaded": True,
        },
        "WETH": {
            "symbol": "WETH",
            "decimals": 18,
            "name": "Wrapped Ether",
            "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        },
        "cbETH": {
            "symbol": "cbETH",
            "decimals": 18,
            "name": "Coinbase Wrapped Staked ETH",
            "address": "0xBe9895146f7AF43049ca1c1AE358B0541Ea49704"
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
        "UST (Wormhole)": {
            "symbol": "UST",
            "decimals": 18,
            "name": "UST",
            "address": "0xa693B19d2931d498c5B318dF961919BB4aee87a5",
            "protocol": "terra chain"
        },
        "SHIB": {
            "symbol": "SHIB",
            "decimals": 18,
            "name": "SHIBA INU",
            "address": "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"
        },
        "SUSHI": {
            "symbol": "SUSHI",
            "decimals": 18,
            "name": "SushiToken",
            "address": "0x6B3595068778DD592e39A122f4f5a5cF09C90fE2"
        },
        "ENS": {
            "symbol": "ENS",
            "decimals": 18,
            "name": "Ethereum Name Service",
            "address": "0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72",
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
        "COMP": {
            "symbol": "COMP",
            "decimals": 18,
            "name": "Compound",
            "address": "0xc00e94Cb662C3520282E6f5717214004A7f26888",
            "protocol": "compound"
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
        "GAL": {
            "symbol": "GAL",
            "decimals": 18,
            "name": "Project Galaxy",
            "address": "0x5fAa989Af96Af85384b8a938c2EdE4A7378D9875"
        },
        "DYDX": {
            "symbol": "DYDX",
            "decimals": 18,
            "name": "dYdX",
            "address": "0x92D6C1e31e14520e676a687F0a93788B716BEff5"
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
        "API3": {
            "symbol": "API3",
            "decimals": 18,
            "name": "API3",
            "address": "0x0b38210ea11411557c13457D4dA7dC6ea731B88a"
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
        },
        "YFM": {
            "symbol": "YFM",
            "decimals": 18,
            "name": "yfarm.finance",
            "address": "0xa665FED1b0C9dA00e91ca582f77dF36E325048c5"
        },
        "KYOKO": {
            "symbol": "KYOKO",
            "decimals": 18,
            "name": "Kyoko GameFi",
            "address": "0xAd097FE9170861937A56E975fE26E877173d325d"
        },
        "CNV": {
            "symbol": "CNV",
            "decimals": 18,
            "name": "Concave",
            "address": "0x000000007a58f5f58E697e51Ab0357BC9e260A04"
        },
        "BOND": {
            "symbol": "BOND",
            "decimals": 18,
            "name": "BarnBridge Governance Token",
            "address": "0x0391D2021f89DC339F60Fff84546EA23E337750f"
        },
        "NEST": {
            "symbol": "NEST",
            "decimals": 18,
            "name": "NEST",
            "address": "0x04abEdA201850aC0124161F037Efd70c74ddC74C"
        },
        "SUKU": {
            "symbol": "SUKU",
            "decimals": 18,
            "name": "SUKU",
            "address": "0x0763fdCCF1aE541A5961815C0872A8c5Bc6DE4d7"
        },
        "gOHM": {
            "symbol": "gOHM",
            "decimals": 18,
            "name": "Governance OHM",
            "address": "0x0ab87046fBb341D058F17CBC4c1133F25a20a52f"
        },
        "YFI": {
            "symbol": "YFI",
            "decimals": 18,
            "name": "yearn.finance",
            "address": "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e"
        },
        "USDD": {
            "symbol": "USDD",
            "decimals": 18,
            "name": "Decentralized USD",
            "address": "0x0C10bF8FcB7Bf5412187A595ab97a3609160b5c6"
        },
        "wNXM": {
            "symbol": "wNXM",
            "decimals": 18,
            "name": "Wrapped NXM",
            "address": "0x0d438F3b5175Bebc262bF23753C1E53d03432bDE"
        },
        "DAO": {
            "symbol": "DAO",
            "decimals": 18,
            "name": "DAO Maker",
            "address": "0x0f51bb10119727a7e5eA3538074fb341F56B09Ad"
        },
        "MANA": {
            "symbol": "MANA",
            "decimals": 18,
            "name": "Decentraland MANA",
            "address": "0x0F5D2fB29fb7d3CFeE444a200298f468908cC942"
        },
        "GVT": {
            "symbol": "GVT",
            "decimals": 18,
            "name": "Genesis Vision Token",
            "address": "0x103c3A209da59d3E7C4A89307e66521e081CFDF0"
        },
        "BLT": {
            "symbol": "BLT",
            "decimals": 18,
            "name": "Bloom Token",
            "address": "0x107c4504cd79C5d2696Ea0030a8dD4e92601B82e"
        },
        "1INCH": {
            "symbol": "1INCH",
            "decimals": 18,
            "name": "1INCH Token",
            "address": "0x111111111117dC0aa78b770fA6A738034120C302"
        },
        "ICHI": {
            "symbol": "ICHI",
            "decimals": 18,
            "name": "ICHI",
            "address": "0x111111517e4929D3dcbdfa7CCe55d30d4B6BC4d6"
        },
        "DPI": {
            "symbol": "DPI",
            "decimals": 18,
            "name": "DefiPulse Index",
            "address": "0x1494CA1F11D487c2bBe4543E90080AeBa4BA3C2b"
        },
        "NMR": {
            "symbol": "NMR",
            "decimals": 18,
            "name": "Numeraire",
            "address": "0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671"
        },
        "REP": {
            "symbol": "REP",
            "decimals": 18,
            "name": "Reputation",
            "address": "0x1985365e9f78359a9B6AD760e32412f4a445E862"
        },
        "agEUR": {
            "symbol": "agEUR",
            "decimals": 18,
            "name": "agEUR",
            "address": "0x1a7e4e63778B4f12a199C062f3eFdD288afCBce8"
        },
        "KP3R": {
            "symbol": "KP3R",
            "decimals": 18,
            "name": "Keep3rV1",
            "address": "0x1cEB5cB57C4D4E2b2433641b95Dd330A33185A44"
        },
        "BNT": {
            "symbol": "BNT",
            "decimals": 18,
            "name": "Bancor Network Token",
            "address": "0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C"
        },
        "OUSD": {
            "symbol": "OUSD",
            "decimals": 18,
            "name": "Origin Dollar",
            "address": "0x2A8e1E676Ec238d8A992307B495b45B3fEAa5e86"
        },
        "MPL": {
            "symbol": "MPL",
            "decimals": 18,
            "name": "Maple Token",
            "address": "0x33349B282065b0284d756F0577FB39c158F935e6"
        },
        "BADGER": {
            "symbol": "BADGER",
            "decimals": 18,
            "name": "Badger",
            "address": "0x3472A5A71965499acd81997a54BBA8D852C6E53d"
        },
        "WDOGE": {
            "symbol": "WDOGE",
            "decimals": 18,
            "name": "Wrapped DogeCoin",
            "address": "0x35a532d376FFd9a705d0Bb319532837337A398E7"
        },
        "HDRN": {
            "symbol": "HDRN",
            "decimals": 9,
            "name": "Hedron",
            "address": "0x3819f64f282bf135d62168C1e513280dAF905e06"
        },
        "cUSDC": {
            "symbol": "cUSDC",
            "decimals": 8,
            "name": "Compound USD Coin",
            "address": "0x39AA39c021dfbaE8faC545936693aC917d5E7563"
        },
        "XMON": {
            "symbol": "XMON",
            "decimals": 18,
            "name": "XMON",
            "address": "0x3aaDA3e213aBf8529606924d8D1c55CbDc70Bf74"
        },
        "XMT": {
            "symbol": "XMT",
            "decimals": 18,
            "name": "MetalSwap",
            "address": "0x3E5D9D8a63CC8a88748f229999CF59487e90721e"
        },
        "REN": {
            "symbol": "REN",
            "decimals": 18,
            "name": "Republic Token",
            "address": "0x408e41876cCCDC0F92210600ef50372656052a38"
        },
        "QRDO": {
            "symbol": "QRDO",
            "decimals": 8,
            "name": "Qredo Token",
            "address": "0x4123a133ae3c521FD134D7b13A2dEC35b56c2463"
        },
        "FUN": {
            "symbol": "FUN",
            "decimals": 8,
            "name": "FunFair",
            "address": "0x419D0d8BdD9aF5e606Ae2232ed285Aff190E711b"
        },
        "PAXG": {
            "symbol": "PAXG",
            "decimals": 18,
            "name": "Paxos Gold",
            "address": "0x45804880De22913dAFE09f4980848ECE6EcbAf78"
        },
        "WPR": {
            "symbol": "WPR",
            "decimals": 18,
            "name": "WePower Token",
            "address": "0x4CF488387F035FF08c371515562CBa712f9015d4"
        },
        "APE": {
            "symbol": "APE",
            "decimals": 18,
            "name": "ApeCoin",
            "address": "0x4d224452801ACEd8B2F0aebE155379bb5D594381"
        },
        "cETH": {
            "symbol": "cETH",
            "decimals": 8,
            "name": "Compound Ether",
            "address": "0x4Ddc2D193948926D02f9B1fE9e1daa0718270ED5"
        },
        "FTX Token": {
            "symbol": "FTX Token",
            "decimals": 18,
            "name": "FTT",
            "address": "0x50D1c9771902476076eCFc8B2A83Ad6b9355a4c9"
        },
        "RAY": {
            "symbol": "RAY",
            "decimals": 6,
            "name": "Raydium",
            "address": "0x5245C0249e5EEB2A0838266800471Fd32Adb1089"
        },
        "XYO": {
            "symbol": "XYO",
            "decimals": 18,
            "name": "XY Oracle",
            "address": "0x55296f69f40Ea6d20E478533C15A6B08B654E758"
        },
        "sUSD": {
            "symbol": "sUSD",
            "decimals": 18,
            "name": "Synth sUSD",
            "address": "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51"
        },
        "LPT": {
            "symbol": "LPT",
            "decimals": 18,
            "name": "Livepeer Token",
            "address": "0x58b6A8A3302369DAEc383334672404Ee733aB239"
        },
        "LDO": {
            "symbol": "LDO",
            "decimals": 18,
            "name": "Lido DAO Token",
            "address": "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32"
        },
        "WFLOW": {
            "symbol": "WFLOW",
            "decimals": 18,
            "name": "Wrapped Flow",
            "address": "0x5c147e74D63B1D31AA3Fd78Eb229B65161983B2b"
        },
        "cDAI": {
            "symbol": "cDAI",
            "decimals": 8,
            "name": "Compound Dai",
            "address": "0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643"
        },
        "LUSD": {
            "symbol": "LUSD",
            "decimals": 18,
            "name": "LUSD Stablecoin",
            "address": "0x5f98805A4E8be255a32880FDeC7F6728C6568bA0"
        },
        "RLC": {
            "symbol": "RLC",
            "decimals": 9,
            "name": "iEx.ec Network Token",
            "address": "0x607F4C5BB672230e8672085532f7e901544a7375"
        },
        "CORE": {
            "symbol": "CORE",
            "decimals": 18,
            "name": "cVault.finance",
            "address": "0x62359Ed7505Efc61FF1D56fEF82158CcaffA23D7"
        },
        "USDN": {
            "symbol": "USDN",
            "decimals": 18,
            "name": "Neutrino USD",
            "address": "0x674C6Ad92Fd080e4004b2312b45f796a192D27a0"
        },
        "GNO": {
            "symbol": "GNO",
            "decimals": 18,
            "name": "Gnosis Token",
            "address": "0x6810e776880C02933D47DB1b9fc05908e5386b96"
        },
        "LQTY": {
            "symbol": "LQTY",
            "decimals": 18,
            "name": "LQTY",
            "address": "0x6DEA81C8171D0bA574754EF6F8b412F2Ed88c54D"
        },
        "INST": {
            "symbol": "INST",
            "decimals": 18,
            "name": "Instadapp",
            "address": "0x6f40d4A6237C257fff2dB00FA0510DeEECd303eb"
        },
        "XSGD": {
            "symbol": "XSGD",
            "decimals": 6,
            "name": "XSGD",
            "address": "0x70e8dE73cE538DA2bEEd35d14187F6959a8ecA96"
        },
        "STRK": {
            "symbol": "STRK",
            "decimals": 18,
            "name": "Strike Token",
            "address": "0x74232704659ef37c08995e386A2E26cc27a8d7B1"
        },
        "TLOS": {
            "symbol": "TLOS",
            "decimals": 18,
            "name": "pTokens TLOS",
            "address": "0x7825e833D495F3d1c28872415a4aee339D26AC88"
        },
        "OGN": {
            "symbol": "OGN",
            "decimals": 18,
            "name": "OriginToken",
            "address": "0x8207c1FfC5B6804F6024322CcF34F29c3541Ae26"
        },
        "ANKR": {
            "symbol": "ANKR",
            "decimals": 18,
            "name": "Ankr Network",
            "address": "0x8290333ceF9e6D528dD5618Fb97a76f268f3EDD4"
        },
        "VVS": {
            "symbol": "VVS",
            "decimals": 18,
            "name": "VVS",
            "address": "0x839e71613f9aA06E5701CF6de63E303616B0DDE3"
        },
        "POLS": {
            "symbol": "POLS",
            "decimals": 18,
            "name": "PolkastarterToken",
            "address": "0x83e6f1E41cdd28eAcEB20Cb649155049Fac3D5Aa"
        },
        "KEEP": {
            "symbol": "KEEP",
            "decimals": 18,
            "name": "KEEP Token",
            "address": "0x85Eee30c52B0b379b046Fb0F85F4f3Dc3009aFEC"
        },
        "UQC": {
            "symbol": "UQC",
            "decimals": 18,
            "name": "Uquid Coin",
            "address": "0x8806926Ab68EB5a7b909DcAf6FdBe5d93271D6e2"
        },
        "⚗️": {
            "symbol": "⚗️",
            "decimals": 18,
            "name": "Alchemist",
            "address": "0x88ACDd2a6425c3FaAE4Bc9650Fd7E27e0Bebb7aB"
        },
        "CHR": {
            "symbol": "CHR",
            "decimals": 6,
            "name": "Chroma",
            "address": "0x8A2279d4A90B6fe1C4B30fa660cC9f926797bAA2"
        },
        "REQ": {
            "symbol": "REQ",
            "decimals": 18,
            "name": "Request Token",
            "address": "0x8f8221aFbB33998d8584A2B05749bA73c37a938a"
        },
        "DFI": {
            "symbol": "DFI",
            "decimals": 8,
            "name": "DeFiChain Token",
            "address": "0x8Fc8f8269ebca376D046Ce292dC7eaC40c8D358A"
        },
        "FEI": {
            "symbol": "FEI",
            "decimals": 18,
            "name": "Fei USD",
            "address": "0x956F47F50A910163D8BF957Cf5846D573E7f87CA"
        },
        "OCEAN": {
            "symbol": "OCEAN",
            "decimals": 18,
            "name": "Ocean Token",
            "address": "0x967da4048cD07aB37855c090aAF366e4ce1b9F48"
        },
        "BAX": {
            "symbol": "BAX",
            "decimals": 18,
            "name": "BAX",
            "address": "0x9a0242b7a33DAcbe40eDb927834F96eB39f8fBCB"
        },
        "ALPHA": {
            "symbol": "ALPHA",
            "decimals": 18,
            "name": "AlphaToken",
            "address": "0xa1faa113cbE53436Df28FF0aEe54275c13B40975"
        },
        "LYXe": {
            "symbol": "LYXe",
            "decimals": 18,
            "name": "LUKSO Token",
            "address": "0xA8b919680258d369114910511cc87595aec0be6D"
        },
        "ETH2x-FLI": {
            "symbol": "ETH2x-FLI",
            "decimals": 18,
            "name": "ETH 2x Flexible Leverage Index",
            "address": "0xAa6E8127831c9DE45ae56bB1b0d4D4Da6e5665BD"
        },
        "rETH": {
            "symbol": "rETH",
            "decimals": 18,
            "name": "Rocket Pool ETH",
            "address": "0xae78736Cd615f374D3085123A210448E74Fc6393"
        },
        "cZRX": {
            "symbol": "cZRX",
            "decimals": 8,
            "name": "Compound 0x",
            "address": "0xB3319f5D18Bc0D84dD1b4825Dcde5d5f7266d407"
        },
        "GMT": {
            "symbol": "GMT",
            "decimals": 18,
            "name": "Global Messaging Token",
            "address": "0xb3Bd49E28f8F832b8d1E246106991e546c323502"
        },
        "AXS": {
            "symbol": "AXS",
            "decimals": 18,
            "name": "Axie Infinity Shard",
            "address": "0xBB0E17EF65F82Ab018d8EDd776e8DD940327B28b"
        },
        "USDM": {
            "symbol": "USDM",
            "decimals": 6,
            "name": "USD Mapped Token",
            "address": "0xbbAec992fc2d637151dAF40451f160bF85f3C8C1"
        },
        "PERP": {
            "symbol": "PERP",
            "decimals": 18,
            "name": "Perpetual",
            "address": "0xbC396689893D065F41bc2C6EcbeE5e0085233447"
        },
        "LUNA (Wormhole)": {
            "symbol": "LUNA",
            "decimals": 6,
            "name": "LUNA",
            "address": "0xbd31EA8212119f94A611FA969881CBa3EA06Fa3d"
        },
        "TRIBE": {
            "symbol": "TRIBE",
            "decimals": 18,
            "name": "Tribe",
            "address": "0xc7283b66Eb1EB5FB86327f08e1B5816b0720212B"
        },
        "SURE": {
            "symbol": "SURE",
            "decimals": 18,
            "name": "inSure",
            "address": "0xcb86c6A22CB56B6cf40CaFEDb06BA0DF188a416E"
        },
        "FLOKI": {
            "symbol": "FLOKI",
            "decimals": 9,
            "name": "FLOKI",
            "address": "0xcf0C122c6b73ff809C693DB761e7BaeBe62b6a2E"
        },
        "ADS": {
            "symbol": "ADS",
            "decimals": 11,
            "name": "Adshares",
            "address": "0xcfcEcFe2bD2FED07A9145222E8a7ad9Cf1Ccd22A"
        },
        "RGT": {
            "symbol": "RGT",
            "decimals": 18,
            "name": "Rari Governance Token",
            "address": "0xD291E7a03283640FDc51b121aC401383A46cC623"
        },
        "RPL": {
            "symbol": "RPL",
            "decimals": 18,
            "name": "Rocket Pool Protocol",
            "address": "0xD33526068D116cE69F19A9ee46F0bd304F21A51f"
        },
        "AMPL": {
            "symbol": "AMPL",
            "decimals": 9,
            "name": "Ampleforth",
            "address": "0xD46bA6D942050d489DBd938a2C909A5d5039A161"
        },
        "CRV": {
            "symbol": "CRV",
            "decimals": 18,
            "name": "Curve DAO Token",
            "address": "0xD533a949740bb3306d119CC777fa900bA034cd52"
        },
        "COTI": {
            "symbol": "COTI",
            "decimals": 18,
            "name": "COTI Token",
            "address": "0xDDB3422497E61e13543BeA06989C0789117555c5"
        },
        "STPT": {
            "symbol": "STPT",
            "decimals": 18,
            "name": "STPT",
            "address": "0xDe7D85157d9714EADf595045CC12Ca4A5f3E2aDb"
        },
        "KNC": {
            "symbol": "KNC",
            "decimals": 18,
            "name": "Kyber Network Crystal v2",
            "address": "0xdeFA4e8a7bcBA345F687a2f1456F5Edd9CE97202"
        },
        "INJ": {
            "symbol": "INJ",
            "decimals": 18,
            "name": "Injective Token",
            "address": "0xe28b3B32B6c345A34Ff64674606124Dd5Aceca30"
        },
        "ZRX": {
            "symbol": "ZRX",
            "decimals": 18,
            "name": "0x Protocol Token",
            "address": "0xE41d2489571d322189246DaFA5ebDe1F4699F498"
        },
        "GT": {
            "symbol": "GT",
            "decimals": 18,
            "name": "GateChainToken",
            "address": "0xE66747a101bFF2dBA3697199DCcE5b743b454759"
        },
        "NEXM": {
            "symbol": "NEXM",
            "decimals": 8,
            "name": "Nexum Coin",
            "address": "0xe831F96A7a1DcE1aa2EB760b1e296c6A74CaA9d5"
        },
        "renBTC": {
            "symbol": "renBTC",
            "decimals": 8,
            "name": "renBTC",
            "address": "0xEB4C2781e4ebA804CE9a9803C67d0893436bB27D"
        },
        "XIDR": {
            "symbol": "XIDR",
            "decimals": 6,
            "name": "XIDR",
            "address": "0xebF2096E01455108bAdCbAF86cE30b6e5A72aa52"
        },
        "MLN": {
            "symbol": "MLN",
            "decimals": 18,
            "name": "Melon Token",
            "address": "0xec67005c4E498Ec7f55E092bd1d35cbC47C91892"
        },
        "AVINOC": {
            "symbol": "AVINOC",
            "decimals": 18,
            "name": "AVINOC Token",
            "address": "0xF1cA9cb74685755965c7458528A36934Df52A3EF"
        },
        "CHP": {
            "symbol": "CHP",
            "decimals": 18,
            "name": "Poker Chips",
            "address": "0xf3db7560E820834658B590C96234c333Cd3D5E5e"
        },
        "LOOKS": {
            "symbol": "LOOKS",
            "decimals": 18,
            "name": "LooksRare Token",
            "address": "0xf4d2888d29D722226FafA5d9B24F9164c092421E"
        },
        "HOPR": {
            "symbol": "HOPR",
            "decimals": 18,
            "name": "HOPR Token",
            "address": "0xF5581dFeFD8Fb0e4aeC526bE659CFaB1f8c781dA"
        },
        "cUSDT": {
            "symbol": "cUSDT",
            "decimals": 8,
            "name": "Compound USDT",
            "address": "0xf650C3d88D12dB855b8bf7D11Be6C55A4e07dCC9"
        },
        "ANY": {
            "symbol": "ANY",
            "decimals": 18,
            "name": "Anyswap",
            "address": "0xf99d58e463A2E07e5692127302C20A191861b4D6"
        },
        "sETH2": {
            "symbol": "sETH2",
            "decimals": 18,
            "name": "StakeWise Staked ETH2",
            "address": "0xFe2e637202056d30016725477c5da089Ab0A043A"
        },
        "GreenMetaverseToken": {
            "symbol": "GMT",
            "decimals": 8,
            "name": "GreenMetaverseToken",
            "address": "0xe3c408BD53c31C085a1746AF401A4042954ff740"
        },
        "wLUNA": {
            "symbol": "LUNA",
            "decimals": 18,
            "name": "Wrapped LUNA Token",
            "address": "0xd2877702675e6cEb975b4A1dFf9fb7BAF4C91ea9"
        },
        "ATOM": {
            "symbol": "ATOM",
            "decimals": 6,
            "name": "Cosmos",
            "address": "0x8D983cb9388EaC77af0474fA441C4815500Cb7BB"
        },
        "NXM": {
            "symbol": "NXM",
            "decimals": 18,
            "name": "NXM",
            "address": "0xd7c49CEE7E9188cCa6AD8FF264C1DA2e69D4Cf3B"
        },
        "IDLE": {
            "symbol": "IDLE",
            "decimals": 18,
            "name": "Idle",
            "address": "0x875773784Af8135eA0ef43b5a374AaD105c5D39e"
        },
        "INDEX": {
            "symbol": "INDEX",
            "decimals": 18,
            "name": "Index",
            "address": "0x0954906da0Bf32d5479e25f46056d22f08464cab"
        },
    },
    int(Network.ArbitrumOne): {
        "$SHARBI": {
            "symbol": "$SHARBI",
            "decimals": 9,
            "name": "SHARBI",
            "address": "0xaa54e84a3e6e5a80288d2c2f8e36ea5ca3a3ca30"
        },
        "0xBTC": {
            "symbol": "0xBTC",
            "decimals": 8,
            "name": "0xBitcoin Token",
            "address": "0x7cb16cb78ea464ad35c8a50abf95dff3c9e09d5d"
        },
        "AAVE": {
            "symbol": "AAVE",
            "decimals": 18,
            "name": "Aave Token",
            "address": "0xba5ddd1f9d7f570dc94a51479a000e3bce967196"
        },
        "ACR": {
            "symbol": "ACR",
            "decimals": 18,
            "name": "AI Card Render",
            "address": "0xdd389517320720f09db75d20a27d8a2cfa5f8568"
        },
        "ADoge": {
            "symbol": "ADoge",
            "decimals": 18,
            "name": "ArbiDoge",
            "address": "0x155f0dd04424939368972f4e1838687d6a831151"
        },
        "AFX": {
            "symbol": "AFX",
            "decimals": 18,
            "name": "Wonderful Protocol AFX Token",
            "address": "0x42972edecd94bdd19a622a6a419bdded2de56e08"
        },
        "ALIEN": {
            "symbol": "ALIEN",
            "decimals": 18,
            "name": "AlienFi",
            "address": "0x6740acb82ac5c63a7ad2397ee1faed7c788f5f8c"
        },
        "AMX": {
            "symbol": "AMX",
            "decimals": 6,
            "name": "Alt Markets",
            "address": "0xb2d948be3a74ecce80378d4093e6cd7f4dc1cf9c"
        },
        "APE": {
            "symbol": "APE",
            "decimals": 18,
            "name": "ApeCoin",
            "address": "0x74885b4d524d497261259b38900f54e6dbad2210"
        },
        "ARBINU": {
            "symbol": "ARBINU",
            "decimals": 18,
            "name": "ArbInu",
            "address": "0xdd8e557c8804d326c72074e987de02a23ae6ef84"
        },
        "ARBIS": {
            "symbol": "ARBIS",
            "decimals": 18,
            "name": "ARBIS | We have the yields",
            "address": "0x9f20de1fc9b161b34089cbeae888168b44b03461"
        },
        "ARBYS": {
            "symbol": "ARBYS",
            "decimals": 18,
            "name": "Arbys",
            "address": "0x86a1012d437bbff84fbdf62569d12d4fd3396f8c"
        },
        "ARC": {
            "symbol": "ARC",
            "decimals": 18,
            "name": "Arcadeum",
            "address": "0x7f465507f058e17ad21623927a120ac05ca32741"
        },
        "axlUSDC": {
            "symbol": "axlUSDC",
            "decimals": 6,
            "name": "Axelar Wrapped USDC",
            "address": "0xeb466342c4d449bc9f53a865d5cb90586f405215"
        },
        "AXS": {
            "symbol": "AXS",
            "decimals": 18,
            "name": "Axie Infinity Shard",
            "address": "0xe88998fb579266628af6a03e3821d5983e5d0089"
        },
        "BADGER": {
            "symbol": "BADGER",
            "decimals": 18,
            "name": "Badger",
            "address": "0xbfa641051ba0a0ad1b0acf549a89536a0d76472e"
        },
        "BAL": {
            "symbol": "BAL",
            "decimals": 18,
            "name": "Balancer",
            "address": "0x040d1edc9569d4bab2d15287dc5a4f10f56a56b8"
        },
        "BBO": {
            "symbol": "BBO",
            "decimals": 18,
            "name": "bamboo",
            "address": "0x86efb351b092a32d833a1ad7374d9bf0fc164aab"
        },
        "BFR": {
            "symbol": "BFR",
            "decimals": 18,
            "name": "Buffer Token",
            "address": "0x1a5b0aaf478bf1fda7b934c76e7692d722982a6d"
        },
        "BICO": {
            "symbol": "BICO",
            "decimals": 18,
            "name": "Biconomy Token",
            "address": "0xa68ec98d7ca870cf1dd0b00ebbb7c4bf60a8e74d"
        },
        "BIFI": {
            "symbol": "BIFI",
            "decimals": 18,
            "name": "beefy.finance",
            "address": "0x99c409e5f62e4bd2ac142f17cafb6810b8f0baae"
        },
        "BOND": {
            "symbol": "BOND",
            "decimals": 18,
            "name": "BarnBridge Governance Token",
            "address": "0x0d81e50bc677fa67341c44d7eaa9228dee64a4e1"
        },
        "BTC": {
            "symbol": "BTC",
            "decimals": 8,
            "name": "Bitcoin",
            "address": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        },
        "BUCK": {
            "symbol": "BUCK",
            "decimals": 18,
            "name": "Arbucks",
            "address": "0xafd871f684f21ab9d7137608c71808f83d75e6fc"
        },
        "BUSD": {
            "symbol": "BUSD",
            "decimals": 18,
            "name": "Binance USD",
            "address": "0x31190254504622cefdfa55a7d3d272e6462629a2"
        },
        "CAP": {
            "symbol": "CAP",
            "decimals": 18,
            "name": "Cap",
            "address": "0x031d35296154279dc1984dcd93e392b1f946737b"
        },
        "CELR": {
            "symbol": "CELR",
            "decimals": 18,
            "name": "CelerToken",
            "address": "0x3a8b787f78d775aecfeea15706d4221b40f345ab"
        },
        "CNFI": {
            "symbol": "CNFI",
            "decimals": 18,
            "name": "Connect Financial",
            "address": "0x6f5401c53e2769c858665621d22ddbf53d8d27c5"
        },
        "COMP": {
            "symbol": "COMP",
            "decimals": 18,
            "name": "Compound",
            "address": "0x354a6da3fcde098f8389cad84b0182725c6c91de"
        },
        "COTI": {
            "symbol": "COTI",
            "decimals": 18,
            "name": "COTI Token",
            "address": "0x6fe14d3cc2f7bddffba5cdb3bbe7467dd81ea101"
        },
        "CREAM": {
            "symbol": "CREAM",
            "decimals": 18,
            "name": "Cream",
            "address": "0xf4d48ce3ee1ac3651998971541badbb9a14d7234"
        },
        "CREDA": {
            "symbol": "CREDA",
            "decimals": 18,
            "name": "CreDA Protocol Token",
            "address": "0xc136e6b376a9946b156db1ed3a34b08afdaed76d"
        },
        "CRV": {
            "symbol": "CRV",
            "decimals": 18,
            "name": "Curve DAO Token",
            "address": "0x11cdb42b0eb46d95f990bedd4695a6e3fa034978"
        },
        "CTSI": {
            "symbol": "CTSI",
            "decimals": 18,
            "name": "Cartesi Token",
            "address": "0x319f865b287fcc10b30d8ce6144e8b6d1b476999"
        },
        "CVI": {
            "symbol": "CVI",
            "decimals": 18,
            "name": "Crypto Volatility Token",
            "address": "0x8096ad3107715747361acefe685943bfb427c722"
        },
        "CVX": {
            "symbol": "CVX",
            "decimals": 18,
            "name": "Convex Token",
            "address": "0xaafcfd42c9954c6689ef1901e03db742520829c5"
        },
        "DAI": {
            "symbol": "DAI",
            "decimals": 18,
            "name": "Dai Stablecoin",
            "address": "0xda10009cbd5d07dd0cecc66161fc93d7c9000da1"
        },
        "DBL": {
            "symbol": "DBL",
            "decimals": 18,
            "name": "Doubloon Token",
            "address": "0xd3f1da62cafb7e7bc6531ff1cef6f414291f03d3"
        },
        "DEGEN": {
            "symbol": "DEGEN",
            "decimals": 18,
            "name": "DEGEN Index",
            "address": "0xae6e3540e97b0b9ea8797b157b510e133afb6282"
        },
        "DF": {
            "symbol": "DF",
            "decimals": 18,
            "name": "dForce",
            "address": "0xae6aab43c4f3e0cea4ab83752c278f8debaba689"
        },
        "DHT": {
            "symbol": "DHT",
            "decimals": 18,
            "name": "dHedge DAO Token",
            "address": "0x8038f3c971414fd1fc220ba727f2d4a0fc98cb65"
        },
        "DODO": {
            "symbol": "DODO",
            "decimals": 18,
            "name": "DODO bird",
            "address": "0x69eb4fa4a2fbd498c257c57ea8b7655a2559a581"
        },
        "DOG": {
            "symbol": "DOG",
            "decimals": 18,
            "name": "The Doge NFT",
            "address": "0x4425742f1ec8d98779690b5a3a6276db85ddc01a"
        },
        "DPX": {
            "symbol": "DPX",
            "decimals": 18,
            "name": "Dopex Governance Token",
            "address": "0x6c2c06790b3e3e3c38e12ee22f8183b37a13ee55"
        },
        "DSLA": {
            "symbol": "DSLA",
            "decimals": 18,
            "name": "DSLA",
            "address": "0x7ce746b45eabd0c4321538dec1b849c79a9a8476"
        },
        "DSQ": {
            "symbol": "DSQ",
            "decimals": 18,
            "name": "DSquared Governance Token",
            "address": "0xdb0c6fc9e01cd95eb1d3bbae6689962de489cd7b"
        },
        "DUSD": {
            "symbol": "DUSD",
            "decimals": 6,
            "name": "DigitalDollar",
            "address": "0xf0b5ceefc89684889e5f7e0a7775bd100fcd3709"
        },
        "DVF": {
            "symbol": "DVF",
            "decimals": 18,
            "name": "DeversiFi Token",
            "address": "0xa7aa2921618e3d63da433829d448b58c9445a4c3"
        },
        "DXD": {
            "symbol": "DXD",
            "decimals": 18,
            "name": "DXdao",
            "address": "0xc3ae0333f0f34aa734d5493276223d95b8f9cb37"
        },
        "EMAX": {
            "symbol": "EMAX",
            "decimals": 18,
            "name": "EthereumMax",
            "address": "0x123389c2f0e9194d9ba98c21e63c375b67614108"
        },
        "ETH": {
            "symbol": "ETH",
            "decimals": 18,
            "name": "Ethereum",
            "address": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
        },
        "FCTR": {
            "symbol": "FCTR",
            "decimals": 18,
            "name": "Factor",
            "address": "0x6dd963c510c2d2f09d5eddb48ede45fed063eb36"
        },
        "FEI": {
            "symbol": "FEI",
            "decimals": 18,
            "name": "Fei USD",
            "address": "0x4a717522566c7a09fd2774ccedc5a8c43c5f9fd2"
        },
        "FLUID": {
            "symbol": "FLUID",
            "decimals": 18,
            "name": "FluidFi",
            "address": "0x876ec6be52486eeec06bc06434f3e629d695c6ba"
        },
        "FOREX": {
            "symbol": "FOREX",
            "decimals": 18,
            "name": "handleFOREX",
            "address": "0xdb298285fe4c5410b05390ca80e8fbe9de1f259b"
        },
        "FRAX": {
            "symbol": "FRAX",
            "decimals": 18,
            "name": "Frax",
            "address": "0x17fc002b466eec40dae837fc4be5c67993ddbd6f"
        },
        "FST": {
            "symbol": "FST",
            "decimals": 18,
            "name": "Futureswap Token",
            "address": "0x488cc08935458403a0458e45e20c0159c8ab2c92"
        },
        "FTD": {
            "symbol": "FTD",
            "decimals": 9,
            "name": "FTDex",
            "address": "0x2a3b32ee6b34c27ebc03fa33fd80c42ea5998434"
        },
        "FXS": {
            "symbol": "FXS",
            "decimals": 18,
            "name": "Frax Share",
            "address": "0x9d2f299715d94d8a7e6f5eaa8e654e8c74a988a7"
        },
        "GEM": {
            "symbol": "GEM",
            "decimals": 18,
            "name": "Gemstone",
            "address": "0x458a2df1a5c74c5dc9ed6e01dd1178e6d353243b"
        },
        "GMD": {
            "symbol": "GMD",
            "decimals": 18,
            "name": "GMD",
            "address": "0x4945970efeec98d393b4b979b9be265a3ae28a8b"
        },
        "GMX": {
            "symbol": "GMX",
            "decimals": 18,
            "name": "GMX",
            "address": "0xfc5a1a6eb076a2c7ad06ed22c90d7e710e35ad0a"
        },
        "GNO": {
            "symbol": "GNO",
            "decimals": 18,
            "name": "Gnosis Token",
            "address": "0xa0b862f60edef4452f25b4160f177db44deb6cf1"
        },
        "GOBLIN": {
            "symbol": "GOBLIN",
            "decimals": 9,
            "name": "Goblin",
            "address": "0xfd559867b6d3445f9589074c3ac46418fdfffda4"
        },
        "gOHM": {
            "symbol": "gOHM",
            "decimals": 18,
            "name": "Governance OHM",
            "address": "0x8d9ba570d6cb60c7e3e0f31343efe75ab8e65fb1"
        },
        "GOVI": {
            "symbol": "GOVI",
            "decimals": 18,
            "name": "GOVI",
            "address": "0x07e49d5de43dda6162fa28d24d5935c151875283"
        },
        "GRAIL": {
            "symbol": "GRAIL",
            "decimals": 18,
            "name": "Camelot token",
            "address": "0x3d9907f9a368ad0a51be60f7da3b97cf940982d8"
        },
        "GRT": {
            "symbol": "GRT",
            "decimals": 18,
            "name": "Graph Token",
            "address": "0x9623063377ad1b27544c965ccd7342f7ea7e88c7"
        },
        "HAMI": {
            "symbol": "HAMI",
            "decimals": 18,
            "name": "Hamachi",
            "address": "0x02150e97271fdc0d6e3a16d9094a0948266f07dd"
        },
        "HDX": {
            "symbol": "HDX",
            "decimals": 9,
            "name": "Hydranet",
            "address": "0xf4fe727c855c2d395852ca43f645cab4b504af23"
        },
        "HEGIC": {
            "symbol": "HEGIC",
            "decimals": 18,
            "name": "Hegic",
            "address": "0x431402e8b9de9aa016c743880e04e517074d8cec"
        },
        "HND": {
            "symbol": "HND",
            "decimals": 18,
            "name": "Hundred Finance",
            "address": "0x10010078a54396f62c96df8532dc2b4847d47ed3"
        },
        "HOP": {
            "symbol": "HOP",
            "decimals": 18,
            "name": "Hop",
            "address": "0xc5102fe9359fd9a28f877a67e36b0f050d81a3cc"
        },
        "HWT": {
            "symbol": "HWT",
            "decimals": 18,
            "name": "HonorWorld Token",
            "address": "0xbcc9c1763d54427bdf5efb6e9eb9494e5a1fbabf"
        },
        "IMO": {
            "symbol": "IMO",
            "decimals": 18,
            "name": "Ideamarket",
            "address": "0xb41bd4c99da73510d9e081c5fadbe7a27ac1f814"
        },
        "JONES": {
            "symbol": "JONES",
            "decimals": 18,
            "name": "Jones DAO",
            "address": "0x10393c20975cf177a3513071bc110f7962cd67da"
        },
        "KNC": {
            "symbol": "KNC",
            "decimals": 18,
            "name": "Kyber Network Crystal v2",
            "address": "0xe4dddfe67e7164b0fe14e218d80dc4c08edc01cb"
        },
        "KROM": {
            "symbol": "KROM",
            "decimals": 18,
            "name": "Kromatika",
            "address": "0x55ff62567f09906a85183b866df84bf599a4bf70"
        },
        "L2DAO": {
            "symbol": "L2DAO",
            "decimals": 18,
            "name": "Layer2DAO",
            "address": "0x2cab3abfc1670d1a452df502e216a66883cdf079"
        },
        "LDO": {
            "symbol": "LDO",
            "decimals": 18,
            "name": "Lido DAO Token",
            "address": "0x13ad51ed4f1b7e9dc168d8a00cb3f4ddd85efa60"
        },
        "LEVI": {
            "symbol": "LEVI",
            "decimals": 18,
            "name": "LeverageInu",
            "address": "0x954ac1c73e16c77198e83c088ade88f6223f3d44"
        },
        "LINK": {
            "symbol": "LINK",
            "decimals": 18,
            "name": "ChainLink Token",
            "address": "0xf97f4df75117a78c1a5a0dbb814af92458539fb4"
        },
        "LIQD": {
            "symbol": "LIQD",
            "decimals": 18,
            "name": "Liquid",
            "address": "0x93c15cd7de26f07265f0272e0b831c5d7fab174f"
        },
        "LON": {
            "symbol": "LON",
            "decimals": 18,
            "name": "Tokenlon",
            "address": "0x55678cd083fcdc2947a0df635c93c838c89454a3"
        },
        "LPT": {
            "symbol": "LPT",
            "decimals": 18,
            "name": "Livepeer Token",
            "address": "0x289ba1701c2f088cf0faf8b3705246331cb8a839"
        },
        "LRC": {
            "symbol": "LRC",
            "decimals": 18,
            "name": "LoopringCoin V2",
            "address": "0x46d0ce7de6247b0a95f67b43b589b4041bae7fbe"
        },
        "MAGIC": {
            "symbol": "MAGIC",
            "decimals": 18,
            "name": "MAGIC",
            "address": "0x539bde0d7dbd336b79148aa742883198bbf60342"
        },
        "MAI": {
            "symbol": "MAI",
            "decimals": 18,
            "name": "Mai Stablecoin",
            "address": "0x3f56e0c36d275367b8c502090edf38289b3dea0d"
        },
        "MATH": {
            "symbol": "MATH",
            "decimals": 18,
            "name": "MATH Token",
            "address": "0x99f40b01ba9c469193b360f72740e416b17ac332"
        },
        "MATIC": {
            "symbol": "MATIC",
            "decimals": 18,
            "name": "Matic Token",
            "address": "0x561877b6b3dd7651313794e5f2894b2f18be0766"
        },
        "MATTER": {
            "symbol": "MATTER",
            "decimals": 18,
            "name": "Antimatter.Finance Governance Token",
            "address": "0xaaa62d9584cbe8e4d68a43ec91bff4ff1fadb202"
        },
        "MCB": {
            "symbol": "MCB",
            "decimals": 18,
            "name": "MCDEX Token",
            "address": "0x4e352cf164e64adcbad318c3a1e222e9eba4ce42"
        },
        "MIM": {
            "symbol": "MIM",
            "decimals": 18,
            "name": "Magic Internet Money",
            "address": "0xfea7a6a0b346362bf88a9e4a88416b77a57d6c2a"
        },
        "MMT": {
            "symbol": "MMT",
            "decimals": 18,
            "name": "MyMetaTrader Token",
            "address": "0x27d8de4c30ffde34e982482ae504fc7f23061f61"
        },
        "MNTO": {
            "symbol": "MNTO",
            "decimals": 18,
            "name": "Minato",
            "address": "0xf0dfad1817b5ba73726b02ab34dd4b4b00bcd392"
        },
        "MOD": {
            "symbol": "MOD",
            "decimals": 18,
            "name": "Modular",
            "address": "0x244ae62439c1ef3187f244d8604ac2c391ef2b53"
        },
        "MYC": {
            "symbol": "MYC",
            "decimals": 18,
            "name": "Mycelium",
            "address": "0xc74fe4c715510ec2f8c61d70d397b32043f55abe"
        },
        "NEU": {
            "symbol": "NEU",
            "decimals": 18,
            "name": "Neutra Token",
            "address": "0xda51015b73ce11f77a115bb1b8a7049e02ddecf0"
        },
        "NFTE": {
            "symbol": "NFTE",
            "decimals": 18,
            "name": "NFTEarth",
            "address": "0xb261104a83887ae92392fb5ce5899fcfe5481456"
        },
        "NIFLOKI": {
            "symbol": "NIFLOKI",
            "decimals": 9,
            "name": "Nitro Floki",
            "address": "0x1fae2a29940015632f2a6ce006dfa7e3225515a7"
        },
        "NISHIB": {
            "symbol": "NISHIB",
            "decimals": 18,
            "name": "NitroShiba",
            "address": "0x4dad357726b41bb8932764340ee9108cc5ad33a0"
        },
        "nitroDOGE": {
            "symbol": "nitroDOGE",
            "decimals": 18,
            "name": "nitroDOGE",
            "address": "0x8e75dafecf75de7747a05b0891177ba03333a166"
        },
        "NYAN": {
            "symbol": "NYAN",
            "decimals": 18,
            "name": "ArbiNYAN",
            "address": "0xed3fb761414da74b74f33e5c5a1f78104b188dfc"
        },
        "O3": {
            "symbol": "O3",
            "decimals": 18,
            "name": "O3 Swap Token",
            "address": "0xee9801669c6138e84bd50deb500827b776777d28"
        },
        "ODIN": {
            "symbol": "ODIN",
            "decimals": 18,
            "name": "AsgardX",
            "address": "0xee9857de0e55d4a54d36a5a5a73a15e57435fdca"
        },
        "OREO": {
            "symbol": "OREO",
            "decimals": 18,
            "name": "OreoSwap",
            "address": "0x319e222de462ac959baf2aec848697aec2bbd770"
        },
        "P4D": {
            "symbol": "P4D",
            "decimals": 18,
            "name": "PoSH4D",
            "address": "0xefc43cf79f406d62960e34d3a62c729a0eebec4b"
        },
        "PANA": {
            "symbol": "PANA",
            "decimals": 18,
            "name": "Pana DAO",
            "address": "0x369eb8197062093a20402935d3a707b4ae414e9d"
        },
        "PAXG": {
            "symbol": "PAXG",
            "decimals": 18,
            "name": "Paxos Gold",
            "address": "0xfeb4dfc8c4cf7ed305bb08065d08ec6ee6728429"
        },
        "PERP": {
            "symbol": "PERP",
            "decimals": 18,
            "name": "Perpetual",
            "address": "0x753d224bcf9aafacd81558c32341416df61d3dac"
        },
        "PGS": {
            "symbol": "PGS",
            "decimals": 18,
            "name": "Pegasus",
            "address": "0x43e4ef7e796a631539f523900da824e73edc3110"
        },
        "PICKLE": {
            "symbol": "PICKLE",
            "decimals": 18,
            "name": "PickleToken",
            "address": "0x965772e0e9c84b6f359c8597c891108dcf1c5b1a"
        },
        "PLS": {
            "symbol": "PLS",
            "decimals": 18,
            "name": "Plutus",
            "address": "0x51318b7d00db7acc4026c88c3952b66278b6a67f"
        },
        "POI$ON": {
            "symbol": "POI$ON",
            "decimals": 18,
            "name": "Poison.Finance Poison",
            "address": "0x31c91d8fb96bff40955dd2dbc909b36e8b104dde"
        },
        "POP": {
            "symbol": "POP",
            "decimals": 18,
            "name": "Popcorn",
            "address": "0x68ead55c258d6fa5e46d67fc90f53211eab885be"
        },
        "PREMIA": {
            "symbol": "PREMIA",
            "decimals": 18,
            "name": "Premia",
            "address": "0x51fc0f6660482ea73330e414efd7808811a57fa2"
        },
        "PSI": {
            "symbol": "PSI",
            "decimals": 9,
            "name": "Trident",
            "address": "0x602eb0d99a5e3e76d1510372c4d2020e12eaea8a"
        },
        "RDNT": {
            "symbol": "RDNT",
            "decimals": 18,
            "name": "Radiant",
            "address": "0x0c4681e6c0235179ec3d4f4fc4df3d14fdd96017"
        },
        "RDPX": {
            "symbol": "RDPX",
            "decimals": 18,
            "name": "Dopex Rebate Token",
            "address": "0x32eb7902d4134bf98a28b963d26de779af92a212"
        },
        "rETH": {
            "symbol": "rETH",
            "decimals": 18,
            "name": "Rocket Pool ETH",
            "address": "0xec70dcb4a1efa46b8f2d97c310c9c4790ba5ffa8"
        },
        "RGT": {
            "symbol": "RGT",
            "decimals": 18,
            "name": "Rari Governance Token",
            "address": "0xef888bca6ab6b1d26dbec977c455388ecd794794"
        },
        "RING": {
            "symbol": "RING",
            "decimals": 18,
            "name": "Darwinia Network Native Token",
            "address": "0x9e523234d36973f9e38642886197d023c88e307e"
        },
        "ROUL": {
            "symbol": "ROUL",
            "decimals": 18,
            "name": "ArbiRoul Casino Chip",
            "address": "0xc7831178793868a75122eaaff634ece07a2ecaaa"
        },
        "SDL": {
            "symbol": "SDL",
            "decimals": 18,
            "name": "Saddle DAO",
            "address": "0x75c9bc761d88f70156daf83aa010e84680baf131"
        },
        "SDT": {
            "symbol": "SDT",
            "decimals": 18,
            "name": "Stake DAO Token",
            "address": "0x7ba4a00d54a07461d9db2aef539e91409943adc9"
        },
        "Silo": {
            "symbol": "Silo",
            "decimals": 18,
            "name": "Silo Governance Token",
            "address": "0x0341c0c0ec423328621788d4854119b97f44e391"
        },
        "SIS": {
            "symbol": "SIS",
            "decimals": 18,
            "name": "Symbiosis",
            "address": "0x9e758b8a98a42d612b3d38b66a22074dc03d7370"
        },
        "SLIZ": {
            "symbol": "SLIZ",
            "decimals": 18,
            "name": "SolidLizard dex token",
            "address": "0x463913d3a3d3d291667d53b8325c598eb88d3b0e"
        },
        "SOL": {
            "symbol": "SOL",
            "decimals": 9,
            "name": "Wrapped SOL (Wormhole)",
            "address": "0xb74da9fe2f96b9e0a5f4a3cf0b92dd2bec617124"
        },
        "SPA": {
            "symbol": "SPA",
            "decimals": 18,
            "name": "Sperax",
            "address": "0x5575552988a3a80504bbaeb1311674fcfd40ad4b"
        },
        "SPELL": {
            "symbol": "SPELL",
            "decimals": 18,
            "name": "Spell Token",
            "address": "0x3e6648c5a70a150a88bce65f4ad4d506fe15d2af"
        },
        "STG": {
            "symbol": "STG",
            "decimals": 18,
            "name": "StargateToken",
            "address": "0x6694340fc020c5e6b96567843da2df01b2ce1eb6"
        },
        "STR": {
            "symbol": "STR",
            "decimals": 18,
            "name": "Sterling",
            "address": "0x5db7b150c5f38c5f5db11dcbdb885028fcc51d68"
        },
        "STRP": {
            "symbol": "STRP",
            "decimals": 18,
            "name": "Strips Token",
            "address": "0x326c33fd1113c1f29b35b4407f3d6312a8518431"
        },
        "sUSD": {
            "symbol": "sUSD",
            "decimals": 18,
            "name": "Synth sUSD",
            "address": "0xa970af1a584579b618be4d69ad6f73459d112f95"
        },
        "SUSHI": {
            "symbol": "SUSHI",
            "decimals": 18,
            "name": "SushiToken",
            "address": "0xd4d42f0b6def4ce0383636770ef773390d85c61a"
        },
        "SYN": {
            "symbol": "SYN",
            "decimals": 18,
            "name": "Synapse",
            "address": "0x080f6aed32fc474dd5717105dba5ea57268f46eb"
        },
        "TAI": {
            "symbol": "TAI",
            "decimals": 9,
            "name": "TronAI",
            "address": "0xd2eb76feff5fbd549ca078908fb5efce7533a09d"
        },
        "TCR": {
            "symbol": "TCR",
            "decimals": 18,
            "name": "Tracer",
            "address": "0xa72159fc390f0e3c6d415e658264c7c4051e9b87"
        },
        "TND": {
            "symbol": "TND",
            "decimals": 18,
            "name": "TND",
            "address": "0xc47d9753f3b32aa9548a7c3f30b6aec3b2d2798c"
        },
        "TROVE": {
            "symbol": "TROVE",
            "decimals": 18,
            "name": "Arbitrove Governance Token",
            "address": "0x982239d38af50b0168da33346d85fb12929c4c07"
        },
        "TUSD": {
            "symbol": "TUSD",
            "decimals": 18,
            "name": "TrueUSD",
            "address": "0x4d15a3a2286d883af0aa1b3f21367843fac63e07"
        },
        "UMAMI": {
            "symbol": "UMAMI",
            "decimals": 9,
            "name": "Umami",
            "address": "0x1622bf67e6e5747b81866fe0b85178a93c7f86e3"
        },
        "UNI": {
            "symbol": "UNI",
            "decimals": 18,
            "name": "Uniswap",
            "address": "0xfa7f8980b0f1e64a2062791cc3b0871572f1f7f0"
        },
        "USDC": {
            "symbol": "USDC",
            "decimals": 6,
            "name": "USD Coin (Arb1)",
            "address": "0xff970a61a04b1ca14834a43f5de4533ebddb5cc8"
        },
        "USDD": {
            "symbol": "USDD",
            "decimals": 18,
            "name": "Decentralized USD",
            "address": "0x680447595e8b7b3aa1b43beb9f6098c79ac2ab3f"
        },
        "USDs": {
            "symbol": "USDs",
            "decimals": 18,
            "name": "Sperax USD",
            "address": "0xd74f5255d557944cf7dd0e45ff521520002d5748"
        },
        "USDT": {
            "symbol": "USDT",
            "decimals": 6,
            "name": "Tether USD",
            "address": "0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9"
        },
        "USX": {
            "symbol": "USX",
            "decimals": 18,
            "name": "dForce USD",
            "address": "0x641441c631e2f909700d2f41fd87f0aa6a6b4edb"
        },
        "VELA": {
            "symbol": "VELA",
            "decimals": 18,
            "name": "VelaToken",
            "address": "0x088cd8f5ef3652623c22d48b1605dcfe860cd704"
        },
        "VISR": {
            "symbol": "VISR",
            "decimals": 18,
            "name": "VISOR",
            "address": "0x995c235521820f2637303ca1970c7c044583df44"
        },
        "VOLTA": {
            "symbol": "VOLTA",
            "decimals": 18,
            "name": "Volta Protocol Token",
            "address": "0x417a1afd44250314bffb11ff68e989775e990ab6"
        },
        "VOX2.0": {
            "symbol": "VOX2.0",
            "decimals": 18,
            "name": "Vox Finance 2.0",
            "address": "0xa0eebb0e5c3859a1c5412c2380c074f2f6725e2e"
        },
        "VSTA": {
            "symbol": "VSTA",
            "decimals": 18,
            "name": "Vesta",
            "address": "0xa684cd057951541187f288294a1e1c2646aa2d24"
        },
        "WBTC": {
            "symbol": "WBTC",
            "decimals": 8,
            "name": "Wrapped BTC",
            "address": "0x2f2a2543b76a4166549f7aab2e75bef0aefc5b0f"
        },
        "WETH": {
            "symbol": "WETH",
            "decimals": 18,
            "name": "Wrapped Ether",
            "address": "0x82af49447d8a07e3bd95bd0d56f35241523fbab1"
        },
        "WHEAT": {
            "symbol": "WHEAT",
            "decimals": 18,
            "name": "Wheat",
            "address": "0x771146816a0c7d74daf652252d646ab0bff7c21a"
        },
        "WOO": {
            "symbol": "WOO",
            "decimals": 18,
            "name": "Wootrade Network",
            "address": "0xcafcd85d8ca7ad1e1c6f82f651fa15e33aefd07b"
        },
        "wstETH": {
            "symbol": "wstETH",
            "decimals": 18,
            "name": "Wrapped liquid staked Ether 2.0",
            "address": "0x5979d7b546e38e414f7e9822514be443a4800529"
        },
        "XCAL": {
            "symbol": "XCAL",
            "decimals": 18,
            "name": "3xcalibur Ecosystem Token",
            "address": "0xd2568accd10a4c98e87c44e9920360031ad89fcb"
        },
        "XETH": {
            "symbol": "XETH",
            "decimals": 18,
            "name": "Wonderful Protocol XETH Token",
            "address": "0x45a21e90a4e95582797982fb8c8318ecdf0a21ae"
        },
        "XTK": {
            "symbol": "XTK",
            "decimals": 18,
            "name": "xToken",
            "address": "0xf0a5717ec0883ee56438932b0fe4a20822735fba"
        },
        "Y2K": {
            "symbol": "Y2K",
            "decimals": 18,
            "name": "Y2K",
            "address": "0x65c936f008bc34fe819bce9fa5afd9dc2d49977f"
        },
        "YFI": {
            "symbol": "YFI",
            "decimals": 18,
            "name": "yearn.finance",
            "address": "0x82e3a8f066a6989666b031d916c43672085b1582"
        },
        "ZYB": {
            "symbol": "ZYB",
            "decimals": 18,
            "name": "Zyber Token",
            "address": "0x3b475f6f2f41853706afc9fa6a6b8c5df1a2724c"
        }
    },
    int(Network.Optimism): {
        "0xBTC": {
            "symbol": "0xBTC",
            "decimals": 8,
            "name": "0xBitcoin Token",
            "address": "0xe0bb0d3de8c10976511e5030ca403dbf4c25165b"
        },
        "AAVE": {
            "symbol": "AAVE",
            "decimals": 18,
            "name": "Aave Token",
            "address": "0x76fb31fb4af56892a25e32cfc43de717950c9278"
        },
        "ACX": {
            "symbol": "ACX",
            "decimals": 18,
            "name": "Across Protocol Token",
            "address": "0xff733b2a3557a7ed6697007ab5d11b79fdd1b76b"
        },
        "AELIN": {
            "symbol": "AELIN",
            "decimals": 18,
            "name": "Aelin Token",
            "address": "0x61baadcf22d2565b0f471b291c475db5555e0b76"
        },
        "alETH": {
            "symbol": "alETH",
            "decimals": 18,
            "name": "Alchemix ETH",
            "address": "0x3e29d3a9316dab217754d13b28646b76607c5f04"
        },
        "BAL": {
            "symbol": "BAL",
            "decimals": 18,
            "name": "Balancer",
            "address": "0xfe8b128ba8c78aabc59d4c64cee7ff28e9379921"
        },
        "BitANT": {
            "symbol": "BitANT",
            "decimals": 18,
            "name": "BitANT",
            "address": "0x5029c236320b8f15ef0a657054b84d90bfbeded3"
        },
        "BOB": {
            "symbol": "BOB",
            "decimals": 18,
            "name": "BOB",
            "address": "0xb0b195aefa3650a6908f15cdac7d92f8a5791b0b"
        },
        "BOND": {
            "symbol": "BOND",
            "decimals": 18,
            "name": "BarnBridge Governance Token (Optimism)",
            "address": "0x3e7ef8f50246f725885102e8238cbba33f276747"
        },
        "BTC": {
            "symbol": "BTC",
            "decimals": 8,
            "name": "Bitcoin",
            "address": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        },
        "BUSD": {
            "symbol": "BUSD",
            "decimals": 18,
            "name": "BUSD Token",
            "address": "0x9c9e5fd8bbc25984b178fdce6117defa39d2db39"
        },
        "COLLAB": {
            "symbol": "COLLAB",
            "decimals": 18,
            "name": "Collab.Land",
            "address": "0x8b21e9b7daf2c4325bf3d18c1beb79a347fe902a"
        },
        "CRV": {
            "symbol": "CRV",
            "decimals": 18,
            "name": "Curve DAO Token",
            "address": "0x0994206dfe8de6ec6920ff4d779b0d950605fb53"
        },
        "CTSI": {
            "symbol": "CTSI",
            "decimals": 18,
            "name": "Cartesi Token",
            "address": "0xec6adef5e1006bb305bb1975333e8fc4071295bf"
        },
        "DAI": {
            "symbol": "DAI",
            "decimals": 18,
            "name": "Dai Stablecoin",
            "address": "0xda10009cbd5d07dd0cecc66161fc93d7c9000da1"
        },
        "DCN": {
            "symbol": "DCN",
            "decimals": 0,
            "name": "Dentacoin",
            "address": "0x1da650c3b2daa8aa9ff6f661d4156ce24d08a062"
        },
        "DHT": {
            "symbol": "DHT",
            "decimals": 18,
            "name": "dHEDGE DAO Token",
            "address": "0xaf9fe3b5ccdae78188b1f8b9a49da7ae9510f151"
        },
        "DOLA": {
            "symbol": "DOLA",
            "decimals": 18,
            "name": "Dola USD Stablecoin",
            "address": "0x8ae125e8653821e851f12a49f7765db9a9ce7384"
        },
        "ENS": {
            "symbol": "ENS",
            "decimals": 18,
            "name": "Ethereum Name Service",
            "address": "0x65559aa14915a70190438ef90104769e5e890a00"
        },
        "EST": {
            "symbol": "EST",
            "decimals": 18,
            "name": "Erica Social Token",
            "address": "0x7b0bcc23851bbf7601efc9e9fe532bf5284f65d3"
        },
        "ETH": {
            "symbol": "ETH",
            "decimals": 18,
            "name": "Ether",
            "address": "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000"
        },
        "FRAX": {
            "symbol": "FRAX",
            "decimals": 18,
            "name": "Frax",
            "address": "0x2e3d870790dc77a83dd1d18184acc7439a53f475"
        },
        "FXS": {
            "symbol": "FXS",
            "decimals": 18,
            "name": "Frax Share",
            "address": "0x67ccea5bb16181e7b4109c9c2143c24a1c2205be"
        },
        "HAN": {
            "symbol": "HAN",
            "decimals": 18,
            "name": "HanChain",
            "address": "0x50bce64397c75488465253c0a034b8097fea6578"
        },
        "HOP": {
            "symbol": "HOP",
            "decimals": 18,
            "name": "Hop",
            "address": "0xc5102fe9359fd9a28f877a67e36b0f050d81a3cc"
        },
        "KNC": {
            "symbol": "KNC",
            "decimals": 18,
            "name": "Kyber Network Crystal v2",
            "address": "0xa00e3a3511aac35ca78530c85007afcd31753819"
        },
        "KROM": {
            "symbol": "KROM",
            "decimals": 18,
            "name": "Kromatika",
            "address": "0xf98dcd95217e15e05d8638da4c91125e59590b07"
        },
        "KWENTA": {
            "symbol": "KWENTA",
            "decimals": 18,
            "name": "Kwenta",
            "address": "0x920cf626a271321c151d027030d5d08af699456b"
        },
        "L2DAO": {
            "symbol": "L2DAO",
            "decimals": 18,
            "name": "Layer2DAO",
            "address": "0xd52f94df742a6f4b4c8b033369fe13a41782bf44"
        },
        "LDO": {
            "symbol": "LDO",
            "decimals": 18,
            "name": "Lido DAO Token",
            "address": "0xfdb794692724153d1488ccdbe0c56c252596735f"
        },
        "LINK": {
            "symbol": "LINK",
            "decimals": 18,
            "name": "ChainLink Token",
            "address": "0x350a791bfc2c21f9ed5d10980dad2e2638ffa7f6"
        },
        "LRC": {
            "symbol": "LRC",
            "decimals": 18,
            "name": "LoopringCoin V2",
            "address": "0xfeaa9194f9f8c1b65429e31341a103071464907e"
        },
        "LUSD": {
            "symbol": "LUSD",
            "decimals": 18,
            "name": "LUSD Stablecoin",
            "address": "0xc40f949f8a4e094d1b49a23ea9241d289b7b2819"
        },
        "LYRA": {
            "symbol": "LYRA",
            "decimals": 18,
            "name": "Lyra Token",
            "address": "0x50c5725949a6f0c72e6c4a641f24049a917db0cb"
        },
        "MAI": {
            "symbol": "MAI",
            "decimals": 18,
            "name": "Mai Stablecoin",
            "address": "0xdfa46478f9e5ea86d57387849598dbfb2e964b02"
        },
        "MASK": {
            "symbol": "MASK",
            "decimals": 18,
            "name": "Mask Network",
            "address": "0x3390108e913824b8ead638444cc52b9abdf63798"
        },
        "MKR": {
            "symbol": "MKR",
            "decimals": 18,
            "name": "Maker",
            "address": "0xab7badef82e9fe11f6f33f87bc9bc2aa27f2fcb5"
        },
        "NFTE": {
            "symbol": "NFTE",
            "decimals": 18,
            "name": "NFTEarth",
            "address": "0xc96f4f893286137ac17e07ae7f217ffca5db3ab6"
        },
        "OP": {
            "symbol": "OP",
            "decimals": 18,
            "name": "Optimism",
            "address": "0x4200000000000000000000000000000000000042"
        },
        "OpenX": {
            "symbol": "OpenX",
            "decimals": 18,
            "name": "OpenX Optimism",
            "address": "0xc3864f98f2a61a7caeb95b039d031b4e2f55e0e9"
        },
        "OPX": {
            "symbol": "OPX",
            "decimals": 18,
            "name": "OPX",
            "address": "0xcdb4bb51801a1f399d4402c61bc098a72c382e65"
        },
        "PAPER": {
            "symbol": "PAPER",
            "decimals": 18,
            "name": "Paper",
            "address": "0x00f932f0fe257456b32deda4758922e56a4f4b42"
        },
        "PERP": {
            "symbol": "PERP",
            "decimals": 18,
            "name": "Perpetual",
            "address": "0x9e1028f5f1d5ede59748ffcee5532509976840e0"
        },
        "POP": {
            "symbol": "POP",
            "decimals": 18,
            "name": "Popcorn",
            "address": "0x6f0fecbc276de8fc69257065fe47c5a03d986394"
        },
        "PREMIA": {
            "symbol": "PREMIA",
            "decimals": 18,
            "name": "Premia",
            "address": "0x374ad0f47f4ca39c78e5cc54f1c9e426ff8f231a"
        },
        "RAI": {
            "symbol": "RAI",
            "decimals": 18,
            "name": "Rai Reflex Index",
            "address": "0x7fb688ccf682d58f86d7e38e03f9d22e7705448b"
        },
        "rETH": {
            "symbol": "rETH",
            "decimals": 18,
            "name": "Rocket Pool ETH",
            "address": "0x9bcef72be871e61ed4fbbc7630889bee758eb81d"
        },
        "RGT": {
            "symbol": "RGT",
            "decimals": 18,
            "name": "Rari Governance Token",
            "address": "0xb548f63d4405466b36c0c0ac3318a22fdcec711a"
        },
        "RILLA": {
            "symbol": "RILLA",
            "decimals": 18,
            "name": "Rilla",
            "address": "0x96d17e1301b31556e5e263389583a9331e6749e9"
        },
        "SARCO": {
            "symbol": "SARCO",
            "decimals": 18,
            "name": "Sarcophagus",
            "address": "0x7c6b91d9be155a6db01f749217d76ff02a7227f2"
        },
        "sETH": {
            "symbol": "sETH",
            "decimals": 18,
            "name": "Synth sETH",
            "address": "0xe405de8f52ba7559f9df3c368500b6e6ae6cee49"
        },
        "SNX": {
            "symbol": "SNX",
            "decimals": 18,
            "name": "Synthetix Network Token",
            "address": "0x8700daec35af8ff88c16bdf0418774cb3d7599b4"
        },
        "SONNE": {
            "symbol": "SONNE",
            "decimals": 18,
            "name": "Sonne",
            "address": "0x1db2466d9f5e10d7090e7152b68d62703a2245f0"
        },
        "sUSD": {
            "symbol": "sUSD",
            "decimals": 18,
            "name": "Synth sUSD",
            "address": "0x8c6f28f2f1a3c87f0f938b96d27520d9751ec8d9"
        },
        "SYN": {
            "symbol": "SYN",
            "decimals": 18,
            "name": "Synapse",
            "address": "0x5a5fff6f753d7c11a56a52fe47a177a87e431655"
        },
        "THALES": {
            "symbol": "THALES",
            "decimals": 18,
            "name": "Thales DAO Token",
            "address": "0x217d47011b23bb961eb6d93ca9945b7501a5bb11"
        },
        "UMA": {
            "symbol": "UMA",
            "decimals": 18,
            "name": "UMA Voting Token v1",
            "address": "0xe7798f023fc62146e8aa1b36da45fb70855a77ea"
        },
        "UNI": {
            "symbol": "UNI",
            "decimals": 18,
            "name": "Uniswap",
            "address": "0x6fd9d7ad17242c41f7131d257212c54a0e816691"
        },
        "USD+": {
            "symbol": "USD+",
            "decimals": 6,
            "name": "USD+",
            "address": "0x73cb180bf0521828d8849bc8cf2b920918e23032"
        },
        "USDC": {
            "symbol": "USDC",
            "decimals": 6,
            "name": "USD Coin",
            "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607"
        },
        "USDT": {
            "symbol": "USDT",
            "decimals": 6,
            "name": "Tether USD",
            "address": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58"
        },
        "USX": {
            "symbol": "USX",
            "decimals": 18,
            "name": "dForce USD",
            "address": "0xbfd291da8a403daaf7e5e9dc1ec0aceacd4848b9"
        },
        "VELO": {
            "symbol": "VELO",
            "decimals": 18,
            "name": "Velodrome",
            "address": "0x3c8b650257cfb5f272f799f5e2b4e65093a11a05"
        },
        "WBTC": {
            "symbol": "WBTC",
            "decimals": 8,
            "name": "Wrapped BTC",
            "address": "0x68f180fcce6836688e9084f035309e29bf0a2095"
        },
        "WETH": {
            "symbol": "WETH",
            "decimals": 18,
            "name": "Wrapped Ether",
            "address": "0x4200000000000000000000000000000000000006"
        },
        "wstETH": {
            "symbol": "wstETH",
            "decimals": 18,
            "name": "Wrapped liquid staked Ether 2.0",
            "address": "0x1f32b1c2345538c0c6f582fcb022739c4a194ebb"
        }
    },
    int(Network.Avalanche): {
        "1INCH.e": {
            "symbol": "1INCH.e",
            "decimals": 18,
            "name": "1INCH Token",
            "address": "0xd501281565bf7789224523144fe5d98e8b28f267"
        },
        "3ULL": {
            "symbol": "3ULL",
            "decimals": 18,
            "name": "3ULL v2",
            "address": "0x9e15f045e44ea5a80e7fbc193a35287712cc5569"
        },
        "AAVE.e": {
            "symbol": "AAVE.e",
            "decimals": 18,
            "name": "Aave Token",
            "address": "0x63a72806098bd3d9520cc43356dd78afe5d386d9"
        },
        "ACRE": {
            "symbol": "ACRE",
            "decimals": 18,
            "name": "Arable Protocol",
            "address": "0x00ee200df31b869a321b10400da10b561f3ee60d"
        },
        "AFINS": {
            "symbol": "AFINS",
            "decimals": 18,
            "name": "altFINS",
            "address": "0xb648fa7a5f5ed3b3c743140346e3dc3fe94a9125"
        },
        "AGF": {
            "symbol": "AGF",
            "decimals": 18,
            "name": "Augmented Finance",
            "address": "0xb67a9374da03d4114a6fb8f0e7f2b82b5cb34ee3"
        },
        "AHILL": {
            "symbol": "AHILL",
            "decimals": 18,
            "name": "Avalanche Hills",
            "address": "0x223174d9f096d8b468b24f620a02f43b70792789"
        },
        "AKITA": {
            "symbol": "AKITA",
            "decimals": 18,
            "name": "Akita Inu",
            "address": "0xcaf5191fc480f43e4df80106c7695eca56e48b18"
        },
        "AKITAX": {
            "symbol": "AKITAX",
            "decimals": 18,
            "name": "AKITAVAX",
            "address": "0xe06fba763c2104db5027f57f6a5be0a0d86308af"
        },
        "ALOT": {
            "symbol": "ALOT",
            "decimals": 18,
            "name": "Dexalot Token",
            "address": "0x093783055f9047c2bff99c4e414501f8a147bc69"
        },
        "Alpha": {
            "symbol": "Alpha",
            "decimals": 18,
            "name": "Alpha Shares",
            "address": "0x9c3254bb4f7f6a05a4aaf2cadce592c848d043c1"
        },
        "ALPHA.e": {
            "symbol": "ALPHA.e",
            "decimals": 18,
            "name": "AlphaToken",
            "address": "0x2147efff675e4a4ee1c2f918d181cdbd7a8e208f"
        },
        "AMPL": {
            "symbol": "AMPL",
            "decimals": 9,
            "name": "Ampleforth secured by Meter Passport",
            "address": "0x027dbca046ca156de9622cd1e2d907d375e53aa7"
        },
        "ANTG": {
            "symbol": "ANTG",
            "decimals": 18,
            "name": "AntGold",
            "address": "0xca1068444196cdfe676fd15a29f35e502580a69e"
        },
        "ANY": {
            "symbol": "ANY",
            "decimals": 18,
            "name": "Anyswap",
            "address": "0xb44a9b6905af7c801311e8f4e76932ee959c663c"
        },
        "APEIN": {
            "symbol": "APEIN",
            "decimals": 18,
            "name": "Ape In",
            "address": "0x938fe3788222a74924e062120e7bfac829c719fb"
        },
        "AVAT": {
            "symbol": "AVAT",
            "decimals": 6,
            "name": "AVAT",
            "address": "0x7086c48c997b8597a1692798155b4fcf2cee7f0f"
        },
        "AVXL": {
            "symbol": "AVXL",
            "decimals": 18,
            "name": "AvaXlauncher",
            "address": "0xbee994ad257dcc84672c0c6e6168a4701041f39f"
        },
        "AVXT": {
            "symbol": "AVXT",
            "decimals": 6,
            "name": "Avaxtars Token",
            "address": "0x397bbd6a0e41bdf4c3f971731e180db8ad06ebc1"
        },
        "aXEN": {
            "symbol": "aXEN",
            "decimals": 18,
            "name": "XEN Crypto",
            "address": "0xc0c5aa69dbe4d6dddfbc89c0957686ec60f24389"
        },
        "AXL": {
            "symbol": "AXL",
            "decimals": 6,
            "name": "Axelar",
            "address": "0x44c784266cf024a60e8acf2427b9857ace194c5d"
        },
        "BAT.e": {
            "symbol": "BAT.e",
            "decimals": 18,
            "name": "Basic Attention Token",
            "address": "0x98443b96ea4b0858fdf3219cd13e98c7a4690588"
        },
        "BAY": {
            "symbol": "BAY",
            "decimals": 18,
            "name": "BAYMAX",
            "address": "0x18706c65b12595edb43643214eacdb4f618dd166"
        },
        "BETA": {
            "symbol": "BETA",
            "decimals": 18,
            "name": "Beta Token",
            "address": "0x511d35c52a3c244e7b8bd92c0c297755fbd89212"
        },
        "BFG": {
            "symbol": "BFG",
            "decimals": 18,
            "name": "BattleForGiostone",
            "address": "0xfd538ca3f58dc309da55b11f007ff53fb4602876"
        },
        "BIFI": {
            "symbol": "BIFI",
            "decimals": 18,
            "name": "beefy.finance",
            "address": "0xd6070ae98b8069de6b494332d1a1a81b6179d960"
        },
        "BioFi": {
            "symbol": "BioFi",
            "decimals": 6,
            "name": "BioFi",
            "address": "0x9366d30feba284e62900f6295bc28c9906f33172"
        },
        "BLZZ": {
            "symbol": "BLZZ",
            "decimals": 18,
            "name": "Blizz.Finance Protocol Token",
            "address": "0x0f34919404a290e71fc6a510cb4a6acb8d764b24"
        },
        "BOG": {
            "symbol": "BOG",
            "decimals": 18,
            "name": "Bogged Finance",
            "address": "0xb09fe1613fe03e7361319d2a43edc17422f36b09"
        },
        "BOOFI": {
            "symbol": "BOOFI",
            "decimals": 18,
            "name": "Boo Finance Token",
            "address": "0xb00f1ad977a949a3ccc389ca1d1282a2946963b0"
        },
        "BPT": {
            "symbol": "BPT",
            "decimals": 18,
            "name": "Bold Point Token",
            "address": "0x1111111111182587795ef1098ac7da81a108c97a"
        },
        "BRIBE": {
            "symbol": "BRIBE",
            "decimals": 18,
            "name": "Police & Thief Game - BRIBE",
            "address": "0xce2fbed816e320258161ced52c2d0cebcdfd8136"
        },
        "BRO": {
            "symbol": "BRO",
            "decimals": 18,
            "name": "Bro Token",
            "address": "0x65031e28cb0e8cc21ae411f9dd22c9b1bd260ce4"
        },
        "BSGG": {
            "symbol": "BSGG",
            "decimals": 18,
            "name": "Betswap.gg",
            "address": "0x63682bdc5f875e9bf69e201550658492c9763f89"
        },
        "BTC": {
            "symbol": "BTC",
            "decimals": 8,
            "name": "Bitcoin",
            "address": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        },
        "BTC.b": {
            "symbol": "BTC.b",
            "decimals": 8,
            "name": "Bitcoin",
            "address": "0x152b9d0fdc40c096757f570a51e494bd4b943e50"
        },
        "BUSD": {
            "symbol": "BUSD",
            "decimals": 18,
            "name": "BUSD Token",
            "address": "0x9c9e5fd8bbc25984b178fdce6117defa39d2db39"
        },
        "BUSINESSES": {
            "symbol": "BUSINESSES",
            "decimals": 18,
            "name": "$BUSINESSES",
            "address": "0x15c841043e13ffaa9a99fabea236d40f45615623"
        },
        "CAI": {
            "symbol": "CAI",
            "decimals": 18,
            "name": "Colony Avalanche Index",
            "address": "0x48f88a3fe843ccb0b5003e70b4192c1d7448bef0"
        },
        "Cake": {
            "symbol": "Cake",
            "decimals": 18,
            "name": "PancakeSwap Token",
            "address": "0x98a4d09036cc5337810096b1d004109686e56afc"
        },
        "CCY": {
            "symbol": "CCY",
            "decimals": 18,
            "name": "ChoccyCoin",
            "address": "0xb723783e0f9015c8e20b87f6cf7ae24df6479e62"
        },
        "CHAM": {
            "symbol": "CHAM",
            "decimals": 18,
            "name": "Champion",
            "address": "0xc65bc1e906771e105fbacbd8dfe3862ee7be378e"
        },
        "CHRO": {
            "symbol": "CHRO",
            "decimals": 18,
            "name": "Chronicum",
            "address": "0xbf1230bb63bfd7f5d628ab7b543bcefa8a24b81b"
        },
        "CLY": {
            "symbol": "CLY",
            "decimals": 18,
            "name": "Colony Token",
            "address": "0xec3492a2508ddf4fdc0cd76f31f340b30d1793e6"
        },
        "COMP.e": {
            "symbol": "COMP.e",
            "decimals": 18,
            "name": "Compound",
            "address": "0xc3048e19e76cb9a3aa9d77d8c03c29fc906e2437"
        },
        "CRA": {
            "symbol": "CRA",
            "decimals": 18,
            "name": "CRA",
            "address": "0xa32608e873f9ddef944b24798db69d80bbb4d1ed"
        },
        "CRAFT": {
            "symbol": "CRAFT",
            "decimals": 18,
            "name": "CRAFT",
            "address": "0x8ae8be25c23833e0a01aa200403e826f611f9cd2"
        },
        "CRV.e": {
            "symbol": "CRV.e",
            "decimals": 18,
            "name": "Curve DAO Token",
            "address": "0x249848beca43ac405b8102ec90dd5f22ca513c06"
        },
        "CTSI": {
            "symbol": "CTSI",
            "decimals": 18,
            "name": "Cartesi Token",
            "address": "0x6b289cceaa8639e3831095d75a3e43520fabf552"
        },
        "CYCLE": {
            "symbol": "CYCLE",
            "decimals": 18,
            "name": "Cycle Token",
            "address": "0x81440c939f2c1e34fc7048e518a637205a632a74"
        },
        "DAI.e": {
            "symbol": "DAI.e",
            "decimals": 18,
            "name": "Dai Stablecoin",
            "address": "0xd586e7f844cea2f87f50152665bcbc2c279d8d70"
        },
        "DBY": {
            "symbol": "DBY",
            "decimals": 18,
            "name": "Metaderby token",
            "address": "0x5085434227ab73151fad2de546210cbc8663df96"
        },
        "DCAR": {
            "symbol": "DCAR",
            "decimals": 18,
            "name": "Dragon Crypto Argenti",
            "address": "0x250bdca7d1845cd543bb55e7d82dca24d48e9f0f"
        },
        "DCAU": {
            "symbol": "DCAU",
            "decimals": 18,
            "name": "Dragon Crypto Aurum",
            "address": "0x100cc3a819dd3e8573fd2e46d1e66ee866068f30"
        },
        "DEG": {
            "symbol": "DEG",
            "decimals": 18,
            "name": "DegisToken",
            "address": "0x9f285507ea5b4f33822ca7abb5ec8953ce37a645"
        },
        "DFIAT": {
            "symbol": "DFIAT",
            "decimals": 18,
            "name": "DeFiato [via ChainPort.io]",
            "address": "0xafe3d2a31231230875dee1fa1eef14a412443d22"
        },
        "DGNX": {
            "symbol": "DGNX",
            "decimals": 18,
            "name": "DegenX",
            "address": "0x51e48670098173025c477d9aa3f0eff7bf9f7812"
        },
        "DLQ": {
            "symbol": "DLQ",
            "decimals": 18,
            "name": "Deliq",
            "address": "0x50c72103940d419fb64448f258f7eabba784f84b"
        },
        "DON": {
            "symbol": "DON",
            "decimals": 18,
            "name": "Dogeon Token",
            "address": "0x1db749847c4abb991d8b6032102383e6bfd9b1c7"
        },
        "DYP": {
            "symbol": "DYP",
            "decimals": 18,
            "name": "DeFiYieldProtocol",
            "address": "0x961c8c0b1aad0c0b10a51fef6a867e3091bcef17"
        },
        "ECD": {
            "symbol": "ECD",
            "decimals": 18,
            "name": "Echidna Token",
            "address": "0xeb8343d5284caec921f035207ca94db6baaacbcd"
        },
        "EGG": {
            "symbol": "EGG",
            "decimals": 18,
            "name": "chikn egg",
            "address": "0x7761e2338b35bceb6bda6ce477ef012bde7ae611"
        },
        "ELK": {
            "symbol": "ELK",
            "decimals": 18,
            "name": "Elk",
            "address": "0xeeeeeb57642040be42185f49c52f7e9b38f8eeee"
        },
        "ETH": {
            "symbol": "ETH",
            "decimals": 18,
            "name": "Ethereum",
            "address": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
        },
        "EVO": {
            "symbol": "EVO",
            "decimals": 18,
            "name": "EVO",
            "address": "0x42006ab57701251b580bdfc24778c43c9ff589a1"
        },
        "FERT": {
            "symbol": "FERT",
            "decimals": 18,
            "name": "chikn fert",
            "address": "0x9c846d808a41328a209e235b5e3c4e626dab169e"
        },
        "FITFI": {
            "symbol": "FITFI",
            "decimals": 18,
            "name": "STEP.APP",
            "address": "0x714f020c54cc9d104b6f4f6998c63ce2a31d1888"
        },
        "FLY": {
            "symbol": "FLY",
            "decimals": 18,
            "name": "FLY",
            "address": "0x78ea3fef1c1f07348199bf44f45b803b9b0dbe28"
        },
        "FRAX": {
            "symbol": "FRAX",
            "decimals": 18,
            "name": "Frax",
            "address": "0xd24c2ad096400b6fbcd2ad8b24e7acbc21a1da64"
        },
        "FXS": {
            "symbol": "FXS",
            "decimals": 18,
            "name": "Frax Share",
            "address": "0x214db107654ff987ad859f34125307783fc8e387"
        },
        "GAJ": {
            "symbol": "GAJ",
            "decimals": 18,
            "name": "PolyGaj Token",
            "address": "0x595c8481c48894771ce8fade54ac6bf59093f9e8"
        },
        "GAU": {
            "symbol": "GAU",
            "decimals": 18,
            "name": "GAU Token",
            "address": "0xca8ebfb8e1460aaac7c272cb9053b3d42412aac2"
        },
        "GB": {
            "symbol": "GB",
            "decimals": 9,
            "name": "Good Bridging",
            "address": "0x90842eb834cfd2a1db0b1512b254a18e4d396215"
        },
        "GENI": {
            "symbol": "GENI",
            "decimals": 9,
            "name": "Genius",
            "address": "0x444444444444c1a66f394025ac839a535246fcc8"
        },
        "GM": {
            "symbol": "GM",
            "decimals": 8,
            "name": "GhostMarket Token",
            "address": "0x0b53b5da7d0f275c31a6a182622bdf02474af253"
        },
        "GMX": {
            "symbol": "GMX",
            "decimals": 18,
            "name": "GMX",
            "address": "0x62edc0692bd897d2295872a9ffcac5425011c661"
        },
        "gOHM": {
            "symbol": "gOHM",
            "decimals": 18,
            "name": "Governance OHM",
            "address": "0x321e7092a180bb43555132ec53aaa65a5bf84251"
        },
        "GRAPE": {
            "symbol": "GRAPE",
            "decimals": 18,
            "name": "Grape Finance",
            "address": "0x5541d83efad1f281571b343977648b75d95cdac2"
        },
        "GRO": {
            "symbol": "GRO",
            "decimals": 18,
            "name": "Growth-Peg Token",
            "address": "0x72699ba15cc734f8db874fa9652c8de12093f187"
        },
        "GRT.e": {
            "symbol": "GRT.e",
            "decimals": 18,
            "name": "Graph Token",
            "address": "0x8a0cac13c7da965a312f08ea4229c37869e85cb9"
        },
        "GTON": {
            "symbol": "GTON",
            "decimals": 18,
            "name": "Graviton",
            "address": "0x4e720dd3ac5cfe1e1fbde4935f386bb1c66f4642"
        },
        "GVILLE": {
            "symbol": "GVILLE",
            "decimals": 18,
            "name": "Grantsville",
            "address": "0x7c22e823b5ee641ed534ce3e368b59b5f0a3b7e0"
        },
        "HCT": {
            "symbol": "HCT",
            "decimals": 18,
            "name": "Hurricane Token",
            "address": "0x45c13620b55c35a5f539d26e88247011eb10fdbd"
        },
        "HeC": {
            "symbol": "HeC",
            "decimals": 18,
            "name": "HeroesChained",
            "address": "0xc7f4debc8072e23fe9259a5c0398326d8efb7f5c"
        },
        "HON": {
            "symbol": "HON",
            "decimals": 18,
            "name": "HonToken",
            "address": "0xed2b42d3c9c6e97e11755bb37df29b6375ede3eb"
        },
        "HOOF": {
            "symbol": "HOOF",
            "decimals": 18,
            "name": "Metaderby game token",
            "address": "0xe0bb6fed446a2dbb27f84d3c27c4ed8ea7603366"
        },
        "HOTCROSS": {
            "symbol": "HOTCROSS",
            "decimals": 18,
            "name": "Hot Cross Token",
            "address": "0x2f86508f41310d8d974b76deb3d246c0caa71cf5"
        },
        "HUSKY": {
            "symbol": "HUSKY",
            "decimals": 18,
            "name": "Husky",
            "address": "0x65378b697853568da9ff8eab60c13e1ee9f4a654"
        },
        "IDIA": {
            "symbol": "IDIA",
            "decimals": 18,
            "name": "Impossible Decentralized Incubator Access Token",
            "address": "0xfcaf13227dcbfa2dc2b1928acfca03b85e2d25dd"
        },
        "iDYP": {
            "symbol": "iDYP",
            "decimals": 18,
            "name": "iDeFiYieldProtocol",
            "address": "0xbd100d061e120b2c67a24453cf6368e63f1be056"
        },
        "IME": {
            "symbol": "IME",
            "decimals": 18,
            "name": "Imperium Empires Token",
            "address": "0xf891214fdcf9cdaa5fdc42369ee4f27f226adad6"
        },
        "INSUR": {
            "symbol": "INSUR",
            "decimals": 18,
            "name": "Avalanche INSUR Token",
            "address": "0x544c42fbb96b39b21df61cf322b5edc285ee7429"
        },
        "ISA": {
            "symbol": "ISA",
            "decimals": 18,
            "name": "Islander",
            "address": "0x3eefb18003d033661f84e48360ebecd181a84709"
        },
        "JNS": {
            "symbol": "JNS",
            "decimals": 18,
            "name": "Janus Network",
            "address": "0x7a023a408f51c23760eb31190fc731bc12b52954"
        },
        "JOE": {
            "symbol": "JOE",
            "decimals": 18,
            "name": "JoeToken",
            "address": "0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd"
        },
        "JPYC": {
            "symbol": "JPYC",
            "decimals": 18,
            "name": "JPY Coin",
            "address": "0x431d5dff03120afa4bdf332c61a6e1766ef37bdb"
        },
        "KACY": {
            "symbol": "KACY",
            "decimals": 18,
            "name": "Kassandra",
            "address": "0xf32398dae246c5f672b52a54e9b413dffcae1a44"
        },
        "KLO": {
            "symbol": "KLO",
            "decimals": 18,
            "name": "Kalao Token",
            "address": "0xb27c8941a7df8958a1778c0259f76d1f8b711c35"
        },
        "KNC": {
            "symbol": "KNC",
            "decimals": 18,
            "name": "Kyber Network Crystal v2",
            "address": "0x39fc9e94caeacb435842fadedecb783589f50f5f"
        },
        "KTE": {
            "symbol": "KTE",
            "decimals": 18,
            "name": "KyteOne",
            "address": "0x056d114ff1e01de3bca30f0efa3655df42880e5b"
        },
        "LINK.e": {
            "symbol": "LINK.e",
            "decimals": 18,
            "name": "Chainlink Token",
            "address": "0x5947bb275c521040051d82396192181b413227a3"
        },
        "LIQR": {
            "symbol": "LIQR",
            "decimals": 18,
            "name": "LIQR",
            "address": "0x33333ee26a7d02e41c33828b42fb1e0889143477"
        },
        "LOST": {
            "symbol": "LOST",
            "decimals": 18,
            "name": "LostToken",
            "address": "0x449674b82f05d498e126dd6615a1057a9c088f2c"
        },
        "LUNA": {
            "symbol": "LUNA",
            "decimals": 6,
            "name": "LUNA",
            "address": "0x70928e5b188def72817b7775f0bf6325968e563b"
        },
        "LYD": {
            "symbol": "LYD",
            "decimals": 18,
            "name": "LydiaFinance Token",
            "address": "0x4c9b4e1ac6f24cde3660d5e4ef1ebf77c710c084"
        },
        "MAGE": {
            "symbol": "MAGE",
            "decimals": 18,
            "name": "MetaBrands",
            "address": "0x921f99719eb6c01b4b8f0ba7973a7c24891e740a"
        },
        "MATIC": {
            "symbol": "MATIC",
            "decimals": 18,
            "name": "Matic Token",
            "address": "0xa56b1b9f4e5a1a1e0868f5fd4352ce7cdf0c2a4f"
        },
        "METAG": {
            "symbol": "METAG",
            "decimals": 18,
            "name": "METAG",
            "address": "0x2b0b320b47d8e0dd0e4477cf90c307c7ed984ad2"
        },
        "MIM": {
            "symbol": "MIM",
            "decimals": 18,
            "name": "Magic Internet Money",
            "address": "0x130966628846bfd36ff31a822705796e8cb8c18d"
        },
        "miMatic": {
            "symbol": "miMatic",
            "decimals": 18,
            "name": "MAI",
            "address": "0x3b55e45fd6bd7d4724f5c47e0d1bcaedd059263e"
        },
        "MIND+": {
            "symbol": "MIND+",
            "decimals": 18,
            "name": "MIND+",
            "address": "0x92876c3a3e2b0788c841587a14989392a555bffe"
        },
        "MKR.e": {
            "symbol": "MKR.e",
            "decimals": 18,
            "name": "Maker",
            "address": "0x88128fd4b259552a9a1d457f435a6527aab72d42"
        },
        "MONEY": {
            "symbol": "MONEY",
            "decimals": 18,
            "name": "Moremoney USD",
            "address": "0x0f577433bf59560ef2a79c124e9ff99fca258948"
        },
        "MOR": {
            "symbol": "MOR",
            "decimals": 18,
            "name": "Mor Stablecoin",
            "address": "0x87bade473ea0513d4aa7085484aeaa6cb6ebe7e3"
        },
        "MORE": {
            "symbol": "MORE",
            "decimals": 18,
            "name": "More Token",
            "address": "0xd9d90f882cddd6063959a9d837b05cb748718a05"
        },
        "MU": {
            "symbol": "MU",
            "decimals": 18,
            "name": "Mu Coin",
            "address": "0xd036414fa2bcbb802691491e323bff1348c5f4ba"
        },
        "MULTI": {
            "symbol": "MULTI",
            "decimals": 18,
            "name": "Multichain",
            "address": "0x9fb9a33956351cf4fa040f65a13b835a3c8764e3"
        },
        "ncash": {
            "symbol": "ncash",
            "decimals": 18,
            "name": "NitroNetwork",
            "address": "0xc69eba65e87889f0805db717af06797055a0ba07"
        },
        "NEWO": {
            "symbol": "NEWO",
            "decimals": 18,
            "name": "New Order",
            "address": "0x4bfc90322dd638f81f034517359bd447f8e0235a"
        },
        "NHCT": {
            "symbol": "NHCT",
            "decimals": 18,
            "name": "Hurricane NFT Token",
            "address": "0x3ce2fcec09879af073b53bef5f4d04327a1bc032"
        },
        "NNT": {
            "symbol": "NNT",
            "decimals": 18,
            "name": "NunuToken",
            "address": "0x771c01e1917b5ab5b791f7b96f0cd69e22f6dbcf"
        },
        "NXRA": {
            "symbol": "NXRA",
            "decimals": 18,
            "name": "AllianceBlock Nexera Token",
            "address": "0x644192291cc835a93d6330b24ea5f5fedd0eef9e"
        },
        "ODDZ": {
            "symbol": "ODDZ",
            "decimals": 18,
            "name": "OddzToken",
            "address": "0xb0a6e056b587d0a85640b39b1cb44086f7a26a1e"
        },
        "OH": {
            "symbol": "OH",
            "decimals": 18,
            "name": "Oh! Finance",
            "address": "0x937e077abaea52d3abf879c9b9d3f2ebd15baa21"
        },
        "OKSE": {
            "symbol": "OKSE",
            "decimals": 18,
            "name": "Okse",
            "address": "0xbc7b0223dd16cbc679c0d04ba3f4530d76dfba87"
        },
        "OLIVE": {
            "symbol": "OLIVE",
            "decimals": 18,
            "name": "OliveCash Token",
            "address": "0x617724974218a18769020a70162165a539c07e8a"
        },
        "ORBIT": {
            "symbol": "ORBIT",
            "decimals": 18,
            "name": "Europa Token",
            "address": "0x340990358ae38008181b6db6156d9021a2d425da"
        },
        "ORCA": {
            "symbol": "ORCA",
            "decimals": 18,
            "name": "OrcaDAO",
            "address": "0x8b1d98a91f853218ddbb066f20b8c63e782e2430"
        },
        "pAVAX": {
            "symbol": "pAVAX",
            "decimals": 18,
            "name": "pAVAX",
            "address": "0x6ca558bd3eab53da1b25ab97916dd14bf6cfee4e"
        },
        "PEFI": {
            "symbol": "PEFI",
            "decimals": 18,
            "name": "PenguinToken",
            "address": "0xe896cdeaac9615145c0ca09c8cd5c25bced6384c"
        },
        "PERA": {
            "symbol": "PERA",
            "decimals": 18,
            "name": "Pera Finance",
            "address": "0xfda866cfece71f4c17b4a5e5f9a00ac08c72eadc"
        },
        "PIGGY": {
            "symbol": "PIGGY",
            "decimals": 18,
            "name": "PIGGY",
            "address": "0x1a877b68bda77d78eea607443ccde667b31b0cdf"
        },
        "PIZZA": {
            "symbol": "PIZZA",
            "decimals": 18,
            "name": "Pizza",
            "address": "0x6121191018baf067c6dc6b18d42329447a164f05"
        },
        "PLN": {
            "symbol": "PLN",
            "decimals": 18,
            "name": "Pollen",
            "address": "0x7b2b702706d9b361dfe3f00bd138c0cfda7fb2cf"
        },
        "PNG": {
            "symbol": "PNG",
            "decimals": 18,
            "name": "Pangolin",
            "address": "0x60781c2586d68229fde47564546784ab3faca982"
        },
        "POLAR": {
            "symbol": "POLAR",
            "decimals": 18,
            "name": "POLAR",
            "address": "0x6c1c0319d8ddcb0ffe1a68c5b3829fd361587db4"
        },
        "PTP": {
            "symbol": "PTP",
            "decimals": 18,
            "name": "Platypus",
            "address": "0x22d4002028f537599be9f666d1c4fa138522f9c8"
        },
        "QI": {
            "symbol": "QI",
            "decimals": 18,
            "name": "BENQI",
            "address": "0x8729438eb15e2c8b576fcc6aecda6a148776c0f5"
        },
        "RADIO": {
            "symbol": "RADIO",
            "decimals": 18,
            "name": "RadioShack Token",
            "address": "0x02bfd11499847003de5f0f5aa081c43854d48815"
        },
        "RAI": {
            "symbol": "RAI",
            "decimals": 18,
            "name": "Rai Reflex Index",
            "address": "0x97cd1cfe2ed5712660bb6c14053c0ecb031bff7d"
        },
        "RELAY": {
            "symbol": "RELAY",
            "decimals": 18,
            "name": "Relay Token",
            "address": "0x78c42324016cd91d1827924711563fb66e33a83a"
        },
        "RISE": {
            "symbol": "RISE",
            "decimals": 18,
            "name": "EverRise",
            "address": "0xc17c30e98541188614df99239cabd40280810ca3"
        },
        "rloop": {
            "symbol": "rloop",
            "decimals": 18,
            "name": "rLoop",
            "address": "0x822b906e74d493d07223cf6858620ccda66b2154"
        },
        "ROCO": {
            "symbol": "ROCO",
            "decimals": 18,
            "name": "ROCO",
            "address": "0xb2a85c5ecea99187a977ac34303b80acbddfa208"
        },
        "ROY": {
            "symbol": "ROY",
            "decimals": 18,
            "name": "Royale",
            "address": "0x68ee0d0aad9e1984af85ca224117e4d20eaf68be"
        },
        "RUX": {
            "symbol": "RUX",
            "decimals": 18,
            "name": "RunBlox Token",
            "address": "0xa1afcc973d44ce1c65a21d9e644cb82489d26503"
        },
        "sAVAX": {
            "symbol": "sAVAX",
            "decimals": 18,
            "name": "Staked AVAX",
            "address": "0x2b2c81e08f1af8835a78bb2a90ae924ace0ea4be"
        },
        "SB": {
            "symbol": "SB",
            "decimals": 9,
            "name": "Snowbank",
            "address": "0x7d1232b90d3f809a54eeaeebc639c62df8a8942f"
        },
        "sifu": {
            "symbol": "sifu",
            "decimals": 18,
            "name": "Sifu",
            "address": "0x237917e8a998b37759c8ee2faa529d60c66c2927"
        },
        "SLIME": {
            "symbol": "SLIME",
            "decimals": 18,
            "name": "Snail Trail",
            "address": "0x5a15bdcf9a3a8e799fa4381e666466a516f2d9c8"
        },
        "SLOT": {
            "symbol": "SLOT",
            "decimals": 18,
            "name": "Snowtomb Lot",
            "address": "0x924157b5dbb387a823719916b25256410a4ad470"
        },
        "SMRTr": {
            "symbol": "SMRTr",
            "decimals": 18,
            "name": "SmarterCoin",
            "address": "0x6d923f688c7ff287dc3a5943caeefc994f97b290"
        },
        "SNOB": {
            "symbol": "SNOB",
            "decimals": 18,
            "name": "Snowball",
            "address": "0xc38f41a296a4493ff429f1238e030924a1542e50"
        },
        "SNX.e": {
            "symbol": "SNX.e",
            "decimals": 18,
            "name": "Synthetix Network Token",
            "address": "0xbec243c995409e6520d7c41e404da5deba4b209b"
        },
        "SOL": {
            "symbol": "SOL",
            "decimals": 9,
            "name": "Wrapped SOL",
            "address": "0xfe6b19286885a4f7f55adad09c3cd1f906d2478f"
        },
        "SPELL": {
            "symbol": "SPELL",
            "decimals": 18,
            "name": "Spell Token",
            "address": "0xce1bffbd5374dac86a2893119683f4911a2f7814"
        },
        "START": {
            "symbol": "START",
            "decimals": 18,
            "name": "BSCstarter",
            "address": "0xf44fb887334fa17d2c5c0f970b5d320ab53ed557"
        },
        "STEAK": {
            "symbol": "STEAK",
            "decimals": 18,
            "name": "STEAK",
            "address": "0xb279f8dd152b99ec1d84a489d32c35bc0c7f5674"
        },
        "STG": {
            "symbol": "STG",
            "decimals": 18,
            "name": "StargateToken",
            "address": "0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590"
        },
        "STOMB": {
            "symbol": "STOMB",
            "decimals": 18,
            "name": "Snowtomb Token",
            "address": "0x9e6832d13b29d0b1c1c3465242681039b31c7a05"
        },
        "STORM": {
            "symbol": "STORM",
            "decimals": 18,
            "name": " STORM Token",
            "address": "0x6afd5a1ea4b793cc1526d6dc7e99a608b356ef7b"
        },
        "SURE": {
            "symbol": "SURE",
            "decimals": 18,
            "name": "inSure",
            "address": "0x5fc17416925789e0852fbfcd81c490ca4abc51f9"
        },
        "SUSHI.e": {
            "symbol": "SUSHI.e",
            "decimals": 18,
            "name": "SushiToken",
            "address": "0x37b608519f91f70f2eeb0e5ed9af4061722e4f76"
        },
        "SYN": {
            "symbol": "SYN",
            "decimals": 18,
            "name": "Synapse",
            "address": "0x1f1e7c893855525b303f99bdf5c3c05be09ca251"
        },
        "TAZOR": {
            "symbol": "TAZOR",
            "decimals": 9,
            "name": "TAZOR",
            "address": "0xee65d8b88f86ace0f7ba42ba2d2c679b6f604bf0"
        },
        "THOR": {
            "symbol": "THOR",
            "decimals": 18,
            "name": "THOR v2",
            "address": "0x8f47416cae600bccf9530e9f3aeaa06bdd1caa79"
        },
        "TIME": {
            "symbol": "TIME",
            "decimals": 9,
            "name": "Time",
            "address": "0xb54f16fb19478766a268f172c9480f8da1a7c9c3"
        },
        "TRYB": {
            "symbol": "TRYB",
            "decimals": 6,
            "name": "BiLira",
            "address": "0x564a341df6c126f90cf3ecb92120fd7190acb401"
        },
        "TSD": {
            "symbol": "TSD",
            "decimals": 18,
            "name": "TSD Stablecoin",
            "address": "0x4fbf0429599460d327bd5f55625e30e4fc066095"
        },
        "TUNDRA": {
            "symbol": "TUNDRA",
            "decimals": 18,
            "name": "TUNDRAToken",
            "address": "0x21c5402c3b7d40c89cc472c9df5dd7e51bbab1b1"
        },
        "TUS": {
            "symbol": "TUS",
            "decimals": 18,
            "name": "Treasure Under Sea",
            "address": "0xf693248f96fe03422fea95ac0afbbbc4a8fdd172"
        },
        "TUSD": {
            "symbol": "TUSD",
            "decimals": 18,
            "name": "TrueUSD",
            "address": "0x1c20e891bab6b1727d14da358fae2984ed9b59eb"
        },
        "UFARM": {
            "symbol": "UFARM",
            "decimals": 18,
            "name": "UNIFARM Token",
            "address": "0xd60effed653f3f1b69047f2d2dc4e808a548767b"
        },
        "UMA.e": {
            "symbol": "UMA.e",
            "decimals": 18,
            "name": "UMA Voting Token v1",
            "address": "0x3bd2b1c7ed8d396dbb98ded3aebb41350a5b2339"
        },
        "UNI.e": {
            "symbol": "UNI.e",
            "decimals": 18,
            "name": "Uniswap",
            "address": "0x8ebaf22b6f053dffeaf46f4dd9efa95d89ba8580"
        },
        "USD+": {
            "symbol": "USD+",
            "decimals": 6,
            "name": "USD+",
            "address": "0xe80772eaf6e2e18b651f160bc9158b2a5cafca65"
        },
        "USDC": {
            "symbol": "USDC",
            "decimals": 6,
            "name": "USD Coin",
            "address": "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e"
        },
        "USDC.e": {
            "symbol": "USDC.e",
            "decimals": 6,
            "name": "USD Coin",
            "address": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664"
        },
        "USDt": {
            "symbol": "USDt",
            "decimals": 6,
            "name": "TetherToken",
            "address": "0x9702230a8ea53601f5cd2dc00fdbc13d4df4a8c7"
        },
        "USDT.e": {
            "symbol": "USDT.e",
            "decimals": 6,
            "name": "Tether USD",
            "address": "0xc7198437980c041c805a1edcba50c1ce5db95118"
        },
        "UST": {
            "symbol": "UST",
            "decimals": 6,
            "name": "UST",
            "address": "0xb599c3590f42f8f995ecfa0f85d2980b76862fc1"
        },
        "VEE": {
            "symbol": "VEE",
            "decimals": 18,
            "name": "Vee",
            "address": "0x3709e8615e02c15b096f8a9b460ccb8ca8194e86"
        },
        "VPND": {
            "symbol": "VPND",
            "decimals": 18,
            "name": "VaporNodes",
            "address": "0x83a283641c6b4df383bcddf807193284c84c5342"
        },
        "VSO": {
            "symbol": "VSO",
            "decimals": 18,
            "name": "VersoToken",
            "address": "0x846d50248baf8b7ceaa9d9b53bfd12d7d7fbb25a"
        },
        "VTX": {
            "symbol": "VTX",
            "decimals": 18,
            "name": "Vector",
            "address": "0x5817d4f0b62a59b17f75207da1848c2ce75e7af4"
        },
        "WAVAX": {
            "symbol": "WAVAX",
            "decimals": 18,
            "name": "Wrapped AVAX",
            "address": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"
        },
        "WBNB": {
            "symbol": "WBNB",
            "decimals": 18,
            "name": "Wrapped BNB",
            "address": "0x442f7f22b1ee2c842beaff52880d4573e9201158"
        },
        "WBTC.e": {
            "symbol": "WBTC.e",
            "decimals": 8,
            "name": "Wrapped BTC",
            "address": "0x50b7545627a5162f82a992c33b87adc75187b218"
        },
        "WETH": {
            "symbol": "WETH",
            "decimals": 18,
            "name": "Wrapped Ether",
            "address": "0x8b82a291f83ca07af22120aba21632088fc92931"
        },
        "WETH.e": {
            "symbol": "WETH.e",
            "decimals": 18,
            "name": "Wrapped Ether",
            "address": "0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab"
        },
        "WINE": {
            "symbol": "WINE",
            "decimals": 18,
            "name": "Wine Shares",
            "address": "0xc55036b5348cfb45a932481744645985010d3a44"
        },
        "WMATIC": {
            "symbol": "WMATIC",
            "decimals": 18,
            "name": "Wrapped Matic",
            "address": "0xf2f13f0b7008ab2fa4a2418f4ccc3684e49d20eb"
        },
        "wMEMO": {
            "symbol": "wMEMO",
            "decimals": 18,
            "name": "Wrapped MEMO",
            "address": "0x0da67235dd5787d67955420c84ca1cecd4e5bb3b"
        },
        "WOO.e": {
            "symbol": "WOO.e",
            "decimals": 18,
            "name": "Wootrade Network",
            "address": "0xabc9547b534519ff73921b1fba6e672b5f58d083"
        },
        "WORM": {
            "symbol": "WORM",
            "decimals": 18,
            "name": "chikn worm",
            "address": "0x79ba10485ae46a9436d560d9664369176ec2eb2b"
        },
        "WOW": {
            "symbol": "WOW",
            "decimals": 18,
            "name": "WOWswap",
            "address": "0xa384bc7cdc0a93e686da9e7b8c0807cd040f4e0b"
        },
        "WTF": {
            "symbol": "WTF",
            "decimals": 18,
            "name": "Waterfall Governance Token",
            "address": "0x873801ae2ff12d816db9a7b082f5796bec64c82c"
        },
        "WTR": {
            "symbol": "WTR",
            "decimals": 18,
            "name": "Deepwaters",
            "address": "0xd05b010eddb2dc65d5bd5a1389330d475049a4d5"
        },
        "WXT": {
            "symbol": "WXT",
            "decimals": 18,
            "name": "Wirex Token",
            "address": "0xfcde4a87b8b6fa58326bb462882f1778158b02f1"
        },
        "XAVA": {
            "symbol": "XAVA",
            "decimals": 18,
            "name": "Avalaunch",
            "address": "0xd1c3f94de7e5b45fa4edbba472491a9f4b166fc4"
        },
        "YAK": {
            "symbol": "YAK",
            "decimals": 18,
            "name": "Yak Token",
            "address": "0x59414b3089ce2af0010e7523dea7e2b35d776ec7"
        },
        "YAY": {
            "symbol": "YAY",
            "decimals": 18,
            "name": "YAY Games",
            "address": "0x01c2086facfd7aa38f69a6bd8c91bef3bb5adfca"
        },
        "YETI": {
            "symbol": "YETI",
            "decimals": 18,
            "name": "Yeti Finance",
            "address": "0x77777777777d4554c39223c354a05825b2e8faa3"
        },
        "YFI.e": {
            "symbol": "YFI.e",
            "decimals": 18,
            "name": "yearn.finance",
            "address": "0x9eaac1b23d935365bd7b542fe22ceee2922f52dc"
        },
        "YUSD": {
            "symbol": "YUSD",
            "decimals": 18,
            "name": "YUSD Stablecoin",
            "address": "0x111111111111ed1d73f860f57b2798b683f2d325"
        },
        "yyAVAX": {
            "symbol": "yyAVAX",
            "decimals": 18,
            "name": "YieldYak gAVAX",
            "address": "0xf7d9281e8e363584973f946201b82ba72c965d27"
        },
        "ZOO": {
            "symbol": "ZOO",
            "decimals": 18,
            "name": "ZooToken",
            "address": "0x1b88d7ad51626044ec62ef9803ea264da4442f32"
        },
        "ZRX.e": {
            "symbol": "ZRX.e",
            "decimals": 18,
            "name": "ZRX",
            "address": "0x596fa47043f99a4e0f122243b841e55375cde0d2"
        }
    },
    int(Network.Fantom): {
        "1ART": {
            "symbol": "1ART",
            "decimals": 18,
            "name": "ArtWallet",
            "address": "0xd3c325848d7c6e29b574cb0789998b2ff901f17e"
        },
        "2OMB": {
            "symbol": "2OMB",
            "decimals": 18,
            "name": "2omb Token",
            "address": "0x7a6e4e3cc2ac9924605dca4ba31d1831c84b44ae"
        },
        "2SHARES": {
            "symbol": "2SHARES",
            "decimals": 18,
            "name": "2SHARE Token",
            "address": "0xc54a1684fd1bef1f077a336e6be4bd9a3096a6ca"
        },
        "AAVE": {
            "symbol": "AAVE",
            "decimals": 18,
            "name": "Aave",
            "address": "0x6a07a792ab2965c72a5b8088d3a069a7ac3a993b"
        },
        "ALM": {
            "symbol": "ALM",
            "decimals": 18,
            "name": "AliumToken on Fantom",
            "address": "0x38540b4613d2e57ecf190d3486ae6f74591eb8a9"
        },
        "ALPACA": {
            "symbol": "ALPACA",
            "decimals": 18,
            "name": "AlpacaToken",
            "address": "0xad996a45fd2373ed0b10efa4a8ecb9de445a4302"
        },
        "ANY": {
            "symbol": "ANY",
            "decimals": 18,
            "name": "Anyswap",
            "address": "0xddcb3ffd12750b45d32e084887fdf1aabab34239"
        },
        "anyFSN": {
            "symbol": "anyFSN",
            "decimals": 18,
            "name": "Fusion",
            "address": "0x50eb82cc284e3d35936827023b048106aaecfc5f"
        },
        "AVAX": {
            "symbol": "AVAX",
            "decimals": 18,
            "name": "Avalanche",
            "address": "0x511d35c52a3c244e7b8bd92c0c297755fbd89212"
        },
        "AXL": {
            "symbol": "AXL",
            "decimals": 6,
            "name": "Axelar",
            "address": "0x8b1f4432f943c465a973fedc6d7aa50fc96f1f65"
        },
        "BAND": {
            "symbol": "BAND",
            "decimals": 18,
            "name": "Band",
            "address": "0x46e7628e8b4350b2716ab470ee0ba1fa9e76c6c5"
        },
        "BASED": {
            "symbol": "BASED",
            "decimals": 18,
            "name": "BASED",
            "address": "0x8d7d3409881b51466b483b11ea1b8a03cded89ae"
        },
        "BEETS": {
            "symbol": "BEETS",
            "decimals": 18,
            "name": "BeethovenxToken",
            "address": "0xf24bcf4d1e507740041c9cfd2dddb29585adce1e"
        },
        "BIFI": {
            "symbol": "BIFI",
            "decimals": 18,
            "name": "Beefy.Finance",
            "address": "0xd6070ae98b8069de6b494332d1a1a81b6179d960"
        },
        "binSPIRIT": {
            "symbol": "binSPIRIT",
            "decimals": 18,
            "name": "binSPIRIT",
            "address": "0x44e314190d9e4ce6d4c0903459204f8e21ff940a"
        },
        "BNB": {
            "symbol": "BNB",
            "decimals": 18,
            "name": "Binance",
            "address": "0xd67de0e0a0fd7b15dc8348bb9be742f3c5850454"
        },
        "BOO": {
            "symbol": "BOO",
            "decimals": 18,
            "name": "SpookyToken",
            "address": "0x841fad6eae12c286d1fd18d1d525dffa75c7effe"
        },
        "BRIDGE": {
            "symbol": "BRIDGE",
            "decimals": 18,
            "name": "Cross-Chain Bridge Token",
            "address": "0x92868a5255c628da08f550a858a802f5351c5223"
        },
        "BRO": {
            "symbol": "BRO",
            "decimals": 18,
            "name": "DexBrowser",
            "address": "0x230576a0455d7ae33c6defe64182c0bb68bafaf3"
        },
        "BRUSH": {
            "symbol": "BRUSH",
            "decimals": 18,
            "name": "PaintSwap Token",
            "address": "0x85dec8c4b2680793661bca91a8f129607571863d"
        },
        "BSGG": {
            "symbol": "BSGG",
            "decimals": 18,
            "name": "Betswap.gg",
            "address": "0x5a33869045db8a6a16c9f351293501cfd92cf7ed"
        },
        "BTC": {
            "symbol": "BTC",
            "decimals": 8,
            "name": "Bitcoin",
            "address": "0x321162cd933e2be498cd2267a90534a804051b11"
        },
        "CHARM": {
            "symbol": "CHARM",
            "decimals": 18,
            "name": "Charm Token",
            "address": "0x248cb87dda803028dfead98101c9465a2fbda0d4"
        },
        "CODE7": {
            "symbol": "CODE7",
            "decimals": 18,
            "name": "Code7 Finance",
            "address": "0xf77864fcffec4598813e3378681c9330b771ca88"
        },
        "CONK": {
            "symbol": "CONK",
            "decimals": 18,
            "name": "ShibaPoconkToken",
            "address": "0xb715f8dce2f0e9b894c753711bd55ee3c04dca4e"
        },
        "COVAL": {
            "symbol": "COVAL",
            "decimals": 8,
            "name": "Circuits of Value V2",
            "address": "0x8b8407c6184f1f0fd1082e83d6a3b8349caced12"
        },
        "COVER": {
            "symbol": "COVER",
            "decimals": 18,
            "name": "Cover Protocol Governance",
            "address": "0xb01e8419d842beebf1b70a7b5f7142abbaf7159d"
        },
        "CREAM": {
            "symbol": "CREAM",
            "decimals": 18,
            "name": "Cream",
            "address": "0x657a1861c15a3ded9af0b6799a195a249ebdcbc6"
        },
        "CRIME": {
            "symbol": "CRIME",
            "decimals": 18,
            "name": "CrimeGold",
            "address": "0xf378f05a51868c29d94f57e4240d7423cb526083"
        },
        "CRV": {
            "symbol": "CRV",
            "decimals": 18,
            "name": "Curve DAO",
            "address": "0x1e4f97b9f9f913c46f1632781732927b9019c68b"
        },
        "DAI": {
            "symbol": "DAI",
            "decimals": 18,
            "name": "Dai Stablecoin",
            "address": "0x8d11ec38a3eb5e956b052f67da8bdc9bef8abf3e"
        },
        "DARKO": {
            "symbol": "DARKO",
            "decimals": 18,
            "name": "Dark Opera",
            "address": "0x274b7eb297615ce21a1cd5b920f867389a367a8a"
        },
        "DEUS": {
            "symbol": "DEUS",
            "decimals": 18,
            "name": "DEUS",
            "address": "0xde5ed76e7c05ec5e4572cfc88d1acea165109e44"
        },
        "DEVIL": {
            "symbol": "DEVIL",
            "decimals": 18,
            "name": "DEVIL Token",
            "address": "0x174c7106aeecdc11389f7dd21342f05f46ccb40f"
        },
        "DOLA": {
            "symbol": "DOLA",
            "decimals": 18,
            "name": "Dola USD Stablecoin",
            "address": "0x3129662808bec728a27ab6a6b9afd3cbaca8a43c"
        },
        "DP": {
            "symbol": "DP",
            "decimals": 18,
            "name": "Dark Planet",
            "address": "0x08b1c9a96c663ee1e0cd7029f13aced7dcf5e373"
        },
        "DSHARE": {
            "symbol": "DSHARE",
            "decimals": 18,
            "name": "DSHARE",
            "address": "0x6e209329a33a63c463dbb65ae2d6655fe5c98411"
        },
        "ELK": {
            "symbol": "ELK",
            "decimals": 18,
            "name": "Elk",
            "address": "0xeeeeeb57642040be42185f49c52f7e9b38f8eeee"
        },
        "ETH": {
            "symbol": "ETH",
            "decimals": 18,
            "name": "Ethereum",
            "address": "0x74b23882a30290451a17c44f4f05243b6b58c76d"
        },
        "FAME": {
            "symbol": "FAME",
            "decimals": 18,
            "name": "FAME",
            "address": "0x904f51a2e7eeaf76aaf0418cbaf0b71149686f4a"
        },
        "FHM": {
            "symbol": "FHM",
            "decimals": 9,
            "name": "Fantohm",
            "address": "0xfa1fbb8ef55a4855e5688c0ee13ac3f202486286"
        },
        "FLIBERO": {
            "symbol": "FLIBERO",
            "decimals": 18,
            "name": "Fantom Libero Financial Freedom",
            "address": "0xc3f069d7439baf6d4d6e9478d9cc77778e62d147"
        },
        "fOLIVE": {
            "symbol": "fOLIVE",
            "decimals": 18,
            "name": "OliveCash Token",
            "address": "0xa9937092c4e2b0277c16802cc8778d252854688a"
        },
        "FRAX": {
            "symbol": "FRAX",
            "decimals": 18,
            "name": "Frax",
            "address": "0xdc301622e621166bd8e82f2ca0a26c13ad0be355"
        },
        "FS": {
            "symbol": "FS",
            "decimals": 18,
            "name": "FantomStarter",
            "address": "0xc758295cd1a564cdb020a78a681a838cf8e0627d"
        },
        "FUSD": {
            "symbol": "FUSD",
            "decimals": 18,
            "name": "Fantom USD",
            "address": "0xad84341756bf337f5a0164515b1f6f993d194e1f"
        },
        "fUSDT": {
            "symbol": "fUSDT",
            "decimals": 6,
            "name": "Frapped USDT",
            "address": "0x049d68029688eabf473097a2fc38ef61633a3c7a"
        },
        "FXS": {
            "symbol": "FXS",
            "decimals": 18,
            "name": "Frax Share",
            "address": "0x7d016eec9c25232b01f23ef992d98ca97fc2af5a"
        },
        "GEIST": {
            "symbol": "GEIST",
            "decimals": 18,
            "name": "Geist.Finance Protocol Token",
            "address": "0xd8321aa83fb0a4ecd6348d4577431310a6e0814d"
        },
        "gOHM": {
            "symbol": "gOHM",
            "decimals": 18,
            "name": "Governance OHM",
            "address": "0x91fa20244fb509e8289ca630e5db3e9166233fdc"
        },
        "GRO": {
            "symbol": "GRO",
            "decimals": 18,
            "name": "Growth-Peg Token",
            "address": "0x91f1430833879272643658f8ed07d60257ddf321"
        },
        "GTON": {
            "symbol": "GTON",
            "decimals": 18,
            "name": "Graviton",
            "address": "0xc1be9a4d5d45beeacae296a7bd5fadbfc14602c4"
        },
        "HEC": {
            "symbol": "HEC",
            "decimals": 9,
            "name": "Hector",
            "address": "0x5c4fdfc5233f935f20d2adba572f770c2e377ab0"
        },
        "HEGIC": {
            "symbol": "HEGIC",
            "decimals": 18,
            "name": "Hegic",
            "address": "0x44b26e839eb3572c5e959f994804a5de66600349"
        },
        "HND": {
            "symbol": "HND",
            "decimals": 18,
            "name": "Hundred Finance",
            "address": "0x10010078a54396f62c96df8532dc2b4847d47ed3"
        },
        "IB": {
            "symbol": "IB",
            "decimals": 18,
            "name": "IronBank",
            "address": "0x00a35fd824c717879bf370e70ac6868b95870dfb"
        },
        "ICE": {
            "symbol": "ICE",
            "decimals": 18,
            "name": "IceToken",
            "address": "0xf16e81dce15b08f326220742020379b855b87df9"
        },
        "KP3R": {
            "symbol": "KP3R",
            "decimals": 18,
            "name": "Keep3r",
            "address": "0x2a5062d22adcfaafbd5c541d4da82e4b450d4212"
        },
        "LINK": {
            "symbol": "LINK",
            "decimals": 18,
            "name": "ChainLink",
            "address": "0xb3654dc3d10ea7645f8319668e8f54d2574fbdc8"
        },
        "LIQR": {
            "symbol": "LIQR",
            "decimals": 18,
            "name": "LIQR",
            "address": "0x33333ee26a7d02e41c33828b42fb1e0889143477"
        },
        "LQDR": {
            "symbol": "LQDR",
            "decimals": 18,
            "name": "Liquid Driver",
            "address": "0x10b620b2dbac4faa7d7ffd71da486f5d44cd86f9"
        },
        "MAGIK": {
            "symbol": "MAGIK",
            "decimals": 18,
            "name": "MAGIK",
            "address": "0x87a5c9b60a3aaf1064006fe64285018e50e0d020"
        },
        "MARS": {
            "symbol": "MARS",
            "decimals": 9,
            "name": "ProjectMars Token",
            "address": "0xbe41772587872a92184873d55b09c6bb6f59f895"
        },
        "MCRT": {
            "symbol": "MCRT",
            "decimals": 9,
            "name": "MagicCraft",
            "address": "0xe705af5f63fcabdcdf5016aa838eaaac35d12890"
        },
        "MIM": {
            "symbol": "MIM",
            "decimals": 18,
            "name": "Magic Internet Money",
            "address": "0x82f0b8b456c1a451378467398982d4834b6829c1"
        },
        "miMATIC": {
            "symbol": "miMATIC",
            "decimals": 18,
            "name": "miMATIC",
            "address": "0xfb98b335551a418cd0737375a2ea0ded62ea213b"
        },
        "MMY": {
            "symbol": "MMY",
            "decimals": 18,
            "name": "MUMMY",
            "address": "0x01e77288b38b416f972428d562454fb329350bac"
        },
        "MODA": {
            "symbol": "MODA",
            "decimals": 18,
            "name": "moda",
            "address": "0x6496994241804d7fe2b032901931e03bcd82301f"
        },
        "MSHARE": {
            "symbol": "MSHARE",
            "decimals": 18,
            "name": "MSHARE",
            "address": "0xc8ca9026ad0882133ef126824f6852567c571a4e"
        },
        "MST": {
            "symbol": "MST",
            "decimals": 18,
            "name": "Monster",
            "address": "0x152888854378201e173490956085c711f1ded565"
        },
        "MULTI": {
            "symbol": "MULTI",
            "decimals": 18,
            "name": "Multichain",
            "address": "0x9fb9a33956351cf4fa040f65a13b835a3c8764e3"
        },
        "MvDOLLAR": {
            "symbol": "MvDOLLAR",
            "decimals": 18,
            "name": "MiniVerse Dollar",
            "address": "0x57976c467608983513c9355238dc6de1b1abbcca"
        },
        "NOKU": {
            "symbol": "NOKU",
            "decimals": 18,
            "name": "NOKU v2",
            "address": "0xfb4d42bed5618fb1a377ddb64eb56b92a6d117f2"
        },
        "OATH": {
            "symbol": "OATH",
            "decimals": 18,
            "name": "Oath Token",
            "address": "0x21ada0d2ac28c3a5fa3cd2ee30882da8812279b6"
        },
        "OBOL": {
            "symbol": "OBOL",
            "decimals": 18,
            "name": "OBOL",
            "address": "0x1539c63037d95f84a5981f96e43850d1451b6216"
        },
        "OKSE": {
            "symbol": "OKSE",
            "decimals": 18,
            "name": "Okse",
            "address": "0x3b53d2c7b44d40be05fa5e2309ffeb6eb2492d88"
        },
        "OOZE": {
            "symbol": "OOZE",
            "decimals": 18,
            "name": "Ooze",
            "address": "0x60e6afeb3ac2fbc82a8d312bea3b47dc6b4848d2"
        },
        "ORKAN": {
            "symbol": "ORKAN",
            "decimals": 9,
            "name": "Orkan",
            "address": "0xfb66e49e303a186a4c57414ceeed651a7a78161a"
        },
        "OXD": {
            "symbol": "OXD",
            "decimals": 18,
            "name": "0xDAO",
            "address": "0xc165d941481e68696f43ee6e99bfb2b23e0e3114"
        },
        "PAE": {
            "symbol": "PAE",
            "decimals": 18,
            "name": "Ripae",
            "address": "0x8a41f13a4fae75ca88b1ee726ee9d52b148b0498"
        },
        "PANIC": {
            "symbol": "PANIC",
            "decimals": 18,
            "name": "PanicSwap",
            "address": "0xa882ceac81b22fc2bef8e1a82e823e3e9603310b"
        },
        "pFTM": {
            "symbol": "pFTM",
            "decimals": 18,
            "name": "pFTM",
            "address": "0x112df7e3b4b7ab424f07319d4e92f41e6608c48b"
        },
        "PGK": {
            "symbol": "PGK",
            "decimals": 18,
            "name": "Penguin Karts",
            "address": "0x188a168280589bc3e483d77aae6b4a1d26bd22dc"
        },
        "POOCH": {
            "symbol": "POOCH",
            "decimals": 18,
            "name": "Pooch",
            "address": "0x31a47b49b4dbdc54d403b8c4880ac9bb1a9ebae8"
        },
        "PREMIA": {
            "symbol": "PREMIA",
            "decimals": 18,
            "name": "Premia",
            "address": "0x3028b4395f98777123c7da327010c40f3c7cc4ef"
        },
        "PUNCH": {
            "symbol": "PUNCH",
            "decimals": 18,
            "name": "Punchy Token",
            "address": "0x18ee5e886750cc1afdc728c5608da33305837da8"
        },
        "RAINI": {
            "symbol": "RAINI",
            "decimals": 18,
            "name": "Raini",
            "address": "0xe83dfaaafd3310474d917583ae9633b4f68fb036"
        },
        "RAINSPIRIT": {
            "symbol": "RAINSPIRIT",
            "decimals": 18,
            "name": "rainSpirit",
            "address": "0xf9c6e3c123f0494a4447100bd7dbd536f43cc33a"
        },
        "REAPER": {
            "symbol": "REAPER",
            "decimals": 18,
            "name": "ReaperToken",
            "address": "0x117db78176c8ede4f12fcd29d85cd96b91a4cbbb"
        },
        "RING": {
            "symbol": "RING",
            "decimals": 18,
            "name": "OneRing",
            "address": "0x582423c10c9e83387a96d00a69ba3d11ee47b7b5"
        },
        "RISE": {
            "symbol": "RISE",
            "decimals": 18,
            "name": "EverRise",
            "address": "0xc17c30e98541188614df99239cabd40280810ca3"
        },
        "SCAR": {
            "symbol": "SCAR",
            "decimals": 18,
            "name": "SCAR",
            "address": "0x0b41469497f46efa3937fba4ed92153146f55ca9"
        },
        "SCARE": {
            "symbol": "SCARE",
            "decimals": 18,
            "name": "ScareCrow",
            "address": "0x46e1ee17f51c52661d04238f1700c547de3b84a1"
        },
        "SCREAM": {
            "symbol": "SCREAM",
            "decimals": 18,
            "name": "Scream",
            "address": "0xe0654c8e6fd4d733349ac7e09f6f23da256bf475"
        },
        "SEX": {
            "symbol": "SEX",
            "decimals": 18,
            "name": "Solidex",
            "address": "0xd31fcd1f7ba190dbc75354046f6024a9b86014d7"
        },
        "sFTMX": {
            "symbol": "sFTMX",
            "decimals": 18,
            "name": "sFTMX",
            "address": "0xd7028092c830b5c8fce061af2e593413ebbc1fc1"
        },
        "SHADE": {
            "symbol": "SHADE",
            "decimals": 18,
            "name": "ShadeToken",
            "address": "0x3a3841f5fa9f2c283ea567d5aeea3af022dd2262"
        },
        "SNX": {
            "symbol": "SNX",
            "decimals": 18,
            "name": "Synthetix Network",
            "address": "0x56ee926bd8c72b2d5fa1af4d9e4cbb515a1e3adc"
        },
        "SOL": {
            "symbol": "SOL",
            "decimals": 18,
            "name": "SOL",
            "address": "0x44f7237df00e386af8e79b817d05ed9f6fe0f296"
        },
        "SOLID": {
            "symbol": "SOLID",
            "decimals": 18,
            "name": "Solidly",
            "address": "0x888ef71766ca594ded1f0fa3ae64ed2941740a20"
        },
        "SOUL": {
            "symbol": "SOUL",
            "decimals": 18,
            "name": "SoulPower",
            "address": "0xe2fb177009ff39f52c0134e8007fa0e4baacbd07"
        },
        "SPA": {
            "symbol": "SPA",
            "decimals": 9,
            "name": "Spartacus",
            "address": "0x5602df4a94eb6c680190accfa2a475621e0ddbdc"
        },
        "SPELL": {
            "symbol": "SPELL",
            "decimals": 18,
            "name": "Spell Token",
            "address": "0x468003b688943977e6130f4f68f23aad939a1040"
        },
        "SPIRIT": {
            "symbol": "SPIRIT",
            "decimals": 18,
            "name": "SpiritSwap Token",
            "address": "0x5cc61a78f164885776aa610fb0fe1257df78e59b"
        },
        "STA": {
            "symbol": "STA",
            "decimals": 18,
            "name": "Statera",
            "address": "0x89d5e71e275b4be094df9551627bcf4e3b24ce22"
        },
        "STG": {
            "symbol": "STG",
            "decimals": 18,
            "name": "StargateToken",
            "address": "0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590"
        },
        "SUPA": {
            "symbol": "SUPA",
            "decimals": 18,
            "name": "SUPA Foundation",
            "address": "0x59d07a115fe3ffe5db3d52029d43cc0ef5e9ba08"
        },
        "sUSD": {
            "symbol": "sUSD",
            "decimals": 18,
            "name": "Synth sUSD",
            "address": "0x0e1694483ebb3b74d3054e383840c6cf011e518e"
        },
        "SUSHI": {
            "symbol": "SUSHI",
            "decimals": 18,
            "name": "Sushi",
            "address": "0xae75a438b2e0cb8bb01ec1e1e376de11d44477cc"
        },
        "SYN": {
            "symbol": "SYN",
            "decimals": 18,
            "name": "Synapse",
            "address": "0xe55e19fb4f2d85af758950957714292dac1e25b2"
        },
        "TAKE": {
            "symbol": "TAKE",
            "decimals": 18,
            "name": "Takepile Token",
            "address": "0xe9e5a97acc59bb68813bf368487fbffd0a39713b"
        },
        "TAROT": {
            "symbol": "TAROT",
            "decimals": 18,
            "name": "Tarot",
            "address": "0xc5e2b037d30a390e62180970b3aa4e91868764cd"
        },
        "TART": {
            "symbol": "TART",
            "decimals": 18,
            "name": "TARTARUS",
            "address": "0xe36ac17edb23bdd89d363d152365df019e3eaf71"
        },
        "TAZOR": {
            "symbol": "TAZOR",
            "decimals": 9,
            "name": "TAZOR",
            "address": "0xee65d8b88f86ace0f7ba42ba2d2c679b6f604bf0"
        },
        "TOMB": {
            "symbol": "TOMB",
            "decimals": 18,
            "name": "TOMB",
            "address": "0x6c021ae822bea943b2e66552bde1d2696a53fbb7"
        },
        "TOR": {
            "symbol": "TOR",
            "decimals": 18,
            "name": "TOR",
            "address": "0x74e23df9110aa9ea0b6ff2faee01e740ca1c642e"
        },
        "TRAVA": {
            "symbol": "TRAVA",
            "decimals": 18,
            "name": "TravaFinance Token",
            "address": "0x477a9d5df9beda06f6b021136a2efe7be242fcc9"
        },
        "TREAT": {
            "symbol": "TREAT",
            "decimals": 18,
            "name": "Treat",
            "address": "0x484f2ff94a7790759d56fb1efbace8075aba5e06"
        },
        "TREEB": {
            "symbol": "TREEB",
            "decimals": 18,
            "name": "Treeb",
            "address": "0xc60d7067dfbc6f2caf30523a064f416a5af52963"
        },
        "TSHARE": {
            "symbol": "TSHARE",
            "decimals": 18,
            "name": "TSHARE",
            "address": "0x4cdf39285d7ca8eb3f090fda0c069ba5f4145b37"
        },
        "TUSD": {
            "symbol": "TUSD",
            "decimals": 18,
            "name": "TrueUSD",
            "address": "0x9879abdea01a879644185341f7af7d8343556b7a"
        },
        "UNDEAD": {
            "symbol": "UNDEAD",
            "decimals": 18,
            "name": "Undead Finance",
            "address": "0x551c61db482289994e7d426fc4db6493918bb81d"
        },
        "UNIDX": {
            "symbol": "UNIDX",
            "decimals": 18,
            "name": "UniDex",
            "address": "0x2130d2a1e51112d349ccf78d2a1ee65843ba36e0"
        },
        "USDB": {
            "symbol": "USDB",
            "decimals": 18,
            "name": "USD Balance",
            "address": "0x6fc9383486c163fa48becdec79d6058f984f62ca"
        },
        "USDC": {
            "symbol": "USDC",
            "decimals": 6,
            "name": "USD Coin",
            "address": "0x04068da6c83afcfa0e13ba15a6696662335d5b75"
        },
        "UST": {
            "symbol": "UST",
            "decimals": 6,
            "name": "UST",
            "address": "0x846e4d51d7e2043c1a87e0ab7490b93fb940357b"
        },
        "VOID": {
            "symbol": "VOID",
            "decimals": 18,
            "name": "VOID",
            "address": "0x80f2b8cdbc470c4db4452cc7e4a62f5277db7061"
        },
        "WATERFALL": {
            "symbol": "WATERFALL",
            "decimals": 18,
            "name": "Waterfall",
            "address": "0x6b2a7b82d3f7a6e1f5a5831ab40666ec717645d5"
        },
        "WBOND": {
            "symbol": "WBOND",
            "decimals": 18,
            "name": "War Bond Token",
            "address": "0x59c6606ed2af925f270733e378d6af7829b5b3cf"
        },
        "WeVE": {
            "symbol": "WeVE",
            "decimals": 18,
            "name": "veDAO Token",
            "address": "0x911da02c1232a3c3e1418b834a311921143b04d7"
        },
        "WFTM": {
            "symbol": "WFTM",
            "decimals": 18,
            "name": "Wrapped Fantom",
            "address": "0x21be370d5312f44cb42ce377bc9b8a0cef1a4c83"
        },
        "WIGO": {
            "symbol": "WIGO",
            "decimals": 18,
            "name": "WigoSwap Token",
            "address": "0xe992beab6659bff447893641a378fbbf031c5bd6"
        },
        "WIS": {
            "symbol": "WIS",
            "decimals": 18,
            "name": "WingSwap",
            "address": "0xf24be6c063bee7c7844dd90a21fdf7d783d41a94"
        },
        "WOO": {
            "symbol": "WOO",
            "decimals": 18,
            "name": "Wootrade Network",
            "address": "0x6626c47c00f1d87902fc13eecfac3ed06d5e8d8a"
        },
        "wsHEC": {
            "symbol": "wsHEC",
            "decimals": 18,
            "name": "Wrapped sHEC",
            "address": "0x94ccf60f700146bea8ef7832820800e2dfa92eda"
        },
        "WV": {
            "symbol": "WV",
            "decimals": 18,
            "name": "Wolf Ventures",
            "address": "0x911d1feae99e112b5014cfa60038325d863352f1"
        },
        "YEL": {
            "symbol": "YEL",
            "decimals": 18,
            "name": "YEL Token",
            "address": "0xd3b71117e6c1558c1553305b44988cd944e97300"
        },
        "YFI": {
            "symbol": "YFI",
            "decimals": 18,
            "name": "yearn.finance",
            "address": "0x29b0da86e484e1c0029b56e817912d778ac0ec69"
        },
        "YOSHI": {
            "symbol": "YOSHI",
            "decimals": 18,
            "name": "Yoshi.exchange",
            "address": "0x3dc57b391262e3aae37a08d91241f9ba9d58b570"
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
