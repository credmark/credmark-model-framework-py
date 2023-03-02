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
    },
    int(Network.ArbitrumOne): {
        "symbol": "ETH",
        "address": '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        "decimals": 18,
        "name": "Ethereum",
        "is_native_token": True,
        "wrapped": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
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
    }
}

FUNGIBLE_TOKEN_DATA_BY_ADDRESS = {
    chain_id: {
        chain_meta['address']: chain_meta
        for chain_meta in chain_tokens.values()
    }
    for chain_id, chain_tokens in FUNGIBLE_TOKEN_DATA_BY_SYMBOL.items()
}
