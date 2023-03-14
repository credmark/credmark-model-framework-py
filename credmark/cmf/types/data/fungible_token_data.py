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
        "address": '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c',
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
        "address": '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        "decimals": 18,
        "name": "Ethereum",
        "is_native_token": True,
        "wrapped": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    },
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
    }
}

FUNGIBLE_TOKEN_DATA_BY_ADDRESS = {
    chain_id: {
        chain_meta['address']: chain_meta
        for chain_meta in chain_tokens.values()
    }
    for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items()
}
