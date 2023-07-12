# pylint:disable=too-many-lines

BSC_TOKENS = {
    "BTC": {
        "symbol": "BTC",
        "decimals": 8,
        "name": "Bitcoin",
        "address": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "set_loaded": True,
    },
    "BNB": {
        "symbol": "BNB",
        "decimals": 18,
        "name": "BSC",
        "address": '0x0000000000000000010000100100111001000010',
        "is_native_token": True,
    },
    "WBNB": {
        "symbol": "WBNB",
        "decimals": 18,
        "name": "Wrapped BNB",
        "address": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
    },
    "BUSD": {
        "symbol": "BUSD",
        "decimals": 18,
        "name": "BUSD Token",
        "address": "0xe9e7cea3dedca5984780bafc599bd69add087d56"
    },
    "LINK": {
        "symbol": "LINK",
        "decimals": 18,
        "name": "ChainLink Token",
        "address": "0xf8a0bf9cf54bb92f17374d9e9a321e6a111a51bd"
    },
    "FIL": {
        "symbol": "FIL",
        "decimals": 18,
        "name": "Filecoin",
        "address": "0x0d8ce2a99bb6e3b7db580ed848240e4a0f9ae153"
    },
    "USDT": {
        "symbol": "USDT",
        "decimals": 18,
        "name": "Tether USD",
        "address": "0x55d398326f99059ff775485246999027b3197955"
    },
    "TRX": {
        "symbol": "TRX",
        "decimals": 6,
        "name": "TRON",
        "address": "0xce7de646e7208a4ef112cb6ed5038fa6cc6b12e3"
    },
    "ETH": {
        "symbol": "ETH",
        "decimals": 18,
        "name": "Ethereum Token",
        "address": "0x2170ed0880ac9a755fd29b2688956bd959f933f8"
    },
    "AXS": {
        "symbol": "AXS",
        "decimals": 18,
        "name": "Axie Infinity Shard",
        "address": "0x715d400f88c167884bbcc41c5fea407ed4d2f8a0"
    },
    "Cake": {
        "symbol": "Cake",
        "decimals": 18,
        "name": "PancakeSwap Token",
        "address": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"
    },
    "DAI": {
        "symbol": "DAI",
        "decimals": 18,
        "name": "Dai Token",
        "address": "0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3"
    },
    "DOGE": {
        "symbol": "DOGE",
        "decimals": 8,
        "name": "Dogecoin",
        "address": "0xba2ae424d960c26247dd6c32edc70b295c744c43"
    },
    "BTCB": {
        "symbol": "BTCB",
        "decimals": 18,
        "name": "BTCB Token",
        "address": "0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c"
    },
    "XRP": {
        "symbol": "XRP",
        "decimals": 18,
        "name": "XRP Token",
        "address": "0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe"
    },
    ###
    " BTCPAY": {
        "symbol": " BTCPAY",
        "decimals": 18,
        "name": "Bitcoin Pay",
        "address": "0x9f5c37e0fd9bf729b1f0a6f39ce57be5e9bfd435"
    },
    "$ANRX": {
        "symbol": "$ANRX",
        "decimals": 18,
        "name": "pTokens $ANRX",
        "address": "0xe2e7329499e8ddb1f2b04ee4b35a8d7f6881e4ea"
    },
    "$BART": {
        "symbol": "$BART",
        "decimals": 9,
        "name": "BART SIMPSON COIN",
        "address": "0x16e79e09b3b56bcbba83667aff88dc6ca727af2e"
    },
    "$BeAI": {
        "symbol": "$BeAI",
        "decimals": 9,
        "name": "BeNFT AI",
        "address": "0x8f7ebc23212f6adcc7a5f1c86197ec337c2f4997"
    },
    "$CRDN": {
        "symbol": "$CRDN",
        "decimals": 18,
        "name": "Cardence",
        "address": "0xfa17b330bcc4e7f3e2456996d89a5a54ab044831"
    },
    "$DEV": {
        "symbol": "$DEV",
        "decimals": 9,
        "name": "DevOps",
        "address": "0xfc7104975fde57040fce04ccee6a9e97d559dc12"
    },
    "$FUR": {
        "symbol": "$FUR",
        "decimals": 18,
        "name": "Furio",
        "address": "0x48378891d6e459ca9a56b88b406e8f4eab2e39bf"
    },
    "$GARFIELD": {
        "symbol": "$GARFIELD",
        "decimals": 18,
        "name": "Garfield",
        "address": "0x2a49840ba994486dd3ceb93e1124308f7226f219"
    },
    "$Lordz": {
        "symbol": "$Lordz",
        "decimals": 9,
        "name": "Meme Lordz",
        "address": "0x2541be91fe0d220ffcbe65f11d88217a87a43bda"
    },
    "$MANGA": {
        "symbol": "$MANGA",
        "decimals": 18,
        "name": "Manga token",
        "address": "0xc2cb89bbb5bba6e21db1dfe13493dfd7dcbabd68"
    },
    "$MOONPOT": {
        "symbol": "$MOONPOT",
        "decimals": 9,
        "name": "MoonPot",
        "address": "0x971341c2e487bb51643573bc8b9f08b44dbc92e6"
    },
    "$NEUTR": {
        "symbol": "$NEUTR",
        "decimals": 18,
        "name": "Neutrinos",
        "address": "0xb695806cc5a3cd8623b92bbd221e3bec6e8e3bed"
    },
    "$POV": {
        "symbol": "$POV",
        "decimals": 18,
        "name": "Pepe Original Version",
        "address": "0xc2eaaf69e6439abab12dd21f560ba0ec7f17cff7"
    },
    "$SANDWICH": {
        "symbol": "$SANDWICH",
        "decimals": 18,
        "name": "Sandwich Network",
        "address": "0xd3253fc0a42e6dcf4f66ab147f628e3f29e9b214"
    },
    "$STRIP": {
        "symbol": "$STRIP",
        "decimals": 18,
        "name": "STRIPTO",
        "address": "0xa1ac3b22b102caa62c9ecaf418585528855b0ddd"
    },
    "$TIMESERIES": {
        "symbol": "$TIMESERIES",
        "decimals": 9,
        "name": "Timeseries AI",
        "address": "0xb27607d439751555003506455dd9e763a53e5b1d"
    },
    "$tipsy": {
        "symbol": "$tipsy",
        "decimals": 18,
        "name": "TipsyCoin",
        "address": "0xe097bceb09bfb18047cf259f321cc129b7beba5e"
    },
    "10SET": {
        "symbol": "10SET",
        "decimals": 18,
        "name": "10Set Token",
        "address": "0x1ae369a6ab222aff166325b7b87eb9af06c86e57"
    },
    "1ART": {
        "symbol": "1ART",
        "decimals": 18,
        "name": "ArtWallet",
        "address": "0xd3c325848d7c6e29b574cb0789998b2ff901f17e"
    },
    # "1COIN": {
    #     "symbol": "1COIN",
    #     "decimals": 8,
    #     "name": "1COIN",
    #     "address": "0xf31327c3c16b58d365efc82e66b7a38cd123cbf8"
    # },
    "1INCH": {
        "symbol": "1INCH",
        "decimals": 18,
        "name": "1INCH Token",
        "address": "0x111111111117dc0aa78b770fa6a738034120c302"
    },
    "1MIL": {
        "symbol": "1MIL",
        "decimals": 18,
        "name": "1MILNFT",
        "address": "0xa4ef4b0b23c1fc81d3f9ecf93510e64f58a4a016"
    },
    "1MT": {
        "symbol": "1MT",
        "decimals": 18,
        "name": "1move",
        "address": "0x7c56d81ecb5e1d287a1e22b89b01348f07be3541"
    },
    "2CRZ": {
        "symbol": "2CRZ",
        "decimals": 18,
        "name": "2CrazyToken",
        "address": "0x3a6e8b36645d6c252714daddd28ec0673535a109"
    },
    "2GCC": {
        "symbol": "2GCC",
        "decimals": 18,
        "name": "2G CARBON COIN",
        "address": "0x1a515bf4e35aa2df67109281de6b3b00ec37675e"
    },
    "2LC": {
        "symbol": "2LC",
        "decimals": 18,
        "name": "2local Token",
        "address": "0x11f6ecc9e2658627e0876212f1078b9f84d3196e"
    },
    "3AIR": {
        "symbol": "3AIR",
        "decimals": 18,
        "name": "3air",
        "address": "0x596834746b5b78f31a089ee7853fa595682824b7"
    },
    "3P": {
        "symbol": "3P",
        "decimals": 18,
        "name": "Web3Camp Token",
        "address": "0xb806fa32ebdc04e5dbdd2ad83e75c8f7d8e8ef8b"
    },
    "4JNET": {
        "symbol": "4JNET",
        "decimals": 9,
        "name": "4JNET",
        "address": "0xbfb1a68962fb4ed040fd3a0a71dc2c2015bcc667"
    },
    "7PXS": {
        "symbol": "7PXS",
        "decimals": 18,
        "name": "7Pixels",
        "address": "0x82bec5483dbab4305f32b191d76dc6cb020ae76d"
    },
    "8PAY": {
        "symbol": "8PAY",
        "decimals": 18,
        "name": "8PAY Network",
        "address": "0xfeea0bdd3d07eb6fe305938878c0cadbfa169042"
    },
    'agEUR': {
        'symbol': 'agEUR',
        'decimals': 18,
        'name': 'agEUR',
        'address': '0x12f31B73D812C6Bb0d735a218c086d44D5fe5f89',
    },
    "ankrETH": {
        "symbol": "ankrETH",
        "decimals": 18,
        "name": "Ankr Staked ETH",
        "address": "0xe05A08226c49b636ACf99c40Da8DC6aF83CE5bB3",
    },
    "A4": {
        "symbol": "A4",
        "decimals": 6,
        "name": "A4",
        "address": "0x9767203e89dcd34851240b3919d4900d3e5069f1"
    },
    "AAA": {
        "symbol": "AAA",
        "decimals": 18,
        "name": "MoonRabbit",
        "address": "0xa39bf0446268d99c5c0a85ecf92970611912d386"
    },
    "AAVE": {
        "symbol": "AAVE",
        "decimals": 18,
        "name": "Aave Token",
        "address": "0xfb6115445bff7b52feb98650c87f44907e58f802"
    },
    "ABB": {
        "symbol": "ABB",
        "decimals": 18,
        "name": "Astro Token",
        "address": "0x277ae79c42c859ca858d5a92c22222c8b65c6d94"
    },
    "ACH": {
        "symbol": "ACH",
        "decimals": 8,
        "name": "Alchemy",
        "address": "0xbc7d6b50616989655afd682fb42743507003056d"
    },
    "ACK": {
        "symbol": "ACK",
        "decimals": 18,
        "name": "AcknoLedger",
        "address": "0xf7b5fb4607abfe0ecf332c23cbdcc9e425b443a8"
    },
    "ACS": {
        "symbol": "ACS",
        "decimals": 18,
        "name": "ACryptoS",
        "address": "0x4197c6ef3879a08cd51e5560da5064b773aa1d29"
    },
    "ACT": {
        "symbol": "ACT",
        "decimals": 18,
        "name": "Acet Token",
        "address": "0x9f3bcbe48e8b754f331dfc694a894e8e686ac31d"
    },
    "ACY": {
        "symbol": "ACY",
        "decimals": 18,
        "name": "ACY",
        "address": "0xc94595b56e301f3ffedb8ccc2d672882d623e53a"
    },
    "ADA": {
        "symbol": "ADA",
        "decimals": 18,
        "name": "Cardano Token",
        "address": "0x3ee2200efb3400fabb9aacf31297cbdd1d435d47"
    },
    "ADAO": {
        "symbol": "ADAO",
        "decimals": 18,
        "name": "ADADAO",
        "address": "0x3b76374cc2dfe28cc373dca6d5024791b2586335"
    },
    "ADAPAD": {
        "symbol": "ADAPAD",
        "decimals": 18,
        "name": "ADAPAD.io",
        "address": "0xdb0170e2d0c1cc1b2e7a90313d9b9afa4f250289"
    },
    "ADR": {
        "symbol": "ADR",
        "decimals": 18,
        "name": "Adroverse Token",
        "address": "0x36f1f32c728c3f330409ec1f0928fa3ab3c8a76f"
    },
    "ADS": {
        "symbol": "ADS",
        "decimals": 11,
        "name": "Adshares",
        "address": "0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a"
    },
    "ADX": {
        "symbol": "ADX",
        "decimals": 18,
        "name": "AdEx Network",
        "address": "0x6bff4fb161347ad7de4a625ae5aa3a1ca7077819"
    },
    "AFD": {
        "symbol": "AFD",
        "decimals": 18,
        "name": "Animal Farm Dogs",
        "address": "0x198271b868dae875bfea6e6e4045cdda5d6b9829"
    },
    "AFEN": {
        "symbol": "AFEN",
        "decimals": 18,
        "name": "Afen",
        "address": "0xd0840d5f67206f865aee7cce075bd4484cd3cc81"
    },
    "AFNTY": {
        "symbol": "AFNTY",
        "decimals": 9,
        "name": "Affinity",
        "address": "0xface67c5ce2bb48c29779b0dede5360cc9ef5fd5"
    },
    "AFP": {
        "symbol": "AFP",
        "decimals": 18,
        "name": "PIGS Token",
        "address": "0x9a3321e1acd3b9f6debee5e042dd2411a1742002"
    },
    "AG": {
        "symbol": "AG",
        "decimals": 18,
        "name": "AGAME",
        "address": "0x88888888faedeb25b94a015af705f18666079038"
    },
    "AGI": {
        "symbol": "AGI",
        "decimals": 18,
        "name": "AGI Token",
        "address": "0x818835503f55283cd51a4399f595e295a9338753"
    },
    "AGRO": {
        "symbol": "AGRO",
        "decimals": 4,
        "name": "AGRO GLOBAL",
        "address": "0x39cc67690d0f2d4acd68d3d9b612a80d780b84c0"
    },
    "AGS": {
        "symbol": "AGS",
        "decimals": 18,
        "name": "Collector Coin",
        "address": "0x73ffdf2d2afb3def5b10bf967da743f2306a51db"
    },
    "AI": {
        "symbol": "AI",
        "decimals": 18,
        "name": "Chat AI",
        "address": "0xa89bf95c5f15a847c8eb8d348cd7fed719ad7d80"
    },
    "AIAI": {
        "symbol": "AIAI",
        "decimals": 18,
        "name": "All In AI",
        "address": "0x1e05f5a582e45b58cba5fa318d10344a77fb1d94"
    },
    "AIDogeMini": {
        "symbol": "AIDogeMini",
        "decimals": 18,
        "name": "AI DogeMini",
        "address": "0xf709e948daed701a6a018e6f6090ca1930055966"
    },
    "AIDOGEX": {
        "symbol": "AIDOGEX",
        "decimals": 9,
        "name": "AI DogeX",
        "address": "0x246fcdc18bf3781b4c5100b3a6decef8dbcc8a31"
    },
    "AIE": {
        "symbol": "AIE",
        "decimals": 18,
        "name": "A.I.Earn",
        "address": "0x1e30bbee322b3b11c60cb434a47f1605c2a99483"
    },
    "AIFLOKI": {
        "symbol": "AIFLOKI",
        "decimals": 9,
        "name": "AI Floki",
        "address": "0x0cd5c0e24a29225b2e0eae25c3ab8f62ef70df9d"
    },
    "AIGPT": {
        "symbol": "AIGPT",
        "decimals": 18,
        "name": "All In GPT",
        "address": "0xeb05ac86959725f9e7284cf67b052ba82aeb446e"
    },
    "AiONE": {
        "symbol": "AiONE",
        "decimals": 18,
        "name": "AiONE",
        "address": "0x4634d58982138e93c951c1485d25bc619cbd1f75"
    },
    "AIonMars": {
        "symbol": "AIonMars",
        "decimals": 18,
        "name": "AIon Mars",
        "address": "0xa2214039c2ccb9b86d351000ba2f126f45ce44a4"
    },
    "AIOZ": {
        "symbol": "AIOZ",
        "decimals": 18,
        "name": "AIOZ Network",
        "address": "0x33d08d8c7a168333a85285a68c0042b39fc3741d"
    },
    "AIPAD": {
        "symbol": "AIPAD",
        "decimals": 18,
        "name": "AIPAD.tech",
        "address": "0xe55d97a97ae6a17706ee281486e98a84095d8aaf"
    },
    "AIR": {
        "symbol": "AIR",
        "decimals": 18,
        "name": "AIR",
        "address": "0xd8a2ae43fd061d24acd538e3866ffc2c05151b53"
    },
    "AIRI": {
        "symbol": "AIRI",
        "decimals": 18,
        "name": "aiRight Token",
        "address": "0x7e2a35c746f2f7c240b664f1da4dd100141ae71f"
    },
    "AIRT": {
        "symbol": "AIRT",
        "decimals": 18,
        "name": "AirNFT Token",
        "address": "0x016cf83732f1468150d87dcc5bdf67730b3934d3"
    },
    "AIT": {
        "symbol": "AIT",
        "decimals": 18,
        "name": "AIT Token",
        "address": "0x4238e5ccc619dcc8c00ade4cfc5d3d9020b24898"
    },
    "AiWallet": {
        "symbol": "AiWallet",
        "decimals": 18,
        "name": "AiWallet Token",
        "address": "0x309d43cb7bb1e07371eee4947103aa019121a973"
    },
    "ALEPH": {
        "symbol": "ALEPH",
        "decimals": 18,
        "name": "aleph.im v2",
        "address": "0x82d2f8e02afb160dd5a480a617692e62de9038c4"
    },
    "ALGOBLK": {
        "symbol": "ALGOBLK",
        "decimals": 18,
        "name": "Algoblocks",
        "address": "0xfecca80ff6deb2b492e93df3b67f0c523cfd3a48"
    },
    "ALI": {
        "symbol": "ALI",
        "decimals": 18,
        "name": "Alita Token",
        "address": "0x557233e794d1a5fbcc6d26dca49147379ea5073c"
    },
    "ALICE": {
        "symbol": "ALICE",
        "decimals": 6,
        "name": "ALICE",
        "address": "0xac51066d7bec65dc4589368da368b212745d63e8"
    },
    "alif": {
        "symbol": "alif",
        "decimals": 18,
        "name": "ALIF",
        "address": "0x967784950655b8e74a2d3d3503933f0015660074"
    },
    "ALLBI": {
        "symbol": "ALLBI",
        "decimals": 18,
        "name": "ALLBESTICO.com",
        "address": "0x613e18f13391cd4bfedf8a904991077c7ef29ee6"
    },
    "ALLOY": {
        "symbol": "ALLOY",
        "decimals": 18,
        "name": "HyperAlloy",
        "address": "0x5ef5994fa33ff4eb6c82d51ee1dc145c546065bd"
    },
    "ALM": {
        "symbol": "ALM",
        "decimals": 18,
        "name": "AliumToken",
        "address": "0x7c38870e93a1f959cb6c533eb10bbc3e438aac11"
    },
    "ALMR": {
        "symbol": "ALMR",
        "decimals": 18,
        "name": "Almira",
        "address": "0xee7f7c9459d8e910209849ed010c96f2dfe39d3b"
    },
    "ALN": {
        "symbol": "ALN",
        "decimals": 18,
        "name": "Aluna",
        "address": "0xf44fb887334fa17d2c5c0f970b5d320ab53ed557"
    },
    "ALP": {
        "symbol": "ALP",
        "decimals": 9,
        "name": "CoinAlpha",
        "address": "0x6775729fad1438116b2e3b4fb2878539795297a7"
    },
    "ALPACA": {
        "symbol": "ALPACA",
        "decimals": 18,
        "name": "AlpacaToken",
        "address": "0x8f0528ce5ef7b51152a59745befdd91d97091d2f"
    },
    "ALPHA": {
        "symbol": "ALPHA",
        "decimals": 18,
        "name": "AlphaToken",
        "address": "0xa1faa113cbe53436df28ff0aee54275c13b40975"
    },
    "ALPINE": {
        "symbol": "ALPINE",
        "decimals": 8,
        "name": "ALPINE Fan Token",
        "address": "0x287880ea252b52b63cc5f40a2d3e5a44aa665a76"
    },
    "ALT": {
        "symbol": "ALT",
        "decimals": 9,
        "name": "Alphabet",
        "address": "0xfe2f3580856376377c14e2287fa15bcb703e5fb5"
    },
    "ALTB": {
        "symbol": "ALTB",
        "decimals": 18,
        "name": "Altbase",
        "address": "0x9b3a01f8b4abd2e2a74597b21b7c269abf4e9f41"
    },
    "ALTN": {
        "symbol": "ALTN",
        "decimals": 18,
        "name": "Alterna Network",
        "address": "0xc841780c34c17190bceeefb6d986aaca4fb95e31"
    },
    "ALTRU": {
        "symbol": "ALTRU",
        "decimals": 18,
        "name": "Altrucoin",
        "address": "0x377ef66728d344bfa2bb370186ab4b57092577bd"
    },
    "ALU": {
        "symbol": "ALU",
        "decimals": 18,
        "name": "Altura",
        "address": "0x8263cd1601fe73c066bf49cc09841f35348e3be0"
    },
    "ALYA": {
        "symbol": "ALYA",
        "decimals": 9,
        "name": "ALYATTES",
        "address": "0x49a9f9a2271d8c5da44c57e7102aca79c222f4a9"
    },
    "AmazingTeam": {
        "symbol": "AmazingTeam",
        "decimals": 18,
        "name": "AmazingTeamDao",
        "address": "0x44ece1031e5b5e2d9169546cc10ea5c95ba96237"
    },
    "AMB": {
        "symbol": "AMB",
        "decimals": 9,
        "name": "Apple",
        "address": "0x95977a9daa14a00258f89a14f75b6e35d5b730d4"
    },
    "AMPL": {
        "symbol": "AMPL",
        "decimals": 9,
        "name": "AMPL secured by Meter Passport",
        "address": "0xdb021b1b247fe2f1fa57e0a87c748cc1e321f07f"
    },
    "ANCHOR": {
        "symbol": "ANCHOR",
        "decimals": 18,
        "name": "AnchorSwap Token",
        "address": "0x4aac18de824ec1b553dbf342829834e4ff3f7a9f"
    },
    "ANJI": {
        "symbol": "ANJI",
        "decimals": 9,
        "name": "Anji",
        "address": "0xfc619ffcc0e0f30427bf938f9a1b2bfae15bdf84"
    },
    "ANKR": {
        "symbol": "ANKR",
        "decimals": 18,
        "name": "Ankr",
        "address": "0xf307910a4c7bbc79691fd374889b36d8531b08e3"
    },
    "ankrBNB": {
        "symbol": "ankrBNB",
        "decimals": 18,
        "name": "Ankr Staked BNB",
        "address": "0x52f24a5e03aee338da5fd9df68d2b6fae1178827"
    },
    "ANML": {
        "symbol": "ANML",
        "decimals": 18,
        "name": "Animal Concerts Token",
        "address": "0x06fda0758c17416726f77cb11305eac94c074ec0"
    },
    "ANTX": {
        "symbol": "ANTX",
        "decimals": 18,
        "name": "AntNetworX",
        "address": "0x9186359f82c3c0cc005a0b3563dc4ccd2627d82a"
    },
    "ANY": {
        "symbol": "ANY",
        "decimals": 18,
        "name": "Anyswap-BEP20",
        "address": "0xf68c9df95a18b2a5a5fa1124d79eeeffbad0b6fa"
    },
    "anyMTLX": {
        "symbol": "anyMTLX",
        "decimals": 18,
        "name": "MTLX-ERC20",
        "address": "0x5921dee8556c4593eefcfad3ca5e2f618606483b"
    },
    "AOG": {
        "symbol": "AOG",
        "decimals": 18,
        "name": "AgeOfGods",
        "address": "0x40c8225329bd3e28a043b029e0d07a5344d2c27c"
    },
    "APAD": {
        "symbol": "APAD",
        "decimals": 18,
        "name": "AnyPad",
        "address": "0x366d71ab095735b7dae83ce2b82d5262ef655f10"
    },
    "APC": {
        "symbol": "APC",
        "decimals": 18,
        "name": "ArenaPlay",
        "address": "0x2aa504586d6cab3c59fa629f74c586d78b93a025"
    },
    "APE": {
        "symbol": "APE",
        "decimals": 18,
        "name": "ApeMove Game Token",
        "address": "0xed3d88d3321f82e5c25ca9ac6d5b427ec93f567e"
    },
    "APRIL": {
        "symbol": "APRIL",
        "decimals": 18,
        "name": "April Token",
        "address": "0xbfea674ce7d16e26e39e3c088810367a708ef94c"
    },
    "APT": {
        "symbol": "APT",
        "decimals": 18,
        "name": "Apidae Token",
        "address": "0xa49c8cbbddfe4dbc8605f0f5c8f2845c5e225d22"
    },
    "APX": {
        "symbol": "APX",
        "decimals": 18,
        "name": "ApolloX Token",
        "address": "0x78f5d389f5cdccfc41594abab4b0ed02f31398b3"
    },
    "AQT": {
        "symbol": "AQT",
        "decimals": 18,
        "name": "Alpha Quark Token",
        "address": "0xda5be69074afd12354173b4350ec9117e73e92e2"
    },
    "ARA": {
        "symbol": "ARA",
        "decimals": 18,
        "name": "Adora",
        "address": "0xa9243aeb1e1038273d479436d4f4dece656c62f3"
    },
    # "ARBI": {
    #     "symbol": "ARBI",
    #     "decimals": 18,
    #     "name": "Arbipad",
    #     "address": "0xa7bd657c5838472ddf85ff0797a2e6fce8fd4833"
    # },
    "ARCONA": {
        "symbol": "ARCONA",
        "decimals": 18,
        "name": "ARCONA",
        "address": "0x8fc4532be3003fb5a3a2f9afc7e95b3bfbd5faab"
    },
    "ARCS": {
        "symbol": "ARCS",
        "decimals": 18,
        "name": "Arbitrum Charts",
        "address": "0x888ed27c3ab248868c29dabe3d1b3d7cc5c89c5b"
    },
    "ARDN": {
        "symbol": "ARDN",
        "decimals": 18,
        "name": "Ariadne",
        "address": "0xa0a9961b7477d1a530f06a1ee805d5e532e73d97"
    },
    "AREA": {
        "symbol": "AREA",
        "decimals": 18,
        "name": "AREON",
        "address": "0x3cb26f04223e948b8d810a7bd170620afbd42e67"
    },
    "ARES": {
        "symbol": "ARES",
        "decimals": 18,
        "name": "Ares Protocol",
        "address": "0xf9752a6e8a5e5f5e6eb3ab4e7d8492460fb319f0"
    },
    "ARGON": {
        "symbol": "ARGON",
        "decimals": 18,
        "name": "ArgonToken",
        "address": "0x851f7a700c5d67db59612b871338a85526752c25"
    },
    "ARI10": {
        "symbol": "ARI10",
        "decimals": 18,
        "name": "ARI10",
        "address": "0x80262f604acac839724f66846f290a2cc8b48662"
    },
    "ARIX": {
        "symbol": "ARIX",
        "decimals": 18,
        "name": "Arix",
        "address": "0x4db2495afad4c0e481ffc40fdaf66e13a786b619"
    },
    "ARKER": {
        "symbol": "ARKER",
        "decimals": 18,
        "name": "ARKER",
        "address": "0x9c67638c4fa06fd47fb8900fc7f932f7eab589de"
    },
    "ARKN": {
        "symbol": "ARKN",
        "decimals": 18,
        "name": "ArkRivals",
        "address": "0xaa20c2e278d99f978989daa4460f933745f862d5"
    },
    "ARMA": {
        "symbol": "ARMA",
        "decimals": 18,
        "name": "Aarma",
        "address": "0xe405b8148d731e4e1117e00542264dac5375bc97"
    },
    "ARMOUR": {
        "symbol": "ARMOUR",
        "decimals": 18,
        "name": "Armour Wallet",
        "address": "0x48a356df5140ed37034afada32d03b74d4271d6a"
    },
    "AROR": {
        "symbol": "AROR",
        "decimals": 9,
        "name": "ARORA",
        "address": "0x305bbd18f9a3b55047740843889521722dab1fde"
    },
    "ARPA": {
        "symbol": "ARPA",
        "decimals": 18,
        "name": "ARPA Token",
        "address": "0x6f769e65c14ebd1f68817f5f1dcdb61cfa2d6f7e"
    },
    "ARV": {
        "symbol": "ARV",
        "decimals": 8,
        "name": "ARIVA",
        "address": "0x6679eb24f59dfe111864aec72b443d1da666b360"
    },
    "ASIA": {
        "symbol": "ASIA",
        "decimals": 18,
        "name": "ASIA COIN",
        "address": "0xebaffc2d2ea7c66fb848c48124b753f93a0a90ec"
    },
    "ASPO": {
        "symbol": "ASPO",
        "decimals": 18,
        "name": "ASPOToken",
        "address": "0x1a9b49e9f075c37fe5f86c916bac9deb33556d7e"
    },
    "ASR": {
        "symbol": "ASR",
        "decimals": 2,
        "name": " AS Roma",
        "address": "0x80d5f92c2c8c682070c95495313ddb680b267320"
    },
    "ASS": {
        "symbol": "ASS",
        "decimals": 9,
        "name": "Australian Shepherd Token",
        "address": "0x7c63f96feafacd84e75a594c00fac3693386fbf0"
    },
    "ASSA": {
        "symbol": "ASSA",
        "decimals": 18,
        "name": "ASSA",
        "address": "0xa25d074d5300f9f997a76994840a3266a72f77e4"
    },
    "ASSET": {
        "symbol": "ASSET",
        "decimals": 18,
        "name": "iAssets",
        "address": "0x6b471d5ab9f3d92a600e7d49a0b135bf6d4c6a5b"
    },
    "AST": {
        "symbol": "AST",
        "decimals": 18,
        "name": "Absolute Sync Token",
        "address": "0x7ed86d2769fe9a2cad7bac4ceac45e40c82295d6"
    },
    "ASTRO": {
        "symbol": "ASTRO",
        "decimals": 18,
        "name": "ASTROSWAP.app",
        "address": "0x72eb7ca07399ec402c5b7aa6a65752b6a1dc0c27"
    },
    "ASVA": {
        "symbol": "ASVA",
        "decimals": 18,
        "name": "Asva",
        "address": "0xf7b6d7e3434cb9441982f9534e6998c43eef144a"
    },
    "ASY": {
        "symbol": "ASY",
        "decimals": 18,
        "name": "ASYAGRO",
        "address": "0xc0cc1e5761ba5786916fd055562551798e50d573"
    },
    "ATA": {
        "symbol": "ATA",
        "decimals": 18,
        "name": "Automata",
        "address": "0xa2120b9e674d3fc3875f415a7df52e382f141225"
    },
    "ATD": {
        "symbol": "ATD",
        "decimals": 18,
        "name": "A2DAO Token",
        "address": "0x1ce440d1a64eea6aa1db2a5aa51c9b326930957c"
    },
    "ATHENASV2": {
        "symbol": "ATHENASV2",
        "decimals": 18,
        "name": "ATHENASV2",
        "address": "0x95d07a6b1dd22cfc6f775e9574e4374995e7ef89"
    },
    "ATL": {
        "symbol": "ATL",
        "decimals": 18,
        "name": "Atlantis",
        "address": "0x1fd991fb6c3102873ba68a4e6e6a87b3a5c10271"
    },
    "ATM": {
        "symbol": "ATM",
        "decimals": 2,
        "name": "Atletico de Madrid",
        "address": "0x25e9d05365c867e59c1904e7463af9f312296f9e"
    },
    "ATOM": {
        "symbol": "ATOM",
        "decimals": 18,
        "name": "Cosmos Token",
        "address": "0x0eb3a705fc54725037cc9e008bdede697f62f335"
    },
    "ATOZ": {
        "symbol": "ATOZ",
        "decimals": 18,
        "name": "Race_Kingdom",
        "address": "0x3606f220daeaeb3d47ac1923a8ce2a61205c88cd"
    },
    "ATPAD": {
        "symbol": "ATPAD",
        "decimals": 18,
        "name": "AtomPad",
        "address": "0x48ee0cc862143772feabaf9b4757c36735d1052e"
    },
    "ATR": {
        "symbol": "ATR",
        "decimals": 9,
        "name": "Artrade Token",
        "address": "0x7559c49c3aec50e763a486bb232fa8d0d76078e4"
    },
    "ATX": {
        "symbol": "ATX",
        "decimals": 18,
        "name": "AstroX",
        "address": "0xf892bb5a36c4457901130e041bdeb470bd72242f"
    },
    "AU": {
        "symbol": "AU",
        "decimals": 18,
        "name": "AutoCrypto",
        "address": "0x8ea2f890cb86dfb0e376137451c6fd982afefc15"
    },
    "AURA": {
        "symbol": "AURA",
        "decimals": 6,
        "name": "Aura",
        "address": "0x23c5d1164662758b3799103effe19cc064d897d6"
    },
    "AUTO": {
        "symbol": "AUTO",
        "decimals": 18,
        "name": "AUTOv2",
        "address": "0xa184088a740c695e156f91f5cc086a06bb78b827"
    },
    "AVA": {
        "symbol": "AVA",
        "decimals": 18,
        "name": "Travala.com Token",
        "address": "0x13616f44ba82d63c8c0dc3ff843d36a8ec1c05a9"
    },
    "AVAX": {
        "symbol": "AVAX",
        "decimals": 18,
        "name": "Avalanche",
        "address": "0x1ce0c2827e2ef14d5c4f29a091d735a204794041"
    },
    "AVG": {
        "symbol": "AVG",
        "decimals": 18,
        "name": "Avocado DAO Token",
        "address": "0xa41f142b6eb2b164f8164cae0716892ce02f311f"
    },
    "AVN": {
        "symbol": "AVN",
        "decimals": 18,
        "name": "AVNRich Token",
        "address": "0xbf151f63d8d1287db5fc7a3bc104a9c38124cdeb"
    },
    "AVXL": {
        "symbol": "AVXL",
        "decimals": 18,
        "name": "AvaXlauncher",
        "address": "0xbd29490383edfd560426c3b63d01534408bc2da6"
    },
    "AXL": {
        "symbol": "AXL",
        "decimals": 6,
        "name": "Axelar",
        "address": "0x8b1f4432f943c465a973fedc6d7aa50fc96f1f65"
    },
    "axlUSDC": {
        "symbol": "axlUSDC",
        "decimals": 6,
        "name": "Axelar Wrapped USDC",
        "address": "0x4268b8f0b87b6eae5d897996e6b845ddbd99adf3"
    },
    "AZ": {
        "symbol": "AZ",
        "decimals": 18,
        "name": "Azbit",
        "address": "0xaaaafdc2e08371b956be515b3f3ff735ab9c9d74"
    },
    "AZY": {
        "symbol": "AZY",
        "decimals": 18,
        "name": "Amazy Token",
        "address": "0x7b665b2f633d9363b89a98b094b1f9e732bd8f86"
    },
    "B2M": {
        "symbol": "B2M",
        "decimals": 18,
        "name": "Bit2Me",
        "address": "0x6e2a5ea25b161befa6a8444c71ae3a89c39933c6"
    },
    "BABBC": {
        "symbol": "BABBC",
        "decimals": 8,
        "name": "Binance ABBC",
        "address": "0xe83ce6bfb580583bd6a62b4be7b34fc25f02910d"
    },
    "BABI": {
        "symbol": "BABI",
        "decimals": 18,
        "name": "Babylons Governance Token",
        "address": "0xec15a508a187e8ddfe572a5423faa82bbdd65120"
    },
    "BABY": {
        "symbol": "BABY",
        "decimals": 18,
        "name": "BabySwap Token",
        "address": "0x53e562b9b7e5e94b81f10e96ee70ad06df3d2657"
    },
    "BabyBNBTiger": {
        "symbol": "BabyBNBTiger",
        "decimals": 9,
        "name": "BabyBNBTiger",
        "address": "0x5a04565ee1c90c84061ad357ae9e2f1c32d57dc6"
    },
    "BabyCEO": {
        "symbol": "BabyCEO",
        "decimals": 9,
        "name": "Baby Doge CEO",
        "address": "0xed1a89fa419e3d1042d4ea2e938fb62a216594c6"
    },
    "BabyDoge": {
        "symbol": "BabyDoge",
        "decimals": 9,
        "name": "Baby Doge Coin",
        "address": "0xc748673057861a797275cd8a068abb95a902e8de"
    },
    "BABYPEPE": {
        "symbol": "BABYPEPE",
        "decimals": 9,
        "name": "BabyPepe",
        "address": "0xb65528415eb3d737033fe9101a536f6e4c27a8b0"
    },
    "babyrabbit": {
        "symbol": "babyrabbit",
        "decimals": 18,
        "name": "babyrabbit",
        "address": "0xf20f2ad6a36e9a4f585755aceb0da750de80ed4e"
    },
    "BabyShibaInu": {
        "symbol": "BabyShibaInu",
        "decimals": 9,
        "name": "Baby Shiba Inu",
        "address": "0xaecf6d1aff214fef70042740054f0f6d0caa98ab"
    },
    "BACON": {
        "symbol": "BACON",
        "decimals": 18,
        "name": "BaconDAO",
        "address": "0x0615dbba33fe61a31c7ed131bda6655ed76748b1"
    },
    "BAFC": {
        "symbol": "BAFC",
        "decimals": 9,
        "name": "BabyApeFunClub",
        "address": "0x035ad59058c557be4532141fbcd60f0998fce413"
    },
    "BAKE": {
        "symbol": "BAKE",
        "decimals": 18,
        "name": "BakeryToken",
        "address": "0xe02df9e3e622debdd69fb838bb799e3f168902c5"
    },
    "BALA": {
        "symbol": "BALA",
        "decimals": 18,
        "name": "SHAMBALA",
        "address": "0x34ba3af693d6c776d73c7fa67e2b2e79be8ef4ed"
    },
    "bAlvey": {
        "symbol": "bAlvey",
        "decimals": 9,
        "name": "Baby Alvey",
        "address": "0x4c496592fd52c2810651b4862cc9fe13940fea31"
    },
    "BAMBOO": {
        "symbol": "BAMBOO",
        "decimals": 18,
        "name": "BambooDeFi",
        "address": "0x198abb2d13faa2e52e577d59209b5c23c20cd6b3"
    },
    "BANANA": {
        "symbol": "BANANA",
        "decimals": 18,
        "name": "ApeSwapFinance Banana",
        "address": "0x603c7f932ed1fc6575303d8fb018fdcbb0f39a95"
    },
    "BAND": {
        "symbol": "BAND",
        "decimals": 18,
        "name": "Band Protocol Token",
        "address": "0xad6caeb32cd2c308980a548bd0bc5aa4306c6c18"
    },
    "BAS": {
        "symbol": "BAS",
        "decimals": 18,
        "name": "BlockApeScissors",
        "address": "0x8ddeec6b677c7c552c9f3563b99e4ff90b862ebc"
    },
    "BAT": {
        "symbol": "BAT",
        "decimals": 18,
        "name": "Basic Attention Token",
        "address": "0x101d82428437127bf1608f699cd651e6abf9766e"
    },
    "BATH": {
        "symbol": "BATH",
        "decimals": 18,
        "name": "Battle Hero Coin",
        "address": "0x0bc89aa98ad94e6798ec822d0814d934ccd0c0ce"
    },
    "BBANK": {
        "symbol": "BBANK",
        "decimals": 18,
        "name": "BlockBank",
        "address": "0xf4b5470523ccd314c6b9da041076e7d79e0df267"
    },
    "BBC": {
        "symbol": "BBC",
        "decimals": 18,
        "name": "Bull BTC Club",
        "address": "0x37e5da11b6a4dc6d2f7abe232cdd30b0b8fc63b1"
    },
    "BBS": {
        "symbol": "BBS",
        "decimals": 18,
        "name": "BBS [via ChainPort.io]",
        "address": "0xa477a79a118a84a0d371a53c8f46f8ce883ec1dd"
    },
    "BBT": {
        "symbol": "BBT",
        "decimals": 8,
        "name": "BitBook",
        "address": "0xd48474e7444727bf500a32d5abe01943f3a59a64"
    },
    "BCA": {
        "symbol": "BCA",
        "decimals": 18,
        "name": "BITCOIVA",
        "address": "0xddae5f343b7768eadaad88a7f520fff54f198211"
    },
    "BCDT": {
        "symbol": "BCDT",
        "decimals": 18,
        "name": "Blockchain Certified Data Token",
        "address": "0x8683e604cdf911cd72652a04bf9d571697a86a60"
    },
    "BCG": {
        "symbol": "BCG",
        "decimals": 18,
        "name": "Block Chain Games",
        "address": "0xaa988635cdb9ca6dedb1d97ddc8e7de4285fe5f6"
    },
    "BCH": {
        "symbol": "BCH",
        "decimals": 18,
        "name": "Bitcoin Cash Token",
        "address": "0x8ff795a6f4d97e7887c79bea79aba5cc76444adf"
    },
    "bCHAIN": {
        "symbol": "bCHAIN",
        "decimals": 18,
        "name": "Chain Games",
        "address": "0x35de111558f691f77f791fb0c08b2d6b931a9d47"
    },
    "BCL": {
        "symbol": "BCL",
        "decimals": 18,
        "name": "BITCOIN LEGEND",
        "address": "0x02b84f8b64e6c67ae6c797ff4ec4efb06ff19b44"
    },
    "BCMC": {
        "symbol": "BCMC",
        "decimals": 18,
        "name": "Blockchain Monster Coin",
        "address": "0xc10358f062663448a3489fc258139944534592ac"
    },
    "BCOIN": {
        "symbol": "BCOIN",
        "decimals": 18,
        "name": "Bomber Coin",
        "address": "0x00e1656e45f18ec6747f5a8496fd39b50b38396d"
    },
    "bCOLX": {
        "symbol": "bCOLX",
        "decimals": 8,
        "name": "ColossusXT",
        "address": "0xf8acf86194443dcde55fc5b9e448e183c290d8cb"
    },
    "bCOT": {
        "symbol": "bCOT",
        "decimals": 18,
        "name": "CoTrader",
        "address": "0x304fc73e86601a61a6c6db5b0eafea587622acdc"
    },
    "BCT": {
        "symbol": "BCT",
        "decimals": 18,
        "name": "BabyChita Token",
        "address": "0xf6d2657ebb5602bf823901412c5e41e030f3ece2"
    },
    "bECH": {
        "symbol": "bECH",
        "decimals": 18,
        "name": "Bridged Echelon",
        "address": "0x00eafc9c1fb1b7f7889c7e91441ab62de0259ad5"
    },
    "BEL": {
        "symbol": "BEL",
        "decimals": 18,
        "name": "Bella Protocol",
        "address": "0x8443f091997f06a61670b735ed92734f5628692f"
    },
    "bELAND": {
        "symbol": "bELAND",
        "decimals": 18,
        "name": "Etherland",
        "address": "0x708cb02ad77e1b245b1640cee51b3cc844bcaef4"
    },
    "BELT": {
        "symbol": "BELT",
        "decimals": 18,
        "name": "BELT Token",
        "address": "0xe0e514c71282b6f4e823703a39374cf58dc3ea4f"
    },
    "BEM": {
        "symbol": "BEM",
        "decimals": 18,
        "name": "Bemil",
        "address": "0x7b86b0836f3454e50c6f6a190cd692bb17da1928"
    },
    "BENX": {
        "symbol": "BENX",
        "decimals": 7,
        "name": "BlueBenx",
        "address": "0x315be92aba5c3aaaf82b0c0c613838342c1416e7"
    },
    "BEPR": {
        "symbol": "BEPR",
        "decimals": 9,
        "name": "BEUROP",
        "address": "0xbf0cf158e84ebacca1b7746e794d507073e5adfe"
    },
    "BETA": {
        "symbol": "BETA",
        "decimals": 18,
        "name": "Beta Token",
        "address": "0xbe1a001fe942f96eea22ba08783140b9dcc09d28"
    },
    "BETH": {
        "symbol": "BETH",
        "decimals": 18,
        "name": "Binance Beacon ETH",
        "address": "0x250632378e573c6be1ac2f97fcdf00515d0aa91b"
    },
    "BETS": {
        "symbol": "BETS",
        "decimals": 18,
        "name": "BetSwirl Token",
        "address": "0x3e0a7c7db7bb21bda290a80c9811de6d47781671"
    },
    "BETU": {
        "symbol": "BETU",
        "decimals": 18,
        "name": "BETU",
        "address": "0x0df1b3f30865c5b324797f8db9d339514cac4e94"
    },
    "BFG": {
        "symbol": "BFG",
        "decimals": 18,
        "name": "BFG Token",
        "address": "0xbb46693ebbea1ac2070e59b4d043b47e2e095f86"
    },
    "BFHT": {
        "symbol": "BFHT",
        "decimals": 6,
        "name": "BeFaster Holder Token",
        "address": "0x577ad06f635b402fc2724efd6a53a3a0aed3d155"
    },
    "BFK": {
        "symbol": "BFK",
        "decimals": 18,
        "name": "BFK WARZONE",
        "address": "0xa5438df34698df262d5ed463f10387c998edc24a"
    },
    "BFT": {
        "symbol": "BFT",
        "decimals": 9,
        "name": "The Big Five Token",
        "address": "0x4b87f578d6fabf381f43bd2197fbb2a877da6ef8"
    },
    "BG": {
        "symbol": "BG",
        "decimals": 18,
        "name": "BunnyPark Game",
        "address": "0xd04c116c4f02f3cca44b7d4e5209225c8779c8b8"
    },
    "BGC": {
        "symbol": "BGC",
        "decimals": 18,
        "name": "BeeToken",
        "address": "0x3eac3819403ff5aec83dc87c93e3ec3951183799"
    },
    "BGN": {
        "symbol": "BGN",
        "decimals": 18,
        "name": "BeatGen",
        "address": "0xe5e0ebb9982ccb9c6e46efee69cbe02ddeb6fcdd"
    },
    "BGS": {
        "symbol": "BGS",
        "decimals": 18,
        "name": "Battle of Guardians Share",
        "address": "0xf339e8c294046e6e7ef6ad4f6fa9e202b59b556b"
    },
    "BGVT": {
        "symbol": "BGVT",
        "decimals": 18,
        "name": "BIT GAME VERSE TOKEN",
        "address": "0xa03110800894b3ccf8723d991d80875561f96777"
    },
    "BHC": {
        "symbol": "BHC",
        "decimals": 18,
        "name": "Billion Happiness",
        "address": "0x6fd7c98458a943f469e1cf4ea85b173f5cd342f4"
    },
    "BHO": {
        "symbol": "BHO",
        "decimals": 18,
        "name": "Bholdus Token",
        "address": "0x8717e80eff08f53a45b4a925009957e14860a8a8"
    },
    "BIB": {
        "symbol": "BIB",
        "decimals": 18,
        "name": "BIBToken",
        "address": "0x2b339d46e157cf93de6a919aa05350e952f67359"
    },
    "BIBI": {
        "symbol": "BIBI",
        "decimals": 18,
        "name": "BIBI",
        "address": "0xfe8bf5b8f5e4eb5f9bc2be16303f7dab8cf56aa8"
    },
    "BIBL": {
        "symbol": "BIBL",
        "decimals": 18,
        "name": "BIBLE COIN",
        "address": "0xdd041e030ade3db3b2221ce681b65f9650f250d7"
    },
    "BIDR": {
        "symbol": "BIDR",
        "decimals": 18,
        "name": "BIDR BEP20",
        "address": "0x9a2f5556e9a637e8fbce886d8e3cf8b316a1d8a2"
    },
    "BIDZ": {
        "symbol": "BIDZ",
        "decimals": 18,
        "name": "Bidz Coin",
        "address": "0xc2ebaa5f640b30c0d6712a6e0656fb816c10a7d4"
    },
    "BIFI": {
        "symbol": "BIFI",
        "decimals": 18,
        "name": "beefy.finance",
        "address": "0xca3f508b8e4dd382ee878a314789373d80a5190a"
    },
    "BIGB": {
        "symbol": "BIGB",
        "decimals": 18,
        "name": "BIGH BULL",
        "address": "0x0bcf5693655a159bd7d9dc5064de9bd692a7b7c6"
    },
    "BIN": {
        "symbol": "BIN",
        "decimals": 18,
        "name": "Binemon",
        "address": "0xe56842ed550ff2794f010738554db45e60730371"
    },
    "BIPX": {
        "symbol": "BIPX",
        "decimals": 18,
        "name": "Minter BIP",
        "address": "0xf2ba89a6f9670459ed5aeefbd8db52be912228b8"
    },
    "BIRD": {
        "symbol": "BIRD",
        "decimals": 18,
        "name": "Bird",
        "address": "0x8780fea4c6b242677d4a397fe1110ac09ce99ad2"
    },
    "BIST": {
        "symbol": "BIST",
        "decimals": 18,
        "name": "pTokens BIST",
        "address": "0xbd525e51384905c6c0936a431bc7efb6c4903ea0"
    },
    "BIT": {
        "symbol": "BIT",
        "decimals": 9,
        "name": "BIT TOKEN",
        "address": "0xc864019047b864b6ab609a968ae2725dfaee808a"
    },
    "BITORB": {
        "symbol": "BITORB",
        "decimals": 18,
        "name": "BITORBIT.com",
        "address": "0xed0c1c9c64ff7c7cc37c3af0dfcf5b02efe0bb5f"
    },
    "BitV": {
        "symbol": "BitV",
        "decimals": 18,
        "name": "BitValley",
        "address": "0xdd8b490001d081ed065239644dae8d1a77b8a91f"
    },
    "BITWALLET": {
        "symbol": "BITWALLET",
        "decimals": 6,
        "name": "BITCOIN E-WALLET",
        "address": "0xc868642d123289f0a6cb34a3c2810a0a46141947"
    },
    "bKANGAL": {
        "symbol": "bKANGAL",
        "decimals": 18,
        "name": "Kangal",
        "address": "0xd632bd021a07af70592ce1e18717ab9aa126decb"
    },
    "BLACK": {
        "symbol": "BLACK",
        "decimals": 18,
        "name": "Black Token",
        "address": "0xa2f1a99a74d4cc072b810b1696239e4dd76221c4"
    },
    "BLAST": {
        "symbol": "BLAST",
        "decimals": 9,
        "name": "SafeBLAST",
        "address": "0xddc0dbd7dc799ae53a98a60b54999cb6ebb3abf0"
    },
    "bLEO": {
        "symbol": "bLEO",
        "decimals": 3,
        "name": "BEP20 LEO",
        "address": "0x6421531af54c7b14ea805719035ebf1e3661c44a"
    },
    "BLI": {
        "symbol": "BLI",
        "decimals": 18,
        "name": "BALI TOKEN",
        "address": "0x42be29132756ddd6e8b3b94584ca0bab20545eec"
    },
    "BLID": {
        "symbol": "BLID",
        "decimals": 18,
        "name": "Bolide",
        "address": "0x766afcf83fd5eaf884b3d529b432ca27a6d84617"
    },
    "blink": {
        "symbol": "blink",
        "decimals": 6,
        "name": "BLinkToken",
        "address": "0x63870a18b6e42b01ef1ad8a2302ef50b7132054f"
    },
    "BLITZ": {
        "symbol": "BLITZ",
        "decimals": 18,
        "name": "Blitz Token",
        "address": "0xf376807dcdbaa0d7fa86e7c9eacc58d11ad710e4"
    },
    "BLKC": {
        "symbol": "BLKC",
        "decimals": 8,
        "name": "BlackHat",
        "address": "0x8626264b6a1b4e920905efd381002aba52ea0eea"
    },
    "BLOCK": {
        "symbol": "BLOCK",
        "decimals": 6,
        "name": "Blockasset",
        "address": "0xbc7a566b85ef73f935e640a06b5a8b031cd975df"
    },
    "BLOVELY": {
        "symbol": "BLOVELY",
        "decimals": 9,
        "name": "Baby Lovely Inu",
        "address": "0x04df8c91fccfd703cd15047bf6c1ce76d335c6ce"
    },
    "BLP": {
        "symbol": "BLP",
        "decimals": 18,
        "name": "Bull Perks",
        "address": "0xfe1d7f7a8f0bda6e415593a2e4f82c64b446d404"
    },
    "BLXM": {
        "symbol": "BLXM",
        "decimals": 18,
        "name": "bloXmove Token",
        "address": "0x40e51e0ec04283e300f12f6bb98da157bb22036e"
    },
    "BLZ": {
        "symbol": "BLZ",
        "decimals": 18,
        "name": "Bluzelle Token ",
        "address": "0x935a544bf5816e3a7c13db2efe3009ffda0acda2"
    },
    "BMON": {
        "symbol": "BMON",
        "decimals": 18,
        "name": "Binamon",
        "address": "0x08ba0619b1e7a582e0bce5bbe9843322c954c340"
    },
    "bMVL": {
        "symbol": "bMVL",
        "decimals": 18,
        "name": "Binance Wrapped MVL",
        "address": "0x5f588efaf8eb57e3837486e834fc5a4e07768d98"
    },
    "BNBP": {
        "symbol": "BNBP",
        "decimals": 18,
        "name": "BNBPot",
        "address": "0x4d9927a8dc4432b93445da94e4084d292438931f"
    },
    "BNBTiger": {
        "symbol": "BNBTiger",
        "decimals": 9,
        "name": "Bnb Tiger Inu",
        "address": "0xac68931b666e086e9de380cfdb0fb5704a35dc2d"
    },
    "BNBx": {
        "symbol": "BNBx",
        "decimals": 18,
        "name": "Liquid Staking BNB",
        "address": "0x1bdd3cf7f79cfb8edbb955f20ad99211551ba275"
    },
    "BNF": {
        "symbol": "BNF",
        "decimals": 18,
        "name": "BonFi",
        "address": "0xca14caf9e8dd2793e7010fc48dfe6c6af8445136"
    },
    "BNI": {
        "symbol": "BNI",
        "decimals": 18,
        "name": "Bitindi Chain",
        "address": "0x77fc65deda64f0cca9e3aea7b9d8521f4151882e"
    },
    "BNU": {
        "symbol": "BNU",
        "decimals": 18,
        "name": "ByteNext",
        "address": "0x4954e0062e0a7668a2fe3df924cd20e6440a7b77"
    },
    "BOB": {
        "symbol": "BOB",
        "decimals": 18,
        "name": "BOB",
        "address": "0xb0b195aefa3650a6908f15cdac7d92f8a5791b0b"
    },
    "BOBC": {
        "symbol": "BOBC",
        "decimals": 18,
        "name": "BOBC",
        "address": "0xce6bd1833bd077f62b2c1f9a777bb829801d6811"
    },
    "BOG": {
        "symbol": "BOG",
        "decimals": 18,
        "name": "Bogged Finance",
        "address": "0xb09fe1613fe03e7361319d2a43edc17422f36b09"
    },
    "BOMB": {
        "symbol": "BOMB",
        "decimals": 18,
        "name": "bomb.money",
        "address": "0x522348779dcb2911539e76a1042aa922f9c47ee3"
    },
    "BONDLY": {
        "symbol": "BONDLY",
        "decimals": 18,
        "name": "Bondly",
        "address": "0x5d0158a5c3ddf47d4ea4517d8db0d76aa2e87563"
    },
    "BONE": {
        "symbol": "BONE",
        "decimals": 18,
        "name": "BONE",
        "address": "0x67915e893b68fbc436a288564fff1476b632b009"
    },
    "BONFIRE": {
        "symbol": "BONFIRE",
        "decimals": 9,
        "name": "Bonfire",
        "address": "0x5e90253fbae4dab78aa351f4e6fed08a64ab5590"
    },
    "BORING": {
        "symbol": "BORING",
        "decimals": 18,
        "name": "BoringDAO",
        "address": "0xffeecbf8d7267757c2dc3d13d730e97e15bfdf7f"
    },
    "BOSS": {
        "symbol": "BOSS",
        "decimals": 9,
        "name": "Boss Token",
        "address": "0x49324d59327fb799813b902db55b2a118d601547"
    },
    "BOT": {
        "symbol": "BOT",
        "decimals": 18,
        "name": "BOT",
        "address": "0x1ab7e7deda201e5ea820f6c02c65fce7ec6bed32"
    },
    "BP": {
        "symbol": "BP",
        "decimals": 18,
        "name": "BunnyPark",
        "address": "0xacb8f52dc63bb752a51186d1c55868adbffee9c1"
    },
    "BPAD": {
        "symbol": "BPAD",
        "decimals": 18,
        "name": "BPAD",
        "address": "0x29132062319aa375e764ef8ef756f2b28c77a9c9"
    },
    "BPLC": {
        "symbol": "BPLC",
        "decimals": 18,
        "name": "BlackPearl Token",
        "address": "0x65c8743a5a266c3512eabd34e65ade42d4355ef1"
    },
    "BPRCY": {
        "symbol": "BPRCY",
        "decimals": 8,
        "name": "Wrapped PRCY",
        "address": "0xdfc3829b127761a3218bfcee7fc92e1232c9d116"
    },
    "bPRIVA": {
        "symbol": "bPRIVA",
        "decimals": 8,
        "name": "PRIVA",
        "address": "0xd0f4afa85a667d27837e9c07c81169869c16dd16"
    },
    "BRAND": {
        "symbol": "BRAND",
        "decimals": 9,
        "name": "BrandPad",
        "address": "0x4d993ec7b44276615bb2f6f20361ab34fbf0ec49"
    },
    "BRB": {
        "symbol": "BRB",
        "decimals": 18,
        "name": "BerylBit",
        "address": "0xca0823d3d04b9faea7803ccb87fa8596775190dd"
    },
    "BRDG": {
        "symbol": "BRDG",
        "decimals": 18,
        "name": "Bridge Token",
        "address": "0x1562c99ad7179b7d1d862ff4e8bff6cc016a97ee"
    },
    "BRE": {
        "symbol": "BRE",
        "decimals": 18,
        "name": "Brewery",
        "address": "0x9ebbeb7f6b842377714eadd987caa4510205107a"
    },
    "BREW": {
        "symbol": "BREW",
        "decimals": 18,
        "name": "CafeSwap Token",
        "address": "0x790be81c3ca0e53974be2688cdb954732c9862e1"
    },
    "BREWLABS": {
        "symbol": "BREWLABS",
        "decimals": 9,
        "name": "Brewlabs",
        "address": "0x6aac56305825f712fd44599e59f2ede51d42c3e7"
    },
    "BRG": {
        "symbol": "BRG",
        "decimals": 18,
        "name": "Bridge",
        "address": "0x6e4a971b81ca58045a2aa982eaa3d50c4ac38f42"
    },
    "BRICKS": {
        "symbol": "BRICKS",
        "decimals": 9,
        "name": "BRICKS",
        "address": "0x13e1070e3a388e53ec35480ff494538f9ffc5b8d"
    },
    "BRIDGE": {
        "symbol": "BRIDGE",
        "decimals": 18,
        "name": "Cross-Chain Bridge Token",
        "address": "0x92868a5255c628da08f550a858a802f5351c5223"
    },
    "BRISE": {
        "symbol": "BRISE",
        "decimals": 9,
        "name": "Bitrise Token",
        "address": "0x8fff93e810a2edaafc326edee51071da9d398e83"
    },
    "BRKL": {
        "symbol": "BRKL",
        "decimals": 18,
        "name": "Brokoli Token [via ChainPort.io]",
        "address": "0x66cafcf6c32315623c7ffd3f2ff690aa36ebed38"
    },
    "BRN": {
        "symbol": "BRN",
        "decimals": 18,
        "name": "BRN Metaverse",
        "address": "0x926ecc7687fcfb296e97a2b4501f41a6f5f8c214"
    },
    "Brs": {
        "symbol": "Brs",
        "decimals": 18,
        "name": "Broovs",
        "address": "0x98c6fd0281a9a0300cb88553bf386a3492bb70f7"
    },
    "BRT": {
        "symbol": "BRT",
        "decimals": 18,
        "name": "BRT",
        "address": "0xfc9f81b107f51f2383fce56650fedb59c5fd59bd"
    },
    "BRY": {
        "symbol": "BRY",
        "decimals": 18,
        "name": "Berry Tributes",
        "address": "0xf859bf77cbe8699013d6dbc7c2b926aaf307f830"
    },
    "BSC-HO": {
        "symbol": "BSC-HO",
        "decimals": 18,
        "name": "Binance-Peg BSC-HO",
        "address": "0x41515885251e724233c6ca94530d6dcf3a20dec7"
    },
    "BSCD": {
        "symbol": "BSCD",
        "decimals": 18,
        "name": "BSCDium Token",
        "address": "0xe0387845f8289fd5875e7193064392e061f46e58"
    },
    "BSCPAD": {
        "symbol": "BSCPAD",
        "decimals": 18,
        "name": "BSCPAD.com",
        "address": "0x5a3010d4d8d3b5fb49f8b6e57fb9e48063f16700"
    },
    "BSCS": {
        "symbol": "BSCS",
        "decimals": 18,
        "name": "BSCS Token",
        "address": "0xbcb24afb019be7e93ea9c43b7e22bb55d5b7f45d"
    },
    "BSCX": {
        "symbol": "BSCX",
        "decimals": 18,
        "name": "BSCX",
        "address": "0x5ac52ee5b2a633895292ff6d8a89bb9190451587"
    },
    "BSHARE": {
        "symbol": "BSHARE",
        "decimals": 18,
        "name": "BSHARE",
        "address": "0x531780face85306877d7e1f05d713d1b50a37f7a"
    },
    "BSR": {
        "symbol": "BSR",
        "decimals": 18,
        "name": "BinStarter",
        "address": "0xab287e6d370c61f105630e656b5468acb4d00423"
    },
    "BSW": {
        "symbol": "BSW",
        "decimals": 18,
        "name": "Biswap",
        "address": "0x965f527d9159dce6288a2219db51fc6eef120dd1"
    },
    "BTAF": {
        "symbol": "BTAF",
        "decimals": 18,
        "name": "BTAF",
        "address": "0xcae3d82d63e2b0094bc959752993d3d3743b5d08"
    },
    "BTCI": {
        "symbol": "BTCI",
        "decimals": 9,
        "name": "BITCOIN INTERNATIONAL",
        "address": "0x79f8e9862c5240f316fabf31e5406e497d65484d"
    },
    "BTCMT": {
        "symbol": "BTCMT",
        "decimals": 18,
        "name": "Minto Bitcoin Hashrate Token",
        "address": "0x410a56541bd912f9b60943fcb344f1e3d6f09567"
    },
    "BTCST": {
        "symbol": "BTCST",
        "decimals": 17,
        "name": "StandardBTCHashrateToken",
        "address": "0x78650b139471520656b9e7aa7a5e9276814a38e9"
    },
    "BTE": {
        "symbol": "BTE",
        "decimals": 18,
        "name": "Betero",
        "address": "0x7faaf8d4c411218415d9d3f82d56214658349dbb"
    },
    "BTH": {
        "symbol": "BTH",
        "decimals": 18,
        "name": "Bit Hotel Token",
        "address": "0x57bc18f6177cdaffb34ace048745bc913a1b1b54"
    },
    "BTL": {
        "symbol": "BTL",
        "decimals": 6,
        "name": "Bitlocus Token",
        "address": "0x51e7b598c9155b9dccb04eb42519f6eec9c841e9"
    },
    "BTNTV2": {
        "symbol": "BTNTV2",
        "decimals": 18,
        "name": "BitNautic Token V2",
        "address": "0xcbd787129d6e36225d93e46fa08556cc7f3a2458"
    },
    "BTSC": {
        "symbol": "BTSC",
        "decimals": 18,
        "name": "BTS Chain",
        "address": "0x18e596bcefdd0ff9dc8c50d0b9d329ea770d5ef1"
    },
    "BTT": {
        "symbol": "BTT",
        "decimals": 18,
        "name": "BitTorrent",
        "address": "0x8595f9da7b868b1822194faed312235e43007b49"
    },
    "BTYC": {
        "symbol": "BTYC",
        "decimals": 18,
        "name": "BigTycoon",
        "address": "0x42dabca1af369fbd9e8ea286dafba45b23fc92d9"
    },
    "BUILD": {
        "symbol": "BUILD",
        "decimals": 18,
        "name": "Build Token",
        "address": "0x83b27de2fca046fa63a11c7ce7743de33ec58822"
    },
    "BULL": {
        "symbol": "BULL",
        "decimals": 18,
        "name": "BULL COIN",
        "address": "0xf483af09917ba63f1e274056978036d266eb56e6"
    },
    "BUNI": {
        "symbol": "BUNI",
        "decimals": 18,
        "name": "Buni Token",
        "address": "0x0e7beec376099429b85639eb3abe7cf22694ed49"
    },
    "BUNNY": {
        "symbol": "BUNNY",
        "decimals": 18,
        "name": "Bunny Token",
        "address": "0xc9849e6fdb743d08faee3e34dd2d1bc69ea11a51"
    },
    "BUPI": {
        "symbol": "BUPI",
        "decimals": 18,
        "name": "Pawtocol Network UPI Token",
        "address": "0x0d35a2b85c5a63188d566d104bebf7c694334ee4"
    },
    "BURD": {
        "symbol": "BURD",
        "decimals": 9,
        "name": "tudaBirds",
        "address": "0x00ceb4868501b456207856bb6f949c3d2af09a66"
    },
    "BURGER": {
        "symbol": "BURGER",
        "decimals": 18,
        "name": "Burger Swap",
        "address": "0xae9269f27437f0fcbc232d39ec814844a51d6b8f"
    },
    "BUUN": {
        "symbol": "BUUN",
        "decimals": 18,
        "name": "Business Universe",
        "address": "0x15b09ca8a1ef990c726d1fd82939a7cf9a48d5c8"
    },
    "BUX": {
        "symbol": "BUX",
        "decimals": 18,
        "name": "BUX Token",
        "address": "0x211ffbe424b90e25a15531ca322adf1559779e45"
    },
    "BUY": {
        "symbol": "BUY",
        "decimals": 18,
        "name": "BUY Token",
        "address": "0x40225c6277b29bf9056b4acb7ee1512cbff11671"
    },
    "BVC": {
        "symbol": "BVC",
        "decimals": 18,
        "name": "BattleVerse Coin",
        "address": "0x9bee0c15676a65ef3c8cdb38cb3dd31c675bbd12"
    },
    "BVT": {
        "symbol": "BVT",
        "decimals": 18,
        "name": "Bovine Verse Token",
        "address": "0x1dacbcd9b3fc2d6a341dca3634439d12bc71ca4d"
    },
    "BWJ": {
        "symbol": "BWJ",
        "decimals": 9,
        "name": "Baby Woj",
        "address": "0x83f41c98d028842ccc8060b4ec7738df3eb9a2e6"
    },
    "bwJUP": {
        "symbol": "bwJUP",
        "decimals": 18,
        "name": "BSC Wrapped Jupiter",
        "address": "0x0231f91e02debd20345ae8ab7d71a41f8e140ce7"
    },
    "BX": {
        "symbol": "BX",
        "decimals": 18,
        "name": "BlockXpress",
        "address": "0x2a6788bf2354ebc4940656d4721afa0ad0f25f6b"
    },
    "bXEN": {
        "symbol": "bXEN",
        "decimals": 18,
        "name": "XEN Crypto",
        "address": "0x2ab0e9e4ee70fff1fb9d67031e44f6410170d00e"
    },
    "BZEN": {
        "symbol": "BZEN",
        "decimals": 9,
        "name": "BITZEN",
        "address": "0xdacc0417add48b63cbefb77efbe4a3801aad51ba"
    },
    "C98": {
        "symbol": "C98",
        "decimals": 18,
        "name": "Coin98",
        "address": "0xaec945e04baf28b135fa7c640f624f8d90f1c3a6"
    },
    "CADINU": {
        "symbol": "CADINU",
        "decimals": 18,
        "name": "Canadian Inuit Dog V2",
        "address": "0x76e112203ef59d445452ef7556386dd2df3ed914"
    },
    "CAI": {
        "symbol": "CAI",
        "decimals": 9,
        "name": "Crypto AI",
        "address": "0x3cef8d4cc106a169902ea985cec2dc6ab055ad4c"
    },
    "CAL": {
        "symbol": "CAL",
        "decimals": 18,
        "name": "Fitburn",
        "address": "0x859c940f080b197659b3effc804fd622df66f0a1"
    },
    "CALO": {
        "symbol": "CALO",
        "decimals": 18,
        "name": "CALO",
        "address": "0xb6b91269413b6b99242b1c0bc611031529999999"
    },
    "CAPO": {
        "symbol": "CAPO",
        "decimals": 18,
        "name": "ILCAPO",
        "address": "0x922722e9ef614ec9a3e94b78496e92abfbb5a624"
    },
    "CAPS": {
        "symbol": "CAPS",
        "decimals": 18,
        "name": "Capsule Coin",
        "address": "0xffba7529ac181c2ee1844548e6d7061c9a597df4"
    },
    "CAPY": {
        "symbol": "CAPY",
        "decimals": 18,
        "name": "Capybara Coin",
        "address": "0x0aec1e4ce3cd3ccee64ff1a2ee47770fd2b0d8d3"
    },
    "CARAT": {
        "symbol": "CARAT",
        "decimals": 18,
        "name": "AlaskaGoldRush",
        "address": "0x426c1c971fb00caaf1883bd801323a8becb0c919"
    },
    "CARBO": {
        "symbol": "CARBO",
        "decimals": 18,
        "name": "CLEANCARBON",
        "address": "0xa52262da176186105199a597ac8cf094ff71b0c5"
    },
    "CAS": {
        "symbol": "CAS",
        "decimals": 18,
        "name": " Cashaa",
        "address": "0x780207b8c0fdc32cf60e957415bfa1f2d4d9718c"
    },
    "CAT": {
        "symbol": "CAT",
        "decimals": 18,
        "name": "Cat",
        "address": "0x0173295183685f27c84db046b5f0bea3e683c24b"
    },
    "CATCOIN": {
        "symbol": "CATCOIN",
        "decimals": 9,
        "name": "Catcoin",
        "address": "0x06df77854793849f770b6af0af4b22511df53a11"
    },
    "CATE": {
        "symbol": "CATE",
        "decimals": 9,
        "name": "CateCoin",
        "address": "0xe4fae3faa8300810c835970b9187c268f55d998f"
    },
    "CATGIRL": {
        "symbol": "CATGIRL",
        "decimals": 9,
        "name": "CatGirl",
        "address": "0x79ebc9a2ce02277a4b5b3a768b1c0a4ed75bd936"
    },
    "CATS": {
        "symbol": "CATS",
        "decimals": 0,
        "name": "Catcoin",
        "address": "0x2f0c6e147974bfbf7da557b88643d74c324053a2"
    },
    "CATVILLS": {
        "symbol": "CATVILLS",
        "decimals": 8,
        "name": "CATVILLSCOIN",
        "address": "0xa531a733070a5ff4866d1327d82e403fa35290a6"
    },
    "CAWCEO": {
        "symbol": "CAWCEO",
        "decimals": 18,
        "name": "CAW CEO",
        "address": "0xd96e43fb44be20e9e9a5872ce1904ebaa9975ead"
    },
    "CBD": {
        "symbol": "CBD",
        "decimals": 18,
        "name": "Greenheart",
        "address": "0x0e2b41ea957624a314108cc4e33703e9d78f4b3c"
    },
    "CBIX-P": {
        "symbol": "CBIX-P",
        "decimals": 18,
        "name": "Cubiex Power",
        "address": "0x39bff8613defd221b0410ed3d4e5c07512d55f2d"
    },
    "CBSL": {
        "symbol": "CBSL",
        "decimals": 18,
        "name": "CeBioLabs",
        "address": "0xbfb8f92e8f3a9034019ac97fd9f85c6dfb513834"
    },
    "CC": {
        "symbol": "CC",
        "decimals": 18,
        "name": "CloudChat Token",
        "address": "0x0c2bfa54d6d4231b6213803df616a504767020ea"
    },
    "CCGDS": {
        "symbol": "CCGDS",
        "decimals": 18,
        "name": "CCGDS",
        "address": "0x1baadfd674c641149b0d5a39e697ec877ab47083"
    },
    "CCHG": {
        "symbol": "CCHG",
        "decimals": 18,
        "name": "C+Charge",
        "address": "0x24f2f371d74b25da7597adeae55895fe6b5c2fde"
    },
    "CCOIN": {
        "symbol": "CCOIN",
        "decimals": 18,
        "name": "CRYPTERIUM COIN",
        "address": "0xc209831f7349d4e200d420326b3401899ab9ae68"
    },
    "CDT": {
        "symbol": "CDT",
        "decimals": 18,
        "name": "CheckDot",
        "address": "0x0cbd6fadcf8096cc9a43d90b45f65826102e3ece"
    },
    "CDTC": {
        "symbol": "CDTC",
        "decimals": 18,
        "name": "Credit Coin",
        "address": "0x0faf802036e30b4b58a20c359012821152872397"
    },
    "CEEK": {
        "symbol": "CEEK",
        "decimals": 18,
        "name": "CEEK",
        "address": "0xe0f94ac5462997d2bc57287ac3a3ae4c31345d66"
    },
    "CELLS ": {
        "symbol": "CELLS ",
        "decimals": 18,
        "name": "CellsToken",
        "address": "0x3022d80e02075f5a2a442a318229487f9ea66d82"
    },
    "CELR": {
        "symbol": "CELR",
        "decimals": 18,
        "name": "CelerToken",
        "address": "0x1f9f6a696c6fd109cd3956f45dc709d2b3902163"
    },
    "CENS": {
        "symbol": "CENS",
        "decimals": 8,
        "name": "CENTURY",
        "address": "0x9e1fd9ba2590af57f926177850eae1611d447874"
    },
    "CENT": {
        "symbol": "CENT",
        "decimals": 18,
        "name": "Centaurify",
        "address": "0xb9b41da7fa895b093b95340a3379383bba36735e"
    },
    "CENX": {
        "symbol": "CENX",
        "decimals": 9,
        "name": "Centcex",
        "address": "0x739e81bcd49854d7bdf526302989f14a2e7994b2"
    },
    "CEO": {
        "symbol": "CEO",
        "decimals": 18,
        "name": "CEO",
        "address": "0x237ace23ab2c36a004aa5e4fb134fe5c1cedf06c"
    },
    "CERBY": {
        "symbol": "CERBY",
        "decimals": 18,
        "name": "Cerby Token",
        "address": "0xdef1fac7bf08f173d286bbbdcbeeade695129840"
    },
    "CFi": {
        "symbol": "CFi",
        "decimals": 18,
        "name": "CyberFi Token",
        "address": "0x6a545f9c64d8f7b957d8d2e6410b52095a9e6c29"
    },
    "CGG": {
        "symbol": "CGG",
        "decimals": 18,
        "name": "pTokens CGG",
        "address": "0x1613957159e9b0ac6c80e824f7eea748a32a0ae2"
    },
    "CGPT": {
        "symbol": "CGPT",
        "decimals": 18,
        "name": "ChainGPT",
        "address": "0x9840652dc04fb9db2c43853633f0f62be6f00f98"
    },
    "CGU": {
        "symbol": "CGU",
        "decimals": 8,
        "name": "Crypto Gaming United",
        "address": "0x747d74db20cc422f39ab54edb2a3ce21f3c98af1"
    },
    "CHA": {
        "symbol": "CHA",
        "decimals": 18,
        "name": "Chains",
        "address": "0xa037f4cb3d319876cdbe585c89663c246615c975"
    },
    "CHAOS": {
        "symbol": "CHAOS",
        "decimals": 18,
        "name": "WarriorEmpires.io",
        "address": "0x1c5a65ededa96e7daf0715d978cc643184fbbd6c"
    },
    "CHEEL": {
        "symbol": "CHEEL",
        "decimals": 18,
        "name": "CHEELEE",
        "address": "0x1f1c90aeb2fd13ea972f0a71e35c0753848e3db0"
    },
    "CHEERS": {
        "symbol": "CHEERS",
        "decimals": 18,
        "name": "CHEERS",
        "address": "0xbbbcb350c64fe974e5c42a55c7070644191823f3"
    },
    "CHER": {
        "symbol": "CHER",
        "decimals": 18,
        "name": "Cherry Token",
        "address": "0x8f36cc333f55b09bb71091409a3d7ade399e3b1c"
    },
    "CHESS": {
        "symbol": "CHESS",
        "decimals": 18,
        "name": "Chess",
        "address": "0x20de22029ab63cf9a7cf5feb2b737ca1ee4c82a6"
    },
    "CHEX": {
        "symbol": "CHEX",
        "decimals": 18,
        "name": "Chintai Exchange Token",
        "address": "0x9ce84f6a69986a83d92c324df10bc8e64771030f"
    },
    "CHITCAT": {
        "symbol": "CHITCAT",
        "decimals": 18,
        "name": "ChitCAT",
        "address": "0x7cf551258d6871b72ee1bd1624588a6245bf48c4"
    },
    "CHMB": {
        "symbol": "CHMB",
        "decimals": 18,
        "name": "Chumbi Valley",
        "address": "0x5492ef6aeeba1a3896357359ef039a8b11621b45"
    },
    "CHR": {
        "symbol": "CHR",
        "decimals": 6,
        "name": "Chroma",
        "address": "0xf9cec8d50f6c8ad3fb6dccec577e05aa32b224fe"
    },
    "CHRP": {
        "symbol": "CHRP",
        "decimals": 18,
        "name": "Chirpley Token",
        "address": "0xed00fc7d48b57b81fe65d1ce71c0985e4cf442cb"
    },
    "CHT": {
        "symbol": "CHT",
        "decimals": 18,
        "name": "CyberHarbor",
        "address": "0x67d8e0080b612afae75a7f7229bfed3cdb998462"
    },
    "CINU": {
        "symbol": "CINU",
        "decimals": 9,
        "name": "CheemsInu",
        "address": "0x842defb310cace2b923c1fd7b3db067d3d0fcc34"
    },
    "CIRUS": {
        "symbol": "CIRUS",
        "decimals": 18,
        "name": "Cirus",
        "address": "0x4c888e116d57a32f84865f3789dcb131fdc9fab6"
    },
    "CJET": {
        "symbol": "CJET",
        "decimals": 18,
        "name": "CryptoJetski",
        "address": "0x38fc43bbddb64cd23bc8d085f88722ab1f9a6c50"
    },
    "CKP": {
        "symbol": "CKP",
        "decimals": 18,
        "name": "CakePad",
        "address": "0x81f7bbfc362994badcdcae1b38d426be4d82894a"
    },
    "CLCT": {
        "symbol": "CLCT",
        "decimals": 18,
        "name": "CollectCoin",
        "address": "0x3249fa9e11efece7cb03b4ad2994f46e54a35843"
    },
    "CLEG": {
        "symbol": "CLEG",
        "decimals": 18,
        "name": "Chain of Legends Token",
        "address": "0x4027d91ecd3140e53ae743d657549adfeebb27ab"
    },
    "CLNX": {
        "symbol": "CLNX",
        "decimals": 8,
        "name": "Coloniume",
        "address": "0x9ece397ec3d23fc6ae356545d63fa4348dbb038d"
    },
    "CLOAK": {
        "symbol": "CLOAK",
        "decimals": 9,
        "name": "Cloak Coin",
        "address": "0x8077398ff2c530f129a6dd8d7f1e8840312440cd"
    },
    "Cloud": {
        "symbol": "Cloud",
        "decimals": 9,
        "name": "CloudTx",
        "address": "0xffad7f9f704a5fdc6265e24b436b4b35ed52def2"
    },
    "CLS": {
        "symbol": "CLS",
        "decimals": 18,
        "name": "Coldstack",
        "address": "0x668048e70284107a6afab1711f28d88df3e72948"
    },
    "CLU": {
        "symbol": "CLU",
        "decimals": 9,
        "name": "CluCoin",
        "address": "0x1162e2efce13f99ed259ffc24d99108aaa0ce935"
    },
    "CLV": {
        "symbol": "CLV",
        "decimals": 18,
        "name": "Clover",
        "address": "0x09e889bb4d5b474f561db0491c38702f367a4e4d"
    },
    "CMAI": {
        "symbol": "CMAI",
        "decimals": 18,
        "name": "CoinMatch Ai",
        "address": "0x77140a6f53c09c36abf10ef947655317a7670a3b"
    },
    "CMCX": {
        "symbol": "CMCX",
        "decimals": 18,
        "name": "CORE MultiChain Token",
        "address": "0xb2343143f814639c9b1f42961c698247171df34a"
    },
    "CMQ": {
        "symbol": "CMQ",
        "decimals": 18,
        "name": "COMMUNIQUE",
        "address": "0x074e91c178e4b4c6228357a5a0b6df5ad824f0d8"
    },
    "CNAME": {
        "symbol": "CNAME",
        "decimals": 18,
        "name": "Cloudname",
        "address": "0xfc3514474306e2d4aa8350fd8fa9c46c165fe8cd"
    },
    "CNS": {
        "symbol": "CNS",
        "decimals": 8,
        "name": "Centric SWAP",
        "address": "0xf6cb4ad242bab681effc5de40f7c8ff921a12d63"
    },
    "CO": {
        "symbol": "CO",
        "decimals": 6,
        "name": "CO",
        "address": "0x936b6659ad0c1b244ba8efe639092acae30dc8d6"
    },
    "COGI": {
        "symbol": "COGI",
        "decimals": 18,
        "name": "COGI Coin",
        "address": "0x6cb755c4b82e11e727c05f697c790fdbc4253957"
    },
    "COINSALE": {
        "symbol": "COINSALE",
        "decimals": 18,
        "name": "CoinSale Token",
        "address": "0xaf099ef77575a9f981660b1c9e3b78a3ba89ffd9"
    },
    "COINSCOPE": {
        "symbol": "COINSCOPE",
        "decimals": 18,
        "name": "Coinscope",
        "address": "0xd41c4805a9a3128f9f7a7074da25965371ba50d5"
    },
    "COL": {
        "symbol": "COL",
        "decimals": 18,
        "name": "Clash of lilliput",
        "address": "0x9ce116224459296abc7858627abd5879514bc629"
    },
    "COLLIE": {
        "symbol": "COLLIE",
        "decimals": 18,
        "name": "COLLIE INU",
        "address": "0x31491c35c094a0336f4859dd94ab9466709dec45"
    },
    "COMP": {
        "symbol": "COMP",
        "decimals": 18,
        "name": "Compound Coin",
        "address": "0x52ce071bd9b1c4b00a0b92d298c512478cad67e8"
    },
    "COOK": {
        "symbol": "COOK",
        "decimals": 18,
        "name": "Poly-Peg COOK",
        "address": "0x965b0df5bda0e7a0649324d78f03d5f7f2de086a"
    },
    "COOKIE": {
        "symbol": "COOKIE",
        "decimals": 18,
        "name": "CookieSale",
        "address": "0x6d342877fc199c629f49a5c6c521c297b15bc92d"
    },
    "COP": {
        "symbol": "COP",
        "decimals": 18,
        "name": "Copiosa Coin",
        "address": "0x8789337a176e6e7223ff115f1cd85c993d42c25c"
    },
    "COPI": {
        "symbol": "COPI",
        "decimals": 18,
        "name": "Cornucopias [via ChainPort.io]",
        "address": "0xfea292e5ea4510881bdb840e3cec63abd43f936f"
    },
    "COPYCAT": {
        "symbol": "COPYCAT",
        "decimals": 18,
        "name": "Copycat Token",
        "address": "0xd635b32688f36ee4a7fe117b4c91dd811277acb6"
    },
    "COR": {
        "symbol": "COR",
        "decimals": 18,
        "name": "COR Token",
        "address": "0xa4b6573c9ae09d81e4d1360e6402b81f52557098"
    },
    "CORAI": {
        "symbol": "CORAI",
        "decimals": 18,
        "name": "CORAI",
        "address": "0x17c8c198c06f16a8db68148d9ac460f5aed029d8"
    },
    "CORGIB": {
        "symbol": "CORGIB",
        "decimals": 18,
        "name": "The Corgi of PolkaBrige",
        "address": "0x1cfd6813a59d7b90c41dd5990ed99c3bf2eb8f55"
    },
    "CORX": {
        "symbol": "CORX",
        "decimals": 18,
        "name": "CorionX",
        "address": "0x141383cdb8158982fb3469c3e49cc82f8026d968"
    },
    "COS": {
        "symbol": "COS",
        "decimals": 18,
        "name": "Cradle of Sins",
        "address": "0x4d9f39f7cb7c7444335077223ceef33dbb58096f"
    },
    "COSMIC": {
        "symbol": "COSMIC",
        "decimals": 18,
        "name": "COSMIC FOMO",
        "address": "0xbabacc135bbf2ce30f9c0f12665b244d3689a29c"
    },
    "COTI": {
        "symbol": "COTI",
        "decimals": 18,
        "name": "COTI Token",
        "address": "0xadbaf88b39d37dc68775ed1541f1bf83a5a45feb"
    },
    "COV": {
        "symbol": "COV",
        "decimals": 18,
        "name": "Covesting",
        "address": "0x0f237db17aa4e6de062e6f052bd9c805789b01c3"
    },
    "COVAL": {
        "symbol": "COVAL",
        "decimals": 8,
        "name": "Circuits of Value V2",
        "address": "0xd15cee1deafbad6c0b3fd7489677cc102b141464"
    },
    "COW": {
        "symbol": "COW",
        "decimals": 18,
        "name": "CoinWind Token",
        "address": "0x422e3af98bc1de5a1838be31a56f75db4ad43730"
    },
    "COWRIE": {
        "symbol": "COWRIE",
        "decimals": 18,
        "name": "Cowrie",
        "address": "0xde51d1599339809cafb8194189ce67d5bdca9e9e"
    },
    "CPAN": {
        "symbol": "CPAN",
        "decimals": 18,
        "name": "CryptoPlanes",
        "address": "0x04260673729c5f2b9894a467736f3d85f8d34fc8"
    },
    "CPD": {
        "symbol": "CPD",
        "decimals": 18,
        "name": "Coinspaid",
        "address": "0x2406dce4da5ab125a18295f4fb9fd36a0f7879a2"
    },
    "CPO": {
        "symbol": "CPO",
        "decimals": 18,
        "name": "Cryptopolis",
        "address": "0xea395dfafed39924988b475f2ca7f4c72655203a"
    },
    "CPOS": {
        "symbol": "CPOS",
        "decimals": 18,
        "name": "Cpos Cloud Payment",
        "address": "0xc0dc5adfae1dada9111f376810d772cabd9b6f13"
    },
    "CPS": {
        "symbol": "CPS",
        "decimals": 18,
        "name": "Cryptostone",
        "address": "0x569f4957176ffa0dff76c507604f6a66d4b9c578"
    },
    "CRA": {
        "symbol": "CRA",
        "decimals": 5,
        "name": "CRACLE",
        "address": "0x0fc0b3f6f5c769c138088266ac21760ab33f76ca"
    },
    "CRACE": {
        "symbol": "CRACE",
        "decimals": 18,
        "name": "Coinracer",
        "address": "0xfbb4f2f342c6daab63ab85b0226716c4d1e26f36"
    },
    "CRBN": {
        "symbol": "CRBN",
        "decimals": 18,
        "name": "Carbon",
        "address": "0x5a4fb10e7c4cbb9a2b9d9a942f9a875ebd3489ea"
    },
    "CREAM": {
        "symbol": "CREAM",
        "decimals": 18,
        "name": "Cream",
        "address": "0xd4cb328a82bdf5f03eb737f37fa6b370aef3e888"
    },
    "CREDI": {
        "symbol": "CREDI",
        "decimals": 18,
        "name": "CREDI [via ChainPort.io]",
        "address": "0x2235e79086dd23135119366da45851c741874e5b"
    },
    "CREO": {
        "symbol": "CREO",
        "decimals": 18,
        "name": "CreoEngine",
        "address": "0x9521728bf66a867bc65a93ece4a543d817871eb7"
    },
    "CROOM": {
        "symbol": "CROOM",
        "decimals": 18,
        "name": "CRYPTOSROOM",
        "address": "0xf939cce5b35fb465c920b6602d0de7d40498d5a8"
    },
    "CROWN": {
        "symbol": "CROWN",
        "decimals": 18,
        "name": "KingPad",
        "address": "0x7a3ba320d44192ae9f6c061f15bcebd7a6217242"
    },
    "CRS": {
        "symbol": "CRS",
        "decimals": 18,
        "name": "CRYSTALS",
        "address": "0xa1a5ad28c250b9383c360c0f69ad57d70379851e"
    },
    "CRTS": {
        "symbol": "CRTS",
        "decimals": 18,
        "name": "Cratos BEP20",
        "address": "0x678e840c640f619e17848045d23072844224dd37"
    },
    "CRUX": {
        "symbol": "CRUX",
        "decimals": 18,
        "name": "CryptoMines Reborn",
        "address": "0xe0191fefdd0d2b39b1a2e4e029ccda8a481b7995"
    },
    "CRX": {
        "symbol": "CRX",
        "decimals": 18,
        "name": "CryptEx Token",
        "address": "0x97a30c692ece9c317235d48287d23d358170fc40"
    },
    "CS": {
        "symbol": "CS",
        "decimals": 9,
        "name": "Child Support",
        "address": "0x502b8136c48977b975a6c62b08ac4e15dabc8172"
    },
    "CSIX": {
        "symbol": "CSIX",
        "decimals": 18,
        "name": "Carbon",
        "address": "0x04756126f044634c9a0f0e985e60c88a51acc206"
    },
    "CSPD": {
        "symbol": "CSPD",
        "decimals": 18,
        "name": "CasperPad",
        "address": "0xef9481115ff33e94d3e28a52d3a8f642bf3521e5"
    },
    "CSTC": {
        "symbol": "CSTC",
        "decimals": 18,
        "name": "CryptosTribe",
        "address": "0x78f1a611cceba2ff17ea53570dbee7d43629e8bc"
    },
    "CSWAP": {
        "symbol": "CSWAP",
        "decimals": 18,
        "name": "CrossSwap.com",
        "address": "0xe0b0c16038845bed3fcf70304d3e167df81ce225"
    },
    "CT": {
        "symbol": "CT",
        "decimals": 9,
        "name": "Create",
        "address": "0xa85c461c66038ffc8433e2a961339b7f36656e16"
    },
    "CTG": {
        "symbol": "CTG",
        "decimals": 18,
        "name": "City Tycoon Games",
        "address": "0xb3ba14f6a482dfdebc3c2fb726ac10df91ee504c"
    },
    "CTK": {
        "symbol": "CTK",
        "decimals": 6,
        "name": "CertiK Token",
        "address": "0xa8c2b8eec3d368c0253ad3dae65a5f2bbb89c929"
    },
    "CTN": {
        "symbol": "CTN",
        "decimals": 18,
        "name": "ContinuumFinance",
        "address": "0x4861ba0ce919fee66b41c85a08a7476557914275"
    },
    "CTP": {
        "symbol": "CTP",
        "decimals": 8,
        "name": "CTOMORROW PLATFORM",
        "address": "0xb850cac12ab85d4400db61ac78dc5fc2418b6868"
    },
    "CTR": {
        "symbol": "CTR",
        "decimals": 18,
        "name": "Creator Chain",
        "address": "0xd6cce248263ea1e2b8cb765178c944fc16ed0727"
    },
    "CTSI": {
        "symbol": "CTSI",
        "decimals": 18,
        "name": "Cartesi Token",
        "address": "0x8da443f84fea710266c8eb6bc34b71702d033ef2"
    },
    "CTT": {
        "symbol": "CTT",
        "decimals": 18,
        "name": "CryptoTycoon Token",
        "address": "0x464863745ed3af8b9f8871f1082211c55f8f884d"
    },
    "CTY": {
        "symbol": "CTY",
        "decimals": 18,
        "name": "Custodiy (V3)",
        "address": "0xba08da6b46e3dd153dd8b66a6e4cfd37a6359559"
    },
    "CUB": {
        "symbol": "CUB",
        "decimals": 18,
        "name": "Cub Finance",
        "address": "0x50d809c74e0b8e49e7b4c65bb3109abe3ff4c1c1"
    },
    "CUMMIES": {
        "symbol": "CUMMIES",
        "decimals": 18,
        "name": "CumRocket",
        "address": "0x27ae27110350b98d564b9a3eed31baebc82d878d"
    },
    "CURE": {
        "symbol": "CURE",
        "decimals": 9,
        "name": "CURE Token V2",
        "address": "0x76aecb353abf596bd61ee6bdb07d70787dec4fd6"
    },
    "CURVE": {
        "symbol": "CURVE",
        "decimals": 9,
        "name": "Curve Network",
        "address": "0xecbddf83687e9842837e08c5a650658f2260b376"
    },
    "CUSD": {
        "symbol": "CUSD",
        "decimals": 18,
        "name": "Coin98 Dollar",
        "address": "0xfa4ba88cf97e282c505bea095297786c16070129"
    },
    "CVL": {
        "symbol": "CVL",
        "decimals": 18,
        "name": "Civilization",
        "address": "0x9ae0290cd677dc69a5f2a1e435ef002400da70f5"
    },
    "CWT": {
        "symbol": "CWT",
        "decimals": 18,
        "name": "CROSSWALLET.app",
        "address": "0x5a726a26edb0df8fd55f03cc30af8a7cea81e78d"
    },
    "CXPAD": {
        "symbol": "CXPAD",
        "decimals": 18,
        "name": "CoinxPad",
        "address": "0xe90d1567ecef9282cc1ab348d9e9e2ac95659b99"
    },
    "CYC": {
        "symbol": "CYC",
        "decimals": 18,
        "name": "Cyclone Protocol",
        "address": "0x810ee35443639348adbbc467b33310d2ab43c168"
    },
    "CZR": {
        "symbol": "CZR",
        "decimals": 18,
        "name": "CZRed",
        "address": "0x5cd0c2c744caf04cda258efc6558a3ed3defe97b"
    },
    "D3D": {
        "symbol": "D3D",
        "decimals": 18,
        "name": "D3D",
        "address": "0xd3c7e51caab1089002ec05569a04d14bcc478bc4"
    },
    "DAL": {
        "symbol": "DAL",
        "decimals": 18,
        "name": "DAOLaunch",
        "address": "0x53e4b7aa6caccb9576548be3259e62de4ddd4417"
    },
    "DALI": {
        "symbol": "DALI",
        "decimals": 9,
        "name": "Dali",
        "address": "0x5a119762b09ed0bcb3b16075159ae43a62651383"
    },
    "DAO": {
        "symbol": "DAO",
        "decimals": 18,
        "name": "DAO Maker",
        "address": "0x4d2d32d8652058bf98c772953e1df5c5c85d9f45"
    },
    "DAOP": {
        "symbol": "DAOP",
        "decimals": 18,
        "name": "DaoSpace",
        "address": "0xda179357b3e05cd91e0fde992c7ef4158b37eafb"
    },
    "DAR": {
        "symbol": "DAR",
        "decimals": 6,
        "name": "Dalarnia",
        "address": "0x23ce9e926048273ef83be0a3a8ba9cb6d45cd978"
    },
    "DARA": {
        "symbol": "DARA",
        "decimals": 18,
        "name": "Immutable",
        "address": "0x0255af6c9f86f6b0543357bacefa262a2664f80f"
    },
    "DARC": {
        "symbol": "DARC",
        "decimals": 18,
        "name": "DARC Token",
        "address": "0x8ebc361536094fd5b4ffb8521e31900614c9f55d"
    },
    "DARK": {
        "symbol": "DARK",
        "decimals": 8,
        "name": "Dark Token",
        "address": "0x12fc07081fab7de60987cad8e8dc407b606fb2f8"
    },
    "DATA": {
        "symbol": "DATA",
        "decimals": 18,
        "name": "Streamr",
        "address": "0x0864c156b3c5f69824564dec60c629ae6401bf2a"
    },
    "DBA": {
        "symbol": "DBA",
        "decimals": 8,
        "name": "Digital Bank of Africa",
        "address": "0x1006ea3289b833b6720aaa82746990ec77de8c36"
    },
    "DCB": {
        "symbol": "DCB",
        "decimals": 18,
        "name": "Decubate Token",
        "address": "0xeac9873291ddaca754ea5642114151f3035c67a2"
    },
    "DCO": {
        "symbol": "DCO",
        "decimals": 18,
        "name": "DCOREUM",
        "address": "0xdfa1c5fcd4d64729cdf6d553b2fb1def11a7c689"
    },
    "DCU": {
        "symbol": "DCU",
        "decimals": 9,
        "name": "DecentralizedUnited",
        "address": "0xcb1ddc8f705e2737685a9c1e6b84a63d04d200e5"
    },
    "DDD": {
        "symbol": "DDD",
        "decimals": 18,
        "name": "DotDot",
        "address": "0x84c97300a190676a19d1e13115629a11f8482bd1"
    },
    "DDIM": {
        "symbol": "DDIM",
        "decimals": 18,
        "name": "DuckDaoDime",
        "address": "0xc9132c76060f6b319764ea075973a650a1a53bc9"
    },
    "DDL": {
        "symbol": "DDL",
        "decimals": 18,
        "name": "DeFi Degen Land",
        "address": "0x88803312628fd21542f706b0c7dc8495c1c10b2e"
    },
    "DDOS": {
        "symbol": "DDOS",
        "decimals": 18,
        "name": "Disbalancer",
        "address": "0x7fbec0bb6a7152e77c30d005b5d49cbc08a602c3"
    },
    "DEBT": {
        "symbol": "DEBT",
        "decimals": 8,
        "name": "DEBT",
        "address": "0xc632f90affec7121120275610bf17df9963f181c"
    },
    "DEC": {
        "symbol": "DEC",
        "decimals": 3,
        "name": "DarkEnergyCrystals",
        "address": "0xe9d7023f2132d55cbd4ee1f78273cb7a3e74f10a"
    },
    "DEFIAI": {
        "symbol": "DEFIAI",
        "decimals": 18,
        "name": "DeFiAI Token",
        "address": "0xe1a0ce8b94c6a5e4791401086763d7bd0a6c18f5"
    },
    "DEFX": {
        "symbol": "DEFX",
        "decimals": 18,
        "name": "DeFinity",
        "address": "0xbe4cb2c354480042a39350a0c6c26bf54786539f"
    },
    "DEGEN": {
        "symbol": "DEGEN",
        "decimals": 18,
        "name": "DegenReborn Token",
        "address": "0x1a131f7b106d58f33eaf0fe5b47db2f2045e5732"
    },
    "DEGOV2": {
        "symbol": "DEGOV2",
        "decimals": 18,
        "name": "dego.finance",
        "address": "0x3da932456d082cba208feb0b096d49b202bf89c8"
    },
    "DEK": {
        "symbol": "DEK",
        "decimals": 18,
        "name": "DekBox",
        "address": "0xe52c5a3590952f3ed6fccf89a0bd7f38e11c5b98"
    },
    "DELOT": {
        "symbol": "DELOT",
        "decimals": 18,
        "name": "DELOT.IO",
        "address": "0x3e24bbb2c9a0f2faecfdbdca20bba6f35b73c4cb"
    },
    "DEP": {
        "symbol": "DEP",
        "decimals": 18,
        "name": "DEAPCOIN",
        "address": "0xcaf5191fc480f43e4df80106c7695eca56e48b18"
    },
    "DERC": {
        "symbol": "DERC",
        "decimals": 18,
        "name": "DeRace Token",
        "address": "0x373e768f79c820aa441540d254dca6d045c6d25b"
    },
    "DERI": {
        "symbol": "DERI",
        "decimals": 18,
        "name": "Deri",
        "address": "0xe60eaf5a997dfae83739e035b005a33afdcc6df5"
    },
    "DES": {
        "symbol": "DES",
        "decimals": 18,
        "name": "DeSpace Protocol",
        "address": "0xb38b3c34e4bb6144c1e5283af720e046ee833a2a"
    },
    "DESU": {
        "symbol": "DESU",
        "decimals": 18,
        "name": "Dexsport Protocol Native Token",
        "address": "0x32f1518baace69e85b9e5ff844ebd617c52573ac"
    },
    "DEVO": {
        "symbol": "DEVO",
        "decimals": 18,
        "name": "DeVolution",
        "address": "0x0fd98b8c58560167a236f1d0553a9c2a42342ccf"
    },
    "DEX": {
        "symbol": "DEX",
        "decimals": 9,
        "name": "dexIRA",
        "address": "0x147e07976e1ae78287c33aafaab87760d32e50a5"
    },
    "DEXE": {
        "symbol": "DEXE",
        "decimals": 18,
        "name": "DeXe",
        "address": "0x039cb485212f996a9dbb85a9a75d898f94d38da6"
    },
    "DEXO": {
        "symbol": "DEXO",
        "decimals": 18,
        "name": "DEXO",
        "address": "0xf9114498b7f38f3337d6295a3a0f3edf8da71326"
    },
    "DEXShare": {
        "symbol": "DEXShare",
        "decimals": 18,
        "name": "DEXShare",
        "address": "0xf4914e6d97a75f014acfcf4072f11be5cffc4ca6"
    },
    "DEXT": {
        "symbol": "DEXT",
        "decimals": 18,
        "name": "DEXTools",
        "address": "0xe91a8d2c584ca93c7405f15c22cdfe53c29896e3"
    },
    "DF": {
        "symbol": "DF",
        "decimals": 18,
        "name": "dForce",
        "address": "0x4a9a2b2b04549c3927dd2c9668a5ef3fca473623"
    },
    "DFG": {
        "symbol": "DFG",
        "decimals": 18,
        "name": "DeFiGram",
        "address": "0xb661f4576d5e0b622fee6ab041fd5451fe02ba4c"
    },
    "DFH": {
        "symbol": "DFH",
        "decimals": 18,
        "name": "DefiHorse",
        "address": "0x5fdab5bdbad5277b383b3482d085f4bfef68828c"
    },
    "DFI": {
        "symbol": "DFI",
        "decimals": 18,
        "name": "DFI (DefiChain)",
        "address": "0x361c60b7c2828fcab80988d00d1d542c83387b50"
    },
    "DFY": {
        "symbol": "DFY",
        "decimals": 18,
        "name": "DeFi For You.",
        "address": "0xd98560689c6e748dc37bc410b4d3096b1aa3d8c2"
    },
    "DGH": {
        "symbol": "DGH",
        "decimals": 18,
        "name": "Digihealth",
        "address": "0xa87584cfeb892c33a1c9a233e4a733b45c4160e6"
    },
    "DHB": {
        "symbol": "DHB",
        "decimals": 18,
        "name": "DeHub",
        "address": "0x680d3113caf77b61b510f332d5ef4cf5b41a761d"
    },
    "DHLT": {
        "symbol": "DHLT",
        "decimals": 18,
        "name": "DeHealth",
        "address": "0xb148df3c114b1233b206160a0f2a74999bb2fbf3"
    },
    "DHN": {
        "symbol": "DHN",
        "decimals": 18,
        "name": "Dohrnii",
        "address": "0xff8bbc599ea030aa69d0298035dfe263740a95bc"
    },
    "DHR": {
        "symbol": "DHR",
        "decimals": 18,
        "name": "DeHR",
        "address": "0x9fef6766ecf9e105b2753f7f8968dc8293a69460"
    },
    "DHS": {
        "symbol": "DHS",
        "decimals": 9,
        "name": "Dhahab Sports",
        "address": "0x9b9fdacab5347c78a493840ecfea04ff5aa45734"
    },
    "DHV": {
        "symbol": "DHV",
        "decimals": 18,
        "name": "DeHive.finance",
        "address": "0x58759dd469ae5631c42cf8a473992335575b58d7"
    },
    "DIA": {
        "symbol": "DIA",
        "decimals": 18,
        "name": "DIAToken",
        "address": "0x99956d38059cf7beda96ec91aa7bb2477e0901dd"
    },
    "DIE": {
        "symbol": "DIE",
        "decimals": 18,
        "name": "Art Can Die",
        "address": "0xd1e007d66470d3f775f1d4de52ed158fcc3b7189"
    },
    "DIFI": {
        "symbol": "DIFI",
        "decimals": 18,
        "name": "Digital Files",
        "address": "0x0938a5d325a8496c186cf122946e9dd22f8a625b"
    },
    "DIFX": {
        "symbol": "DIFX",
        "decimals": 18,
        "name": "DigitalFinancialExch",
        "address": "0x697bd938e7e572e787ecd7bc74a31f1814c21264"
    },
    "DIGICHAIN": {
        "symbol": "DIGICHAIN",
        "decimals": 9,
        "name": "DIGICHAIN COIN",
        "address": "0x4732a86106064577933552fcea993d30bec950a5"
    },
    "DINGER": {
        "symbol": "DINGER",
        "decimals": 9,
        "name": "Dinger Token",
        "address": "0x0d3843f92d622468ba67df5a6a4149b484a75af3"
    },
    "DKEY": {
        "symbol": "DKEY",
        "decimals": 18,
        "name": "dkey",
        "address": "0xf3ed4770e6efe9168c3f2f50a6d9d0f97a550df1"
    },
    "DKS": {
        "symbol": "DKS",
        "decimals": 18,
        "name": "DarkShield",
        "address": "0x121235cff4c59eec80b14c1d38b44e7de3a18287"
    },
    "DLC": {
        "symbol": "DLC",
        "decimals": 18,
        "name": "DiamondLaunch Coin",
        "address": "0xde83180dd1166d4f8e5c2b7de14a2163b1bb4a87"
    },
    "DLTA": {
        "symbol": "DLTA",
        "decimals": 18,
        "name": "Chainport.io-Peg delta.theta",
        "address": "0x3a06212763caf64bf101daa4b0cebb0cd393fa1a"
    },
    "DMC": {
        "symbol": "DMC",
        "decimals": 18,
        "name": "Decentralized Mining Coin",
        "address": "0xa5342d72d04c133180f376753f90a4b2eee29bb3"
    },
    "DMLG": {
        "symbol": "DMLG",
        "decimals": 18,
        "name": "Defi Monster Legends",
        "address": "0x1c796c140de269e255372ea687ef7644bab87935"
    },
    "DMOD": {
        "symbol": "DMOD",
        "decimals": 18,
        "name": "Demodyfi Token",
        "address": "0x002d8563759f5e1eaf8784181f3973288f6856e4"
    },
    "Dmoon": {
        "symbol": "Dmoon",
        "decimals": 18,
        "name": "dollarmoon",
        "address": "0x7d18f3fe6e638fad0adacc5db1a47f871a2c2cc4"
    },
    "DMS": {
        "symbol": "DMS",
        "decimals": 18,
        "name": "Dragon Mainland Shards",
        "address": "0x9a26e6d24df036b0b015016d1b55011c19e76c87"
    },
    "DNFT": {
        "symbol": "DNFT",
        "decimals": 18,
        "name": "DareNFT",
        "address": "0x162c2332e92be409254ac7c59ad559c16a3f506e"
    },
    "DNXC": {
        "symbol": "DNXC",
        "decimals": 18,
        "name": "DinoX Coin",
        "address": "0x3c1748d647e6a56b37b66fcd2b5626d0461d3aa0"
    },
    "DOBO": {
        "symbol": "DOBO",
        "decimals": 9,
        "name": "DogeBonk.com",
        "address": "0xae2df9f730c54400934c06a17462c41c08a06ed8"
    },
    "DODO": {
        "symbol": "DODO",
        "decimals": 18,
        "name": "DODO bird",
        "address": "0x67ee3cb086f8a16f34bee3ca72fad36f7db929e2"
    },
    "DOG": {
        "symbol": "DOG",
        "decimals": 18,
        "name": "The Doge NFT",
        "address": "0xaa88c603d142c371ea0eac8756123c5805edee03"
    },
    "DOGAI": {
        "symbol": "DOGAI",
        "decimals": 18,
        "name": "Dogai",
        "address": "0x94db03752342bc9b5bbf89e3bf0132494f0cb2b3"
    },
    "DOGBOSS ": {
        "symbol": "DOGBOSS ",
        "decimals": 18,
        "name": "DOG BOSS",
        "address": "0x86c86ffdc0482d8dd918fc657c3fc51c4a1e3e5c"
    },
    "DOGEAI": {
        "symbol": "DOGEAI",
        "decimals": 18,
        "name": "DogeCEO Ai",
        "address": "0xd85f89ea9a43942d86965c62b93ece0867925765"
    },
    "DOGEBLUE": {
        "symbol": "DOGEBLUE",
        "decimals": 9,
        "name": "Doge Blue",
        "address": "0xb38a5cdc7304ad3d53ce280a8dc63b2921d0a72f"
    },
    "DOGECEO": {
        "symbol": "DOGECEO",
        "decimals": 9,
        "name": "Doge CEO",
        "address": "0x9cbb03effd6fb7d79c9bab1b0ceaf4232e957521"
    },
    "DOGECOIN": {
        "symbol": "DOGECOIN",
        "decimals": 9,
        "name": "Buff Doge Coin",
        "address": "0x23125108bc4c63e4677b2e253fa498ccb4b3298b"
    },
    "DOGECOLA": {
        "symbol": "DOGECOLA",
        "decimals": 18,
        "name": "DogeCola",
        "address": "0x4756cd85cd07769c2ce07a73497f208d56d48ec1"
    },
    "DOGEDIGGER": {
        "symbol": "DOGEDIGGER",
        "decimals": 18,
        "name": "DOGEDIGGER",
        "address": "0xce18eae0303a0f285f99a345f39819b15833266b"
    },
    "DogeKing": {
        "symbol": "DogeKing",
        "decimals": 18,
        "name": "DogeKing ",
        "address": "0x641ec142e67ab213539815f67e4276975c2f8d50"
    },
    "DOGGY": {
        "symbol": "DOGGY",
        "decimals": 18,
        "name": "DOGGY",
        "address": "0x74926b3d118a63f6958922d3dc05eb9c6e6e00c6"
    },
    "DOGRMY": {
        "symbol": "DOGRMY",
        "decimals": 9,
        "name": "DogeArmy",
        "address": "0xbf758f2afec32b92e8008b5671088d42af616515"
    },
    "DOGS": {
        "symbol": "DOGS",
        "decimals": 9,
        "name": "Dogcoin",
        "address": "0xbccd27062ae1a2bea5731c904b96edfb163aba21"
    },
    "DOLA": {
        "symbol": "DOLA",
        "decimals": 18,
        "name": "Dola USD Stablecoin",
        "address": "0x2f29bc0ffaf9bff337b31cbe6cb5fb3bf12e5840"
    },
    "DOME": {
        "symbol": "DOME",
        "decimals": 18,
        "name": "Everdome",
        "address": "0x475bfaa1848591ae0e6ab69600f48d828f61a80e"
    },
    "DOMI": {
        "symbol": "DOMI",
        "decimals": 18,
        "name": "Domi",
        "address": "0xbbca42c60b5290f2c48871a596492f93ff0ddc82"
    },
    "DON": {
        "symbol": "DON",
        "decimals": 18,
        "name": "Donkey",
        "address": "0x86b3f23b6e90f5bbfac59b5b2661134ef8ffd255"
    },
    "DONS": {
        "symbol": "DONS",
        "decimals": 18,
        "name": "The DONS",
        "address": "0x95c91eef65f50570cfc3f269961a00108cf7bf59"
    },
    "DOR": {
        "symbol": "DOR",
        "decimals": 18,
        "name": "Dor Token",
        "address": "0x3465fd2d9f900e34280abab60e8d9987b5b5bb47"
    },
    "DOSE": {
        "symbol": "DOSE",
        "decimals": 18,
        "name": "DOSE",
        "address": "0x7837fd820ba38f95c54d6dac4ca3751b81511357"
    },
    "DOT": {
        "symbol": "DOT",
        "decimals": 18,
        "name": "Polkadot Token",
        "address": "0x7083609fce4d1d8dc0c979aab8c869ea2c873402"
    },
    "DOUGH": {
        "symbol": "DOUGH",
        "decimals": 18,
        "name": "Dough",
        "address": "0xede5020492be8e265db6141cb0a1d2df9dbae9bb"
    },
    "DOV": {
        "symbol": "DOV",
        "decimals": 18,
        "name": "Dovu",
        "address": "0xc9457161320210d22f0d0d5fc1309acb383d4609"
    },
    "DOWS": {
        "symbol": "DOWS",
        "decimals": 18,
        "name": "Shadows",
        "address": "0xfb7400707df3d76084fbeae0109f41b178f71c02"
    },
    "DPAD": {
        "symbol": "DPAD",
        "decimals": 8,
        "name": "DPAD Finance",
        "address": "0x4dcaaa68170053afbbde15774931adba09272a55"
    },
    "DPET": {
        "symbol": "DPET",
        "decimals": 18,
        "name": "My DeFi Pet Token",
        "address": "0xfb62ae373aca027177d1c18ee0862817f9080d08"
    },
    "DPR": {
        "symbol": "DPR",
        "decimals": 18,
        "name": "Deeper Network",
        "address": "0xa0a2ee912caf7921eaabc866c6ef6fec8f7e90a4"
    },
    "DPS": {
        "symbol": "DPS",
        "decimals": 9,
        "name": "DEEPSPACE",
        "address": "0xf275e1ac303a4c9d987a2c48b8e555a77fec3f1c"
    },
    "DPT": {
        "symbol": "DPT",
        "decimals": 18,
        "name": "Diviner Protocol",
        "address": "0xe69caef10a488d7af31da46c89154d025546e990"
    },
    "DRAC": {
        "symbol": "DRAC",
        "decimals": 18,
        "name": "DRAC Token",
        "address": "0x123458c167a371250d325bd8b1fff12c8af692a7"
    },
    "DRB": {
        "symbol": "DRB",
        "decimals": 9,
        "name": "DigimonRabbit",
        "address": "0x485d37ca1c8d4e0b5b11b87604816a4843c079ed"
    },
    "DREAMS": {
        "symbol": "DREAMS",
        "decimals": 18,
        "name": "Dreams Quest",
        "address": "0x54523d5fb56803bac758e8b10b321748a77ae9e9"
    },
    "DREP": {
        "symbol": "DREP",
        "decimals": 18,
        "name": "DREP",
        "address": "0xec583f25a049cc145da9a256cdbe9b6201a705ff"
    },
    "DRF": {
        "symbol": "DRF",
        "decimals": 18,
        "name": "DRIFE",
        "address": "0x9400aa8eb5126d20cde45c7822836bfb70f19878"
    },
    "DRFLY": {
        "symbol": "DRFLY",
        "decimals": 18,
        "name": "DRAGON FLY",
        "address": "0x4181d0f55a5f455ab611b2a0c062714467d7a999"
    },
    "DRIP": {
        "symbol": "DRIP",
        "decimals": 18,
        "name": "DRIP Token",
        "address": "0x20f663cea80face82acdfa3aae6862d246ce0333"
    },
    "DRIVECRYPTO": {
        "symbol": "DRIVECRYPTO",
        "decimals": 18,
        "name": "Drive Crypto",
        "address": "0xa151f5d8d9558c85a70cd556e265a874073159fb"
    },
    "DSHARE": {
        "symbol": "DSHARE",
        "decimals": 18,
        "name": "DSHARE",
        "address": "0x26d3163b165be95137cee97241e716b2791a7572"
    },
    "DSLA": {
        "symbol": "DSLA",
        "decimals": 18,
        "name": "DSLA",
        "address": "0x1861c9058577c3b48e73d91d6f25c18b17fbffe0"
    },
    "Dsun": {
        "symbol": "Dsun",
        "decimals": 18,
        "name": "Dsun Token",
        "address": "0x1384555d00144c7725ac71da2bb1fd67b9ad889a"
    },
    "DTC": {
        "symbol": "DTC",
        "decimals": 9,
        "name": "TrumpCoin",
        "address": "0xab8c98491816fede394582f7758a5effeb4368d7"
    },
    "DTG": {
        "symbol": "DTG",
        "decimals": 9,
        "name": "Defi Tiger",
        "address": "0xb1957bdba889686ebde631df970ece6a7571a1b6"
    },
    "DUCK": {
        "symbol": "DUCK",
        "decimals": 18,
        "name": "DLP Duck Token",
        "address": "0x5d186e28934c6b0ff5fc2fece15d1f34f78cbd87"
    },
    "DuckyAI": {
        "symbol": "DuckyAI",
        "decimals": 18,
        "name": "DuckyCoinAI",
        "address": "0xd38de430d355a7a8337204c2a4c80392e61475a6"
    },
    "DUET": {
        "symbol": "DUET",
        "decimals": 18,
        "name": "Duet Governance Token",
        "address": "0x95ee03e1e2c5c4877f9a298f1c0d6c98698fab7b"
    },
    "Duke": {
        "symbol": "Duke",
        "decimals": 9,
        "name": "Duke inu Token",
        "address": "0xaee234825dc4687fae606485c1ebd06336052bcc"
    },
    "DUSK": {
        "symbol": "DUSK",
        "decimals": 18,
        "name": "Dusk Network",
        "address": "0xb2bd0749dbe21f623d9baba856d3b0f0e1bfec9c"
    },
    "DVRS": {
        "symbol": "DVRS",
        "decimals": 18,
        "name": "DaoVerse",
        "address": "0xa155464b1566cdddf9782205602651b8b871b3d5"
    },
    "DWT": {
        "symbol": "DWT",
        "decimals": 18,
        "name": "Decentralized Exchange Wallet",
        "address": "0x865a0e15ac5c309e7ea61410cebdea1df686dbb2"
    },
    "DXCT": {
        "symbol": "DXCT",
        "decimals": 18,
        "name": "DNAxCAT",
        "address": "0x5b1baec64af6dc54e6e04349315919129a6d3c23"
    },
    "DXT": {
        "symbol": "DXT",
        "decimals": 9,
        "name": "DEXIT",
        "address": "0x2b2ff80c489dad868318a19fd6f258889a026da5"
    },
    "DYNA": {
        "symbol": "DYNA",
        "decimals": 9,
        "name": "Dynamix",
        "address": "0xc41689a727469c1573009757200371edf36d540e"
    },
    "DYNMT": {
        "symbol": "DYNMT",
        "decimals": 2,
        "name": "DYNAMITE",
        "address": "0xb1ce906c610004e27e74415aa9bcc90e46366f90"
    },
    "DYOR": {
        "symbol": "DYOR",
        "decimals": 9,
        "name": "DYOR Token",
        "address": "0x10051147418c42218986cedd0adc266441f8a14f"
    },
    "DYP": {
        "symbol": "DYP",
        "decimals": 18,
        "name": "DeFiYieldProtocol",
        "address": "0x961c8c0b1aad0c0b10a51fef6a867e3091bcef17"
    },
    "EARN": {
        "symbol": "EARN",
        "decimals": 18,
        "name": "Yearn Classic",
        "address": "0x63a18bc38d1101db7f0efcbcbdcbe927a5879039"
    },
    "EarnX": {
        "symbol": "EarnX",
        "decimals": 18,
        "name": "EarnX",
        "address": "0x0f76142d83ddef359753cca33647cc4dcee1c6d1"
    },
    "EBA": {
        "symbol": "EBA",
        "decimals": 18,
        "name": "Elpis Battle",
        "address": "0x3944ac66b9b9b40a6474022d6962b6caa001b5e3"
    },
    "ECC": {
        "symbol": "ECC",
        "decimals": 8,
        "name": "Etherconnect Coin",
        "address": "0x8d047f4f57a190c96c8b9704b39a1379e999d82b"
    },
    "ECO": {
        "symbol": "ECO",
        "decimals": 18,
        "name": "EcoToken",
        "address": "0xede2f059545e8cde832d8da3985caacf795b8765"
    },
    "EDE": {
        "symbol": "EDE",
        "decimals": 18,
        "name": "EDE",
        "address": "0x4136129ac3ac90cf9817548b24d35e73e9457e05"
    },
    "EDG": {
        "symbol": "EDG",
        "decimals": 18,
        "name": "Edgeware",
        "address": "0xad1898d4d222ccb2ae8e36585c7bf2a59984a736"
    },
    "EDU": {
        "symbol": "EDU",
        "decimals": 18,
        "name": "EDU Coin",
        "address": "0xbdeae1ca48894a1759a8374d63925f21f2ee2639"
    },
    "EDUX": {
        "symbol": "EDUX",
        "decimals": 18,
        "name": "EDUFEX",
        "address": "0x2b1b730c997d81db2e792b47d0bc42a64ee6aa55"
    },
    "EFBAI": {
        "symbol": "EFBAI",
        "decimals": 9,
        "name": "EuroFootball AI",
        "address": "0x8c8f52e1b08333edf558e41fc252baa87f118296"
    },
    "EFT": {
        "symbol": "EFT",
        "decimals": 18,
        "name": "Energyfi Token",
        "address": "0xae98e63db1c4646bf5b40b29c664bc922f71bc65"
    },
    "EG": {
        "symbol": "EG",
        "decimals": 18,
        "name": "EG Token",
        "address": "0x74afe449d1beffc90456cfebd700ab391abd7daf"
    },
    "EGC": {
        "symbol": "EGC",
        "decimals": 9,
        "name": "EverGrow Coin",
        "address": "0xc001bbe2b87079294c63ece98bdd0a88d761434e"
    },
    "EGG": {
        "symbol": "EGG",
        "decimals": 18,
        "name": "Goose Golden Egg",
        "address": "0xf952fc3ca7325cc27d15885d37117676d25bfda6"
    },
    "EGLD": {
        "symbol": "EGLD",
        "decimals": 18,
        "name": "Elrond",
        "address": "0xbf7c81fff98bbe61b40ed186e4afd6ddd01337fe"
    },
    "EGON": {
        "symbol": "EGON",
        "decimals": 18,
        "name": "EgonSwap Token",
        "address": "0x05995a068bdac17c582ec75ab46bb8e7394be1d9"
    },
    "EiFI": {
        "symbol": "EiFI",
        "decimals": 8,
        "name": "Eifi",
        "address": "0xbbf33a3c83cf86d0965a66e108669d272dfe4214"
    },
    "EKTA v2": {
        "symbol": "EKTA v2",
        "decimals": 18,
        "name": "EKTA v2",
        "address": "0x45808ce43eb2d7685ff0242631f0feb6f3d8701a"
    },
    "ELEPHANT": {
        "symbol": "ELEPHANT",
        "decimals": 9,
        "name": "Elephant Money",
        "address": "0xe283d0e3b8c102badf5e8166b73e02d96d92f688"
    },
    "ELF": {
        "symbol": "ELF",
        "decimals": 18,
        "name": "ELF Token",
        "address": "0xa3f020a5c92e15be13caf0ee5c95cf79585eecc9"
    },
    "ELK": {
        "symbol": "ELK",
        "decimals": 18,
        "name": "Elk",
        "address": "0xeeeeeb57642040be42185f49c52f7e9b38f8eeee"
    },
    "ELMON": {
        "symbol": "ELMON",
        "decimals": 18,
        "name": "Elemon Token",
        "address": "0xe3233fdb23f1c27ab37bd66a19a1f1762fcf5f3f"
    },
    "ELON": {
        "symbol": "ELON",
        "decimals": 18,
        "name": "Dogelon Mars",
        "address": "0x7bd6fabd64813c48545c9c0e312a0099d9be2540"
    },
    "ELP": {
        "symbol": "ELP",
        "decimals": 18,
        "name": "Everlasting Parachain Token",
        "address": "0xe3894cb9e92ca78524fb6a30ff072fa5e533c162"
    },
    "ELT": {
        "symbol": "ELT",
        "decimals": 18,
        "name": "ECLAT",
        "address": "0xae90ca218f9c3b1aa84af33a7907e4890ec6a167"
    },
    "eLunr": {
        "symbol": "eLunr",
        "decimals": 4,
        "name": "Ethereum-bridged Lunr Token",
        "address": "0x37807d4fbeb84124347b8899dd99616090d3e304"
    },
    "Elys": {
        "symbol": "Elys",
        "decimals": 18,
        "name": "Elysium",
        "address": "0xf8dfc70a422ccf0ab206adf7b043fdfb410caab5"
    },
    "EMBR": {
        "symbol": "EMBR",
        "decimals": 18,
        "name": "EMBR",
        "address": "0x6cb8065f96d63630425fd95a408a0d6cd697c662"
    },
    "ENV": {
        "symbol": "ENV",
        "decimals": 18,
        "name": "ENVOY [via ChainPort.io]",
        "address": "0x4d6b129db8a502b85fedc3443fa4f58b50327238"
    },
    "EOS": {
        "symbol": "EOS",
        "decimals": 18,
        "name": "EOS Token",
        "address": "0x56b6fb708fc5732dec1afc8d8556423a2edccbd6"
    },
    "EPIK": {
        "symbol": "EPIK",
        "decimals": 18,
        "name": "Epik Prime [via ChainPort.io]",
        "address": "0x368ce786ea190f32439074e8d22e12ecb718b44c"
    },
    "EPIX": {
        "symbol": "EPIX",
        "decimals": 18,
        "name": "Byepix",
        "address": "0x90e1f81b298f6c180ce6f71a6bdb4acf41be8e01"
    },
    "EPS": {
        "symbol": "EPS",
        "decimals": 18,
        "name": "Ellipsis",
        "address": "0xa7f552078dcc247c2684336020c03648500c6d9f"
    },
    "EPX": {
        "symbol": "EPX",
        "decimals": 18,
        "name": "Ellipsis X",
        "address": "0xaf41054c1487b0e5e2b9250c0332ecbce6ce9d71"
    },
    "eQUAD": {
        "symbol": "eQUAD",
        "decimals": 18,
        "name": "QuadrantProtocol",
        "address": "0x564bef31ec942ffe1bff250786f76a5c5141b9f3"
    },
    "EQX": {
        "symbol": "EQX",
        "decimals": 18,
        "name": "EQIFi Token",
        "address": "0x436c52a8cee41d5e9c5e6f4cb146e66d552fb700"
    },
    "EQZ": {
        "symbol": "EQZ",
        "decimals": 18,
        "name": "Equalizer",
        "address": "0x1da87b114f35e1dc91f72bf57fc07a768ad40bb0"
    },
    "ERA": {
        "symbol": "ERA",
        "decimals": 18,
        "name": "Era Token",
        "address": "0x6f9f0c4ad9af7ebd61ac5a1d4e0f2227f7b0e5f9"
    },
    "ERC20": {
        "symbol": "ERC20",
        "decimals": 18,
        "name": "ERC20",
        "address": "0x58730ae0faa10d73b0cddb5e7b87c3594f7a20cb"
    },
    "ERTHA": {
        "symbol": "ERTHA",
        "decimals": 18,
        "name": "ERTHA Token",
        "address": "0x62823659d09f9f9d2222058878f89437425eb261"
    },
    "ES2": {
        "symbol": "ES2",
        "decimals": 5,
        "name": "EverSAFUv2",
        "address": "0xfef0c1670cb569008bb3d070918922dbb4f92de4"
    },
    "ESCROW": {
        "symbol": "ESCROW",
        "decimals": 18,
        "name": "Cryptegrity DAO",
        "address": "0x7764bdfc4ab0203a7d4e3edf33b181f395458870"
    },
    "EShib": {
        "symbol": "EShib",
        "decimals": 9,
        "name": "Euro Shiba Inu",
        "address": "0xffaa85705ae216363e4e843b67ff3c238fcf0de2"
    },
    "ESNC": {
        "symbol": "ESNC",
        "decimals": 18,
        "name": "Essence Token",
        "address": "0xbbf1889f22d37640bc70c58b2f643106db0542de"
    },
    "ETC": {
        "symbol": "ETC",
        "decimals": 18,
        "name": "Ethereum Classic",
        "address": "0x3d6545b08693dae087e957cb1180ee38b9e3c25e"
    },
    "ETERNAL": {
        "symbol": "ETERNAL",
        "decimals": 18,
        "name": "CryptoMines Eternal",
        "address": "0xd44fd09d74cd13838f137b590497595d6b3feea4"
    },
    "ETHAX": {
        "symbol": "ETHAX",
        "decimals": 18,
        "name": "ETHAX",
        "address": "0x854f7cd3677737241e3eed0dc3d7f33dfaf72bc4"
    },
    "ETHO": {
        "symbol": "ETHO",
        "decimals": 18,
        "name": "Wrapped ETHO",
        "address": "0x48b19b7605429acaa8ea734117f39726a9aab1f9"
    },
    "ETHPAD": {
        "symbol": "ETHPAD",
        "decimals": 18,
        "name": "ETHPAD.network",
        "address": "0x8db1d28ee0d822367af8d220c0dc7cb6fe9dc442"
    },
    "ETNA": {
        "symbol": "ETNA",
        "decimals": 18,
        "name": "ETNA Network",
        "address": "0x51f35073ff7cf54c9e86b7042e59a8cc9709fc46"
    },
    "EV": {
        "symbol": "EV",
        "decimals": 8,
        "name": "EVAI",
        "address": "0x2167afa1c658dc5c4ec975f4af608ff075a8b8ae"
    },
    "EVDC": {
        "symbol": "EVDC",
        "decimals": 9,
        "name": "EV Direct Currency",
        "address": "0xc3b4c4ef3fe02ad91cb57efda593ed07a9278cc0"
    },
    "EverETH": {
        "symbol": "EverETH",
        "decimals": 9,
        "name": "EverETH",
        "address": "0x16dcc0ec78e91e868dca64be86aec62bf7c61037"
    },
    "EVRY": {
        "symbol": "EVRY",
        "decimals": 18,
        "name": "EvrynetToken",
        "address": "0xc2d4a3709e076a7a3487816362994a78ddaeabb6"
    },
    "EVU": {
        "symbol": "EVU",
        "decimals": 9,
        "name": "Evulus Token",
        "address": "0x18b5f22266343ccd180c6285a66cc9a23dc262e9"
    },
    "EXOS": {
        "symbol": "EXOS",
        "decimals": 18,
        "name": "EXOS",
        "address": "0x16b8dba442cc9faa40d0dd53f698087546ccf096"
    },
    "eYe": {
        "symbol": "eYe",
        "decimals": 18,
        "name": "eYe on BSC",
        "address": "0x9a257c90fa239fba07771ef7da2d554d148c2e89"
    },
    "EZ": {
        "symbol": "EZ",
        "decimals": 18,
        "name": "Easy V2",
        "address": "0x5512014efa6cd57764fa743756f7a6ce3358cc83"
    },
    "EZY": {
        "symbol": "EZY",
        "decimals": 18,
        "name": "EZZY game token",
        "address": "0xb452bc9cead0b08c4ef99da0feb8e10ef6bb86bb"
    },
    "F2C": {
        "symbol": "F2C",
        "decimals": 18,
        "name": "Ftribe Fighters Coin",
        "address": "0x657b632714e08ac66b79444ad3f3875526ee6689"
    },
    "FABRIC": {
        "symbol": "FABRIC",
        "decimals": 18,
        "name": "MetaFabric",
        "address": "0x73ff5dd853cb87c144f463a555dce0e43954220d"
    },
    "FaceDAO": {
        "symbol": "FaceDAO",
        "decimals": 18,
        "name": "FaceDAO",
        "address": "0xb700597d8425ced17677bc68042d7d92764acf59"
    },
    "FACTR": {
        "symbol": "FACTR",
        "decimals": 18,
        "name": "Defactor",
        "address": "0xdefac16715671b7b6aeefe012125f1e19ee4b7d7"
    },
    "FAI": {
        "symbol": "FAI",
        "decimals": 18,
        "name": "Flokiter",
        "address": "0x459fab6be3b07558e28fecb07b64a481d0e8c6a3"
    },
    "FALCONS": {
        "symbol": "FALCONS",
        "decimals": 18,
        "name": "FalconSwaps Token",
        "address": "0xb139ed26b743c7254a246cf91eb594d097238524"
    },
    "FALCX": {
        "symbol": "FALCX",
        "decimals": 9,
        "name": "FalconX",
        "address": "0x2d862c9fc46608d7ff83293ceb83330d6135be5e"
    },
    "FAME": {
        "symbol": "FAME",
        "decimals": 18,
        "name": "FAME MMA",
        "address": "0x28ce223853d123b52c74439b10b43366d73fd3b5"
    },
    "FAN": {
        "symbol": "FAN",
        "decimals": 18,
        "name": "Fanadise",
        "address": "0xb6d48fcef36e19681ee29896b19c1b6cbd1eab1b"
    },
    "FARA": {
        "symbol": "FARA",
        "decimals": 18,
        "name": "FaraCrystal",
        "address": "0xf4ed363144981d3a65f42e7d0dc54ff9eef559a1"
    },
    "FARM": {
        "symbol": "FARM",
        "decimals": 18,
        "name": "FARM Reward Token",
        "address": "0x4b5c23cac08a567ecf0c1ffca8372a45a5d33743"
    },
    "FAST": {
        "symbol": "FAST",
        "decimals": 18,
        "name": "PodFast",
        "address": "0x391088b4594e41c003463c7e3a56a8ba00b8e7a9"
    },
    "FATCAT": {
        "symbol": "FATCAT",
        "decimals": 9,
        "name": "FAT CAT",
        "address": "0x55493e35e33fcf811571707ac5bf1dbcb658bafc"
    },
    "FATHOM": {
        "symbol": "FATHOM",
        "decimals": 18,
        "name": "Fathom",
        "address": "0x56513627e7cea535b9b5a18da7643a4b21999994"
    },
    "fBOMB": {
        "symbol": "fBOMB",
        "decimals": 18,
        "name": "Fantom Bomb",
        "address": "0x74ccbe53f77b08632ce0cb91d3a545bf6b8e0979"
    },
    "FBX": {
        "symbol": "FBX",
        "decimals": 18,
        "name": "ForthBox Coin",
        "address": "0xfd57ac98aa8e445c99bc2c41b23997573fadf795"
    },
    "FCF": {
        "symbol": "FCF",
        "decimals": 18,
        "name": "French connection finance",
        "address": "0x4673f018cc6d401aad0402bdbf2abcbf43dd69f3"
    },
    "FDC": {
        "symbol": "FDC",
        "decimals": 18,
        "name": "Fidance",
        "address": "0x6d1a4650e83708b583c35d5e0952a0b46354ca9b"
    },
    "FDT": {
        "symbol": "FDT",
        "decimals": 18,
        "name": "Frutti Dino",
        "address": "0x3a599e584075065eaaac768d75eaef85c2f2ff64"
    },
    "FEAR": {
        "symbol": "FEAR",
        "decimals": 18,
        "name": "Chainport.io-Peg Fear NFTs",
        "address": "0x9ba6a67a6f3b21705a46b380a1b97373a33da311"
    },
    "FEG": {
        "symbol": "FEG",
        "decimals": 9,
        "name": "FEGtoken",
        "address": "0xacfc95585d80ab62f67a14c566c1b7a49fe91167"
    },
    "FERMA": {
        "symbol": "FERMA",
        "decimals": 8,
        "name": "FERMA",
        "address": "0x6aa150fff813e0bec1273691f349ad080df7216d"
    },
    "FET": {
        "symbol": "FET",
        "decimals": 18,
        "name": "Fetch",
        "address": "0x031b41e504677879370e9dbcf937283a8691fa7f"
    },
    "FEVR": {
        "symbol": "FEVR",
        "decimals": 18,
        "name": "FevrToken",
        "address": "0x82030cdbd9e4b7c5bb0b811a61da6360d69449cc"
    },
    "FFE": {
        "symbol": "FFE",
        "decimals": 18,
        "name": "FORBIDDEN FRUIT ENERGY",
        "address": "0x9e0335fb61958fe19bb120f3f8408b4297921820"
    },
    "FGD": {
        "symbol": "FGD",
        "decimals": 18,
        "name": "FGDTOKEN",
        "address": "0x0566b9a8ffb8908682796751eed00722da967be0"
    },
    "FIBO": {
        "symbol": "FIBO",
        "decimals": 9,
        "name": "FiboDex",
        "address": "0xf892561596b7b8085fad1b03b902d00096ae31ad"
    },
    "FIGHT": {
        "symbol": "FIGHT",
        "decimals": 18,
        "name": "Fight Token",
        "address": "0x4f39c3319188a723003670c3f9b9e7ef991e52f3"
    },
    "FINA": {
        "symbol": "FINA",
        "decimals": 18,
        "name": "DEFINA TOKEN",
        "address": "0x426c72701833fddbdfc06c944737c6031645c708"
    },
    "FINE": {
        "symbol": "FINE",
        "decimals": 18,
        "name": "Refinable",
        "address": "0x4e6415a5727ea08aae4580057187923aec331227"
    },
    "FINS": {
        "symbol": "FINS",
        "decimals": 18,
        "name": "Fins Token",
        "address": "0x1b219aca875f8c74c33cff9ff98f3a9b62fcbff5"
    },
    "FIRO": {
        "symbol": "FIRO",
        "decimals": 8,
        "name": "Firo",
        "address": "0xd5d0322b6bab6a762c79f8c81a0b674778e13aed"
    },
    "FIST": {
        "symbol": "FIST",
        "decimals": 6,
        "name": "FistToken",
        "address": "0xc9882def23bc42d53895b8361d0b1edc7570bc6a"
    },
    "FIT": {
        "symbol": "FIT",
        "decimals": 18,
        "name": "FIT Token",
        "address": "0x77922a521182a719a48ba650ac2a040269888888"
    },
    "FITFI": {
        "symbol": "FITFI",
        "decimals": 18,
        "name": "STEP.APP",
        "address": "0x7588df009c3d82378be6ab81f2108fa963c10fc8"
    },
    "FITM": {
        "symbol": "FITM",
        "decimals": 18,
        "name": "Fitmax",
        "address": "0x41d52514f6ea0c90993ad36152072a144c12bdc7"
    },
    "FIU": {
        "symbol": "FIU",
        "decimals": 18,
        "name": "beFITTER Token",
        "address": "0xef7d50069406a2f5a53806f7250a6c0f17ad9dcd"
    },
    "FIWA": {
        "symbol": "FIWA",
        "decimals": 18,
        "name": "Defi Warrior Token",
        "address": "0x633237c6fa30fae46cc5bb22014da30e50a718cc"
    },
    "FLIGHT": {
        "symbol": "FLIGHT",
        "decimals": 4,
        "name": "FLIGHT CLUP COIN",
        "address": "0xf397680d99a92e4b60637e9f5c71a4def1f6c7b5"
    },
    "FLN": {
        "symbol": "FLN",
        "decimals": 18,
        "name": "Falcon",
        "address": "0x37d39950f9c753d62529dbf68fcb4dca4004fbfd"
    },
    "FLOC": {
        "symbol": "FLOC",
        "decimals": 18,
        "name": "Christmas Floki",
        "address": "0xe5765e33e349b2dcf22a37b2b4e87c10ad43f165"
    },
    "FLOH": {
        "symbol": "FLOH",
        "decimals": 18,
        "name": "Halloween Floki",
        "address": "0x2c0e76dade015bc390a13c1b80cc1bafd9edd326"
    },
    "FLOKI": {
        "symbol": "FLOKI",
        "decimals": 9,
        "name": "FLOKI",
        "address": "0xfb5b838b6cfeedc2873ab27866079ac55363d37e"
    },
    "FLOKICASH": {
        "symbol": "FLOKICASH",
        "decimals": 18,
        "name": "FLOKI CASH",
        "address": "0xa11ff9976018fda2a8c4ccfa6ffbe8423c5ab668"
    },
    "FLOKICEO": {
        "symbol": "FLOKICEO",
        "decimals": 9,
        "name": "FLOKI CEO",
        "address": "0x45289007706e7ee7b42b1fa506661d97740edfb4"
    },
    "FLOKISANTA": {
        "symbol": "FLOKISANTA",
        "decimals": 9,
        "name": "Floki Santa",
        "address": "0xf9db7dbad683dc7868be8b03ff0f4aa25f5cc6f6"
    },
    "Floshido": {
        "symbol": "Floshido",
        "decimals": 9,
        "name": "FLOSHIDO INU",
        "address": "0x87e04a05499cb8d352c2e367870d4cf0ead460f0"
    },
    "FLURRY": {
        "symbol": "FLURRY",
        "decimals": 18,
        "name": "Flurry Governance Token",
        "address": "0x47c9bcef4fe2dbcdf3abf508f147f1bbe8d4fef2"
    },
    "FLUX": {
        "symbol": "FLUX",
        "decimals": 8,
        "name": "Flux",
        "address": "0xaff9084f2374585879e8b434c399e29e80cce635"
    },
    "FLy": {
        "symbol": "FLy",
        "decimals": 4,
        "name": "Franklin",
        "address": "0x681fd3e49a6188fc526784ee70aa1c269ee2b887"
    },
    "FMT": {
        "symbol": "FMT",
        "decimals": 18,
        "name": "FitrMetaverseToken",
        "address": "0x4133ae786381c028c3d7aa738a07368d96eab9dc"
    },
    "FND": {
        "symbol": "FND",
        "decimals": 18,
        "name": "Rare Fnd",
        "address": "0x264387ad73d19408e34b5d5e13a93174a35cea33"
    },
    "FNDZ": {
        "symbol": "FNDZ",
        "decimals": 18,
        "name": "FNDZ Token",
        "address": "0x7754c0584372d29510c019136220f91e25a8f706"
    },
    "FOC": {
        "symbol": "FOC",
        "decimals": 18,
        "name": "TheForce Coin",
        "address": "0x3051cfb958dcd408fba70256073adba943fdf552"
    },
    "FODL": {
        "symbol": "FODL",
        "decimals": 18,
        "name": "Fodl",
        "address": "0x43f5b29d63cedc5a7c1724dbb1d698fde05ada21"
    },
    "FOMO": {
        "symbol": "FOMO",
        "decimals": 18,
        "name": "FomoBSC",
        "address": "0xb93dab50c96b90c63b590bcafa91bf2fdd8403af"
    },
    "FOR": {
        "symbol": "FOR",
        "decimals": 18,
        "name": "The Force Token",
        "address": "0x658a109c5900bc6d2357c87549b651670e5b0539"
    },
    "FORM": {
        "symbol": "FORM",
        "decimals": 18,
        "name": "Formation Finance",
        "address": "0x25a528af62e56512a19ce8c3cab427807c28cc19"
    },
    "FOTA": {
        "symbol": "FOTA",
        "decimals": 18,
        "name": "Fight Of The Ages",
        "address": "0x0a4e1bdfa75292a98c15870aef24bd94bffe0bd4"
    },
    "FOUR": {
        "symbol": "FOUR",
        "decimals": 18,
        "name": "The 4th Pillar Token on xDai from xDai",
        "address": "0xd882739fca9cbae00f3821c4c65189e2d7e26147"
    },
    "FOXV2": {
        "symbol": "FOXV2",
        "decimals": 9,
        "name": "FoxFinanceV2",
        "address": "0x16a7460b9246ae508f18e87bda4e5b4c1ae8f112"
    },
    "FPIS": {
        "symbol": "FPIS",
        "decimals": 18,
        "name": "Frax Price Index Share",
        "address": "0xd1738eb733a636d1b8665f48bc8a24da889c2562"
    },
    "FRAX": {
        "symbol": "FRAX",
        "decimals": 18,
        "name": "Frax",
        "address": "0x90c97f71e18723b0cf0dfa30ee176ab653e89f40"
    },
    "FREE": {
        "symbol": "FREE",
        "decimals": 18,
        "name": "FREE coin BSC",
        "address": "0x12e34cdf6a031a10fe241864c32fb03a4fdad739"
    },
    "FREL": {
        "symbol": "FREL",
        "decimals": 18,
        "name": "Poly-Peg FreelaToken",
        "address": "0xfd5af95c12446b60d23e16a4ea95690ce942e5dc"
    },
    "FRM": {
        "symbol": "FRM",
        "decimals": 18,
        "name": "Ferrum Network Token",
        "address": "0xa719b8ab7ea7af0ddb4358719a34631bb79d15dc"
    },
    "FRONT": {
        "symbol": "FRONT",
        "decimals": 18,
        "name": "Frontier Token",
        "address": "0x928e55dab735aa8260af3cedada18b5f70c72f1b"
    },
    "Froyo": {
        "symbol": "Froyo",
        "decimals": 18,
        "name": "Froyo",
        "address": "0xe369fec23380f9f14ffd07a1dc4b7c1a9fdd81c9"
    },
    "FRP": {
        "symbol": "FRP",
        "decimals": 18,
        "name": "FAME REWARD PLUS",
        "address": "0x8eca5c1b51a801a822912167153041ed0b92a397"
    },
    "frxETH": {
        "symbol": "frxETH",
        "decimals": 18,
        "name": "Frax Ether",
        "address": "0x64048a7eecf3a2f1ba9e144aac3d7db6e58f555e"
    },
    "Frzss": {
        "symbol": "Frzss",
        "decimals": 18,
        "name": "Frz solar system",
        "address": "0xac41fb8013c0b63588fc63997785a5d79e73eb28"
    },
    "FSN": {
        "symbol": "FSN",
        "decimals": 18,
        "name": "Fusion",
        "address": "0xfa4fa764f15d0f6e20aaec8e0d696870e5b77c6e"
    },
    "FTC": {
        "symbol": "FTC",
        "decimals": 18,
        "name": "Fintoken Coin",
        "address": "0x8a8a6930ea308042d6d2d4676444d2af9b35a418"
    },
    "FTM": {
        "symbol": "FTM",
        "decimals": 18,
        "name": "Fantom",
        "address": "0xad29abb318791d579433d831ed122afeaf29dcfe"
    },
    "FTS": {
        "symbol": "FTS",
        "decimals": 18,
        "name": "Fortress",
        "address": "0x4437743ac02957068995c48e08465e0ee1769fbe"
    },
    "Fuel": {
        "symbol": "Fuel",
        "decimals": 18,
        "name": "Fuel Token",
        "address": "0x2090c8295769791ab7a3cf1cc6e0aa19f35e441a"
    },
    "FUFU": {
        "symbol": "FUFU",
        "decimals": 18,
        "name": "FUFU",
        "address": "0x509a51394cc4d6bb474fefb2994b8975a55a6e79"
    },
    "Funex": {
        "symbol": "Funex",
        "decimals": 18,
        "name": "Funex",
        "address": "0xa07c39f8df11ca675f77efc19501e3dddacd03ed"
    },
    "FUSE": {
        "symbol": "FUSE",
        "decimals": 18,
        "name": "Fuse Token on BSC",
        "address": "0x5857c96dae9cf8511b08cb07f85753c472d36ea3"
    },
    "FUTURE": {
        "symbol": "FUTURE",
        "decimals": 18,
        "name": "FUTURECOIN",
        "address": "0x9fbff386a9405b4c98329824418ec02b5c20976b"
    },
    "Future of Fintech": {
        "symbol": "Future of Fintech",
        "decimals": 8,
        "name": "FOF",
        "address": "0xe8a8db73f7fb1ab5f05c619a8a631c8930c782ae"
    },
    "Future-AI": {
        "symbol": "Future-AI",
        "decimals": 18,
        "name": "Future AI",
        "address": "0x0ff534801e98a4976246d1f418e441783fc9aa15"
    },
    "Fwc": {
        "symbol": "Fwc",
        "decimals": 9,
        "name": "QATAR 2022 TOKEN",
        "address": "0x6d3a160b86edcd46d8f9bba25c2f88cccade19fc"
    },
    "Fwcl": {
        "symbol": "Fwcl",
        "decimals": 9,
        "name": "FWC LEGENDS",
        "address": "0x83adb07bb91ddde95a24982f1b2d343963ba3995"
    },
    "FWT": {
        "symbol": "FWT",
        "decimals": 18,
        "name": "FreewayToken",
        "address": "0x90a1e4bbade88366dc44436535f1571d95e666c7"
    },
    "FXF": {
        "symbol": "FXF",
        "decimals": 18,
        "name": "Finxflo",
        "address": "0x8a40c222996f9f3431f63bf80244c36822060f12"
    },
    "FXS": {
        "symbol": "FXS",
        "decimals": 18,
        "name": "Frax Share",
        "address": "0xe48a3d7d0bc88d552f730b62c006bc925eadb9ee"
    },
    "FYT": {
        "symbol": "FYT",
        "decimals": 18,
        "name": "Flora Yield Token",
        "address": "0x77f2be773ca0887ba2b3ef8344c8cf13c98d8ca7"
    },
    "GAFA": {
        "symbol": "GAFA",
        "decimals": 9,
        "name": "Gafa",
        "address": "0x495205d4c6307a73595c5c11b44bee9b3418ac69"
    },
    "GAFI": {
        "symbol": "GAFI",
        "decimals": 18,
        "name": "GameFi",
        "address": "0x89af13a10b32f1b2f8d1588f93027f69b6f4e27e"
    },
    "GAIA": {
        "symbol": "GAIA",
        "decimals": 18,
        "name": "GAIA Everworld",
        "address": "0x347e430b7cd1235e216be58ffa13394e5009e6e2"
    },
    "GAINS": {
        "symbol": "GAINS",
        "decimals": 18,
        "name": "Gains",
        "address": "0xd9ea58350bf120e2169a35fa1afc31975b07de01"
    },
    "GAL": {
        "symbol": "GAL",
        "decimals": 18,
        "name": "Project Galaxy",
        "address": "0xe4cc45bb5dbda06db6183e8bf016569f40497aa5"
    },
    "GALEON": {
        "symbol": "GALEON",
        "decimals": 18,
        "name": "Galeon",
        "address": "0x1d0ac23f03870f768ca005c84cbb6fb82aa884fd"
    },
    "GAME": {
        "symbol": "GAME",
        "decimals": 5,
        "name": "Game Coin [via ChainPort.io]",
        "address": "0x66109633715d2110dda791e64a7b2afadb517abb"
    },
    "GAMER": {
        "symbol": "GAMER",
        "decimals": 18,
        "name": "GameStation",
        "address": "0x3f6b3595ecf70735d3f48d69b09c4e4506db3f47"
    },
    "GAMES": {
        "symbol": "GAMES",
        "decimals": 18,
        "name": "Gaming Stars",
        "address": "0xf300e4f1a193dd047b0c6747ad4e16dedf886297"
    },
    "GAMI": {
        "symbol": "GAMI",
        "decimals": 6,
        "name": "GamiWorld.io",
        "address": "0x1236a887ef31b4d32e1f0a2b5e4531f52cec7e75"
    },
    "GAN": {
        "symbol": "GAN",
        "decimals": 18,
        "name": "Galactic Arena: The NFTverse",
        "address": "0x8f1408171eae06aec4549fd0a5808a42cee6dd84"
    },
    "GBK": {
        "symbol": "GBK",
        "decimals": 8,
        "name": "GBANK APY",
        "address": "0xda0638ea374c4c5bf2914e6f4d5b2335deb8d80d"
    },
    "GBT": {
        "symbol": "GBT",
        "decimals": 18,
        "name": "Green Block Token",
        "address": "0xd7d5d7bcd0680cd8aa5afc34bc7037c3040f8210"
    },
    "GBYTE": {
        "symbol": "GBYTE",
        "decimals": 18,
        "name": "Imported GBYTE",
        "address": "0xeb34de0c4b2955ce0ff1526cdf735c9e6d249d09"
    },
    "GCAKE": {
        "symbol": "GCAKE",
        "decimals": 18,
        "name": "Pancake GAMES",
        "address": "0x61d5822dd7b3ed495108733e6550d4529480c8f6"
    },
    "GCME": {
        "symbol": "GCME",
        "decimals": 9,
        "name": "Go Crypto Me",
        "address": "0x9528cceb678b90daf02ca5ca45622d5cbaf58a30"
    },
    "GDX": {
        "symbol": "GDX",
        "decimals": 18,
        "name": "GridX",
        "address": "0x7ffb5a90cdbd2ae2a65d5bfe259ac936cc302be2"
    },
    "GEAR": {
        "symbol": "GEAR",
        "decimals": 18,
        "name": "MetaGear Token",
        "address": "0xb4404dab7c0ec48b428cf37dec7fb628bcc41b36"
    },
    "GEEK": {
        "symbol": "GEEK",
        "decimals": 18,
        "name": "Geek Protocol",
        "address": "0xd467d078fa363985805b1c3624f26045ba5709df"
    },
    "GEM": {
        "symbol": "GEM",
        "decimals": 18,
        "name": "NFTmall GEM Token",
        "address": "0xbac1df744df160877cdc45e13d0394c06bc388ff"
    },
    "GEMG": {
        "symbol": "GEMG",
        "decimals": 18,
        "name": "GemGuardian",
        "address": "0x885c5fb8f0e67b2b0cf3a437e6cc6ebc0f9f9014"
    },
    "GENE": {
        "symbol": "GENE",
        "decimals": 18,
        "name": "Genopets",
        "address": "0x9df465460938f9ebdf51c38cc87d72184471f8f0"
    },
    "GENS": {
        "symbol": "GENS",
        "decimals": 18,
        "name": "Genshiro Token",
        "address": "0x2cd14cba3f26254beed1d78158cd2b6f91809600"
    },
    "Germany": {
        "symbol": "Germany",
        "decimals": 18,
        "name": "Germany",
        "address": "0xd9d0e3dd09c78930de4ac83856bd0af6d3dd2022"
    },
    "GEURO": {
        "symbol": "GEURO",
        "decimals": 18,
        "name": "GEURO",
        "address": "0x6f13b1fb6b2897bb40adbc09f7f6cfad181c0904"
    },
    "GFAL": {
        "symbol": "GFAL",
        "decimals": 18,
        "name": "Games For A Living",
        "address": "0x47c454ca6be2f6def6f32b638c80f91c9c3c5949"
    },
    "GFI": {
        "symbol": "GFI",
        "decimals": 18,
        "name": "GameFi",
        "address": "0xdd6c6c114db071efe0bab6051268227ce64c3ffe"
    },
    "GFN": {
        "symbol": "GFN",
        "decimals": 18,
        "name": "Graphene",
        "address": "0xf209ce1960fb7e750ff30ba7794ea11c6acdc1f3"
    },
    "GFT": {
        "symbol": "GFT",
        "decimals": 18,
        "name": "Gifto",
        "address": "0x72ff5742319ef07061836f5c924ac6d72c919080"
    },
    "GFX": {
        "symbol": "GFX",
        "decimals": 18,
        "name": "GamyFi",
        "address": "0x65ad6a2288b2dd23e466226397c8f5d1794e58fc"
    },
    "GGG": {
        "symbol": "GGG",
        "decimals": 18,
        "name": "Good Games Guild",
        "address": "0xd8047afecb86e44eff3add991b9f063ed4ca716b"
    },
    "GGR": {
        "symbol": "GGR",
        "decimals": 18,
        "name": "Gagarin",
        "address": "0xa90da9e3c71ddfcc2d793f80029acbd21a4a0db6"
    },
    "GGT": {
        "symbol": "GGT",
        "decimals": 18,
        "name": "GoatGang",
        "address": "0x0195af07ff81e2dcdd40bb8f7719fb4426a978c9"
    },
    "GGTKN": {
        "symbol": "GGTKN",
        "decimals": 18,
        "name": "GG TOKEN",
        "address": "0x1f7e8fe01aeba6fdaea85161746f4d53dc9bda4f"
    },
    "GHD": {
        "symbol": "GHD",
        "decimals": 18,
        "name": "Giftedhands on BSC",
        "address": "0xfdfd27ae39cebefdbaac8615f18aa68ddd0f15f5"
    },
    "GHNY": {
        "symbol": "GHNY",
        "decimals": 18,
        "name": "Grizzly Honey",
        "address": "0xa045e37a0d1dd3a45fefb8803d22457abc0a728a"
    },
    "GHX": {
        "symbol": "GHX",
        "decimals": 18,
        "name": "GamerCoin",
        "address": "0xbd7b8e4de08d9b01938f7ff2058f110ee1e0e8d4"
    },
    "GINOA": {
        "symbol": "GINOA",
        "decimals": 18,
        "name": "Ginoa Token",
        "address": "0x2ff90b0c29ededdaf11c847925ea4a17789e88c3"
    },
    "Ginza": {
        "symbol": "Ginza",
        "decimals": 18,
        "name": "Ginza",
        "address": "0x32d7da6a7cf25ed1b86e1b0ee9a62b0252d46b16"
    },
    "GLB": {
        "symbol": "GLB",
        "decimals": 9,
        "name": "Golden Ball",
        "address": "0x52eb6c887a4691f10bee396778603927c23be1fc"
    },
    "GLCH": {
        "symbol": "GLCH",
        "decimals": 18,
        "name": "Glitch",
        "address": "0xf0902eb0049a4003793bab33f3566a22d2834442"
    },
    "GLE": {
        "symbol": "GLE",
        "decimals": 18,
        "name": "Green Life Energy",
        "address": "0x405ef490862ad5fb2d80995b35459594290a7aa9"
    },
    "GLF": {
        "symbol": "GLF",
        "decimals": 18,
        "name": "GalaxyFinance",
        "address": "0xc8b44fc9e6b8fd806111a04b1f208a0087baf9b1"
    },
    "GLR": {
        "symbol": "GLR",
        "decimals": 18,
        "name": "Glory",
        "address": "0x1fc71fe3e333d5262828f3d348c12c7e52306b8a"
    },
    "GM": {
        "symbol": "GM",
        "decimals": 18,
        "name": "GoldMiner",
        "address": "0xe2604c9561d490624aa35e156e65e590eb749519"
    },
    "GMEE": {
        "symbol": "GMEE",
        "decimals": 18,
        "name": "GAMEE",
        "address": "0x84e9a6f9d240fdd33801f7135908bfa16866939a"
    },
    "GMETA": {
        "symbol": "GMETA",
        "decimals": 9,
        "name": "Green_Meta_v2",
        "address": "0xfc352fcec6135edc384fe50bbf2bc2d1cdd7fc4e"
    },
    "GMEX": {
        "symbol": "GMEX",
        "decimals": 9,
        "name": "Game Coin",
        "address": "0xe9d78bf51ae04c7e1263a76ed89a65537b9ca903"
    },
    "GMM": {
        "symbol": "GMM",
        "decimals": 18,
        "name": "Gamium",
        "address": "0x5b6bf0c7f989de824677cfbd507d9635965e9cd3"
    },
    "GMPD": {
        "symbol": "GMPD",
        "decimals": 18,
        "name": "GMPD",
        "address": "0x9720ca160bbd4e7f3dd4bb3f8bd4227ca0342e63"
    },
    "GMR": {
        "symbol": "GMR",
        "decimals": 18,
        "name": "GAMER",
        "address": "0x168e3b1746aa249a9b3603b70605924fe255ee1a"
    },
    "GMT": {
        "symbol": "GMT",
        "decimals": 8,
        "name": "Green Metaverse Token",
        "address": "0x3019bf2a2ef8040c242c9a4c5c4bd4c81678b2a1"
    },
    "GNP": {
        "symbol": "GNP",
        "decimals": 18,
        "name": "Genie",
        "address": "0xfa139cc2f5c5b8c72309be8e63c3024d03b7e63c"
    },
    "GNY": {
        "symbol": "GNY",
        "decimals": 18,
        "name": "GNY",
        "address": "0xe4a4ad6e0b773f47d28f548742a23efd73798332"
    },
    "GO!": {
        "symbol": "GO!",
        "decimals": 18,
        "name": "GO!",
        "address": "0x7ae1cbec5c315b31948dd2a5a7c2a6a6040d3d5b"
    },
    "GoC": {
        "symbol": "GoC",
        "decimals": 18,
        "name": "GoCrypto",
        "address": "0x4b85a666dec7c959e88b97814e46113601b07e57"
    },
    "GODE": {
        "symbol": "GODE",
        "decimals": 6,
        "name": "GodeChain",
        "address": "0x245d9f531757f83064ad808b4c9b220c703a4934"
    },
    "GOLC": {
        "symbol": "GOLC",
        "decimals": 18,
        "name": "GOLCOIN",
        "address": "0xeb52620b04e8eacfd795353f2827673887f292e0"
    },
    "Gold": {
        "symbol": "Gold",
        "decimals": 18,
        "name": "CyberDragon Gold",
        "address": "0xb3a6381070b1a15169dea646166ec0699fdaea79"
    },
    "gold8": {
        "symbol": "gold8",
        "decimals": 18,
        "name": "GOLD8",
        "address": "0x066aee69d93dee28b32a57febd1878a2d94f6b0c"
    },
    "GOT": {
        "symbol": "GOT",
        "decimals": 18,
        "name": "Era GOT Token",
        "address": "0xda71e3ec0d579fed5dbaba31eead3ceb9e77a928"
    },
    "GOV": {
        "symbol": "GOV",
        "decimals": 18,
        "name": "GovWorld Official",
        "address": "0xcc7a91413769891de2e9ebbfc96d2eb1874b5760"
    },
    "GQ": {
        "symbol": "GQ",
        "decimals": 18,
        "name": "Galactic Quadrant",
        "address": "0xf700d4c708c2be1463e355f337603183d20e0808"
    },
    "GRBE": {
        "symbol": "GRBE",
        "decimals": 18,
        "name": "Green_Beli_v2",
        "address": "0x5ca4e7294b14ea5745ee2a688990e0cb68503219"
    },
    "Grimace": {
        "symbol": "Grimace",
        "decimals": 18,
        "name": "GrimaceCoin",
        "address": "0xc6759a4fc56b3ce9734035a56b36e8637c45b77e"
    },
    "GRV": {
        "symbol": "GRV",
        "decimals": 8,
        "name": "GroveC",
        "address": "0xf33893de6eb6ae9a67442e066ae9abd228f5290c"
    },
    "GS": {
        "symbol": "GS",
        "decimals": 18,
        "name": "Gen Shards",
        "address": "0x9ba4c78b048eeed69f4ed3cfddeda7b51baf7ca8"
    },
    "GSC": {
        "symbol": "GSC",
        "decimals": 18,
        "name": "Gunstar Metaverse Currency",
        "address": "0x639fc0c006bd7050e2c359295b41a79cb28694ba"
    },
    "GST": {
        "symbol": "GST",
        "decimals": 8,
        "name": "GreenSatoshiToken",
        "address": "0x4a2c860cec6471b9f5f5a336eb4f38bb21683c98"
    },
    "GTH": {
        "symbol": "GTH",
        "decimals": 18,
        "name": "Gather",
        "address": "0xeb986da994e4a118d5956b02d8b7c3c7ce373674"
    },
    "GTON": {
        "symbol": "GTON",
        "decimals": 18,
        "name": "Graviton",
        "address": "0x64d5baf5ac030e2b7c435add967f787ae94d0205"
    },
    "GUILD": {
        "symbol": "GUILD",
        "decimals": 18,
        "name": "BlockchainSpace [via ChainPort.io]",
        "address": "0x0565805ca3a4105faee51983b0bd8ffb5ce1455c"
    },
    "GULF": {
        "symbol": "GULF",
        "decimals": 18,
        "name": "Gulf Coin",
        "address": "0x014a087b646bd90e7dcead3993f49eb1f4b5f30a"
    },
    "GULL": {
        "symbol": "GULL",
        "decimals": 18,
        "name": "PolyGod",
        "address": "0xca830317146bfdde71e7c0b880e2ec1f66e273ee"
    },
    "GUM": {
        "symbol": "GUM",
        "decimals": 18,
        "name": "GourmetGalaxy",
        "address": "0xc53708664b99df348dd27c3ac0759d2da9c40462"
    },
    "GVT": {
        "symbol": "GVT",
        "decimals": 18,
        "name": "Genesis Vision Token",
        "address": "0xf25868b9e9c62f12192650ac668a2aa69f965f44"
    },
    "GWT": {
        "symbol": "GWT",
        "decimals": 18,
        "name": "GalaxyWarToken",
        "address": "0x552594612f935441c01c6854edf111f343c1ca07"
    },
    "GXE": {
        "symbol": "GXE",
        "decimals": 18,
        "name": "XENO Governance Token",
        "address": "0x510975eda48a97e0ca228dd04d1217292487bea6"
    },
    "GXT": {
        "symbol": "GXT",
        "decimals": 18,
        "name": "Gem Exchange and Trading",
        "address": "0x3107c0a1126268ca303f8d99c712392fa596e6d7"
    },
    "GYM AI": {
        "symbol": "GYM AI",
        "decimals": 18,
        "name": "GYM AI",
        "address": "0xe65725fedb66586cbe32615e097a01c0aa43ae89"
    },
    "GYMNET": {
        "symbol": "GYMNET",
        "decimals": 18,
        "name": "GYM NETWORK V2",
        "address": "0x0012365f0a1e5f30a5046c680dcb21d07b15fcf7"
    },
    "GYRO": {
        "symbol": "GYRO",
        "decimals": 9,
        "name": "Gyro",
        "address": "0x1b239abe619e74232c827fbe5e49a4c072bd869d"
    },
    "GZONE": {
        "symbol": "GZONE",
        "decimals": 18,
        "name": "GAMEZONE.io",
        "address": "0xb6adb74efb5801160ff749b1985fd3bd5000e938"
    },
    "H2O": {
        "symbol": "H2O",
        "decimals": 18,
        "name": "Trickle",
        "address": "0xb8b932d41d6be935ce1666aaf41f056093f9faee"
    },
    "HAI": {
        "symbol": "HAI",
        "decimals": 8,
        "name": "Hacken Token",
        "address": "0xaa9e582e5751d703f85912903bacaddfed26484c"
    },
    "HAKA": {
        "symbol": "HAKA",
        "decimals": 18,
        "name": "TribeOne",
        "address": "0xd85ad783cc94bd04196a13dc042a3054a9b52210"
    },
    "HAKKA": {
        "symbol": "HAKKA",
        "decimals": 18,
        "name": "Hakka Finance on xDai on BSC",
        "address": "0x1d1eb8e8293222e1a29d2c0e4ce6c0acfd89aaac"
    },
    "HALO": {
        "symbol": "HALO",
        "decimals": 9,
        "name": "HALO COIN",
        "address": "0x1894251aebcff227133575ed3069be9670e25db0"
    },
    "HAM": {
        "symbol": "HAM",
        "decimals": 7,
        "name": "Hamster",
        "address": "0x679d5b2d94f454c950d683d159b87aa8eae37c9e"
    },
    "HAPI": {
        "symbol": "HAPI",
        "decimals": 18,
        "name": "HAPI",
        "address": "0xd9c2d319cd7e6177336b0a9c93c21cb48d84fb54"
    },
    "HAPPY": {
        "symbol": "HAPPY",
        "decimals": 18,
        "name": "HappyFans",
        "address": "0xf5d8a096cccb31b9d7bce5afe812be23e3d4690d"
    },
    "HAY": {
        "symbol": "HAY",
        "decimals": 18,
        "name": "Hay Destablecoin",
        "address": "0x0782b6d8c4551b9760e74c0545a9bcd90bdc41e5"
    },
    "HBIT": {
        "symbol": "HBIT",
        "decimals": 18,
        "name": "HashBit-Peg HBIT Token",
        "address": "0xeda3866f07566d9379a91a07f8d62e19c03183e0"
    },
    "HDV": {
        "symbol": "HDV",
        "decimals": 5,
        "name": "Hydracoin",
        "address": "0x8cd0d76c0ad377378ab6ce878a7be686223497ee"
    },
    "HE": {
        "symbol": "HE",
        "decimals": 18,
        "name": "Heroes&Empires",
        "address": "0x20d39a5130f799b95b55a930e5b7ebc589ea9ed8"
    },
    "HEC": {
        "symbol": "HEC",
        "decimals": 9,
        "name": "Hector",
        "address": "0x638eebe886b0e9e7c6929e69490064a6c94d204d"
    },
    "HEE": {
        "symbol": "HEE",
        "decimals": 18,
        "name": "BFHealthToken",
        "address": "0xb47e21328b4f1c6d685c213d707fab3edb234fa0"
    },
    "Hegg": {
        "symbol": "Hegg",
        "decimals": 18,
        "name": "Hummingbird Egg Token",
        "address": "0x778682c19797d985c595429fbc51d67736013a86"
    },
    "HELLO": {
        "symbol": "HELLO",
        "decimals": 18,
        "name": "HELLO",
        "address": "0x0f1cbed8efa0e012adbccb1638d0ab0147d5ac00"
    },
    "Helmet": {
        "symbol": "Helmet",
        "decimals": 18,
        "name": "Helmet.insure Governance Token",
        "address": "0x948d2a81086a075b3130bac19e4c6dee1d2e3fe8"
    },
    "HER": {
        "symbol": "HER",
        "decimals": 9,
        "name": "HerityNetwork",
        "address": "0x8c18ffd66d943c9b0ad3dc40e2d64638f1e6e1ab"
    },
    "HERA": {
        "symbol": "HERA",
        "decimals": 18,
        "name": "HERA TOKEN",
        "address": "0x49c7295ff86eabf5bf58c6ebc858db4805738c01"
    },
    "HERO": {
        "symbol": "HERO",
        "decimals": 18,
        "name": "Metahero",
        "address": "0xd40bedb44c081d2935eeba6ef5a3c8a31a1bbe13"
    },
    "HEROEGG": {
        "symbol": "HEROEGG",
        "decimals": 18,
        "name": "HeroFiEgg",
        "address": "0xcfbb1bfa710cb2eba070cc3bec0c35226fea4baf"
    },
    "HF": {
        "symbol": "HF",
        "decimals": 9,
        "name": "Have Fun",
        "address": "0x759bd4ed07a34b9ea761f8f2ed9f0e102675a29c"
    },
    "HGHG": {
        "symbol": "HGHG",
        "decimals": 8,
        "name": "HUGHUG",
        "address": "0xb626213cb1d52caa1ed71e2a0e62c0113ed8d642"
    },
    "HI": {
        "symbol": "HI",
        "decimals": 18,
        "name": "hi Dollar",
        "address": "0x77087ab5df23cfb52449a188e80e9096201c2097"
    },
    "HIBIKI": {
        "symbol": "HIBIKI",
        "decimals": 18,
        "name": "Hibiki.finance",
        "address": "0xa532cfaa916c465a094daf29fea07a13e41e5b36"
    },
    "HIGH": {
        "symbol": "HIGH",
        "decimals": 18,
        "name": "Highstreet Token",
        "address": "0x5f4bde007dc06b867f86ebfe4802e34a1ffeed63"
    },
    "HK": {
        "symbol": "HK",
        "decimals": 18,
        "name": "Hongkong",
        "address": "0x57534804b9485209a2fc55698a0f2112ae389342"
    },
    "HKD": {
        "symbol": "HKD",
        "decimals": 18,
        "name": "HongKongDAO",
        "address": "0xb1a1d06d42a43a8fcfdc7fdcd744f7ef03e8ad1a"
    },
    "HMR": {
        "symbol": "HMR",
        "decimals": 18,
        "name": "HOMEROS",
        "address": "0x32d12029f62260e239b5b5c8f0bea9cb382cfdd6"
    },
    "HMT": {
        "symbol": "HMT",
        "decimals": 8,
        "name": "Humanize",
        "address": "0x71e67b8d88718d113fc7edbd95f7ca380222b3c6"
    },
    "HNTR": {
        "symbol": "HNTR",
        "decimals": 18,
        "name": "Hunter Token",
        "address": "0x83451a4e3585fda74feb348ad929f2c4ca189660"
    },
    "HOD": {
        "symbol": "HOD",
        "decimals": 18,
        "name": "Hodooi.com Token",
        "address": "0x19a4866a85c652eb4a2ed44c42e4cb2863a62d51"
    },
    "HODL": {
        "symbol": "HODL",
        "decimals": 9,
        "name": "HODL",
        "address": "0x0e9766df73973abcfedde700497c57110ee5c301"
    },
    "HOGE": {
        "symbol": "HOGE",
        "decimals": 9,
        "name": "hoge.finance",
        "address": "0xa4fffc757e8c4f24e7b209c033c123d20983ad40"
    },
    "HOL": {
        "symbol": "HOL",
        "decimals": 18,
        "name": "Hololoot Coin",
        "address": "0xa797fa4bda7c5a4b3afe73573b9d2ab942365c6f"
    },
    "HomieCoin": {
        "symbol": "HomieCoin",
        "decimals": 18,
        "name": "Homie Wars",
        "address": "0xb534b21082e44a9c5865876f41f8dd348278fdf2"
    },
    "HOOK": {
        "symbol": "HOOK",
        "decimals": 18,
        "name": "Hook Token",
        "address": "0xa260e12d2b924cb899ae80bb58123ac3fee1e2f0"
    },
    "HOOP": {
        "symbol": "HOOP",
        "decimals": 18,
        "name": "Primal Hoop",
        "address": "0xf19cfb40b3774df6eed83169ad5ab0aaf6865f25"
    },
    "HOP": {
        "symbol": "HOP",
        "decimals": 9,
        "name": "HOPPY",
        "address": "0x984811e6f2695192add6f88615df637bf52a5cae"
    },
    "HORD": {
        "symbol": "HORD",
        "decimals": 18,
        "name": "Chainport.io-Peg HORD Token",
        "address": "0x39d4549908e7adcee9b439429294eeb4c65c2c9e"
    },
    "HOTCROSS": {
        "symbol": "HOTCROSS",
        "decimals": 18,
        "name": "Hot Cross Token",
        "address": "0x4fa7163e153419e0e1064e418dd7a99314ed27b6"
    },
    "HotDoge": {
        "symbol": "HotDoge",
        "decimals": 9,
        "name": "Hot Doge",
        "address": "0x1991501f1398663f69dd7391c055bb0df6514f76"
    },
    "HotMoon": {
        "symbol": "HotMoon",
        "decimals": 18,
        "name": "HotMoon Token",
        "address": "0xc1357d32bf23fd5fe3280681a36755b6f150442e"
    },
    "HP": {
        "symbol": "HP",
        "decimals": 18,
        "name": "Heropark",
        "address": "0xede1f9cdb98b4ca6a804de268b0aca18dce192e8"
    },
    "HPO": {
        "symbol": "HPO",
        "decimals": 18,
        "name": "Hippopotamus",
        "address": "0xa0ed3c520dc0632657ad2eaaf19e26c4fd431a84"
    },
    "HSE": {
        "symbol": "HSE",
        "decimals": 18,
        "name": "Hest stake",
        "address": "0x4a6d76c3a65f296468d7910c79f12fdd5202a920"
    },
    "HSF": {
        "symbol": "HSF",
        "decimals": 18,
        "name": "Hillstone.Finance",
        "address": "0xda8929a6338f408cc78c1845fb4f71bffd2cfcfb"
    },
    "HTD": {
        "symbol": "HTD",
        "decimals": 18,
        "name": "HeroesTD",
        "address": "0x5e2689412fae5c29bd575fbe1d5c1cd1e0622a8f"
    },
    "HTZ": {
        "symbol": "HTZ",
        "decimals": 4,
        "name": "Hertz Network",
        "address": "0xb5bba78b4df2d47dd46078514a3e296ab3c344fe"
    },
    "HUB": {
        "symbol": "HUB",
        "decimals": 18,
        "name": "ScoutHUB Token",
        "address": "0xee7b7c840de85ad277cdddaef63b3b29672a3c58"
    },
    "HUDI": {
        "symbol": "HUDI",
        "decimals": 18,
        "name": "HUDI",
        "address": "0x83d8ea5a4650b68cd2b57846783d86df940f7458"
    },
    "HUMAI": {
        "symbol": "HUMAI",
        "decimals": 18,
        "name": "Humanoid AI",
        "address": "0xf6b52a29671e74e6b3a7592ef79039abb64e2885"
    },
    "HUSKY": {
        "symbol": "HUSKY",
        "decimals": 18,
        "name": "Husky",
        "address": "0x52d88a9a2a20a840d7a336d21e427e9ad093deea"
    },
    "HUSL": {
        "symbol": "HUSL",
        "decimals": 18,
        "name": "The HUSL [via ChainPort.io]",
        "address": "0x284ac5af363bde6ef5296036af8fb0e9cc347b41"
    },
    "HVT": {
        "symbol": "HVT",
        "decimals": 8,
        "name": "HyperVerse Token",
        "address": "0xaafa10755b3b1dbf46e86d973c3f27f3671ed9db"
    },
    "HWL": {
        "symbol": "HWL",
        "decimals": 18,
        "name": "HOWL",
        "address": "0x549cc5df432cdbaebc8b9158a6bdfe1cbd0ba16d"
    },
    "HYDRO": {
        "symbol": "HYDRO",
        "decimals": 18,
        "name": "HYDRO TOKEN",
        "address": "0xf3dbb49999b25c9d6641a9423c7ad84168d00071"
    },
    "HyPC": {
        "symbol": "HyPC",
        "decimals": 6,
        "name": "HyperCycle Token",
        "address": "0x7881cd2b5724431372f57c50e91611352557a606"
    },
    "HYPE": {
        "symbol": "HYPE",
        "decimals": 18,
        "name": "HYPE",
        "address": "0x62891201468a517eeec00fe72f33595a3f9047ee"
    },
    "HYPER": {
        "symbol": "HYPER",
        "decimals": 7,
        "name": "HYPERCHAIN",
        "address": "0xee5b03b769ca6c690d140cafb52fc8de3f38fc28"
    },
    "HYPES": {
        "symbol": "HYPES",
        "decimals": 18,
        "name": "HYPES",
        "address": "0xe8e0d396f0881c0fab9319e441223f9780b8305c"
    },
    "HYVE": {
        "symbol": "HYVE",
        "decimals": 18,
        "name": "HYVE",
        "address": "0xf6565a97dc832d93dc83b75ee9aa5c7e8ecb0f9d"
    },
    "HZN": {
        "symbol": "HZN",
        "decimals": 18,
        "name": "Horizon Protocol",
        "address": "0xc0eff7749b125444953ef89682201fb8c6a917cd"
    },
    "IBAT": {
        "symbol": "IBAT",
        "decimals": 9,
        "name": "BattleInfinity",
        "address": "0x19cd9b8e42d4ef62c3ea124110d5cfd283ceac43"
    },
    "iBG": {
        "symbol": "iBG",
        "decimals": 18,
        "name": "IBG Token",
        "address": "0x5c46c55a699a6359e451b2c99344138420c87261"
    },
    "IBOX": {
        "symbol": "IBOX",
        "decimals": 18,
        "name": "Infinity BOX",
        "address": "0xe919facc09ce21f98d1693e9781af9ea61460e2a"
    },
    "IBS": {
        "symbol": "IBS",
        "decimals": 18,
        "name": "IBStoken",
        "address": "0x57d2a45653b329fac354b04cead92c4db71cf09f"
    },
    "ICE": {
        "symbol": "ICE",
        "decimals": 18,
        "name": "IceToken",
        "address": "0xf16e81dce15b08f326220742020379b855b87df9"
    },
    "ID": {
        "symbol": "ID",
        "decimals": 18,
        "name": "SPACE ID",
        "address": "0x2dff88a56767223a5529ea5960da7a3f5f766406"
    },
    "IDIA": {
        "symbol": "IDIA",
        "decimals": 18,
        "name": "Impossible Decentralized Incubator Access Token",
        "address": "0x0b15ddf19d47e6a86a56148fb4afffc6929bcb89"
    },
    "IDM": {
        "symbol": "IDM",
        "decimals": 9,
        "name": "IDM Token",
        "address": "0x14b13e06f75e1f0fd51ca2e699589ef398e10f4c"
    },
    "iDNA": {
        "symbol": "iDNA",
        "decimals": 18,
        "name": "Wrapped Idena",
        "address": "0x0de08c1abe5fb86dd7fd2ac90400ace305138d5b"
    },
    "IDO": {
        "symbol": "IDO",
        "decimals": 9,
        "name": "INTERSTELLAR DOMAIN ORDER",
        "address": "0x617ba3d39e96c084e60c6db3f7b365a96ee4e555"
    },
    "IDRT": {
        "symbol": "IDRT",
        "decimals": 2,
        "name": "Rupiah Token",
        "address": "0x66207e39bb77e6b99aab56795c7c340c08520d83"
    },
    "iDYP": {
        "symbol": "iDYP",
        "decimals": 18,
        "name": "iDeFiYieldProtocol",
        "address": "0xbd100d061e120b2c67a24453cf6368e63f1be056"
    },
    "IF": {
        "symbol": "IF",
        "decimals": 18,
        "name": "Impossible Finance",
        "address": "0xb0e1fc65c1a741b4662b813eb787d369b8614af1"
    },
    "IGU": {
        "symbol": "IGU",
        "decimals": 18,
        "name": "IGU Token",
        "address": "0x201bc9f242f74c47bbd898a5dc99cdcd81a21943"
    },
    "IGUP": {
        "symbol": "IGUP",
        "decimals": 18,
        "name": "IGUP Token",
        "address": "0x522d0f9f3eff479a5b256bb1c1108f47b8e1a153"
    },
    "IHC": {
        "symbol": "IHC",
        "decimals": 18,
        "name": "Inflation Hedging Coin",
        "address": "0x86a53fcd199212fea44fa7e16eb1f28812be911d"
    },
    "ILA": {
        "symbol": "ILA",
        "decimals": 18,
        "name": "InfiniteLaunch",
        "address": "0x4fbedc7b946e489208ded562e8e5f2bc83b7de42"
    },
    "IM": {
        "symbol": "IM",
        "decimals": 18,
        "name": "Internet Money",
        "address": "0xac5d23ce5e4a5eb11a5407a5fbee201a75e8c8ad"
    },
    "IMO": {
        "symbol": "IMO",
        "decimals": 18,
        "name": "IMO",
        "address": "0x94d79c325268c898d2902050730f27a478c56cc1"
    },
    "IMT": {
        "symbol": "IMT",
        "decimals": 18,
        "name": "IMOV",
        "address": "0x7b8779e01d117ec7e220f8299a6f93672e8eae23"
    },
    "INAZ": {
        "symbol": "INAZ",
        "decimals": 18,
        "name": "Infinity Arena Zeronium",
        "address": "0x6e551e88d0ed3ebd56f6b1f42b03bf9e4d68c47f"
    },
    "IND": {
        "symbol": "IND",
        "decimals": 18,
        "name": "AEROTYME",
        "address": "0x7c59c88fc352ccb7305212a8afd797cdd6a8a845"
    },
    "INF": {
        "symbol": "INF",
        "decimals": 18,
        "name": "Infam",
        "address": "0x000000ef379ee7f4c051f4b9af901a9219d9ec5c"
    },
    "ING": {
        "symbol": "ING",
        "decimals": 18,
        "name": "Infinity Universe Gem",
        "address": "0xae7c682ba26ad6835b6150ffb35f22db9987f509"
    },
    "INJ": {
        "symbol": "INJ",
        "decimals": 18,
        "name": "Injective Protocol",
        "address": "0xa2b726b1145a4773f68593cf171187d8ebe4d495"
    },
    "INR": {
        "symbol": "INR",
        "decimals": 18,
        "name": "INERY",
        "address": "0xab725d0a10c3f24725c89f5765ae5794a26c1336"
    },
    "INSUR": {
        "symbol": "INSUR",
        "decimals": 18,
        "name": "Bsc-Peg INSUR Token",
        "address": "0x3192ccddf1cdce4ff055ebc80f3f0231b86a7e30"
    },
    "INT": {
        "symbol": "INT",
        "decimals": 18,
        "name": "Internet Node Token",
        "address": "0x0e349b8272b2e986436c8bd2b2b7944ae28d8778"
    },
    "INTER": {
        "symbol": "INTER",
        "decimals": 18,
        "name": "Inter",
        "address": "0x5c7bb1e6c45b055a7831f0c82740f9677bbf6d43"
    },
    "INTL": {
        "symbol": "INTL",
        "decimals": 18,
        "name": "Intelly",
        "address": "0xe2efe9d38e21293347018914ee1d23913ecb811c"
    },
    "INUKO": {
        "symbol": "INUKO",
        "decimals": 18,
        "name": "Inuko Coin",
        "address": "0xea51801b8f5b88543ddad3d1727400c15b209d8f"
    },
    "INVEST": {
        "symbol": "INVEST",
        "decimals": 18,
        "name": "Investdex",
        "address": "0x853a8ab1c365ea54719eb13a54d6b22f1fbe7feb"
    },
    "IOEN": {
        "symbol": "IOEN",
        "decimals": 18,
        "name": "Internet of Energy Network",
        "address": "0x033dcfef3366772fbcdea4f33f1d96db8f93676b"
    },
    "IOI": {
        "symbol": "IOI",
        "decimals": 6,
        "name": "IOI Token  via ChainPort.io",
        "address": "0x959229d94c9060552daea25ac17193bca65d7884"
    },
    "IONZ": {
        "symbol": "IONZ",
        "decimals": 6,
        "name": "IONZ",
        "address": "0x7268192a0e5882b21f13fc857cf78299d8e3d75b"
    },
    "IOTX": {
        "symbol": "IOTX",
        "decimals": 18,
        "name": "IoTeX Network",
        "address": "0x9678e42cebeb63f23197d726b29b1cb20d0064e5"
    },
    "iOWN": {
        "symbol": "iOWN",
        "decimals": 18,
        "name": "iOWN Token",
        "address": "0x5d681b9839e237c4f1dc7d7486e6cb0a12b9654f"
    },
    "IPAD": {
        "symbol": "IPAD",
        "decimals": 18,
        "name": "Infinity Pad",
        "address": "0xa7266989b0df675cc8257d53b6bc1358faf6626a"
    },
    "IPISTR": {
        "symbol": "IPISTR",
        "decimals": 18,
        "name": "IPI Shorter",
        "address": "0x888888888888f195e27a2e0f98d712952ab9348e"
    },
    "IPX": {
        "symbol": "IPX",
        "decimals": 18,
        "name": "InpulseX",
        "address": "0xcdb96d3aef363a036c6cf6c9b5736d79f0e404e2"
    },
    "IRENA": {
        "symbol": "IRENA",
        "decimals": 9,
        "name": "IRENA Green Energy",
        "address": "0x9eeb6c5ff183e6001c65a12d70026b900ae76781"
    },
    "IRISTOKEN": {
        "symbol": "IRISTOKEN",
        "decimals": 9,
        "name": "IRIS ECOSYSTEM",
        "address": "0x7b9f36a2f331ece03a7483d2713cfd806f9beef2"
    },
    "IRON": {
        "symbol": "IRON",
        "decimals": 18,
        "name": "IRON Stablecoin",
        "address": "0x7b65b489fe53fce1f6548db886c08ad73111ddd8"
    },
    "IRT": {
        "symbol": "IRT",
        "decimals": 18,
        "name": "Infinity Rocket Token",
        "address": "0xcbe5bca571628894a38836b0bae833ff012f71d8"
    },
    "ISHND": {
        "symbol": "ISHND",
        "decimals": 18,
        "name": "Stronghands Finance",
        "address": "0x1cc1aca0dae2d6c4a0e8ae7b4f2d01eabbc435ee"
    },
    "ISP": {
        "symbol": "ISP",
        "decimals": 18,
        "name": "Ispolink Token",
        "address": "0xd2e7b964770fcf51df088a5f0bb2d33a3c60cccf"
    },
    "ISTEP": {
        "symbol": "ISTEP",
        "decimals": 18,
        "name": "ISTEP",
        "address": "0x67343c29c0fd9827f33e675e0eb80773f9444444"
    },
    "ITAM": {
        "symbol": "ITAM",
        "decimals": 18,
        "name": "ITAM",
        "address": "0x04c747b40be4d535fc83d09939fb0f626f32800b"
    },
    "ITEM": {
        "symbol": "ITEM",
        "decimals": 18,
        "name": "ITEMToken_v1",
        "address": "0x517396bd11d750e4417b82f2b0fcfa62a4f2bb96"
    },
    "ITLR": {
        "symbol": "ITLR",
        "decimals": 18,
        "name": "iTeller",
        "address": "0x7646cbf726b39a5417834aec7fc4d57428111a00"
    },
    "IVG": {
        "symbol": "IVG",
        "decimals": 9,
        "name": "IVOGEL",
        "address": "0x6af6789856a2e820e3d145bfe4950ff17e3a4ecb"
    },
    "JADE": {
        "symbol": "JADE",
        "decimals": 9,
        "name": "JADE",
        "address": "0x7ad7242a99f21aa543f9650a56d141c57e4f6081"
    },
    "JERRY": {
        "symbol": "JERRY",
        "decimals": 9,
        "name": "Jerry Inu",
        "address": "0xdd6978f36c98aff4287e5ac803c9cf1b865641f6"
    },
    "jEUR": {
        "symbol": "jEUR",
        "decimals": 18,
        "name": "Jarvis Synthetic Euro",
        "address": "0x23b8683ff98f9e4781552dfe6f12aa32814924e8"
    },
    "JGN": {
        "symbol": "JGN",
        "decimals": 18,
        "name": "Juggernaut DeFi",
        "address": "0xc13b7a43223bb9bf4b69bd68ab20ca1b79d81c75"
    },
    "JM": {
        "symbol": "JM",
        "decimals": 8,
        "name": "JustMoney",
        "address": "0x388d819724dd6d71760a38f00dc01d310d879771"
    },
    "JMPT": {
        "symbol": "JMPT",
        "decimals": 18,
        "name": "JumpToken",
        "address": "0x88d7e9b65dc24cf54f5edef929225fc3e1580c25"
    },
    "JOE": {
        "symbol": "JOE",
        "decimals": 18,
        "name": "JoeToken",
        "address": "0x371c7ec6d8039ff7933a2aa28eb827ffe1f52f07"
    },
    "JOJO": {
        "symbol": "JOJO",
        "decimals": 9,
        "name": "JOJO",
        "address": "0x78a499a998bdd5a84cf8b5abe49100d82de12f1c"
    },
    "JOLT": {
        "symbol": "JOLT",
        "decimals": 18,
        "name": "Joltify Coin",
        "address": "0x7db21353a0c4659b6a9a0519066aa8d52639dfa5"
    },
    "JP": {
        "symbol": "JP",
        "decimals": 9,
        "name": "JP",
        "address": "0x86cd1faf05abbb705842ec3c98ef5006173fb4d6"
    },
    "JRIT": {
        "symbol": "JRIT",
        "decimals": 18,
        "name": "JeritEx",
        "address": "0xf2619476bd0ca0eda08744029c66b62a904c2bf8"
    },
    "JUV": {
        "symbol": "JUV",
        "decimals": 2,
        "name": "Juventus",
        "address": "0xc40c9a843e1c6d01b7578284a9028854f6683b1b"
    },
    "JW": {
        "symbol": "JW",
        "decimals": 8,
        "name": "Jasan Wellness",
        "address": "0xab785054251db0fc44538f5deebe7507b748b692"
    },
    "KABOSU": {
        "symbol": "KABOSU",
        "decimals": 9,
        "name": "Kabosu",
        "address": "0x4a824ee819955a7d769e03fe36f9e0c3bd3aa60b"
    },
    "KABY": {
        "symbol": "KABY",
        "decimals": 18,
        "name": "Kaby Arena",
        "address": "0x02a40c048ee2607b5f5606e445cfc3633fb20b58"
    },
    "KAI": {
        "symbol": "KAI",
        "decimals": 18,
        "name": "KardiaChain Token",
        "address": "0x39ae8eefb05138f418bb27659c21632dc1ddab10"
    },
    "KAKA": {
        "symbol": "KAKA",
        "decimals": 18,
        "name": "KAKA Metaverse Token",
        "address": "0x26a1bdfa3bb86b2744c4a42ebfdd205761d13a8a"
    },
    "KAKI": {
        "symbol": "KAKI",
        "decimals": 18,
        "name": "Doge KaKi",
        "address": "0x42414624c55a9cba80789f47c8f9828a7974e40f"
    },
    "KALI ": {
        "symbol": "KALI ",
        "decimals": 18,
        "name": "KALISSA ",
        "address": "0x950481789959cd6d77f1b88c2e1f61e30608c4e2"
    },
    "KALM": {
        "symbol": "KALM",
        "decimals": 18,
        "name": "Kalmar Token",
        "address": "0x4ba0057f784858a48fe351445c672ff2a3d43515"
    },
    "KAMPAY": {
        "symbol": "KAMPAY",
        "decimals": 18,
        "name": "Kampay",
        "address": "0x8e984e03ab35795c60242c902ece2450242c90e9"
    },
    "KASA": {
        "symbol": "KASA",
        "decimals": 18,
        "name": "Kasa Central",
        "address": "0x8106789b240e5e1b34643c052f1dc1b7a1a451a5"
    },
    "KATA": {
        "symbol": "KATA",
        "decimals": 18,
        "name": "Katana Inu",
        "address": "0x6d6ba21e4c4b29ca7bfa1c344ba1e35b8dae7205"
    },
    "KATZ": {
        "symbol": "KATZ",
        "decimals": 18,
        "name": "LUCKY CATS",
        "address": "0x683bbaa70fd8e2cf62617e48b100a7609ee48946"
    },
    "KAVA": {
        "symbol": "KAVA",
        "decimals": 6,
        "name": "KAVA",
        "address": "0x5f88ab06e8dfe89df127b2430bba4af600866035"
    },
    "KBD": {
        "symbol": "KBD",
        "decimals": 18,
        "name": "Kyberdyne",
        "address": "0xe3e3f8218562a7c9b594bef2946ec72f1b043ae8"
    },
    "KBOX": {
        "symbol": "KBOX",
        "decimals": 18,
        "name": "KBOX Token",
        "address": "0x3523d58d8036b1c5c9a13493143c97aefc5ad422"
    },
    "KCAKE": {
        "symbol": "KCAKE",
        "decimals": 18,
        "name": "KITTY CAKE",
        "address": "0xc22e8114818a918260662375450e19ac73d32852"
    },
    "KCCPAD": {
        "symbol": "KCCPAD",
        "decimals": 18,
        "name": "KCCPAD.io",
        "address": "0x11582ef4642b1e7f0a023804b497656e2663bc9b"
    },
    "KDG": {
        "symbol": "KDG",
        "decimals": 18,
        "name": "KDG Token",
        "address": "0x87a2d9a9a6b2d61b2a57798f1b4b2ddd19458fb6"
    },
    "KEL": {
        "symbol": "KEL",
        "decimals": 18,
        "name": "KelVPN token",
        "address": "0x4e1b16ef22935a575a6811d4616f98c4077e4408"
    },
    "KEX": {
        "symbol": "KEX",
        "decimals": 6,
        "name": "KIRA Network",
        "address": "0x8d11ec38a3eb5e956b052f67da8bdc9bef8abf3e"
    },
    "KEY": {
        "symbol": "KEY",
        "decimals": 18,
        "name": "MoMo KEY",
        "address": "0x85c128ee1feeb39a59490c720a9c563554b51d33"
    },
    "KEYFI": {
        "symbol": "KEYFI",
        "decimals": 18,
        "name": "KeyFi Token",
        "address": "0x4b6000f9163de2e3f0a01ec37e06e1469dbbce9d"
    },
    "KFT": {
        "symbol": "KFT",
        "decimals": 18,
        "name": "Knit Finance",
        "address": "0x1b41a1ba7722e6431b1a782327dbe466fe1ee9f9"
    },
    "KIAN": {
        "symbol": "KIAN",
        "decimals": 18,
        "name": "Kianite",
        "address": "0x5ece3f1542c4e1a06767457e4d8286bea772fc41"
    },
    "KIBA": {
        "symbol": "KIBA",
        "decimals": 18,
        "name": "Kiba Inu",
        "address": "0xc3afde95b6eb9ba8553cdaea6645d45fb3a7faf5"
    },
    "KICK": {
        "symbol": "KICK",
        "decimals": 10,
        "name": "KickToken",
        "address": "0x824a50df33ac1b41afc52f4194e2e8356c17c3ac"
    },
    "KICKS": {
        "symbol": "KICKS",
        "decimals": 18,
        "name": "GetKicks",
        "address": "0xfeb4e9b932ef708c498cc997abe51d0ee39300cf"
    },
    "KING": {
        "symbol": "KING",
        "decimals": 9,
        "name": "King",
        "address": "0x74f08af7528ffb751e3a435ddd779b5c4565e684"
    },
    "KINGSHIB": {
        "symbol": "KINGSHIB",
        "decimals": 9,
        "name": "KING SHIBA",
        "address": "0x84f4f7cdb4574c9556a494dab18ffc1d1d22316c"
    },
    "KISHIMOTO": {
        "symbol": "KISHIMOTO",
        "decimals": 9,
        "name": "Kishimoto",
        "address": "0xae36155a55f04a696b8362777620027882b31db5"
    },
    "KKC": {
        "symbol": "KKC",
        "decimals": 6,
        "name": "Knoknok",
        "address": "0x2e1a87c9a9b121c0a72ae64d99138f586ffb8929"
    },
    "KKMA": {
        "symbol": "KKMA",
        "decimals": 18,
        "name": "Koakuma",
        "address": "0x18d3be5ecddf79279004e2d90d507594c2d46f85"
    },
    "KKT": {
        "symbol": "KKT",
        "decimals": 18,
        "name": "Kingdom Karnage Token",
        "address": "0xe64017bdacbe7dfc84886c3704a26d566e7550de"
    },
    "KMD": {
        "symbol": "KMD",
        "decimals": 18,
        "name": "Komodo",
        "address": "0x2003f7ba57ea956b05b85c60b4b2ceea9b111256"
    },
    "KMON": {
        "symbol": "KMON",
        "decimals": 18,
        "name": "KmonCoin",
        "address": "0xc732b6586a93b6b7cf5fed3470808bc74998224d"
    },
    "KNC": {
        "symbol": "KNC",
        "decimals": 18,
        "name": "Kyber Network Crystal",
        "address": "0xfe56d5892bdffc7bf58f2e84be1b2c32d21c308b"
    },
    "KNFT": {
        "symbol": "KNFT",
        "decimals": 18,
        "name": "KStarNFT",
        "address": "0x46e83fbcc5623172ee61935c96b7276ab92562de"
    },
    "KNT": {
        "symbol": "KNT",
        "decimals": 18,
        "name": "Kinect",
        "address": "0x078efa21a70337834788c3e6f0a99275f71393f0"
    },
    "KOCHI": {
        "symbol": "KOCHI",
        "decimals": 18,
        "name": "Kochi Ken",
        "address": "0x41b2f7acc00035f9b1cec868b5054a6238c0a910"
    },
    "KODA": {
        "symbol": "KODA",
        "decimals": 9,
        "name": "Koda Cryptocurrency",
        "address": "0x8094e772fa4a60bdeb1dfec56ab040e17dd608d5"
    },
    "KOM": {
        "symbol": "KOM",
        "decimals": 8,
        "name": "Kommunitas",
        "address": "0x471ea49dd8e60e697f4cac262b5fafcc307506e4"
    },
    "KPAD": {
        "symbol": "KPAD",
        "decimals": 18,
        "name": "KickPad",
        "address": "0xcfefa64b0ddd611b125157c41cd3827f2e8e8615"
    },
    "KPL": {
        "symbol": "KPL",
        "decimals": 18,
        "name": "Kepple",
        "address": "0x8ffdcb0cabccf2767366a2eba6e2fdcc37baa1b2"
    },
    "KRD": {
        "symbol": "KRD",
        "decimals": 18,
        "name": "Krypton DAO",
        "address": "0xb020805e0bc7f0e353d1343d67a239f417d57bbf"
    },
    "KRN": {
        "symbol": "KRN",
        "decimals": 9,
        "name": "KRYZA Network",
        "address": "0x4e6d79cddec12c229d53b38c11b204bcec118885"
    },
    "KRS": {
        "symbol": "KRS",
        "decimals": 18,
        "name": "Kingdom Raids",
        "address": "0x37b53894e7429f794b56f22a32e1695567ee9913"
    },
    "KRW": {
        "symbol": "KRW",
        "decimals": 18,
        "name": "KROWN",
        "address": "0x1446f3cedf4d86a9399e49f7937766e6de2a3aab"
    },
    "KSC": {
        "symbol": "KSC",
        "decimals": 18,
        "name": "KingSpeed Crystal",
        "address": "0x3ac0f8cecc1fb0ee6c2017a072d52e85b00c6694"
    },
    "KSN": {
        "symbol": "KSN",
        "decimals": 18,
        "name": "KISSAN",
        "address": "0xc8a11f433512c16ed895245f34bcc2ca44eb06bd"
    },
    "KST": {
        "symbol": "KST",
        "decimals": 18,
        "name": "KSM Starter Token",
        "address": "0x772722b55cdc2a086abd064267a17855eb15e8b3"
    },
    "KSWAP": {
        "symbol": "KSWAP",
        "decimals": 18,
        "name": "KyotoSwap Token",
        "address": "0x29abc4d03d133d8fd1f1c54318428353ce08727e"
    },
    "KT": {
        "symbol": "KT",
        "decimals": 18,
        "name": "KingToken",
        "address": "0x52da44b5e584f730005dac8d2d2acbdee44d4ba3"
    },
    "KTE": {
        "symbol": "KTE",
        "decimals": 18,
        "name": "KyteOne",
        "address": "0x61fa01129ac0bb124d1c60dc9f735c6c579a858b"
    },
    "KTN": {
        "symbol": "KTN",
        "decimals": 18,
        "name": "Kattana",
        "address": "0xdae6c2a48bfaa66b43815c5548b10800919c993e"
    },
    "KUKU": {
        "symbol": "KUKU",
        "decimals": 18,
        "name": "Pankuku",
        "address": "0x84fd7cc4cd689fc021ee3d00759b6d255269d538"
    },
    "KUNCI": {
        "symbol": "KUNCI",
        "decimals": 6,
        "name": "Kunci Coin",
        "address": "0x6cf271270662be1c4fc1b7bb7d7d7fc60cc19125"
    },
    "KVERSE": {
        "symbol": "KVERSE",
        "decimals": 18,
        "name": "KEEPS COIN",
        "address": "0xbe5166e8e8a5cb801f09a6a0a46c42b7c27be755"
    },
    "KWAI": {
        "symbol": "KWAI",
        "decimals": 18,
        "name": "Kwai",
        "address": "0x235d650fc6d9eb7d4bac77e128265295a0054304"
    },
    "KWS": {
        "symbol": "KWS",
        "decimals": 18,
        "name": "Knight War Spirits",
        "address": "0x5d0e95c15ca50f13fb86938433269d03112409fe"
    },
    "KWT": {
        "symbol": "KWT",
        "decimals": 18,
        "name": "Kawaii Token",
        "address": "0x257a8d1e03d17b8535a182301f15290f11674b53"
    },
    "KZEN": {
        "symbol": "KZEN",
        "decimals": 18,
        "name": "Kaizen.Finance",
        "address": "0x4550003152f12014558e5ce025707e4dd841100f"
    },
    "LABS": {
        "symbol": "LABS",
        "decimals": 18,
        "name": "LABS Group V2",
        "address": "0x510ca7d22a84599e7d0f15f09e674056a6255389"
    },
    "LACE": {
        "symbol": "LACE",
        "decimals": 18,
        "name": "Lovelace",
        "address": "0xa3499dd7dbbbd93cb0f8303f8a8ace8d02508e73"
    },
    "LANC": {
        "symbol": "LANC",
        "decimals": 18,
        "name": "Lanceria",
        "address": "0xdd848e0cbfd3771dc7845b10072d973c375271e2"
    },
    "LAUNCH": {
        "symbol": "LAUNCH",
        "decimals": 18,
        "name": "Super Launcher",
        "address": "0xb5389a679151c4b8621b1098c6e0961a3cfee8d4"
    },
    "LAVAX": {
        "symbol": "LAVAX",
        "decimals": 18,
        "name": "LavaX Labs",
        "address": "0xa9be3cd803fa19f2af24412ff0a2a4a67a29de88"
    },
    "Layer": {
        "symbol": "Layer",
        "decimals": 9,
        "name": "Layer Network",
        "address": "0x66e1ecb238b2976fcbd1aeef0e9800b4f03c09f3"
    },
    "LAZIO": {
        "symbol": "LAZIO",
        "decimals": 8,
        "name": "FC Lazio Fan Token",
        "address": "0x77d547256a2cd95f32f67ae0313e450ac200648d"
    },
    "LBL": {
        "symbol": "LBL",
        "decimals": 18,
        "name": "LABEL",
        "address": "0x77edfae59a7948d66e9911a30cc787d2172343d4"
    },
    "LBlock": {
        "symbol": "LBlock",
        "decimals": 9,
        "name": "LuckyBlock",
        "address": "0x2cd96e8c3ff6b5e01169f6e3b61d28204e7810bb"
    },
    "LCEO": {
        "symbol": "LCEO",
        "decimals": 18,
        "name": "LionCeo",
        "address": "0xc60dee4852ee6190cc440e87fc06796ec5ed4bb0"
    },
    "LCR": {
        "symbol": "LCR",
        "decimals": 9,
        "name": "LUCRO",
        "address": "0x988f7c894e4001eeb7b570cde80dffe21cf7b6b9"
    },
    "LCT": {
        "symbol": "LCT",
        "decimals": 18,
        "name": "Local Traders",
        "address": "0x5c65badf7f97345b7b92776b22255c973234efe7"
    },
    "LDO": {
        "symbol": "LDO",
        "decimals": 18,
        "name": "Lido DAO Token",
        "address": "0x986854779804799c1d68867f5e03e601e781e41b"
    },
    "LEAD": {
        "symbol": "LEAD",
        "decimals": 18,
        "name": "Lead Token on BSC",
        "address": "0x2ed9e96edd11a1ff5163599a66fb6f1c77fa9c66"
    },
    "LEGO": {
        "symbol": "LEGO",
        "decimals": 9,
        "name": "Lego Coin",
        "address": "0x520ebccc63e4d0804b35cda25978beb7159bf0cc"
    },
    "LENDA": {
        "symbol": "LENDA",
        "decimals": 18,
        "name": "Lenda",
        "address": "0x2d7a47908d817dd359f9aba7feaa89c92a289c7e"
    },
    "LEO": {
        "symbol": "LEO",
        "decimals": 18,
        "name": "Leo",
        "address": "0x56b331c7e3d68306f26e07492125f0faa9d95343"
    },
    "LEV": {
        "symbol": "LEV",
        "decimals": 18,
        "name": "Lever Token",
        "address": "0xbc194e6f748a222754c3e8b9946922c09e7d4e91"
    },
    "LEVE": {
        "symbol": "LEVE",
        "decimals": 18,
        "name": "Leve Invest",
        "address": "0xb12418ae5284ac6215ee255b5cbc7d795e7016b5"
    },
    "LEVL": {
        "symbol": "LEVL",
        "decimals": 18,
        "name": "Levolution.io Token",
        "address": "0x1cdee2f21c066848a8a135e19f5f302ca29f1f69"
    },
    "LEZ": {
        "symbol": "LEZ",
        "decimals": 18,
        "name": "PEOPLEZ",
        "address": "0xc23be03f64a834b3fa6ae62c97ac8b40f3eec6a9"
    },
    "LFG": {
        "symbol": "LFG",
        "decimals": 18,
        "name": "LFG Token",
        "address": "0xf93f6b686f4a6557151455189a9173735d668154"
    },
    "LFW": {
        "symbol": "LFW",
        "decimals": 18,
        "name": "LFW Token",
        "address": "0xd71239a33c8542bd42130c1b4aca0673b4e4f48b"
    },
    "LGBTQ": {
        "symbol": "LGBTQ",
        "decimals": 18,
        "name": "Gays Inu",
        "address": "0x129daac6e29145499d80a86e9ef3002e9b2de068"
    },
    "LGC": {
        "symbol": "LGC",
        "decimals": 18,
        "name": "LiveGreen Coin",
        "address": "0x3496212ec43cc49f5151ec4405efd4975e036f89"
    },
    "LGO": {
        "symbol": "LGO",
        "decimals": 18,
        "name": "Level Governance Token",
        "address": "0xbe2b6c5e31f292009f495ddbda88e28391c9815e"
    },
    "LGX": {
        "symbol": "LGX",
        "decimals": 18,
        "name": "Legion Token",
        "address": "0x9096b4309224d751fcb43d7eb178dcffc122ad15"
    },
    "LIBERA": {
        "symbol": "LIBERA",
        "decimals": 18,
        "name": "Libera.Financial",
        "address": "0x3a806a3315e35b3f5f46111adb6e2baf4b14a70d"
    },
    "LIBERO": {
        "symbol": "LIBERO",
        "decimals": 18,
        "name": "Libero Financial Freedom",
        "address": "0x0dfcb45eae071b3b846e220560bbcdd958414d78"
    },
    "LIFE": {
        "symbol": "LIFE",
        "decimals": 18,
        "name": "Life Crypto",
        "address": "0x82190d28e710ea9c029d009fad951c6f1d803bb3"
    },
    "LIFT": {
        "symbol": "LIFT",
        "decimals": 18,
        "name": "Uplift",
        "address": "0x513c3200f227ebb62e3b3d00b7a83779643a71cf"
    },
    "lilfloki": {
        "symbol": "lilfloki",
        "decimals": 18,
        "name": "Lil Floki",
        "address": "0x3271d12d5ba36b6582fafa029598fee0f5f6db35"
    },
    "LIME": {
        "symbol": "LIME",
        "decimals": 18,
        "name": "iMe Lab",
        "address": "0x7bc75e291e656e8658d66be1cc8154a3769a35dd"
    },
    "LIMO": {
        "symbol": "LIMO",
        "decimals": 18,
        "name": "LIMOVERSE",
        "address": "0xd2b6bf88b7d9da599331719e338fcdeb235a0b99"
    },
    "LINA": {
        "symbol": "LINA",
        "decimals": 18,
        "name": "Linear Token",
        "address": "0x762539b45a1dcce3d36d080f74d1aed37844b878"
    },
    "LindaCEO": {
        "symbol": "LindaCEO",
        "decimals": 9,
        "name": "LindaYacc Ceo",
        "address": "0x58c764c18b6263ce97c8a22fec857e0139026b06"
    },
    "LION": {
        "symbol": "LION",
        "decimals": 18,
        "name": "Lion Token",
        "address": "0x7969dc3c6e925bccbea9f7fc466a63c74f0115b8"
    },
    "LIQ": {
        "symbol": "LIQ",
        "decimals": 18,
        "name": "Liquidus",
        "address": "0xc7981767f644c7f8e483dabdc413e8a371b83079"
    },
    "LIQR": {
        "symbol": "LIQR",
        "decimals": 18,
        "name": "LIQR",
        "address": "0x33333ee26a7d02e41c33828b42fb1e0889143477"
    },
    "LIT": {
        "symbol": "LIT",
        "decimals": 18,
        "name": "Litentry",
        "address": "0xb59490ab09a0f526cc7305822ac65f2ab12f9723"
    },
    "LITHO": {
        "symbol": "LITHO",
        "decimals": 18,
        "name": "Lithosphere",
        "address": "0x61909950e1bfb5d567c5463cbd33dc1cdc85ee93"
    },
    "LITT": {
        "symbol": "LITT",
        "decimals": 18,
        "name": "LitLabToken",
        "address": "0xcebef3df1f3c5bfd90fde603e71f31a53b11944d"
    },
    "LIUX": {
        "symbol": "LIUX",
        "decimals": 18,
        "name": "LIUX",
        "address": "0x94ade5a1dd2349e604aeb2c0b2cfac486c7e19ae"
    },
    "LIXX": {
        "symbol": "LIXX",
        "decimals": 9,
        "name": "Libra Incentix",
        "address": "0x16530b5c105fcb7c50bc84a039a0a4ed806a5124"
    },
    "LKD": {
        "symbol": "LKD",
        "decimals": 18,
        "name": "LinkDao",
        "address": "0xaf027427dc6d31a3e7e162a710a5fe27e63e275f"
    },
    "LKN": {
        "symbol": "LKN",
        "decimals": 18,
        "name": "Lockness",
        "address": "0x31acfce536b824ad0739e8d7b27cefaa4b8e4673"
    },
    "LKR": {
        "symbol": "LKR",
        "decimals": 18,
        "name": "Polkalokr",
        "address": "0xa5ff48e326958e0ce6fdf9518de561f2b5f57da3"
    },
    "LMCSWAP": {
        "symbol": "LMCSWAP",
        "decimals": 18,
        "name": "LIMOCOIN SWAP",
        "address": "0xa1a6d574728c0125b730cad5092b7d855f0bd920"
    },
    "LMT": {
        "symbol": "LMT",
        "decimals": 18,
        "name": "Lympo Market Token",
        "address": "0x9617857e191354dbea0b714d78bc59e57c411087"
    },
    "LNR": {
        "symbol": "LNR",
        "decimals": 18,
        "name": "Lunar",
        "address": "0xc1a59a17f87ba6651eb8e8f707db7672647c45bd"
    },
    "LOA": {
        "symbol": "LOA",
        "decimals": 18,
        "name": "League Of Ancients",
        "address": "0x94b69263fca20119ae817b6f783fc0f13b02ad50"
    },
    "LOFI": {
        "symbol": "LOFI",
        "decimals": 18,
        "name": "LOFI",
        "address": "0x77f86d401e067365dd911271530b0c90dec3e0f7"
    },
    "LOOM": {
        "symbol": "LOOM",
        "decimals": 18,
        "name": "Loom Token",
        "address": "0xe6ce27025f13f5213bbc560dc275e292965a392f"
    },
    "LOOP": {
        "symbol": "LOOP",
        "decimals": 18,
        "name": "LoopNetwork",
        "address": "0xce186ad6430e2fe494a22c9edbd4c68794a28b35"
    },
    "LOUD": {
        "symbol": "LOUD",
        "decimals": 18,
        "name": "Loud Market",
        "address": "0x3d0e22387ddfe75d1aea9d7108a4392922740b96"
    },
    "LOV": {
        "symbol": "LOV",
        "decimals": 8,
        "name": "The LoveChain",
        "address": "0x2e01a3df69e387e769cc0429f697fd207c02e2f0"
    },
    "LOVELY": {
        "symbol": "LOVELY",
        "decimals": 8,
        "name": "Lovely Inu Finance",
        "address": "0x9e24415d1e549ebc626a13a482bb117a2b43e9cf"
    },
    "lowb": {
        "symbol": "lowb",
        "decimals": 18,
        "name": "loser coin",
        "address": "0x843d4a358471547f51534e3e51fae91cb4dc3f28"
    },
    "LPOOL": {
        "symbol": "LPOOL",
        "decimals": 18,
        "name": "Launchpool token",
        "address": "0xcfb24d3c3767364391340a2e6d99c64f1cbd7a3d"
    },
    "LPY": {
        "symbol": "LPY",
        "decimals": 18,
        "name": "LeisurePay Token V2",
        "address": "0xfbef7220dfefd788a18ee634721a1c82a229f8c6"
    },
    "LQR": {
        "symbol": "LQR",
        "decimals": 18,
        "name": "Laqira Token",
        "address": "0xbc81ea817b579ec0334bca8e65e436b7cb540147"
    },
    "LQT": {
        "symbol": "LQT",
        "decimals": 18,
        "name": "LQT Token",
        "address": "0xbd2c43da85d007b0b3cd856fd55c299578d832bc"
    },
    "LSC": {
        "symbol": "LSC",
        "decimals": 18,
        "name": "LS Coin",
        "address": "0x293faca2e5d6ac7a0e704eafeda628528b3b3f0a"
    },
    "LSS": {
        "symbol": "LSS",
        "decimals": 18,
        "name": "Chainport.io-Peg Lossless Token",
        "address": "0xf7686f43591302cd9b4b9c4fe1291473fae7d9c9"
    },
    "LST": {
        "symbol": "LST",
        "decimals": 8,
        "name": "LOVELY SWAP TOKEN",
        "address": "0x019992270e95b800671d3bc1d763e07e489687b2"
    },
    "LSWAP": {
        "symbol": "LSWAP",
        "decimals": 18,
        "name": "LoopSwap",
        "address": "0x3f8a14f5a3ee2f4a3ed61ccf5eea3c9535c090c8"
    },
    "LTC": {
        "symbol": "LTC",
        "decimals": 18,
        "name": "Litecoin Token",
        "address": "0x4338665cbb7b2485a8855a139b75d5e34ab0db94"
    },
    "LTO": {
        "symbol": "LTO",
        "decimals": 18,
        "name": "LTO Network",
        "address": "0x857b222fc79e1cbbf8ca5f78cb133d1b7cf34bbd"
    },
    "LTRBT": {
        "symbol": "LTRBT",
        "decimals": 9,
        "name": "Little Rabbit",
        "address": "0x6c46422a0f7dbbad9bec3bbbc1189bfaf9794b05"
    },
    "LUC": {
        "symbol": "LUC",
        "decimals": 15,
        "name": "Lucretius",
        "address": "0x87837b7b4850687e200254f78c0af0a34329a491"
    },
    "LUCA": {
        "symbol": "LUCA",
        "decimals": 18,
        "name": "Lucrosus Capital Coin",
        "address": "0xf82aa46120314904cd8119dac84f6bcc7d90ed2e"
    },
    "LUCHOW": {
        "symbol": "LUCHOW",
        "decimals": 18,
        "name": "LunaChow on xDai from xDai",
        "address": "0xe4e8e6878718bfe533702d4a6571eb74d79b0915"
    },
    "LUCK": {
        "symbol": "LUCK",
        "decimals": 4,
        "name": "Luck",
        "address": "0x80f2c1e25391bbe615ef1f5ce82297fb0a624cb7"
    },
    "LUFFY": {
        "symbol": "LUFFY",
        "decimals": 9,
        "name": "LUFFY",
        "address": "0x54012cdf4119de84218f7eb90eeb87e25ae6ebd7"
    },
    "LUNA": {
        "symbol": "LUNA",
        "decimals": 6,
        "name": "LUNA",
        "address": "0x156ab3346823b651294766e23e6cf87254d68962"
    },
    "LunaT": {
        "symbol": "LunaT",
        "decimals": 9,
        "name": "Lunatics",
        "address": "0x2a48ece377b87ce941406657b9278b4459595e06"
    },
    "LUNG": {
        "symbol": "LUNG",
        "decimals": 18,
        "name": "LunaGens",
        "address": "0x28b9aed756de31b6b362aa0f23211d13093ebb79"
    },
    "LUS": {
        "symbol": "LUS",
        "decimals": 18,
        "name": "Luna Rush Token",
        "address": "0xde301d6a2569aefcfe271b9d98f318baee1d30a4"
    },
    "lUSD": {
        "symbol": "lUSD",
        "decimals": 18,
        "name": "lUSD",
        "address": "0x23e8a70534308a4aaf76fb8c32ec13d17a3bd89e"
    },
    "LVL": {
        "symbol": "LVL",
        "decimals": 18,
        "name": "Level Token",
        "address": "0xb64e280e9d1b5dbec4accedb2257a87b400db149"
    },
    "LVM": {
        "symbol": "LVM",
        "decimals": 9,
        "name": "LakeViewMeta",
        "address": "0x02678125fb30d0fe77fc9d10ea531f8b4348c603"
    },
    "LYO": {
        "symbol": "LYO",
        "decimals": 8,
        "name": "LYO Credit",
        "address": "0x9bad6c75b5a4e72df8147cc89d068cc848648e59"
    },
    "M": {
        "symbol": "M",
        "decimals": 18,
        "name": "MetaVerse-M",
        "address": "0x558ad2b02ce979ca54f88206ed8597c8c740774e"
    },
    "MAG": {
        "symbol": "MAG",
        "decimals": 18,
        "name": "MAG Token",
        "address": "0xd4c73fd18f732bc6ee9fb193d109b2eed815df80"
    },
    "MAHA": {
        "symbol": "MAHA",
        "decimals": 18,
        "name": "MahaDAO",
        "address": "0xce86f7fcd3b40791f63b86c3ea3b8b355ce2685b"
    },
    "MAI": {
        "symbol": "MAI",
        "decimals": 18,
        "name": "Mai Stablecoin",
        "address": "0x3f56e0c36d275367b8c502090edf38289b3dea0d"
    },
    "MAIN": {
        "symbol": "MAIN",
        "decimals": 18,
        "name": "MAIN",
        "address": "0xa5f249f401ba8931899a364d8e2699b5fa1d87a9"
    },
    "MARCO": {
        "symbol": "MARCO",
        "decimals": 18,
        "name": "MELEGA",
        "address": "0x963556de0eb8138e97a85f0a86ee0acd159d210b"
    },
    "MARS4": {
        "symbol": "MARS4",
        "decimals": 18,
        "name": "MARS4 [via ChainPort.io]",
        "address": "0x9cd9c5a44cb8fab39b2ee3556f5c439e65e4fddd"
    },
    "MARSH": {
        "symbol": "MARSH",
        "decimals": 18,
        "name": "UnmarshalToken",
        "address": "0x2fa5daf6fe0708fbd63b1a7d1592577284f52256"
    },
    "MARSRISE": {
        "symbol": "MARSRISE",
        "decimals": 9,
        "name": "MarsRise",
        "address": "0x184079ca987f562ae6a0c59f4be5cadb20323863"
    },
    "MARU": {
        "symbol": "MARU",
        "decimals": 18,
        "name": "MARU",
        "address": "0x08a84af1368cd333073ac5dfb2254208e06b3a70"
    },
    "MARVIN": {
        "symbol": "MARVIN",
        "decimals": 18,
        "name": "Marvin Inu",
        "address": "0x71ab195498b6dc1656abb4d9233f83ae5f19495b"
    },
    "MASK": {
        "symbol": "MASK",
        "decimals": 18,
        "name": "Mask Network",
        "address": "0x2ed9a5c8c13b93955103b9a7c167b67ef4d568a3"
    },
    "MASS": {
        "symbol": "MASS",
        "decimals": 18,
        "name": "Momentum",
        "address": "0xe81a79e9d951759aef3fccef17022276b3a0c7e5"
    },
    "MAT": {
        "symbol": "MAT",
        "decimals": 18,
        "name": "mymasterwar.com",
        "address": "0xf3147987a00d35eecc10c731269003ca093740ca"
    },
    "MATA": {
        "symbol": "MATA",
        "decimals": 18,
        "name": "MATA Token",
        "address": "0x175facdd947c995ad547f6ad952d26826758a4da"
    },
    "MATE": {
        "symbol": "MATE",
        "decimals": 18,
        "name": "Mate",
        "address": "0x2198b69b36b86f250549d26d69c5957912a34ec2"
    },
    "MATH": {
        "symbol": "MATH",
        "decimals": 18,
        "name": "MATH Token",
        "address": "0xf218184af829cf2b0019f8e6f0b2423498a36983"
    },
    "MATIC": {
        "symbol": "MATIC",
        "decimals": 18,
        "name": "Matic Token",
        "address": "0xcc42724c6683b7e57334c4e856f4c9965ed682bd"
    },
    "MATICPAD": {
        "symbol": "MATICPAD",
        "decimals": 18,
        "name": "Matic Launchpad",
        "address": "0x1e7e0efb87e609b87f12f1cea1dac48569da2328"
    },
    "MATRIX": {
        "symbol": "MATRIX",
        "decimals": 18,
        "name": "MatrixSwapToken",
        "address": "0xc32bb619966b9a56cf2472528a36fd099ce979e0"
    },
    "Mazi": {
        "symbol": "Mazi",
        "decimals": 18,
        "name": "Mazimatic",
        "address": "0x5b8650cd999b23cf39ab12e3213fbc8709c7f5cb"
    },
    "MBOX": {
        "symbol": "MBOX",
        "decimals": 18,
        "name": "Mobox",
        "address": "0x3203c9e46ca618c8c1ce5dc67e7e9d75f5da2377"
    },
    "MBP": {
        "symbol": "MBP",
        "decimals": 18,
        "name": "MobiPad",
        "address": "0xaf2f53cc6cc0384aba52275b0f715851fb5aff94"
    },
    "MC": {
        "symbol": "MC",
        "decimals": 18,
        "name": "Merit Circle",
        "address": "0x949d48eca67b17269629c7194f4b727d4ef9e5d6"
    },
    "MCB": {
        "symbol": "MCB",
        "decimals": 18,
        "name": "MCDEX Token",
        "address": "0x5fe80d2cd054645b9419657d3d10d26391780a7b"
    },
    "MCC": {
        "symbol": "MCC",
        "decimals": 9,
        "name": "MultiChainCapital",
        "address": "0xc146b7cdbaff065090077151d391f4c96aa09e0c"
    },
    "MCF": {
        "symbol": "MCF",
        "decimals": 9,
        "name": "Max Crowdfund",
        "address": "0xecb19b2a4e9c76ce748cf33f68f0857288f9f090"
    },
    "MCOIN": {
        "symbol": "MCOIN",
        "decimals": 18,
        "name": "mCoin",
        "address": "0x6d86f0a41c3966cef8ea139648db707e912563c9"
    },
    "MCONTENT": {
        "symbol": "MCONTENT",
        "decimals": 6,
        "name": "MContent",
        "address": "0x799e1cf88a236e42b4a87c544a22a94ae95a6910"
    },
    "MCRN": {
        "symbol": "MCRN",
        "decimals": 18,
        "name": "MacaronSwap Token",
        "address": "0xacb2d47827c9813ae26de80965845d80935afd0b"
    },
    "MCRT": {
        "symbol": "MCRT",
        "decimals": 9,
        "name": "MagicCraft",
        "address": "0x4b8285ab433d8f69cb48d5ad62b415ed1a221e4f"
    },
    "MCT": {
        "symbol": "MCT",
        "decimals": 18,
        "name": "Micro Tuber",
        "address": "0x8038b1f3eb4f70436569618530ac96b439d67bae"
    },
    "MDAO": {
        "symbol": "MDAO",
        "decimals": 18,
        "name": "MarsDAO",
        "address": "0x60322971a672b81bcce5947706d22c19daecf6fb"
    },
    "MDB": {
        "symbol": "MDB",
        "decimals": 18,
        "name": "MillionDollarBaby",
        "address": "0x0557a288a93ed0df218785f2787dac1cd077f8f3"
    },
    "MDCx": {
        "symbol": "MDCx",
        "decimals": 9,
        "name": "MDCx",
        "address": "0xe665dd6b4a2af39fadbee280f005df78dab3c7e2"
    },
    "MDX": {
        "symbol": "MDX",
        "decimals": 18,
        "name": "MDX Token",
        "address": "0x9c65ab58d8d978db963e63f2bfb7121627e3a739"
    },
    "MEAN": {
        "symbol": "MEAN",
        "decimals": 6,
        "name": "MEAN",
        "address": "0x6c9297be2e3ce9c10c480a25b7157a43fd992942"
    },
    "MECH": {
        "symbol": "MECH",
        "decimals": 18,
        "name": "MechMaster",
        "address": "0xc7b7844494c516b840a7a4575ff3e60ff0f056a9"
    },
    "MECI": {
        "symbol": "MECI",
        "decimals": 18,
        "name": "META GAME CITY",
        "address": "0x98de6123a56b1818fbfb48a8a7c75d2444c09946"
    },
    "MEFA": {
        "symbol": "MEFA",
        "decimals": 9,
        "name": "META FACE",
        "address": "0x6ad0f087501eee603aeda0407c52864bc7f83322"
    },
    "MEGALAND": {
        "symbol": "MEGALAND",
        "decimals": 18,
        "name": "METAGALAXY LAND",
        "address": "0x7cd8c22d3f4b66230f73d7ffcb48576233c3fe33"
    },
    "MEIN": {
        "symbol": "MEIN",
        "decimals": 18,
        "name": "Mein",
        "address": "0x14a83bb74da432258c4051e3976a3f8f6b02a4d9"
    },
    "MELI": {
        "symbol": "MELI",
        "decimals": 18,
        "name": "MELI",
        "address": "0xad04ac36791d923deb082da4f91ab71675dd18fb"
    },
    "Melo": {
        "symbol": "Melo",
        "decimals": 18,
        "name": "Melo Token",
        "address": "0x38a62b2030068e7b7a5268df7ab7a48bc6e396b4"
    },
    "MEME": {
        "symbol": "MEME",
        "decimals": 9,
        "name": "MEME",
        "address": "0x4a645fb8ae60979edf7f47c5c1a4569b7fb07851"
    },
    "MEPAD": {
        "symbol": "MEPAD",
        "decimals": 18,
        "name": "MemePad",
        "address": "0x9d70a3ee3079a6fa2bb16591414678b7ad91f0b5"
    },
    "MESA": {
        "symbol": "MESA",
        "decimals": 18,
        "name": "myMessage",
        "address": "0xb192d5fc358d35194282a1a06814aba006198010"
    },
    "METAL": {
        "symbol": "METAL",
        "decimals": 18,
        "name": "METAL Token",
        "address": "0x200c234721b5e549c3693ccc93cf191f90dc2af9"
    },
    "METAN": {
        "symbol": "METAN",
        "decimals": 18,
        "name": "Metan Chain",
        "address": "0x879d239bcc0356cf9df8c90442488bce99554c66"
    },
    "METAQ": {
        "symbol": "METAQ",
        "decimals": 8,
        "name": "METAQ Token",
        "address": "0x2824d8ecded273e296ca57d583d80614093c87d4"
    },
    "METAV": {
        "symbol": "METAV",
        "decimals": 18,
        "name": "METAVPAD.com",
        "address": "0x62858686119135cc00c4a3102b436a0eb314d402"
    },
    "METAX": {
        "symbol": "METAX",
        "decimals": 18,
        "name": "METAX",
        "address": "0x03f8fdc10d5bcf7508375585b04e93d656d36954"
    },
    "METFI": {
        "symbol": "METFI",
        "decimals": 18,
        "name": "MetFi",
        "address": "0x3e7f1039896454b9cb27c53cc7383e1ab9d9512a"
    },
    "Metis": {
        "symbol": "Metis",
        "decimals": 18,
        "name": "Metis Token",
        "address": "0xe552fb52a4f19e44ef5a967632dbc320b0820639"
    },
    "METO": {
        "symbol": "METO",
        "decimals": 18,
        "name": "Metafluence",
        "address": "0xa78775bba7a542f291e5ef7f13c6204e704a90ba"
    },
    "METR": {
        "symbol": "METR",
        "decimals": 18,
        "name": "Metria",
        "address": "0x405ce8b2eaeea7d4ba5fc160848cb2a6569e03f0"
    },
    "METT": {
        "symbol": "METT",
        "decimals": 9,
        "name": "Meta Things",
        "address": "0x7082ff3a22e707136c80a9efcb215ec4c1fda810"
    },
    "MEVR": {
        "symbol": "MEVR",
        "decimals": 18,
        "name": "Metaverse VR",
        "address": "0xdde3ed0bb77c1cafabf8b38f9a1e81edddc7ddc9"
    },
    "MF": {
        "symbol": "MF",
        "decimals": 18,
        "name": "MetaFighter Token",
        "address": "0xbb6cdedac5cab4a420211a4a8e8b5dca879b31de"
    },
    "MFB": {
        "symbol": "MFB",
        "decimals": 18,
        "name": "Monster Ball Token",
        "address": "0xa528d8b9cd90b06d373373c37f8f188e44cad3be"
    },
    "MFET": {
        "symbol": "MFET",
        "decimals": 8,
        "name": "Multi Functional Environmental Token",
        "address": "0x6d23970ce32cb0f1929bece7c56d71319e1b4f01"
    },
    "MFI": {
        "symbol": "MFI",
        "decimals": 18,
        "name": "MetaFinance",
        "address": "0x808f1350dff684c099f4837a01d863fc61a86bc6"
    },
    "MFO": {
        "symbol": "MFO",
        "decimals": 18,
        "name": "Moonfarm Finance",
        "address": "0xb46049c79d77ff1d555a67835fba6978536581af"
    },
    "MGA": {
        "symbol": "MGA",
        "decimals": 18,
        "name": "Metagame Arena",
        "address": "0x03ac6ab6a9a91a0fcdec7d85b38bdfbb719ec02f"
    },
    "MGG": {
        "symbol": "MGG",
        "decimals": 18,
        "name": "MetaGaming Guild [via ChainPort.io]",
        "address": "0x6125adcab2f171bc70cfe2caecfec5509273a86a"
    },
    "MGKL": {
        "symbol": "MGKL",
        "decimals": 18,
        "name": "MAGIKAL.ai",
        "address": "0x8abfa6a4f4b9865b0e7acfdce1839a2584636d06"
    },
    "MGOD": {
        "symbol": "MGOD",
        "decimals": 18,
        "name": "MetaGods",
        "address": "0x10a12969cb08a8d88d4bfb5d1fa317d41e0fdab3"
    },
    "MGP": {
        "symbol": "MGP",
        "decimals": 18,
        "name": "Magpie Token",
        "address": "0xd06716e1ff2e492cc5034c2e81805562dd3b45fa"
    },
    "MGXG": {
        "symbol": "MGXG",
        "decimals": 18,
        "name": "MALGO",
        "address": "0xd21a1f1fcec9479d38b570a2eca3277b1b2a959a"
    },
    "MHUNT": {
        "symbol": "MHUNT",
        "decimals": 18,
        "name": "MetaShooter",
        "address": "0x2c717059b366714d267039af8f59125cadce6d8c"
    },
    "MILK2": {
        "symbol": "MILK2",
        "decimals": 18,
        "name": "MilkyWay Token by SpaceSwap v2",
        "address": "0x4a5a34212404f30c5ab7eb61b078fa4a55adc5a5"
    },
    "MILO": {
        "symbol": "MILO",
        "decimals": 9,
        "name": "Milo Inu",
        "address": "0xd9de2b1973e57dc9dba90c35d6cd940ae4a3cbe1"
    },
    "MIM": {
        "symbol": "MIM",
        "decimals": 18,
        "name": "Magic Internet Money",
        "address": "0xfe19f0b51438fd612f6fd59c1dbb3ea319f433ba"
    },
    "MIMIR": {
        "symbol": "MIMIR",
        "decimals": 18,
        "name": "Mimir Token",
        "address": "0x336f5a68fd46a25056a6c1d9c06072c691486acc"
    },
    "MINE": {
        "symbol": "MINE",
        "decimals": 18,
        "name": "SpaceMine",
        "address": "0x93713de5e0be3b7fcbd34257b6cadfb4d96e12b1"
    },
    "MiniFootball": {
        "symbol": "MiniFootball",
        "decimals": 9,
        "name": "MiniFootball",
        "address": "0xd024ac1195762f6f13f8cfdf3cdd2c97b33b248b"
    },
    "MINT": {
        "symbol": "MINT",
        "decimals": 18,
        "name": "Mint.club",
        "address": "0x1f3af095cda17d63cad238358837321e95fc5915"
    },
    "MINTME": {
        "symbol": "MINTME",
        "decimals": 18,
        "name": "MintMe.com Coin",
        "address": "0x138218c8e064ed2a011c9ff203759a8a1e23e6c8"
    },
    "MIR": {
        "symbol": "MIR",
        "decimals": 18,
        "name": "Wrapped MIR Token",
        "address": "0x5b6dcf557e2abe2323c48445e8cc948910d8c2c9"
    },
    "MISA": {
        "symbol": "MISA",
        "decimals": 18,
        "name": "Sangkara",
        "address": "0x934b0633f4874ca9340341ad66ff2f6ce3124b4c"
    },
    "MIST": {
        "symbol": "MIST",
        "decimals": 18,
        "name": "Mist",
        "address": "0x68e374f856bf25468d365e539b700b648bf94b67"
    },
    "MIT": {
        "symbol": "MIT",
        "decimals": 18,
        "name": "Meta Interstellar Token",
        "address": "0xe6906717f129427eebade5406de68cadd57aa0c0"
    },
    "MIX": {
        "symbol": "MIX",
        "decimals": 18,
        "name": "MixMarvel Token",
        "address": "0x398f7827dccbefe6990478876bbf3612d93baf05"
    },
    "MLS": {
        "symbol": "MLS",
        "decimals": 18,
        "name": "MetaLand Shares",
        "address": "0x5f2f6c4c491b690216e0f8ea753ff49ef4e36ba6"
    },
    "MLT": {
        "symbol": "MLT",
        "decimals": 18,
        "name": "Media Licensing Token",
        "address": "0x4518231a8fdf6ac553b9bbd51bbb86825b583263"
    },
    "MLTPX": {
        "symbol": "MLTPX",
        "decimals": 18,
        "name": "Moonlift",
        "address": "0x9d7c580e0bc4ea441db96eebc7e1440d264bce51"
    },
    "MM": {
        "symbol": "MM",
        "decimals": 18,
        "name": "Million",
        "address": "0xbf05279f9bf1ce69bbfed670813b7e431142afa4"
    },
    "MMC": {
        "symbol": "MMC",
        "decimals": 8,
        "name": "Monopoly Millionaire Control",
        "address": "0xbe3fd4d1e0d244ddd98686a28f67355efe223346"
    },
    "MMETA": {
        "symbol": "MMETA",
        "decimals": 18,
        "name": "Duckie Land Multi Metaverse",
        "address": "0x7a9c8d33963aecca9a821802adfaf5bd9392351f"
    },
    "MMG": {
        "symbol": "MMG",
        "decimals": 18,
        "name": "MMG Token",
        "address": "0xf018aea0a08a5d88674f0837bdac27ab89824dee"
    },
    "MMIT": {
        "symbol": "MMIT",
        "decimals": 18,
        "name": "Mango Man Intelligent",
        "address": "0x9767c8e438aa18f550208e6d1fdf5f43541cc2c8"
    },
    "MMO": {
        "symbol": "MMO",
        "decimals": 18,
        "name": "MMOCoin",
        "address": "0x0aa086e7a108d387de63294fe2a88b05820a9855"
    },
    "MMPRO": {
        "symbol": "MMPRO",
        "decimals": 18,
        "name": "MMPRO Token",
        "address": "0x6067490d05f3cf2fdffc0e353b1f5fd6e5ccdf70"
    },
    "MNFT": {
        "symbol": "MNFT",
        "decimals": 18,
        "name": "MANUFACTORY",
        "address": "0x36953b5ec00a13edceceb3af258d034913d2a79d"
    },
    "MNG": {
        "symbol": "MNG",
        "decimals": 9,
        "name": "Moon Nation Game",
        "address": "0x13dfe44c7b461222e10597e517e4485ff4766582"
    },
    "MNST": {
        "symbol": "MNST",
        "decimals": 18,
        "name": "MoonStarter.net",
        "address": "0x6a6ccf15b38da4b5b0ef4c8fe9fefcb472a893f9"
    },
    "MNU": {
        "symbol": "MNU",
        "decimals": 18,
        "name": "MNU-Chain-Token",
        "address": "0x256be284fea694f1bb11f76d556a28ecb496eee9"
    },
    "MNY": {
        "symbol": "MNY",
        "decimals": 18,
        "name": "MoonieNFT Token",
        "address": "0xa6f7645ed967faf708a614a2fca8d4790138586f"
    },
    "MNZ": {
        "symbol": "MNZ",
        "decimals": 18,
        "name": "Menzy",
        "address": "0x861f1e1397dad68289e8f6a09a2ebb567f1b895c"
    },
    "MOD": {
        "symbol": "MOD",
        "decimals": 18,
        "name": "Modefi",
        "address": "0xd4fbc57b6233f268e7fba3b66e62719d74deecbc"
    },
    "MOIL": {
        "symbol": "MOIL",
        "decimals": 18,
        "name": "MOIL",
        "address": "0xa0a4c12aa90fe439b07b16657cd2c12e4d41e25f"
    },
    "MOMA": {
        "symbol": "MOMA",
        "decimals": 18,
        "name": "MOchi MArket",
        "address": "0xb72842d6f5fedf91d22d56202802bb9a79c6322e"
    },
    "MON": {
        "symbol": "MON",
        "decimals": 18,
        "name": "Medamon",
        "address": "0x52b7c9d984ea17e9ee31159ca3fff3790981b64a"
    },
    "MONGBNB": {
        "symbol": "MONGBNB",
        "decimals": 18,
        "name": "MongBNB",
        "address": "0x5d31aa2330efa65acca9567796fdf7d1caa6fa9a"
    },
    "MONI": {
        "symbol": "MONI",
        "decimals": 18,
        "name": "Monsta Infinite Token",
        "address": "0x9573c88ae3e37508f87649f87c4dd5373c9f31e0"
    },
    "MONS": {
        "symbol": "MONS",
        "decimals": 18,
        "name": "Monsters Clan Token",
        "address": "0xe4c797d43631f4d660ec67b5cb0b78ef5c902532"
    },
    "MONSTA": {
        "symbol": "MONSTA",
        "decimals": 18,
        "name": "Cake Monster",
        "address": "0x8a5d7fcd4c90421d21d30fcc4435948ac3618b2f"
    },
    "MOO": {
        "symbol": "MOO",
        "decimals": 18,
        "name": "MooMonster Token",
        "address": "0xa29b6f4e762874846c081e20ed1142ff83faafef"
    },
    "MOONER": {
        "symbol": "MOONER",
        "decimals": 18,
        "name": "CoinMooner",
        "address": "0x34e942859469c9db9c22f4eaf866e2c2401bb795"
    },
    "MOONION": {
        "symbol": "MOONION",
        "decimals": 18,
        "name": "MOONIONS",
        "address": "0x9073b858a7cdf121e6bf8d1367e200e5d0cc0188"
    },
    "MOOO": {
        "symbol": "MOOO",
        "decimals": 18,
        "name": "Hashtagger.com",
        "address": "0xa0b9bb05da11e3b19ffd64554400f59d4a378515"
    },
    "MOOV": {
        "symbol": "MOOV",
        "decimals": 18,
        "name": "dotmoovs",
        "address": "0x0ebd9537a25f56713e34c45b38f421a1e7191469"
    },
    "MOVE": {
        "symbol": "MOVE",
        "decimals": 9,
        "name": "MarketMove",
        "address": "0x231cf6f78620e42fe00d0c5c3088b427f355d01c"
    },
    "MOVEZ": {
        "symbol": "MOVEZ",
        "decimals": 18,
        "name": "MOVEZ.me",
        "address": "0x039cd22cb49084142d55fcd4b6096a4f51ffb3b4"
    },
    "MOWA": {
        "symbol": "MOWA",
        "decimals": 18,
        "name": "Moniwar",
        "address": "0x411ec510c85c9e56271bf4e10364ffa909e685d9"
    },
    "MPAD": {
        "symbol": "MPAD",
        "decimals": 18,
        "name": "MultiPad",
        "address": "0x11d1ac5ec23e3a193e8a491a198f5fc9ee715839"
    },
    "MPG": {
        "symbol": "MPG",
        "decimals": 18,
        "name": "MedPing",
        "address": "0x53f0e242ea207b6e9b63e0a53e788267aa99ff9b"
    },
    "MPI": {
        "symbol": "MPI",
        "decimals": 18,
        "name": "MetaPionner Token",
        "address": "0x82555cc48a532fa4e2194ab883eb6d465149f80e"
    },
    "MR": {
        "symbol": "MR",
        "decimals": 18,
        "name": "Meta Ruffy",
        "address": "0x2456bbad80bfad346aecea45fa38c81a6963132d"
    },
    "MRCR": {
        "symbol": "MRCR",
        "decimals": 18,
        "name": "Mercor Token",
        "address": "0x155dab50f1dded25c099e209e7b375456a70e504"
    },
    "MRHB": {
        "symbol": "MRHB",
        "decimals": 18,
        "name": "Marhaba Network",
        "address": "0xd10332818d6a9b4b84bf5d87dbf9d80012fdf913"
    },
    "MRS": {
        "symbol": "MRS",
        "decimals": 18,
        "name": "Metaracers",
        "address": "0x9e05e646a18bb4cab41aa7992959f019d0aac124"
    },
    "MRUN": {
        "symbol": "MRUN",
        "decimals": 18,
        "name": "METARUN",
        "address": "0xca0d640a401406f3405b4c252a5d0c4d17f38ebb"
    },
    "MRXb": {
        "symbol": "MRXb",
        "decimals": 8,
        "name": "Wrapped Metrix",
        "address": "0x767b28a30e3a15dcece7bff7a020adfde9d19cf8"
    },
    "MS": {
        "symbol": "MS",
        "decimals": 18,
        "name": "Morphswap",
        "address": "0x6d6554939d646f274d0fc3cecb7dab5d76bc908f"
    },
    "MSCP": {
        "symbol": "MSCP",
        "decimals": 18,
        "name": "Moonscape",
        "address": "0x27d72484f1910f5d0226afa4e03742c9cd2b297a"
    },
    "MSH": {
        "symbol": "MSH",
        "decimals": 18,
        "name": "CRIR MSH",
        "address": "0xeae2bbbc0000f605bd37a02c7fe346a3b68b03eb"
    },
    "MSTR": {
        "symbol": "MSTR",
        "decimals": 18,
        "name": "MSTR Token",
        "address": "0x2290c6bd9560e6498dfdf10f9ecb17997ca131f2"
    },
    "MSWAP": {
        "symbol": "MSWAP",
        "decimals": 18,
        "name": "MoneySwap",
        "address": "0xdd5a149740c055bdcdc5c066888f739dbe0bf2d0"
    },
    "MTG": {
        "symbol": "MTG",
        "decimals": 18,
        "name": "MagnetGold",
        "address": "0x68d10dfe87a838d63bbef6c9a0d0b44beb799dc1"
    },
    "MTK": {
        "symbol": "MTK",
        "decimals": 18,
        "name": "Martik",
        "address": "0x116526135380e28836c6080f1997645d5a807fae"
    },
    "MTRG": {
        "symbol": "MTRG",
        "decimals": 18,
        "name": "Wrapped MTRG on BSC by Meter.io",
        "address": "0xbd2949f67dcdc549c6ebe98696449fa79d988a9f"
    },
    "MTRX": {
        "symbol": "MTRX",
        "decimals": 18,
        "name": "Metarix",
        "address": "0x08b87b1cfdba00dfb79d77cac1a5970ba6c9cde2"
    },
    "MTS": {
        "symbol": "MTS",
        "decimals": 18,
        "name": "Metastrike",
        "address": "0x496cc0b4ee12aa2ac4c42e93067484e7ff50294b"
    },
    "MTV": {
        "symbol": "MTV",
        "decimals": 18,
        "name": "MultiVAC",
        "address": "0x8aa688ab789d1848d131c65d98ceaa8875d97ef1"
    },
    "mtvt": {
        "symbol": "mtvt",
        "decimals": 18,
        "name": "Metaverser Token",
        "address": "0xb92c5e0135a510a4a3a8803f143d2cb085bbaf73"
    },
    "MTY": {
        "symbol": "MTY",
        "decimals": 9,
        "name": "Minty",
        "address": "0xde27c2c13d1eeb87744bf3c2a9168c1cbd62ee81"
    },
    "MUDOL2": {
        "symbol": "MUDOL2",
        "decimals": 18,
        "name": "Mudol2 Token",
        "address": "0x5e7f472b9481c80101b22d0ba4ef4253aa61dabc"
    },
    "MULTI": {
        "symbol": "MULTI",
        "decimals": 18,
        "name": "Multichain",
        "address": "0x9fb9a33956351cf4fa040f65a13b835a3c8764e3"
    },
    "multiBTC": {
        "symbol": "multiBTC",
        "decimals": 8,
        "name": "Multichain BTC",
        "address": "0xd9907fcda91ac644f70477b8fc1607ad15b2d7a8"
    },
    "Mura": {
        "symbol": "Mura",
        "decimals": 18,
        "name": "Murasaki",
        "address": "0x166295ebd6a938c7aaf61350eb5161a9939ab2b7"
    },
    "MURATIAI": {
        "symbol": "MURATIAI",
        "decimals": 18,
        "name": "MuratiAI",
        "address": "0x69c2fcae7e30b429166bd616a322e32bec036bcf"
    },
    "MusicAI": {
        "symbol": "MusicAI",
        "decimals": 18,
        "name": "MusicAI",
        "address": "0x0ec674fabb4ea1935514a7be760f7e13aa466a39"
    },
    "MVC": {
        "symbol": "MVC",
        "decimals": 18,
        "name": "Multiverse Capital (MVC.finance)",
        "address": "0x80d04e44955aa9c3f24041b2a824a20a88e735a8"
    },
    "MVK": {
        "symbol": "MVK",
        "decimals": 18,
        "name": "MetaVerseKombat",
        "address": "0x3405ff989f8bb8efd6c85ad6b29219d3383a5fb0"
    },
    "MXZ": {
        "symbol": "MXZ",
        "decimals": 18,
        "name": "Maximus Coin",
        "address": "0x72875158c818d43ea07c514cb9c0e134bb8cb0e7"
    },
    "MYPO": {
        "symbol": "MYPO",
        "decimals": 18,
        "name": "MyPoints",
        "address": "0xd0ba1cad35341acd1cd88a85e16b054ba9ccc385"
    },
    "MYRA": {
        "symbol": "MYRA",
        "decimals": 18,
        "name": "Mytheria",
        "address": "0x6ef238e9e8cd2a96740897761c18894fc086b9d0"
    },
    "MyS": {
        "symbol": "MyS",
        "decimals": 18,
        "name": "Magic Yearn Share",
        "address": "0x021f48697343a6396bafc01795a4c140b637f4b4"
    },
    "MYST": {
        "symbol": "MYST",
        "decimals": 18,
        "name": "Mysterium",
        "address": "0x2ff0b946a6782190c4fe5d4971cfe79f0b6e4df2"
    },
    "N1": {
        "symbol": "N1",
        "decimals": 18,
        "name": "NFTify",
        "address": "0x5989d72a559eb0192f2d20170a43a4bd28a1b174"
    },
    "NABOX": {
        "symbol": "NABOX",
        "decimals": 18,
        "name": "Nabox Token",
        "address": "0x755f34709e369d37c6fa52808ae84a32007d1155"
    },
    "NAFT": {
        "symbol": "NAFT",
        "decimals": 18,
        "name": "Nafter",
        "address": "0xd7730681b1dc8f6f969166b29d8a5ea8568616a3"
    },
    "NANO": {
        "symbol": "NANO",
        "decimals": 18,
        "name": "NanoMatic",
        "address": "0xb15488af39bd1de209d501672a293bcd05f82ab4"
    },
    "NAOS": {
        "symbol": "NAOS",
        "decimals": 18,
        "name": "NAOSToken",
        "address": "0x758d08864fb6cce3062667225ca10b8f00496cc2"
    },
    "NBL": {
        "symbol": "NBL",
        "decimals": 18,
        "name": "Notable",
        "address": "0xfaa0fc7b803919b091dbe5ff709b2dabb61b93d9"
    },
    "NBP": {
        "symbol": "NBP",
        "decimals": 18,
        "name": "NFTBomb Protocol",
        "address": "0x74c22834744e8d5e36c79420ff7b057964aba8a7"
    },
    "NBT": {
        "symbol": "NBT",
        "decimals": 18,
        "name": "NanoByte Token",
        "address": "0x1d3437e570e93581bd94b2fd8fbf202d4a65654a"
    },
    "NEAR": {
        "symbol": "NEAR",
        "decimals": 18,
        "name": "NEAR Protocol",
        "address": "0x1fa4a73a3f0133f0025378af00236f3abdee5d63"
    },
    "NEOFI": {
        "symbol": "NEOFI",
        "decimals": 18,
        "name": "Neofi Token",
        "address": "0xa1578bdcd26773e16631ac626803bf388449c53c"
    },
    "NEST": {
        "symbol": "NEST",
        "decimals": 18,
        "name": "NEST",
        "address": "0x98f8669f6481ebb341b522fcd3663f79a3d1a6a7"
    },
    "NETC": {
        "symbol": "NETC",
        "decimals": 18,
        "name": "Network Capital Token",
        "address": "0x6a061bc3bd2f90fc3fe0b305488c32d121d0093e"
    },
    "NEURALAI": {
        "symbol": "NEURALAI",
        "decimals": 18,
        "name": "Neural AI",
        "address": "0xb9c255c115636d8cbe107fc953364b243cacdbce"
    },
    "NEUROS": {
        "symbol": "NEUROS",
        "decimals": 18,
        "name": "Neuros",
        "address": "0x95b0fffabd2817959ce410070600d77bce93d454"
    },
    "NEVA": {
        "symbol": "NEVA",
        "decimals": 18,
        "name": "NevaCoin",
        "address": "0xe7498f332c35a346b486f3f6a68f05934e92a228"
    },
    "NEWB": {
        "symbol": "NEWB",
        "decimals": 18,
        "name": "NEWB",
        "address": "0x545f90dc35ca1e6129f1fed354b3e2df12034261"
    },
    "NEXM": {
        "symbol": "NEXM",
        "decimals": 8,
        "name": "Nexum Coin",
        "address": "0xfa37e513e6cd506c4694b992825a8b614c035581"
    },
    "NEXT": {
        "symbol": "NEXT",
        "decimals": 18,
        "name": "ShopNEXT Loyalty Token",
        "address": "0xa6c59de838f1eeb82d86f5af0750f5f656439999"
    },
    "NFTART": {
        "symbol": "NFTART",
        "decimals": 9,
        "name": "NFTArt.Finance",
        "address": "0xf7844cb890f4c339c497aeab599abdc3c874b67a"
    },
    "NFTB": {
        "symbol": "NFTB",
        "decimals": 18,
        "name": "NFTB",
        "address": "0xde3dbbe30cfa9f437b293294d1fd64b26045c71a"
    },
    "NFTD": {
        "symbol": "NFTD",
        "decimals": 18,
        "name": "NFTrade Token [via ChainPort.io]",
        "address": "0xac83271abb4ec95386f08ad2b904a46c61777cef"
    },
    "NFTG": {
        "symbol": "NFTG",
        "decimals": 18,
        "name": "NFT Global",
        "address": "0x76f6cd75ce81e88916f8d933ab76efe18ced6ad3"
    },
    "NFTS": {
        "symbol": "NFTS",
        "decimals": 18,
        "name": "NFT STARS COIN",
        "address": "0x08037036451c768465369431da5c671ad9b37dbc"
    },
    "NFTY": {
        "symbol": "NFTY",
        "decimals": 18,
        "name": "NFTY Token",
        "address": "0x5774b2fc3e91af89f89141eacf76545e74265982"
    },
    "NGA": {
        "symbol": "NGA",
        "decimals": 18,
        "name": "NGA TIGER",
        "address": "0xaa3ed6e6ea3ed78d4d57e373aabd6f54df5bb508"
    },
    "NGL": {
        "symbol": "NGL",
        "decimals": 18,
        "name": "Gold Fever Native Gold [via ChainPort.io]",
        "address": "0x0f5d8cd195a4539bcf2ec6118c6da50287c6d5f5"
    },
    "NGT": {
        "symbol": "NGT",
        "decimals": 18,
        "name": "NGT",
        "address": "0x02030d968558fd429eafa6e5b0c7a95a4903233b"
    },
    "NINO": {
        "symbol": "NINO",
        "decimals": 18,
        "name": "Ninneko Token",
        "address": "0x6cad12b3618a3c7ef1feb6c91fdc3251f58c2a90"
    },
    "NIOB": {
        "symbol": "NIOB",
        "decimals": 18,
        "name": "Niob Token",
        "address": "0x5ac5e6af46ef285b3536833e65d245c49b608d9b"
    },
    "NITRO": {
        "symbol": "NITRO",
        "decimals": 18,
        "name": "Nitro",
        "address": "0x8a1cb5289ee4c5a0f0d9dc83225619b11d24e031"
    },
    "NMSP": {
        "symbol": "NMSP",
        "decimals": 9,
        "name": "Nemesis PRO",
        "address": "0x14ab462a88e33d026a687f6d99f3af6e0ea73f9b"
    },
    "NMX": {
        "symbol": "NMX",
        "decimals": 18,
        "name": "Nominex",
        "address": "0xd32d01a43c869edcd1117c640fbdcfcfd97d9d65"
    },
    "NNI": {
        "symbol": "NNI",
        "decimals": 18,
        "name": "NeoNomad Finance",
        "address": "0xf0eb3c9088718a533c8fd64dbcaa5927faed6d18"
    },
    "NNT": {
        "symbol": "NNT",
        "decimals": 18,
        "name": "NunuToken",
        "address": "0x3a2927e68749dd6ad0a568d7c05b587863c0bc10"
    },
    "NOKU": {
        "symbol": "NOKU",
        "decimals": 18,
        "name": "NOKU v2",
        "address": "0xfb4d42bed5618fb1a377ddb64eb56b92a6d117f2"
    },
    "NOOT": {
        "symbol": "NOOT",
        "decimals": 18,
        "name": "NOOT",
        "address": "0x98a2500a2c3b8877b0ed5ac3acc300c50bf7064b"
    },
    "NRV": {
        "symbol": "NRV",
        "decimals": 18,
        "name": "Nerve",
        "address": "0x42f6f551ae042cbe50c739158b4f0cac0edb9096"
    },
    "NSDX": {
        "symbol": "NSDX",
        "decimals": 18,
        "name": "NASDEX Token",
        "address": "0x417871f0682db63924b931fc16ba3ff40343cdcb"
    },
    "NSFW": {
        "symbol": "NSFW",
        "decimals": 18,
        "name": "Pleasure Coin",
        "address": "0xaa076b62efc6f357882e07665157a271ab46a063"
    },
    "NSUR": {
        "symbol": "NSUR",
        "decimals": 6,
        "name": "NSUR",
        "address": "0x3c5fc9d51e99c26a6db1304f6c9dd10a85805ce5"
    },
    "NT": {
        "symbol": "NT",
        "decimals": 18,
        "name": "NEXTYPE",
        "address": "0xfbcf80ed90856af0d6d9655f746331763efdb22c"
    },
    "NTR": {
        "symbol": "NTR",
        "decimals": 18,
        "name": "Nether",
        "address": "0x8182ac1c5512eb67756a89c40fadb2311757bd32"
    },
    "NTX": {
        "symbol": "NTX",
        "decimals": 6,
        "name": "NuNet Utility Token",
        "address": "0x5c4bcc4dbaeabc7659f6435bce4e659314ebad87"
    },
    "NUDES": {
        "symbol": "NUDES",
        "decimals": 8,
        "name": "Nudes",
        "address": "0x301ff7c013ec7043ffb9453cd3fb32754ccaa1a5"
    },
    "NULS": {
        "symbol": "NULS",
        "decimals": 8,
        "name": "Nuls",
        "address": "0x8cd6e29d3686d24d3c2018cee54621ea0f89313b"
    },
    "NUM": {
        "symbol": "NUM",
        "decimals": 18,
        "name": "NUM Token [via ChainPort.io]",
        "address": "0xeceb87cf00dcbf2d4e2880223743ff087a995ad9"
    },
    "NUSA": {
        "symbol": "NUSA",
        "decimals": 18,
        "name": "Nusa Token",
        "address": "0xe11f1d5eee6be945bee3fa20dbf46febbc9f4a19"
    },
    "NUX": {
        "symbol": "NUX",
        "decimals": 18,
        "name": "NUX Peanut.trade",
        "address": "0x6d8734002fbffe1c86495e32c95f732fc77f6f2a"
    },
    "NVS": {
        "symbol": "NVS",
        "decimals": 9,
        "name": "Navis",
        "address": "0x43a8a925c1930a313d283359184a64c51a2bc0e9"
    },
    "NVT": {
        "symbol": "NVT",
        "decimals": 8,
        "name": "NerveNetwork",
        "address": "0xf0e406c49c63abf358030a299c0e00118c4c6ba5"
    },
    "NWC": {
        "symbol": "NWC",
        "decimals": 18,
        "name": "Newscrypto",
        "address": "0x968f6f898a6df937fc1859b323ac2f14643e3fed"
    },
    "NXDT": {
        "symbol": "NXDT",
        "decimals": 18,
        "name": "NXD Next",
        "address": "0xadf6d29572af16de3c44e6b89d2d8e0380044fa6"
    },
    "NXRA": {
        "symbol": "NXRA",
        "decimals": 18,
        "name": "AllianceBlock Nexera Token",
        "address": "0x644192291cc835a93d6330b24ea5f5fedd0eef9e"
    },
    "NZERO": {
        "symbol": "NZERO",
        "decimals": 18,
        "name": "NETZERO",
        "address": "0xa94fb437b8bacb591c6b828bef5a837afe542100"
    },
    "O3": {
        "symbol": "O3",
        "decimals": 18,
        "name": "O3 Swap Token",
        "address": "0xee9801669c6138e84bd50deb500827b776777d28"
    },
    "OASIS": {
        "symbol": "OASIS",
        "decimals": 18,
        "name": "OASIS",
        "address": "0xb19289b436b2f7a92891ac391d8f52580d3087e4"
    },
    "OATH": {
        "symbol": "OATH",
        "decimals": 18,
        "name": "Oath Token",
        "address": "0xd3c6ceedd1cc7bd4304f72b011d53441d631e662"
    },
    "OBROK": {
        "symbol": "OBROK",
        "decimals": 9,
        "name": "OBRok",
        "address": "0x205afd08cefe438377a0abc5a20cb4462e1a8c5c"
    },
    "OBT": {
        "symbol": "OBT",
        "decimals": 18,
        "name": "OBToken",
        "address": "0x8da6113655309f84127e0837fcf5c389892578b3"
    },
    "OCC": {
        "symbol": "OCC",
        "decimals": 18,
        "name": "OCC [via ChainPort.io]",
        "address": "0x2a4dffa1fa0f86ce7f0982f88aecc199fb3476bc"
    },
    "OCP": {
        "symbol": "OCP",
        "decimals": 18,
        "name": "Omni Consumer Protocols",
        "address": "0x3c70260eee0a2bfc4b375feb810325801f289fbd"
    },
    "OCTAVUS": {
        "symbol": "OCTAVUS",
        "decimals": 18,
        "name": "Octavus",
        "address": "0x27348c55a6ca17f0d3cb75049c21a04e08cf6e78"
    },
    "ODDZ": {
        "symbol": "ODDZ",
        "decimals": 18,
        "name": "OddzToken",
        "address": "0xcd40f2670cf58720b694968698a5514e924f742d"
    },
    "ODOGE": {
        "symbol": "ODOGE",
        "decimals": 9,
        "name": "Optimism Doge",
        "address": "0x9528b1166381fe60f24a952315a3e528a56407a0"
    },
    "ODYS": {
        "symbol": "ODYS",
        "decimals": 18,
        "name": "OdysseyWallet",
        "address": "0x54e951e513bc09abaff971641947bc69e31068bd"
    },
    "OG": {
        "symbol": "OG",
        "decimals": 2,
        "name": "OG",
        "address": "0xf05e45ad22150677a017fbd94b84fbb63dc9b44c"
    },
    "OGGY": {
        "symbol": "OGGY",
        "decimals": 9,
        "name": "Oggy Inu",
        "address": "0x92ed61fb8955cc4e392781cb8b7cd04aadc43d0c"
    },
    "OGS": {
        "symbol": "OGS",
        "decimals": 18,
        "name": "OGS",
        "address": "0x416947e6fc78f158fd9b775fa846b72d768879c2"
    },
    "OIN": {
        "symbol": "OIN",
        "decimals": 8,
        "name": "oinfinance",
        "address": "0x658e64ffcf40d240a43d52ca9342140316ae44fa"
    },
    "OK": {
        "symbol": "OK",
        "decimals": 18,
        "name": "Wrapped Okcash BSC",
        "address": "0x523821d20a283d955f6205b4c9252779cd0f964b"
    },
    "OKA": {
        "symbol": "OKA",
        "decimals": 10,
        "name": "Okaleido Token",
        "address": "0x1f3a0425f0d50f1c277b617374ed6c2e95a4ca84"
    },
    "OKG": {
        "symbol": "OKG",
        "decimals": 18,
        "name": "Ookeenga",
        "address": "0x7758a52c1bb823d02878b67ad87b6ba37a0cdbf5"
    },
    "OKS": {
        "symbol": "OKS",
        "decimals": 18,
        "name": "Oikos Network Token",
        "address": "0x18acf236eb40c0d4824fb8f2582ebbecd325ef6a"
    },
    "OKSE": {
        "symbol": "OKSE",
        "decimals": 18,
        "name": "Okse",
        "address": "0x606fb7969fc1b5cad58e64b12cf827fb65ee4875"
    },
    "OLAND": {
        "symbol": "OLAND",
        "decimals": 18,
        "name": "Oceanland",
        "address": "0xb0461d7e8212d311b842a58e9989ede849ac6816"
    },
    "OLE": {
        "symbol": "OLE",
        "decimals": 18,
        "name": "OpenLeverage",
        "address": "0xa865197a84e780957422237b5d152772654341f3"
    },
    "OM": {
        "symbol": "OM",
        "decimals": 18,
        "name": "MANTRA DAO",
        "address": "0xf78d2e7936f5fe18308a3b2951a93b6c4a41f5e2"
    },
    "ONE": {
        "symbol": "ONE",
        "decimals": 18,
        "name": "BigONE Token",
        "address": "0x04baf95fd4c52fd09a56d840baee0ab8d7357bf0"
    },
    "ONG": {
        "symbol": "ONG",
        "decimals": 9,
        "name": "Poly-Peg ONG",
        "address": "0x308bfaeaac8bdab6e9fc5ead8edcb5f95b0599d9"
    },
    "ONI": {
        "symbol": "ONI",
        "decimals": 18,
        "name": "Onino",
        "address": "0xea89199344a492853502a7a699cc4230854451b8"
    },
    "ONT": {
        "symbol": "ONT",
        "decimals": 18,
        "name": "Ontology Token",
        "address": "0xfd7b3a77848f1c2d67e05e54d78d174a0c850335"
    },
    "ONUS": {
        "symbol": "ONUS",
        "decimals": 18,
        "name": "ONUS",
        "address": "0x1851ccd370c444ff494d7505e6103959bce9f9d9"
    },
    "OOE": {
        "symbol": "OOE",
        "decimals": 18,
        "name": "OpenOcean",
        "address": "0x9029fdfae9a03135846381c7ce16595c3554e10a"
    },
    "OPA": {
        "symbol": "OPA",
        "decimals": 18,
        "name": "OPA",
        "address": "0xa2f89a3be1bada5eb9d58d23edc2e2fe0f82f4b0"
    },
    "OPEN": {
        "symbol": "OPEN",
        "decimals": 18,
        "name": "OpenWorld",
        "address": "0x27a339d9b59b21390d7209b78a839868e319301b"
    },
    "OPEPE": {
        "symbol": "OPEPE",
        "decimals": 9,
        "name": "Optimism PEPE",
        "address": "0x0851ad49cff57c024594da73095e6e05d8b1676a"
    },
    "OPINU": {
        "symbol": "OPINU",
        "decimals": 18,
        "name": "Optimus Inu",
        "address": "0x674aa28ac436834051fff3fc7b6e59d6f9c57a1c"
    },
    "OPS": {
        "symbol": "OPS",
        "decimals": 18,
        "name": "Octopus Protocol",
        "address": "0xdf0121a3ba5c10816ea2943c722650c4a4b0dbe6"
    },
    "OPT": {
        "symbol": "OPT",
        "decimals": 9,
        "name": "Optimus",
        "address": "0xdfe29afdf5a7d0bb92a01a56adabfa87d652e0e7"
    },
    "Optimus AI": {
        "symbol": "Optimus AI",
        "decimals": 9,
        "name": "Optimus AI",
        "address": "0xad3063fe9df7355fc6e008c04f8da6e02b40304e"
    },
    "OPUL": {
        "symbol": "OPUL",
        "decimals": 18,
        "name": "OpulousToken [via ChainPort.io]",
        "address": "0x686318000d982bc8dcc1cdcf8ffd22322f0960ed"
    },
    "OPV": {
        "symbol": "OPV",
        "decimals": 18,
        "name": "OpenLive NFT",
        "address": "0x36c7b164f85d6f775cd128966d5819c7d36feff3"
    },
    "ORAI": {
        "symbol": "ORAI",
        "decimals": 18,
        "name": "Oraichain Token",
        "address": "0xa325ad6d9c92b55a3fc5ad7e412b1518f96441c0"
    },
    "ORBS": {
        "symbol": "ORBS",
        "decimals": 18,
        "name": "Orbs",
        "address": "0xebd49b26169e1b52c04cfd19fcf289405df55f80"
    },
    "ORE": {
        "symbol": "ORE",
        "decimals": 18,
        "name": "pTokens ORE [via ChainPort.io]",
        "address": "0x4ef285c8cbe52267c022c39da98b97ca4b7e2ff9"
    },
    "OREO": {
        "symbol": "OREO",
        "decimals": 9,
        "name": "OreoFi",
        "address": "0xf28db5d3ddaa505937cfe27ee52d91da73b1d740"
    },
    "ORIGEN": {
        "symbol": "ORIGEN",
        "decimals": 18,
        "name": "Origen DEFI",
        "address": "0x20dd734594dadc69df313cd143b34a70a3d9214e"
    },
    "ORME": {
        "symbol": "ORME",
        "decimals": 18,
        "name": "Ormeus Coin",
        "address": "0x7e2afe446a30fa67600a5174df7f4002b8e15b03"
    },
    "ORO": {
        "symbol": "ORO",
        "decimals": 18,
        "name": "Operon Origins",
        "address": "0xfc4f5a4d1452b8dc6c3cb745db15b29c00812b19"
    },
    "ORT": {
        "symbol": "ORT",
        "decimals": 8,
        "name": "Okratech",
        "address": "0x9e711221b34a2d4b8f552bd5f4a6c4e7934920f7"
    },
    "OSK": {
        "symbol": "OSK",
        "decimals": 18,
        "name": "OSK",
        "address": "0x04fa9eb295266d9d4650edcb879da204887dc3da"
    },
    "OVR": {
        "symbol": "OVR",
        "decimals": 18,
        "name": "OVR",
        "address": "0x7e35d0e9180bf3a1fc47b0d110be7a21a10b41fe"
    },
    "OWL": {
        "symbol": "OWL",
        "decimals": 18,
        "name": "OwlDAO token",
        "address": "0x9085b4d52c3e0b8b6f9af6213e85a433c7d76f19"
    },
    "OXB": {
        "symbol": "OXB",
        "decimals": 18,
        "name": "OXBULL.TECH",
        "address": "0x7536c00711e41df6aebcca650791107645b6bc52"
    },
    "PACOCA": {
        "symbol": "PACOCA",
        "decimals": 18,
        "name": "Pacoca",
        "address": "0x55671114d774ee99d653d6c12460c780a67f1d18"
    },
    "PAID": {
        "symbol": "PAID",
        "decimals": 18,
        "name": "PAID Network",
        "address": "0xad86d0e9764ba90ddd68747d64bffbd79879a238"
    },
    "PALLA": {
        "symbol": "PALLA",
        "decimals": 18,
        "name": "Pallapay",
        "address": "0x8f49733210700d38098d7375c221c7d02f700cc8"
    },
    "PALM": {
        "symbol": "PALM",
        "decimals": 18,
        "name": "PALM",
        "address": "0x29745314b4d294b7c77cdb411b8aaa95923aae38"
    },
    "PANDA": {
        "symbol": "PANDA",
        "decimals": 9,
        "name": "HashPanda",
        "address": "0x8578eb576e126f67913a8bc0622e0a22eba0989a"
    },
    "PANDAI": {
        "symbol": "PANDAI",
        "decimals": 6,
        "name": "PandAI Token",
        "address": "0x550d7984b7adfff88815e5528e12e322df6d3b9b"
    },
    "PARA": {
        "symbol": "PARA",
        "decimals": 18,
        "name": "Paralink Network",
        "address": "0x076ddce096c93dcf5d51fe346062bf0ba9523493"
    },
    "PARIO": {
        "symbol": "PARIO",
        "decimals": 4,
        "name": "Pario",
        "address": "0xcda88e0fb36a9b5b943f56b3e7825b756e759949"
    },
    "PARMA": {
        "symbol": "PARMA",
        "decimals": 18,
        "name": "Parma FanToken",
        "address": "0xf7f0dc9fd88e436847580d883319137ec2aa6b94"
    },
    "PAWTH": {
        "symbol": "PAWTH",
        "decimals": 9,
        "name": "Pawthereum",
        "address": "0x409e215738e31d8ab252016369c2dd9c2008fee0"
    },
    "PAX": {
        "symbol": "PAX",
        "decimals": 18,
        "name": "Paxos Standard",
        "address": "0xb7f8cd00c5a06c0537e2abff0b58033d02e5e094"
    },
    "PAXG": {
        "symbol": "PAXG",
        "decimals": 18,
        "name": "PAX Gold",
        "address": "0x7950865a9140cb519342433146ed5b40c6f210f7"
    },
    "PAY": {
        "symbol": "PAY",
        "decimals": 18,
        "name": "PayBolt",
        "address": "0xe580074a10360404af3abfe2d524d5806d993ea3"
    },
    "PBR": {
        "symbol": "PBR",
        "decimals": 18,
        "name": "PolkaBridge",
        "address": "0x1d1cb8997570e73949930c01fe5796c88d7336c6"
    },
    "PBX": {
        "symbol": "PBX",
        "decimals": 18,
        "name": "Probinex Token",
        "address": "0xa177bdd433aea3702beb46652adcfc64248d4ab3"
    },
    "PCA": {
        "symbol": "PCA",
        "decimals": 18,
        "name": "Purchasa",
        "address": "0xe700ba35998fad8e669e3cca7b3a350f1fdcacf8"
    },
    "PCNT": {
        "symbol": "PCNT",
        "decimals": 18,
        "name": "Playcent",
        "address": "0xe9b9c1c38dab5eab3b7e2ad295425e89bd8db066"
    },
    "PCSP": {
        "symbol": "PCSP",
        "decimals": 18,
        "name": "Stroke-Prevention GenomicDAO",
        "address": "0xe356337a72d4990a3cfd4d13367659f14f304545"
    },
    "pCWS": {
        "symbol": "pCWS",
        "decimals": 18,
        "name": "PolyCrowns",
        "address": "0xbcf39f0edda668c58371e519af37ca705f2bfcbd"
    },
    "PEAK": {
        "symbol": "PEAK",
        "decimals": 8,
        "name": "PEAKDEFI",
        "address": "0x630d98424efe0ea27fb1b3ab7741907dffeaad78"
    },
    "PEEL": {
        "symbol": "PEEL",
        "decimals": 18,
        "name": "Meta Apes Peel",
        "address": "0x734548a9e43d2d564600b1b2ed5be9c2b911c6ab"
    },
    "PEL": {
        "symbol": "PEL",
        "decimals": 18,
        "name": "Propel Token",
        "address": "0xa75e7928d3de682e3f44da60c26f33117c4e6c5c"
    },
    "PEN": {
        "symbol": "PEN",
        "decimals": 18,
        "name": "Protocon",
        "address": "0xa5dec77c4d1b4eba2807c9926b182812a0cbf9eb"
    },
    "PEPA": {
        "symbol": "PEPA",
        "decimals": 9,
        "name": "Pepa Inu",
        "address": "0xc3137c696796d69f783cd0be4ab4bb96814234aa"
    },
    "PEPE": {
        "symbol": "PEPE",
        "decimals": 18,
        "name": "Pepe Coin",
        "address": "0xb46584e0efde3092e04010a13f2eae62adb3b9f0"
    },
    "PEPEAI": {
        "symbol": "PEPEAI",
        "decimals": 18,
        "name": "Pepe AI",
        "address": "0x24086eab82dbdaa4771d0a5d66b0d810458b0e86"
    },
    "PepeBNB": {
        "symbol": "PepeBNB",
        "decimals": 9,
        "name": "Pepe The Frog",
        "address": "0x47fd014706081068448b89fc6baca2730977216a"
    },
    "PEPEKI": {
        "symbol": "PEPEKI",
        "decimals": 9,
        "name": "Pepeki",
        "address": "0x192eb3e89c09590ddb86af1172094b0719a67b34"
    },
    "PEPELON": {
        "symbol": "PEPELON",
        "decimals": 9,
        "name": "Pepelon",
        "address": "0xdd80c9625e13db655840ed47af90cc78702367ed"
    },
    "PERI": {
        "symbol": "PERI",
        "decimals": 18,
        "name": "Peri Finance Token",
        "address": "0xb49b7e0742ecb4240ffe91661d2a580677460b6a"
    },
    "PERL": {
        "symbol": "PERL",
        "decimals": 18,
        "name": "Perlin",
        "address": "0x0f9e4d49f25de22c2202af916b681fbb3790497b"
    },
    "PERP": {
        "symbol": "PERP",
        "decimals": 18,
        "name": "Perpetual Protocol",
        "address": "0x4e7f408be2d4e9d60f49a64b89bb619c84c7c6f5"
    },
    "PESA": {
        "symbol": "PESA",
        "decimals": 18,
        "name": "Pesabase",
        "address": "0x4adc604a0261e3d340745533964fff6bb130f3c3"
    },
    "PETO": {
        "symbol": "PETO",
        "decimals": 5,
        "name": "Petoverse",
        "address": "0xe327ed2037f133cda9f56171b68b6b7b4dfa6175"
    },
    "PETS": {
        "symbol": "PETS",
        "decimals": 18,
        "name": "MicroPets",
        "address": "0xa77346760341460b42c230ca6d21d4c8e743fa9c"
    },
    "PEX": {
        "symbol": "PEX",
        "decimals": 18,
        "name": "PEAR DAO",
        "address": "0x6a0b66710567b6beb81a71f7e9466450a91a384b"
    },
    "PHB": {
        "symbol": "PHB",
        "decimals": 18,
        "name": "Phoenix Global",
        "address": "0x0409633a72d846fc5bbe2f98d88564d35987904d"
    },
    "PHL": {
        "symbol": "PHL",
        "decimals": 18,
        "name": "PHILCOIN",
        "address": "0x68dd887d012abdf99d3492621e4d576a3f75019d"
    },
    "PHM": {
        "symbol": "PHM",
        "decimals": 18,
        "name": "Phantom Protocol Token",
        "address": "0x4399ae7538c33ca24edd4c28c5dd7ce9a80acf81"
    },
    "PHX": {
        "symbol": "PHX",
        "decimals": 18,
        "name": "Phoenix chain",
        "address": "0x9776191f4ebbba7f358c1663bf82c0a0906c77fa"
    },
    "PIAS": {
        "symbol": "PIAS",
        "decimals": 18,
        "name": "PIAS",
        "address": "0xc669a70e0b3d07e3514afd97ebfb3d134077a4a1"
    },
    "PIG": {
        "symbol": "PIG",
        "decimals": 9,
        "name": "Pig Token",
        "address": "0x8850d2c68c632e3b258e612abaa8fada7e6958e5"
    },
    "PIGGY": {
        "symbol": "PIGGY",
        "decimals": 18,
        "name": "PIGGY",
        "address": "0x1beac6df550be0ad146dd99b4726c6bec9c5c6a5"
    },
    "PING": {
        "symbol": "PING",
        "decimals": 9,
        "name": "PING",
        "address": "0x5546600f77eda1dcf2e8817ef4d617382e7f71f5"
    },
    "PINK": {
        "symbol": "PINK",
        "decimals": 18,
        "name": "Pink Token",
        "address": "0x9133049fb1fddc110c92bf5b7df635abb70c89dc"
    },
    "PINKIE": {
        "symbol": "PINKIE",
        "decimals": 18,
        "name": "Pinkie Inu",
        "address": "0x628e3a6fd5e78564da8de2aa7386d57b84902380"
    },
    "PINKSALE": {
        "symbol": "PINKSALE",
        "decimals": 18,
        "name": "PinkSale",
        "address": "0x602ba546a7b06e0fc7f58fd27eb6996ecc824689"
    },
    "PIP": {
        "symbol": "PIP",
        "decimals": 18,
        "name": "Pi-Protocol",
        "address": "0x25c30340e6f9f6e521827cf03282943da00c0ece"
    },
    "PIRA": {
        "symbol": "PIRA",
        "decimals": 18,
        "name": "Piratera Token",
        "address": "0xb27b68431c9a1819c8633ff75a2dd14f54799a21"
    },
    "PIT": {
        "symbol": "PIT",
        "decimals": 9,
        "name": "Pitbull",
        "address": "0xa57ac35ce91ee92caefaa8dc04140c8e232c2e50"
    },
    "PIXEL": {
        "symbol": "PIXEL",
        "decimals": 18,
        "name": "PixelVerse",
        "address": "0x47db24e17c0c4622523449a239b3de746e2b0b23"
    },
    "PIZA": {
        "symbol": "PIZA",
        "decimals": 18,
        "name": "Half Pizza",
        "address": "0xfc646d0b564bf191b3d3adf2b620a792e485e6da"
    },
    "PKN": {
        "symbol": "PKN",
        "decimals": 18,
        "name": "Poken",
        "address": "0x4b5decb9327b4d511a58137a1ade61434aacdd43"
    },
    "PKR": {
        "symbol": "PKR",
        "decimals": 18,
        "name": "POLKER",
        "address": "0xc49dde62b4a0810074721faca54aab52369f486a"
    },
    "PLACE": {
        "symbol": "PLACE",
        "decimals": 18,
        "name": "PlaceWar Governance Token",
        "address": "0x07728696ee70a28c9c032926577af1d524df30f9"
    },
    "PLAY": {
        "symbol": "PLAY",
        "decimals": 18,
        "name": "PLAY",
        "address": "0xd069599e718f963bd84502b49ba8f8657faf5b3a"
    },
    "PLGR": {
        "symbol": "PLGR",
        "decimals": 18,
        "name": "Pledge Finance",
        "address": "0x6aa91cbfe045f9d154050226fcc830ddba886ced"
    },
    "PLSPAD": {
        "symbol": "PLSPAD",
        "decimals": 18,
        "name": "PULSEPAD.io",
        "address": "0x8a74bc8c372bc7f0e9ca3f6ac0df51be15aec47a"
    },
    "PLT": {
        "symbol": "PLT",
        "decimals": 18,
        "name": "Poollotto.finance",
        "address": "0x631c2f0edabac799f07550aee4ff0bf7fd35212b"
    },
    "PMA": {
        "symbol": "PMA",
        "decimals": 18,
        "name": "PumaPay",
        "address": "0x43a167b15a6f24913a8b4d35488b36ac15d39200"
    },
    "PMG": {
        "symbol": "PMG",
        "decimals": 18,
        "name": "Pomerium Ecosystem Token",
        "address": "0x0733618ab62eeec815f2d1739b7a50bf9e74d8a2"
    },
    "PMON": {
        "symbol": "PMON",
        "decimals": 18,
        "name": "Polkamon",
        "address": "0x1796ae0b0fa4862485106a0de9b654efe301d0b2"
    },
    "PNB": {
        "symbol": "PNB",
        "decimals": 18,
        "name": "Pink BNB",
        "address": "0xf5bde7eb378661f04c841b22ba057326b0370153"
    },
    "PNDR": {
        "symbol": "PNDR",
        "decimals": 18,
        "name": "PANDORA",
        "address": "0x6c1efbed2f57dd486ec091dffd08ee5235a570b1"
    },
    "PNT": {
        "symbol": "PNT",
        "decimals": 18,
        "name": "pNetwork Token",
        "address": "0xdaacb0ab6fb34d24e8a67bfa14bf4d95d4c7af92"
    },
    "POCO": {
        "symbol": "POCO",
        "decimals": 18,
        "name": "Poco Token",
        "address": "0x394bba8f309f3462b31238b3fd04b83f71a98848"
    },
    "POG": {
        "symbol": "POG",
        "decimals": 18,
        "name": "POG Coin",
        "address": "0xfcb0f2d2f83a32a847d8abb183b724c214cd7dd8"
    },
    "PokerFI": {
        "symbol": "PokerFI",
        "decimals": 9,
        "name": "PokerFI.Finance",
        "address": "0xfe073c3b891325ae8686d9cf2c8b3586674f7be2"
    },
    "POLC": {
        "symbol": "POLC",
        "decimals": 18,
        "name": "Polka City",
        "address": "0x6ae9701b9c423f40d54556c9a443409d79ce170a"
    },
    "POLIS": {
        "symbol": "POLIS",
        "decimals": 18,
        "name": "Polis",
        "address": "0xb5bea8a26d587cf665f2d78f077cca3c7f6341bd"
    },
    "POLO": {
        "symbol": "POLO",
        "decimals": 18,
        "name": "PolkaPlayToken",
        "address": "0xb28a7f8f5328faffdd862985177583c2bb71e016"
    },
    "POLS": {
        "symbol": "POLS",
        "decimals": 18,
        "name": "PolkastarterToken",
        "address": "0x7e624fa0e1c4abfd309cc15719b7e2580887f570"
    },
    "POLYPAD": {
        "symbol": "POLYPAD",
        "decimals": 18,
        "name": "POLYPAD.com",
        "address": "0x8ae619d633cce175a2fbcfa1cea119ddc80f1342"
    },
    "POOLX": {
        "symbol": "POOLX",
        "decimals": 18,
        "name": "Poolz Finance",
        "address": "0xbaea9aba1454df334943951d51116ae342eab255"
    },
    "POOLZ": {
        "symbol": "POOLZ",
        "decimals": 18,
        "name": "$Poolz Finance [via ChainPort.io]",
        "address": "0x77018282fd033daf370337a5367e62d8811bc885"
    },
    "POOP": {
        "symbol": "POOP",
        "decimals": 9,
        "name": "PooChain",
        "address": "0xa1611e8d4070dee36ef308952cf34255c92a01c5"
    },
    "POP": {
        "symbol": "POP",
        "decimals": 18,
        "name": "Popcorn",
        "address": "0xe8647ea19496e87c061bbad79f457928b2f52b5a"
    },
    "POR": {
        "symbol": "POR",
        "decimals": 18,
        "name": "Portuma",
        "address": "0x9000cac49c3841926baac5b2e13c87d43e51b6a4"
    },
    "PORNROCKET": {
        "symbol": "PORNROCKET",
        "decimals": 9,
        "name": "PORNROCKET",
        "address": "0xcf9f991b14620f5ad144eec11f9bc7bf08987622"
    },
    "PORTO": {
        "symbol": "PORTO",
        "decimals": 8,
        "name": "FC Porto Fan Token",
        "address": "0x49f2145d6366099e13b10fbf80646c0f377ee7f6"
    },
    "PORTX": {
        "symbol": "PORTX",
        "decimals": 18,
        "name": "ChainPort Token [via ChainPort.io]",
        "address": "0x54c3b88b7e9702f915ddc6e483aaf369b2615f8d"
    },
    "POSI": {
        "symbol": "POSI",
        "decimals": 18,
        "name": "Position Token",
        "address": "0x5ca42204cdaa70d5c773946e69de942b85ca6706"
    },
    "POSS": {
        "symbol": "POSS",
        "decimals": 18,
        "name": "Posschain",
        "address": "0x230f6e7904ffc156abd8adfd7556e56e2a358cb1"
    },
    "POT": {
        "symbol": "POT",
        "decimals": 8,
        "name": "X Protocol",
        "address": "0x4c7b04d50e070848e3c7757995a57624563e0245"
    },
    "POTS": {
        "symbol": "POTS",
        "decimals": 18,
        "name": "Moonpot",
        "address": "0x3fcca8648651e5b974dd6d3e50f61567779772a8"
    },
    "PPAD": {
        "symbol": "PPAD",
        "decimals": 18,
        "name": "PlayPad Token",
        "address": "0x93bb13e90678ccd8bbab07d1daef15086746dc9b"
    },
    "PPAI": {
        "symbol": "PPAI",
        "decimals": 9,
        "name": "Plug Power AI",
        "address": "0xefd1c4bc2d22639ea86b70e249eec0ccabf54f06"
    },
    "PPAY": {
        "symbol": "PPAY",
        "decimals": 18,
        "name": "Plasma",
        "address": "0xfb288d60d3b66f9c3e231a9a39ed3f158a4269aa"
    },
    "PPC": {
        "symbol": "PPC",
        "decimals": 9,
        "name": "PEPE COIN BSC",
        "address": "0x9498c4383406a5bdd9100cff3fe0b550a111dd3d"
    },
    "PPM": {
        "symbol": "PPM",
        "decimals": 18,
        "name": "PUNK PANDA MESSENGER",
        "address": "0xee246aa7e2ecf136466c6fe4808f395861c6a04e"
    },
    "PRI": {
        "symbol": "PRI",
        "decimals": 18,
        "name": "Privateum",
        "address": "0xb10be3f4c7e1f870d86ed6cfd412fed6615feb6f"
    },
    "PRIMAL": {
        "symbol": "PRIMAL",
        "decimals": 18,
        "name": "PRIMAL Token",
        "address": "0xcb5327ed4649548e0d73e70b633cdfd99af6da87"
    },
    "PRIMATE": {
        "symbol": "PRIMATE",
        "decimals": 18,
        "name": "PRIMATE",
        "address": "0xa19863e302fd1b41276fce5a48d9c511dbeef34c"
    },
    "PRL": {
        "symbol": "PRL",
        "decimals": 18,
        "name": "Parallel Token",
        "address": "0xd07e82440a395f3f3551b42da9210cd1ef4f8b24"
    },
    "PRNT": {
        "symbol": "PRNT",
        "decimals": 18,
        "name": "PrimeNumbers",
        "address": "0x9f402f44684574f3535ea6f1bb5cfbffef42ee28"
    },
    "PROM": {
        "symbol": "PROM",
        "decimals": 18,
        "name": "Prometeus",
        "address": "0xaf53d56ff99f1322515e54fdde93ff8b3b7dafd5"
    },
    "PROP": {
        "symbol": "PROP",
        "decimals": 18,
        "name": "Propland",
        "address": "0x58784ca627e15e4a1a2b80444ccaa6320526e21b"
    },
    "PROS": {
        "symbol": "PROS",
        "decimals": 18,
        "name": "Prosper",
        "address": "0xed8c8aa8299c10f067496bb66f8cc7fb338a3405"
    },
    "PRP": {
        "symbol": "PRP",
        "decimals": 9,
        "name": "PERPETUUM",
        "address": "0x84afb95ca5589674e02d227bdd6da7e7dcf31a3e"
    },
    "PRQ": {
        "symbol": "PRQ",
        "decimals": 18,
        "name": "Parsiq Token",
        "address": "0xd21d29b38374528675c34936bf7d5dd693d2a577"
    },
    "PRVC": {
        "symbol": "PRVC",
        "decimals": 18,
        "name": "PrivaCoin",
        "address": "0x5711f19b7b21938d31d07e5736b4660c1159d7d3"
    },
    "PRX": {
        "symbol": "PRX",
        "decimals": 8,
        "name": "PRX",
        "address": "0x90e3414e00e231b962666bd94adb811d5bcd0c2a"
    },
    "PS1": {
        "symbol": "PS1",
        "decimals": 18,
        "name": "PolysportsToken",
        "address": "0x6451c6484d23889003c20be51819d6aa7dbd2b35"
    },
    "PSB": {
        "symbol": "PSB",
        "decimals": 18,
        "name": "PlanetSandbox",
        "address": "0x36bfbb1d5b3c9b336f3d64976599b6020ca805f1"
    },
    "PSG": {
        "symbol": "PSG",
        "decimals": 2,
        "name": "Paris Saint-Germain",
        "address": "0xbc5609612b7c44bef426de600b5fd1379db2ecf1"
    },
    "PSP": {
        "symbol": "PSP",
        "decimals": 18,
        "name": "ParaSwap",
        "address": "0xcafe001067cdef266afb7eb5a286dcfd277f3de5"
    },
    "PSR": {
        "symbol": "PSR",
        "decimals": 18,
        "name": "Pandora Spirit",
        "address": "0xb72ba371c900aa68bb9fa473e93cfbe212030fcb"
    },
    "PSTAKE": {
        "symbol": "PSTAKE",
        "decimals": 18,
        "name": "pStake Finance",
        "address": "0x4c882ec256823ee773b25b414d36f92ef58a7c0c"
    },
    "PTG": {
        "symbol": "PTG",
        "decimals": 18,
        "name": "Pepethegrove",
        "address": "0xd3d91ff2c065ef69aaf0459b95f9770d709a496f"
    },
    "PTOOLS": {
        "symbol": "PTOOLS",
        "decimals": 18,
        "name": "Pricetools",
        "address": "0x92400f8b8c4658153c10c98500b63ac9f87571c2"
    },
    "PTS": {
        "symbol": "PTS",
        "decimals": 18,
        "name": "Petals",
        "address": "0xfa53a4778431712af31a11621edee4d0926df1ac"
    },
    "PTT": {
        "symbol": "PTT",
        "decimals": 18,
        "name": "POTENT",
        "address": "0x057aff3e314e1ca15bed75510df81a20098ce456"
    },
    "PTX": {
        "symbol": "PTX",
        "decimals": 8,
        "name": "PLATINX",
        "address": "0xa469d8e55afcd58003d6cbdc770c0ecc2dd71945"
    },
    "PULI": {
        "symbol": "PULI",
        "decimals": 9,
        "name": "PULI INU",
        "address": "0xaef0a177c8c329cbc8508292bb7e06c00786bbfc"
    },
    "PULSE": {
        "symbol": "PULSE",
        "decimals": 18,
        "name": "PulseFolio",
        "address": "0xba7e020d5a463f29535b35137ccb4aa6f4359272"
    },
    "PVERSE": {
        "symbol": "PVERSE",
        "decimals": 18,
        "name": "PornVerse",
        "address": "0x9733e1038897efb36bb2e526c328c9b6a4b78db2"
    },
    "PVU": {
        "symbol": "PVU",
        "decimals": 18,
        "name": "Plant vs Undead Token",
        "address": "0x31471e0791fcdbe82fbf4c44943255e923f1b794"
    },
    "PWAR": {
        "symbol": "PWAR",
        "decimals": 18,
        "name": "PolkaWar",
        "address": "0x16153214e683018d5aa318864c8e692b66e16778"
    },
    "PXT": {
        "symbol": "PXT",
        "decimals": 18,
        "name": "PIXER",
        "address": "0xeb79c85c6d633ae81c97be71e1691ee7dc6e132d"
    },
    "PZP": {
        "symbol": "PZP",
        "decimals": 18,
        "name": "PLAYZAP",
        "address": "0x6ad9e9c098a45b2b41b519119c31c3dcb02accb2"
    },
    "QANX": {
        "symbol": "QANX",
        "decimals": 18,
        "name": "QANX Token",
        "address": "0xaaa9214f675316182eaa21c85f0ca99160cc3aaa"
    },
    "QMALL": {
        "symbol": "QMALL",
        "decimals": 18,
        "name": "Qmall Token",
        "address": "0x07e551e31a793e20dc18494ff6b03095a8f8ee36"
    },
    "QRT": {
        "symbol": "QRT",
        "decimals": 9,
        "name": "QRKITA TOKEN",
        "address": "0x921d3a6ed8223afb6358410f717e2fb13cbae700"
    },
    "QUA": {
        "symbol": "QUA",
        "decimals": 18,
        "name": "Quarashi",
        "address": "0xfd0fd32a20532ad690731c2685d77c351015ebba"
    },
    "QUACK": {
        "symbol": "QUACK",
        "decimals": 9,
        "name": "RichQUACK.com",
        "address": "0xd74b782e05aa25c50e7330af541d46e18f36661c"
    },
    "QUACKS": {
        "symbol": "QUACKS",
        "decimals": 18,
        "name": "Starquack",
        "address": "0xcfa65d49541a0a930a19321c797e442123822fb4"
    },
    "QUBE": {
        "symbol": "QUBE",
        "decimals": 18,
        "name": "QUBE TOKEN",
        "address": "0x3e9d6430144485873248251fcb92bd856e95d1cd"
    },
    "QUIDD": {
        "symbol": "QUIDD",
        "decimals": 18,
        "name": "QUIDD",
        "address": "0x7961ade0a767c0e5b67dd1a1f78ba44f727642ed"
    },
    "QUINT": {
        "symbol": "QUINT",
        "decimals": 18,
        "name": "QUINT",
        "address": "0x64619f611248256f7f4b72fe83872f89d5d60d64"
    },
    "QUO": {
        "symbol": "QUO",
        "decimals": 18,
        "name": "Quoll Token",
        "address": "0x08b450e4a48c04cdf6db2bd4cf24057f7b9563ff"
    },
    "QUON": {
        "symbol": "QUON",
        "decimals": 18,
        "name": "Quontral",
        "address": "0x8f5a25bfa6ce7bcf1517148724beb3649ac49d64"
    },
    "R3T": {
        "symbol": "R3T",
        "decimals": 18,
        "name": "R3 Token",
        "address": "0xf97c30f0b31aee9b1ab087f8ccf5b14bf354d29f"
    },
    "RAB": {
        "symbol": "RAB",
        "decimals": 18,
        "name": "Rabbit",
        "address": "0x24ef78c7092d255ed14a0281ac1800c359af3afe"
    },
    "RABBIT": {
        "symbol": "RABBIT",
        "decimals": 18,
        "name": "Rabbit Coin",
        "address": "0x95a1199eba84ac5f19546519e287d43d2f0e1b41"
    },
    "RabbitKing": {
        "symbol": "RabbitKing",
        "decimals": 18,
        "name": "RabbitKing",
        "address": "0x626cab57051e80f4b84551856588b62983bdb94e"
    },
    "RACA": {
        "symbol": "RACA",
        "decimals": 18,
        "name": "Radio Caca V2",
        "address": "0x12bb890508c125661e03b09ec06e404bc9289040"
    },
    "RADIO": {
        "symbol": "RADIO",
        "decimals": 18,
        "name": "RadioShack Token",
        "address": "0x30807d3b851a31d62415b8bb7af7dca59390434a"
    },
    "RAGE": {
        "symbol": "RAGE",
        "decimals": 18,
        "name": "RAGE Token",
        "address": "0xd38c1b7b95d359978996e01b8a85286f65b3c011"
    },
    "RAID": {
        "symbol": "RAID",
        "decimals": 18,
        "name": "RAID",
        "address": "0xeb90a6273f616a8ed1cf58a05d3ae1c1129b4de6"
    },
    "RAIN": {
        "symbol": "RAIN",
        "decimals": 18,
        "name": "Rainmaker Games",
        "address": "0x6bcd897d4ba5675f860c7418ddc034f6c5610114"
    },
    "RAINBOW": {
        "symbol": "RAINBOW",
        "decimals": 9,
        "name": "RainbowToken",
        "address": "0x673da443da2f6ae7c5c660a9f0d3dd24d1643d36"
    },
    "RAINI": {
        "symbol": "RAINI",
        "decimals": 18,
        "name": "Rainicorn",
        "address": "0xeb953eda0dc65e3246f43dc8fa13f35623bdd5ed"
    },
    "RAM": {
        "symbol": "RAM",
        "decimals": 9,
        "name": "Ramifi Token",
        "address": "0x63290fc683d11ea077aba09596ff7387d49df912"
    },
    "RAMP": {
        "symbol": "RAMP",
        "decimals": 18,
        "name": "RAMP DEFI",
        "address": "0x8519ea49c997f50ceffa444d240fb655e89248aa"
    },
    "rASKO": {
        "symbol": "rASKO",
        "decimals": 18,
        "name": "rASKO on BSC",
        "address": "0xd118f42edbc839f7e1e85d5269a25288792c141b"
    },
    "RAVEN": {
        "symbol": "RAVEN",
        "decimals": 18,
        "name": "Raven Protocol",
        "address": "0xcd7c5025753a49f1881b31c48caa7c517bb46308"
    },
    "RAZE": {
        "symbol": "RAZE",
        "decimals": 18,
        "name": "Raze Network",
        "address": "0x65e66a61d0a8f1e686c2d6083ad611a10d84d97a"
    },
    "RB": {
        "symbol": "RB",
        "decimals": 18,
        "name": "Hey Reborn",
        "address": "0x441bb79f2da0daf457bad3d401edb68535fb3faa"
    },
    "RBP": {
        "symbol": "RBP",
        "decimals": 18,
        "name": "Rare Ball Portion",
        "address": "0x563ca064e41f3b5d80adeecfe49ab375fd7afbef"
    },
    "RBT": {
        "symbol": "RBT",
        "decimals": 18,
        "name": "Robust Token",
        "address": "0x891e4554227385c5c740f9b483e935e3cbc29f01"
    },
    "RCG": {
        "symbol": "RCG",
        "decimals": 18,
        "name": "Recharge",
        "address": "0x2d94172436d869c1e3c094bead272508fab0d9e3"
    },
    "RDF": {
        "symbol": "RDF",
        "decimals": 18,
        "name": "ReadFi",
        "address": "0xf29cccc3460506e8f9bc038d4716c05b76b0441e"
    },
    "RDNT": {
        "symbol": "RDNT",
        "decimals": 18,
        "name": "Radiant",
        "address": "0xf7de7e8a6bd59ed41a4b5fe50278b3b7f31384df"
    },
    "REAL": {
        "symbol": "REAL",
        "decimals": 18,
        "name": "REAL REALM",
        "address": "0xe91cd52bd65fe23a3eae40e3eb87180e8306399f"
    },
    "REALM": {
        "symbol": "REALM",
        "decimals": 18,
        "name": "REALM",
        "address": "0x464fdb8affc9bac185a7393fd4298137866dcfb8"
    },
    "REAU": {
        "symbol": "REAU",
        "decimals": 9,
        "name": "Vira-lata Finance",
        "address": "0x4c79b8c9cb0bd62b047880603a9decf36de28344"
    },
    "REC": {
        "symbol": "REC",
        "decimals": 18,
        "name": "RecoveryDAO",
        "address": "0xb922aa024e71a25077d78b593bd6f11f2f412e72"
    },
    "RedFlokiCEO": {
        "symbol": "RedFlokiCEO",
        "decimals": 9,
        "name": "Red Floki CEO",
        "address": "0x3c0fe6c4acd3a21615a51372d2a430eb68ccde43"
    },
    "RedPepe": {
        "symbol": "RedPepe",
        "decimals": 18,
        "name": "Red Pepe",
        "address": "0xa93e4bbe09b834b5a13dcd832daeaefe79fb4ae9"
    },
    "REDUX": {
        "symbol": "REDUX",
        "decimals": 18,
        "name": "ReduX",
        "address": "0xa2954b5734a9136bf648dce5bd2f9d2062551faa"
    },
    "REEF": {
        "symbol": "REEF",
        "decimals": 18,
        "name": "Reef.finance",
        "address": "0xf21768ccbc73ea5b6fd3c687208a7c2def2d966e"
    },
    "REFI": {
        "symbol": "REFI",
        "decimals": 18,
        "name": "RealfinanceNetwork",
        "address": "0x641a6dc991a49f7be9fe3c72c5d0fbb223edb12f"
    },
    "REGENT": {
        "symbol": "REGENT",
        "decimals": 18,
        "name": "REGENT COIN",
        "address": "0x4ffa143ce16a24215e8df96c0cef5677a7b91ee4"
    },
    "REGU": {
        "symbol": "REGU",
        "decimals": 18,
        "name": "RegularPresale",
        "address": "0xf1ca73caa1c7ad66af11147ba7d5636243af0493"
    },
    "REIGN": {
        "symbol": "REIGN",
        "decimals": 18,
        "name": "Reign of Terror",
        "address": "0xaa88fd757fa81ebbbce0eb1f324172d0e446093e"
    },
    "RELAY": {
        "symbol": "RELAY",
        "decimals": 18,
        "name": "Relay Token",
        "address": "0xe338d4250a4d959f88ff8789eaae8c32700bd175"
    },
    "RENA": {
        "symbol": "RENA",
        "decimals": 18,
        "name": "Warena Token",
        "address": "0xa9d75cc3405f0450955050c520843f99aff8749d"
    },
    "renBTC": {
        "symbol": "renBTC",
        "decimals": 8,
        "name": "renBTC",
        "address": "0xfce146bf3146100cfe5db4129cf6c82b0ef4ad8c"
    },
    "RET": {
        "symbol": "RET",
        "decimals": 9,
        "name": "Renewable Energy Token",
        "address": "0x10b9dd394467f2cfbc769e07e88dc7e2c41b0965"
    },
    "RETA": {
        "symbol": "RETA",
        "decimals": 18,
        "name": "Realital Metaverse",
        "address": "0x829555f1197171d35ec51c095e27b47a246ac6a6"
    },
    "REUNI": {
        "symbol": "REUNI",
        "decimals": 6,
        "name": "Reunit Token",
        "address": "0x9ed7e4b1bff939ad473da5e7a218c771d1569456"
    },
    "REV3L": {
        "symbol": "REV3L",
        "decimals": 18,
        "name": "REV3AL",
        "address": "0x30b5e345c79255101b8af22a19805a6fb96ddebb"
    },
    "REVA": {
        "symbol": "REVA",
        "decimals": 18,
        "name": "Reva Token",
        "address": "0x4fdd92bd67acf0676bfc45ab7168b3996f7b4a3b"
    },
    "REVO": {
        "symbol": "REVO",
        "decimals": 18,
        "name": "Revomon",
        "address": "0x155040625d7ae3e9cada9a73e3e44f76d3ed1409"
    },
    "REVV": {
        "symbol": "REVV",
        "decimals": 18,
        "name": "REVV",
        "address": "0x833f307ac507d47309fd8cdd1f835bef8d702a93"
    },
    "RFOX": {
        "symbol": "RFOX",
        "decimals": 18,
        "name": "RFOX",
        "address": "0x0a3a21356793b49154fd3bbe91cbc2a16c0457f5"
    },
    "RFuel": {
        "symbol": "RFuel",
        "decimals": 18,
        "name": "Rio Fuel Token",
        "address": "0x69a1913d334b524ea1632461c78797c837ca9fa6"
    },
    "RGEN": {
        "symbol": "RGEN",
        "decimals": 18,
        "name": "Paragen",
        "address": "0x25382fb31e4b22e0ea09cb0761863df5ad97ed72"
    },
    "RGP": {
        "symbol": "RGP",
        "decimals": 18,
        "name": "RigelToken",
        "address": "0xfa262f303aa244f9cc66f312f0755d89c3793192"
    },
    "RHYTHM": {
        "symbol": "RHYTHM",
        "decimals": 9,
        "name": "Rhythm",
        "address": "0xe4318f2acf2b9c3f518a3a03b5412f4999970ddb"
    },
    "RICE": {
        "symbol": "RICE",
        "decimals": 18,
        "name": "RICE",
        "address": "0xcf909ef9a61dc5b05d46b5490a9f00d51c40bb28"
    },
    "RIM": {
        "symbol": "RIM",
        "decimals": 18,
        "name": "MetaRim",
        "address": "0xa25199a79a34cc04b15e5c0bba4e3a557364e532"
    },
    "RISE": {
        "symbol": "RISE",
        "decimals": 18,
        "name": "EverRise",
        "address": "0xc17c30e98541188614df99239cabd40280810ca3"
    },
    "RITE": {
        "symbol": "RITE",
        "decimals": 18,
        "name": "RITE Coin",
        "address": "0x0f5d54b27bdb556823f96f2536496550f8816dc5"
    },
    "RJV": {
        "symbol": "RJV",
        "decimals": 6,
        "name": "Rejuve Token",
        "address": "0x1135883a1bc6776bf90c97845adc491922106dfb"
    },
    "ROAD": {
        "symbol": "ROAD",
        "decimals": 18,
        "name": "Yellow Road",
        "address": "0x1a3057027032a1af433f6f596cab15271e4d8196"
    },
    "ROCK": {
        "symbol": "ROCK",
        "decimals": 18,
        "name": "Bedrock",
        "address": "0xc3387e4285e9f80a7cfdf02b4ac6cdf2476a528a"
    },
    "ROCKI": {
        "symbol": "ROCKI",
        "decimals": 18,
        "name": "ROCKI",
        "address": "0xa01000c52b234a92563ba61e5649b7c76e1ba0f3"
    },
    "ROFI": {
        "symbol": "ROFI",
        "decimals": 18,
        "name": "HeroFi",
        "address": "0x3244b3b6030f374bafa5f8f80ec2f06aaf104b64"
    },
    "ROO": {
        "symbol": "ROO",
        "decimals": 18,
        "name": "LUCKY ROO",
        "address": "0x9d7107c8e30617cadc11f9692a19c82ae8bba938"
    },
    "ROOBEE": {
        "symbol": "ROOBEE",
        "decimals": 18,
        "name": "ROOBEE",
        "address": "0xf77351d8f4ee853135961a936bb8d2e4ffa75f9d"
    },
    "ROOM": {
        "symbol": "ROOM",
        "decimals": 18,
        "name": "OptionRoom Token",
        "address": "0x3c45a24d36ab6fc1925533c1f57bc7e1b6fba8a4"
    },
    "ROTTO": {
        "symbol": "ROTTO",
        "decimals": 9,
        "name": "Rottoken",
        "address": "0x9ae58314b3e11bc836eca62302264b617641c6ed"
    },
    "ROVI": {
        "symbol": "ROVI",
        "decimals": 18,
        "name": "ROVI Token",
        "address": "0xd02d45df2d9e8ee28a15d199689aefb1b4a74043"
    },
    "ROW": {
        "symbol": "ROW",
        "decimals": 18,
        "name": "RageOnWheels",
        "address": "0x026db614f070cb4c7e421da22df84ea1021236eb"
    },
    "ROYA": {
        "symbol": "ROYA",
        "decimals": 18,
        "name": "Royale",
        "address": "0x99415856b37be9e75c0153615c7954f9ddb97a6e"
    },
    "RPG": {
        "symbol": "RPG",
        "decimals": 18,
        "name": "Rangers Protocol Gas",
        "address": "0xc2098a8938119A52B1F7661893c0153A6CB116d5"
    },
    "RPS": {
        "symbol": "RPS",
        "decimals": 18,
        "name": "RPS League Token",
        "address": "0x267022751e06d97b9ee4e5f26cc1023670bdb349"
    },
    "RSC": {
        "symbol": "RSC",
        "decimals": 18,
        "name": "Risecoin",
        "address": "0x6e22bfc7236e95c3aef6acdbd7218bcf59a483ac"
    },
    "RULE": {
        "symbol": "RULE",
        "decimals": 18,
        "name": "RULE Token",
        "address": "0x80aa21b19c2fa7aa29a654859ffec161aa6f04a4"
    },
    "RUN": {
        "symbol": "RUN",
        "decimals": 18,
        "name": "Run Together Token",
        "address": "0xc643e83587818202e0fff5ed96d10abbc8bb48e7"
    },
    "RUNE": {
        "symbol": "RUNE",
        "decimals": 18,
        "name": "Rune",
        "address": "0xa9776b590bfc2f956711b3419910a5ec1f63153e"
    },
    "RVC": {
        "symbol": "RVC",
        "decimals": 18,
        "name": "Revenue Coin",
        "address": "0xbcbdecf8e76a5c32dba69de16985882ace1678c6"
    },
    "RVF": {
        "symbol": "RVF",
        "decimals": 18,
        "name": "RocketVaultRocketX",
        "address": "0x872a34ebb2d54af86827810eebc7b9dc6b2144aa"
    },
    "RVLNG": {
        "symbol": "RVLNG",
        "decimals": 18,
        "name": "RevolutionGames",
        "address": "0x8c11c352731fcec7ea9d16357b69d91c13743dd1"
    },
    "RVLX": {
        "symbol": "RVLX",
        "decimals": 18,
        "name": "REVIVALX",
        "address": "0xceb244a0e126f6ccbf37d631c7b102cf3e11a536"
    },
    "RXS": {
        "symbol": "RXS",
        "decimals": 18,
        "name": "Rune Shards",
        "address": "0x2098fef7eeae592038f4f3c4b008515fed0d5886"
    },
    "RXT": {
        "symbol": "RXT",
        "decimals": 18,
        "name": "RimauNangis",
        "address": "0x8d1427a32f0a4c4bf052252e68e7ff1b2ba80c01"
    },
    "RYIU": {
        "symbol": "RYIU",
        "decimals": 9,
        "name": "RYIU Token",
        "address": "0x5dc2085fe510bbaaba2119d71b09c25098caca3f"
    },
    "Ryoma": {
        "symbol": "Ryoma",
        "decimals": 18,
        "name": "Ryoma",
        "address": "0xa4c53189ec5e6b14c0cc98651f6be8a2b4a749e6"
    },
    "S4F": {
        "symbol": "S4F",
        "decimals": 18,
        "name": "S4FE",
        "address": "0x788d2780992222360f674cc12c36478870b8e6ed"
    },
    "SABA": {
        "symbol": "SABA",
        "decimals": 18,
        "name": "Saba Finance",
        "address": "0xff12afb3841b737289d1b02dfedbe4c85a8ec6e6"
    },
    "SACT": {
        "symbol": "SACT",
        "decimals": 18,
        "name": "srnArtGallery",
        "address": "0x1ba8c21c623c843cd4c60438d70e7ad50f363fbb"
    },
    "SAFE": {
        "symbol": "SAFE",
        "decimals": 18,
        "name": "SAFE(AnWang)",
        "address": "0x4d7fa587ec8e50bd0e9cd837cb4da796f47218a1"
    },
    "SAFEMARS": {
        "symbol": "SAFEMARS",
        "decimals": 9,
        "name": "SafeMars",
        "address": "0x3ad9594151886ce8538c1ff615efa2385a8c3a88"
    },
    "SAFEMOON": {
        "symbol": "SAFEMOON",
        "decimals": 9,
        "name": "SafeMoon",
        "address": "0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3"
    },
    "SAFEZONE": {
        "symbol": "SAFEZONE",
        "decimals": 18,
        "name": "SafeZone",
        "address": "0x33714356e2a3e216d055440eb24d0e23458b1b85"
    },
    "SAFUU": {
        "symbol": "SAFUU",
        "decimals": 5,
        "name": "Safuu",
        "address": "0xe5ba47fd94cb645ba4119222e34fb33f59c7cd90"
    },
    "SAITO": {
        "symbol": "SAITO",
        "decimals": 18,
        "name": "SAITO",
        "address": "0x3c6dad0475d3a1696b359dc04c99fd401be134da"
    },
    "SAKAI": {
        "symbol": "SAKAI",
        "decimals": 18,
        "name": "Sakai Vault",
        "address": "0x43b35e89d15b91162dea1c51133c4c93bdd1c4af"
    },
    "SAKE": {
        "symbol": "SAKE",
        "decimals": 18,
        "name": "SakeToken",
        "address": "0x8bd778b12b15416359a227f0533ce2d91844e1ed"
    },
    "SALE": {
        "symbol": "SALE",
        "decimals": 18,
        "name": "DxSale.Network",
        "address": "0x04f73a09e2eb410205be256054794fb452f0d245"
    },
    "SANTOS": {
        "symbol": "SANTOS",
        "decimals": 8,
        "name": "FC Santos Fan Token",
        "address": "0xa64455a4553c9034236734faddaddbb64ace4cc7"
    },
    "SATA": {
        "symbol": "SATA",
        "decimals": 18,
        "name": "Signata",
        "address": "0x6b1c8765c7eff0b60706b0ae489eb9bb9667465a"
    },
    "SavantAI": {
        "symbol": "SavantAI",
        "decimals": 9,
        "name": "Savant AI",
        "address": "0x8ae14ce43f71201bb79babd00cc8d00a7fadb3bd"
    },
    "SBCC": {
        "symbol": "SBCC",
        "decimals": 18,
        "name": "Smart Block Chain City",
        "address": "0x6e02be885fca1138038420fddd4b41c59a8cea6d"
    },
    "SBG": {
        "symbol": "SBG",
        "decimals": 9,
        "name": "SB GROUP",
        "address": "0x5e95a952a7f79f978585afd54a053af0f51372fa"
    },
    "sBTX": {
        "symbol": "sBTX",
        "decimals": 8,
        "name": "Swapped Bitcore",
        "address": "0x000000089fb24237da101020ff8e2afd14624687"
    },
    "SCAR": {
        "symbol": "SCAR",
        "decimals": 18,
        "name": "VELHALLA.io",
        "address": "0x8d9fb713587174ee97e91866050c383b5cee6209"
    },
    "SCIX": {
        "symbol": "SCIX",
        "decimals": 18,
        "name": "Scientix",
        "address": "0x2cfc48cdfea0678137854f010b5390c5144c0aa5"
    },
    "SCK": {
        "symbol": "SCK",
        "decimals": 18,
        "name": "Space Corsair Key",
        "address": "0x227a3ef4d41d0215123f3197faa087bf71d2236a"
    },
    "SCLP": {
        "symbol": "SCLP",
        "decimals": 18,
        "name": "Scallop",
        "address": "0xf2c96e402c9199682d5ded26d3771c6b192c01af"
    },
    "SCOTTY": {
        "symbol": "SCOTTY",
        "decimals": 18,
        "name": "Scotty Beam",
        "address": "0x000351d035d8bbf2aa3131ebfecd66fb21836f6c"
    },
    "SCRL": {
        "symbol": "SCRL",
        "decimals": 18,
        "name": "Wizarre Scroll",
        "address": "0x52c1751c89fc913ed274d72e8d56dce4ee44a5cf"
    },
    "SCT": {
        "symbol": "SCT",
        "decimals": 18,
        "name": "SuperCells Token",
        "address": "0x405e7454e71aefe8897438adc08e3f3e6d49dfc1"
    },
    "SD": {
        "symbol": "SD",
        "decimals": 18,
        "name": "Stader",
        "address": "0x3bc5ac0dfdc871b365d159f728dd1b9a0b5481e8"
    },
    "SDAO": {
        "symbol": "SDAO",
        "decimals": 18,
        "name": "Singularity Dao",
        "address": "0x90ed8f1dc86388f14b64ba8fb4bbd23099f18240"
    },
    "SDF": {
        "symbol": "SDF",
        "decimals": 9,
        "name": "ShadowFi",
        "address": "0x91d5546564a31ce5f0f4f3302c55f6921e1916af"
    },
    "SDT": {
        "symbol": "SDT",
        "decimals": 18,
        "name": "Stabledoc Token",
        "address": "0x543c7ebb52d56985f63f246a5b3558aff79037d7"
    },
    "SEA": {
        "symbol": "SEA",
        "decimals": 18,
        "name": "SharkShakeSea",
        "address": "0x26193c7fa4354ae49ec53ea2cebc513dc39a10aa"
    },
    "SEEDx": {
        "symbol": "SEEDx",
        "decimals": 18,
        "name": "SEEDx",
        "address": "0x0cbfdea4f45a486cc7db53cb6e37b312a137c605"
    },
    "SEG": {
        "symbol": "SEG",
        "decimals": 18,
        "name": "Solar Energy",
        "address": "0xec126e20e7cb114dd3ba356100eaca2cc2921322"
    },
    "SELLC": {
        "symbol": "SELLC",
        "decimals": 18,
        "name": "SellToken",
        "address": "0xa645995e9801f2ca6e2361edf4c2a138362bade4"
    },
    "SENSI": {
        "symbol": "SENSI",
        "decimals": 9,
        "name": "Sensi",
        "address": "0x63e77cf206801782239d4f126cfa22b517fb4edb"
    },
    "SEON": {
        "symbol": "SEON",
        "decimals": 18,
        "name": "SeedOn",
        "address": "0x7672843c25c5ba11191da8da40c0881d7e77d9e0"
    },
    "SEOR": {
        "symbol": "SEOR",
        "decimals": 18,
        "name": "SEOR Network",
        "address": "0x800a25741a414ea6e6e2b382435081a479a8cc3c"
    },
    "SFEX": {
        "symbol": "SFEX",
        "decimals": 18,
        "name": "SafeX",
        "address": "0x5392ff4a9bd006dc272c1855af6640e17cc5ec0b"
    },
    "SFIL": {
        "symbol": "SFIL",
        "decimals": 8,
        "name": "SFIL",
        "address": "0x965b85d4674f64422c4898c8f8083187f02b32c0"
    },
    "SFM": {
        "symbol": "SFM",
        "decimals": 9,
        "name": "SafeMoon",
        "address": "0x42981d0bfbaf196529376ee702f2a9eb9092fcb5"
    },
    "SFP": {
        "symbol": "SFP",
        "decimals": 18,
        "name": "SafePal Token",
        "address": "0xd41fdb03ba84762dd66a0af1a6c8540ff1ba5dfb"
    },
    "sfrxETH": {
        "symbol": "sfrxETH",
        "decimals": 18,
        "name": "Staked Frax Ether",
        "address": "0x3cd55356433c89e50dc51ab07ee0fa0a95623d53"
    },
    "SFTY": {
        "symbol": "SFTY",
        "decimals": 18,
        "name": "Stella Fantasy Token",
        "address": "0xe9d6d6d7cde5c7d45927f8c37460d932e612c902"
    },
    "SFUEL": {
        "symbol": "SFUEL",
        "decimals": 18,
        "name": "SparkPoint Fuel",
        "address": "0x37ac4d6140e54304d77437a5c11924f61a2d976f"
    },
    "SFUND": {
        "symbol": "SFUND",
        "decimals": 18,
        "name": "SeedifyFund",
        "address": "0x477bc8d23c634c154061869478bce96be6045d12"
    },
    "SGS": {
        "symbol": "SGS",
        "decimals": 18,
        "name": "SING GAME SHOW",
        "address": "0xa6cba90f6246aad9b4f3dcd29918821921a5c1ff"
    },
    "SHA": {
        "symbol": "SHA",
        "decimals": 18,
        "name": "Safe Haven Token",
        "address": "0x40fed5691e547885cabd7a2990de719dcc8497fc"
    },
    "SHAKE": {
        "symbol": "SHAKE",
        "decimals": 18,
        "name": "SHAKE token by SpaceSwap v2",
        "address": "0xba8a6ef5f15ed18e7184f44a775060a6bf91d8d0"
    },
    "SHAUN": {
        "symbol": "SHAUN",
        "decimals": 9,
        "name": "SHAUN INU",
        "address": "0x05f816b53a4c7b6b3bfbe1f759da7fe188689c5b"
    },
    "SHEESHA": {
        "symbol": "SHEESHA",
        "decimals": 18,
        "name": "Sheesha Finance",
        "address": "0x232fb065d9d24c34708eedbf03724f2e95abe768"
    },
    "SHG": {
        "symbol": "SHG",
        "decimals": 18,
        "name": "Shib Generating",
        "address": "0x33af7644b1f60c8e8d62689b19d60a5d132164fc"
    },
    "SHI": {
        "symbol": "SHI",
        "decimals": 18,
        "name": "Shirtum",
        "address": "0x7269d98af4aa705e0b1a5d8512fadb4d45817d5a"
    },
    "SHIB": {
        "symbol": "SHIB",
        "decimals": 18,
        "name": "SHIBA INU",
        "address": "0x2859e4544c4bb03966803b044a93563bd2d0dd4d"
    },
    "SHIBA": {
        "symbol": "SHIBA",
        "decimals": 18,
        "name": "BitShiba",
        "address": "0xb84cbbf09b3ed388a45cd875ebba41a20365e6e7"
    },
    "SHIBARMY": {
        "symbol": "SHIBARMY",
        "decimals": 18,
        "name": "Shib Army",
        "address": "0x940230b6b7ef1979a28f32196a8e3439c645ba49"
    },
    "SHIBCAT": {
        "symbol": "SHIBCAT",
        "decimals": 18,
        "name": "SHIBCAT",
        "address": "0xd5ff3786ce4a75156d27ab026eb04c9ed53b365f"
    },
    "SHIBELON": {
        "symbol": "SHIBELON",
        "decimals": 4,
        "name": "ShibElon",
        "address": "0xc183062db25fc96325485ea369c979ce881ac0ea"
    },
    "SHIBLITE": {
        "symbol": "SHIBLITE",
        "decimals": 18,
        "name": "Shiba Lite",
        "address": "0x76ef2a25b1ea6eb5dc4d079ae82c767d55b0a99e"
    },
    "SHIDO": {
        "symbol": "SHIDO",
        "decimals": 9,
        "name": "Shido Inu",
        "address": "0x733af324146dcfe743515d8d77dc25140a07f9e0"
    },
    "SHIELD": {
        "symbol": "SHIELD",
        "decimals": 18,
        "name": "Shield Protocol",
        "address": "0x00f97c17f4dc4f3bfd2dd9ce5e67f3a339a8a261"
    },
    "SHIELDNET": {
        "symbol": "SHIELDNET",
        "decimals": 18,
        "name": "Shield Network",
        "address": "0xf2e00684457de1a3c87361bc4bfe2de92342306c"
    },
    "SHILL": {
        "symbol": "SHILL",
        "decimals": 18,
        "name": "Shill",
        "address": "0xfb9c339b4bace4fe63ccc1dd9a3c3c531441d5fe"
    },
    "SHINJA": {
        "symbol": "SHINJA",
        "decimals": 9,
        "name": "Shibnobi",
        "address": "0x7dac25b1a665e1c70f25f1fc37d88c99274984ed"
    },
    "SHINO": {
        "symbol": "SHINO",
        "decimals": 9,
        "name": "ShinobiVerse",
        "address": "0x1532c74250de406a83fec3acc8030da4159e4cbb"
    },
    "SHINU": {
        "symbol": "SHINU",
        "decimals": 18,
        "name": "Sheikh Inu",
        "address": "0xe5b5d4bea7468b4994fa676949308a79497aa24c"
    },
    "SHL": {
        "symbol": "SHL",
        "decimals": 18,
        "name": "shelling",
        "address": "0xbb689057fe1c4bfc573a54c0679ae1a7a1982f26"
    },
    "SHOE": {
        "symbol": "SHOE",
        "decimals": 18,
        "name": "ShoeFy",
        "address": "0xc0f42b31d154234a0a3ebe7ec52c662101c1d9bc"
    },
    "SHOOTER": {
        "symbol": "SHOOTER",
        "decimals": 18,
        "name": "SHOOTER",
        "address": "0xbaf928369eb10c71461cda6972f35eede6d2f5fd"
    },
    "SILVA": {
        "symbol": "SILVA",
        "decimals": 9,
        "name": "Silva Token",
        "address": "0x68b5edb385b59e30a7a7db1e681a449e94df0213"
    },
    "SIMPSONSINU": {
        "symbol": "SIMPSONSINU",
        "decimals": 9,
        "name": "The Simpsons Inu",
        "address": "0x5cc97dab7bc2c01556fbe3d06a09b8c559dff7d5"
    },
    "SIN": {
        "symbol": "SIN",
        "decimals": 18,
        "name": "SinCity Token",
        "address": "0x6397de0f9aedc0f7a8fa8b438dde883b9c201010"
    },
    "SINGH": {
        "symbol": "SINGH",
        "decimals": 18,
        "name": "SinghCoin",
        "address": "0x867b96b33b2c13cc8cb78a9aa95420c6cd42c4c6"
    },
    "SIS": {
        "symbol": "SIS",
        "decimals": 18,
        "name": "Symbiosis",
        "address": "0xf98b660adf2ed7d9d9d9daacc2fb0cace4f21835"
    },
    "SK": {
        "symbol": "SK",
        "decimals": 18,
        "name": "SideKick Token",
        "address": "0x5755e18d86c8a6d7a6e25296782cb84661e6c106"
    },
    "SKILL": {
        "symbol": "SKILL",
        "decimals": 18,
        "name": "CryptoBlades Skill Token",
        "address": "0x154a9f9cbd3449ad22fdae23044319d6ef2a1fab"
    },
    "SLEEPEE": {
        "symbol": "SLEEPEE",
        "decimals": 18,
        "name": "Sleep Future",
        "address": "0x80cd73badb406ea36b9a7cdeb8df06aefa7e12d9"
    },
    "SLG": {
        "symbol": "SLG",
        "decimals": 18,
        "name": "Land Of Conquest SLG",
        "address": "0x2348b010fa9c0ce30bb042d54c298a3411361a01"
    },
    "SLGO": {
        "symbol": "SLGO",
        "decimals": 18,
        "name": "Solalgo",
        "address": "0x940580db429da7fa8662d66f7a4d312443f09f52"
    },
    "SLM": {
        "symbol": "SLM",
        "decimals": 18,
        "name": "SoliMax",
        "address": "0xeba457b55fb145ff4451bc50fb6c373e5caa493f"
    },
    "SLP": {
        "symbol": "SLP",
        "decimals": 18,
        "name": "Smooth Love Potion",
        "address": "0x070a08beef8d36734dd67a491202ff35a6a16d97"
    },
    "SM96": {
        "symbol": "SM96",
        "decimals": 9,
        "name": "Safemoon 1996",
        "address": "0x4a76a1eaa365c10bd9b895acab5760d52ff2f7c9"
    },
    "SMARS": {
        "symbol": "SMARS",
        "decimals": 9,
        "name": "SafeMars",
        "address": "0xc0366a104b429f0806bfa98d0008daa9555b2bed"
    },
    "SMBR": {
        "symbol": "SMBR",
        "decimals": 9,
        "name": "SOMBRA",
        "address": "0x8ad8e9b85787ddd0d31b32ecf655e93bfc0747ef"
    },
    "SMCW": {
        "symbol": "SMCW",
        "decimals": 18,
        "name": "Space Crown",
        "address": "0xb2ea51baa12c461327d12a2069d47b30e680b69d"
    },
    "SMTF": {
        "symbol": "SMTF",
        "decimals": 18,
        "name": "SmartFi",
        "address": "0x11fd9ed04f1eb43ef9df6425a6990609f2468895"
    },
    "SMTY": {
        "symbol": "SMTY",
        "decimals": 18,
        "name": "SMTYToken",
        "address": "0xbf776e4fca664d791c4ee3a71e2722990e003283"
    },
    "SMURF": {
        "symbol": "SMURF",
        "decimals": 9,
        "name": "Smurfs INU",
        "address": "0x75afa9915b2210cd6329e820af0365e932bc1dd5"
    },
    "SN": {
        "symbol": "SN",
        "decimals": 18,
        "name": "SpaceN",
        "address": "0x939dd9e433552e325d78c33a16ef4cd8004d2f9c"
    },
    "SNFTS": {
        "symbol": "SNFTS",
        "decimals": 18,
        "name": "Seedify NFT Space",
        "address": "0x6f51a1674befdd77f7ab1246b83adb9f13613762"
    },
    "SNM": {
        "symbol": "SNM",
        "decimals": 18,
        "name": "SONM",
        "address": "0x46d0dac0926fa16707042cadc23f1eb4141fe86b"
    },
    "SNN": {
        "symbol": "SNN",
        "decimals": 3,
        "name": "SeChain",
        "address": "0xa997e5aaae60987eb0b59a336dce6b158b113100"
    },
    "SNP": {
        "symbol": "SNP",
        "decimals": 18,
        "name": "Synapse Network",
        "address": "0x6911f552842236bd9e8ea8ddbb3fb414e2c5fa9d"
    },
    "SNX": {
        "symbol": "SNX",
        "decimals": 18,
        "name": "Synthetix Network Token",
        "address": "0x9ac983826058b8a9c7aa1c9171441191232e8404"
    },
    "SocialAI": {
        "symbol": "SocialAI",
        "decimals": 18,
        "name": "Social AI",
        "address": "0x6f0ad7c4044a3474ccb29caefa182549dc70e802"
    },
    "SOFI": {
        "symbol": "SOFI",
        "decimals": 18,
        "name": "Rai.Finance",
        "address": "0x1a28ed8472f644e8898a169a644503b779748d6e"
    },
    "SOKU": {
        "symbol": "SOKU",
        "decimals": 18,
        "name": "Soku",
        "address": "0x0e4b5ea0259eb3d66e6fcb7cc8785817f8490a53"
    },
    "SOL": {
        "symbol": "SOL",
        "decimals": 18,
        "name": "SOLANA",
        "address": "0x570a5d26f7765ecb712c0924e4de545b89fd43df"
    },
    "Solarix": {
        "symbol": "Solarix",
        "decimals": 6,
        "name": "Solarix",
        "address": "0xfdce54744801c9eb88d8445673ad267f8d43a9ee"
    },
    "SOM": {
        "symbol": "SOM",
        "decimals": 9,
        "name": "SOULS OF META",
        "address": "0x31c573d1a50a745b01862edaf2ae72017cea036a"
    },
    "SON": {
        "symbol": "SON",
        "decimals": 18,
        "name": "Souni Token",
        "address": "0x3b0e967ce7712ec68131a809db4f78ce9490e779"
    },
    "SONIC": {
        "symbol": "SONIC",
        "decimals": 9,
        "name": "Sonic Inu",
        "address": "0x066cda0cca84e9c6ed0a4ecb92aa036a9582544b"
    },
    "SOT": {
        "symbol": "SOT",
        "decimals": 18,
        "name": "SOCCER CRYPTO",
        "address": "0xde1a0f6c7078c5da0a6236eeb04261f4699905c5"
    },
    "SOUL": {
        "symbol": "SOUL",
        "decimals": 8,
        "name": "Phantasma Stake",
        "address": "0x298eff8af1ecebbb2c034eaa3b9a5d0cc56c59cd"
    },
    "SOURCE": {
        "symbol": "SOURCE",
        "decimals": 18,
        "name": "Source",
        "address": "0xea136fc555e695ba96d22e10b7e2151c4c6b2a20"
    },
    "SOWL": {
        "symbol": "SOWL",
        "decimals": 9,
        "name": "SOWL Token",
        "address": "0x73fc38b104b45da06f4b68782ab75b45d0b225b7"
    },
    "SpacePi": {
        "symbol": "SpacePi",
        "decimals": 9,
        "name": "SpacePi Token",
        "address": "0x69b14e8d3cebfdd8196bfe530954a0c226e5008e"
    },
    "SPACES": {
        "symbol": "SPACES",
        "decimals": 9,
        "name": "AstroSpaces.io",
        "address": "0x156df0dd6300c73ac692d805720967cf4464776e"
    },
    "SPARTA": {
        "symbol": "SPARTA",
        "decimals": 18,
        "name": "Spartan Protocol Token V2",
        "address": "0x3910db0600ea925f63c36ddb1351ab6e2c6eb102"
    },
    "SPAY": {
        "symbol": "SPAY",
        "decimals": 18,
        "name": "SpaceY Token",
        "address": "0x13a637026df26f846d55acc52775377717345c06"
    },
    "SPC": {
        "symbol": "SPC",
        "decimals": 18,
        "name": "Storepay Coin",
        "address": "0x1eaffd6b9ef0f45d663f3fbf402226c98609600e"
    },
    "SPE": {
        "symbol": "SPE",
        "decimals": 9,
        "name": "SavePlanetEarth",
        "address": "0x4ac81e3631dcda62109e3117c4cae7bf70bbbbd2"
    },
    "SPELL": {
        "symbol": "SPELL",
        "decimals": 18,
        "name": "Spell Token",
        "address": "0x9fe28d11ce29e340b7124c493f59607cbab9ce48"
    },
    "SPELLFIRE": {
        "symbol": "SPELLFIRE",
        "decimals": 18,
        "name": "SPELLFIRE Token [via ChainPort.io]",
        "address": "0xd6f28f15a5cafc8d29556393c08177124b88de0d"
    },
    "spex": {
        "symbol": "spex",
        "decimals": 18,
        "name": "Speciex",
        "address": "0xf1b6460e7fa76e7afddfe20740c260b0ec6807a8"
    },
    "SPG": {
        "symbol": "SPG",
        "decimals": 18,
        "name": "Space Genesis",
        "address": "0x0ecaf010fc192e2d5cbeb4dfb1fee20fbd733aa1"
    },
    "SPHYNX": {
        "symbol": "SPHYNX",
        "decimals": 18,
        "name": "Sphynx Labs",
        "address": "0xa776f5b86cc520861f55a261515264e3bd86e72e"
    },
    "SPIN": {
        "symbol": "SPIN",
        "decimals": 18,
        "name": "Spintop",
        "address": "0x6aa217312960a21adbde1478dc8cbcf828110a67"
    },
    "SPKY": {
        "symbol": "SPKY",
        "decimals": 18,
        "name": "SpookyShiba",
        "address": "0x9c2b1b3780a8b36b695f0b2781668664ac1bf25a"
    },
    "SPO": {
        "symbol": "SPO",
        "decimals": 18,
        "name": "Spores Token",
        "address": "0x8357c604c5533fa0053beaaa1494da552cea38f7"
    },
    "SPORE": {
        "symbol": "SPORE",
        "decimals": 9,
        "name": "SporeFinance",
        "address": "0x33a3d962955a3862c8093d1273344719f03ca17c"
    },
    "Sports-AI": {
        "symbol": "Sports-AI",
        "decimals": 18,
        "name": "Sports Artificial",
        "address": "0xe1bb77c8e012c1514373a40cfbb8645293075125"
    },
    "SPRT": {
        "symbol": "SPRT",
        "decimals": 18,
        "name": "Sportium Token",
        "address": "0x56156fb7860d7eb0b4b1a5356c5354b295194a45"
    },
    "SPS": {
        "symbol": "SPS",
        "decimals": 18,
        "name": "Splintershards",
        "address": "0x1633b7157e7638c4d6593436111bf125ee74703f"
    },
    "SPXC": {
        "symbol": "SPXC",
        "decimals": 9,
        "name": "SpaceXCoin",
        "address": "0x3d4fe86c53f7e87b317a46942db2806613683e28"
    },
    "SPY": {
        "symbol": "SPY",
        "decimals": 0,
        "name": "Smarty Pay",
        "address": "0x17fd3caa66502c6f1cbd5600d8448f3af8f2aba1"
    },
    "SQF": {
        "symbol": "SQF",
        "decimals": 9,
        "name": "SquadFund",
        "address": "0x3e89a5e7cf9dfcff5a9aedf19ab6246c6b506582"
    },
    "SQUA": {
        "symbol": "SQUA",
        "decimals": 18,
        "name": "Square Token",
        "address": "0xb82beb6ee0063abd5fc8e544c852237aa62cbb14"
    },
    "SQUAD": {
        "symbol": "SQUAD",
        "decimals": 18,
        "name": "SQUAD",
        "address": "0x724a32dfff9769a0a0e1f0515c0012d1fb14c3bd"
    },
    "SQUID": {
        "symbol": "SQUID",
        "decimals": 18,
        "name": "Squid Game",
        "address": "0x87230146e138d3f296a9a77e497a2a83012e9bc5"
    },
    "SquidGrow": {
        "symbol": "SquidGrow",
        "decimals": 19,
        "name": "SquidGrow",
        "address": "0x88479186bac914e4313389a64881f5ed0153c765"
    },
    "SRBP": {
        "symbol": "SRBP",
        "decimals": 18,
        "name": "Super Rare Ball Portion",
        "address": "0xd0e98827d675a3231c2ea69d1f3ed12270df1435"
    },
    "SRG": {
        "symbol": "SRG",
        "decimals": 18,
        "name": "STREET RUNNER",
        "address": "0x722f41f6511ff7cda73a1cb0a9ea2f731738c4a0"
    },
    "SRP": {
        "symbol": "SRP",
        "decimals": 18,
        "name": "Starpunk",
        "address": "0xcb2b25e783a414f0d20a65afa741c51b1ad84c49"
    },
    "SSS": {
        "symbol": "SSS",
        "decimals": 18,
        "name": "StarSharks",
        "address": "0xc3028fbc1742a16a5d69de1b334cbce28f5d7eb3"
    },
    "SSTX": {
        "symbol": "SSTX",
        "decimals": 7,
        "name": "Silver Stonks",
        "address": "0x5396734569e26101677eb39c89413f7fa7d8006f"
    },
    "ST": {
        "symbol": "ST",
        "decimals": 18,
        "name": "Sacred Tails",
        "address": "0x1e4f2ab406aa9764ff05a9a8c8bf6b1c8b6f531f"
    },
    "STA": {
        "symbol": "STA",
        "decimals": 8,
        "name": "STA TOKEN",
        "address": "0x4d1e90ab966ae26c778b2f9f365aa40abb13f53c"
    },
    "STACK": {
        "symbol": "STACK",
        "decimals": 18,
        "name": "StackOS",
        "address": "0x6855f7bb6287f94ddcc8915e37e73a3c9fee5cf3"
    },
    "STAI": {
        "symbol": "STAI",
        "decimals": 18,
        "name": "StereoAI",
        "address": "0xebc148d40313be9c9f214d3beb9f2ddebec0ec52"
    },
    "STARLY": {
        "symbol": "STARLY",
        "decimals": 8,
        "name": "StarlyToken",
        "address": "0xb0a480e2fa5af51c733a0af9fcb4de62bc48c38b"
    },
    "STARS": {
        "symbol": "STARS",
        "decimals": 18,
        "name": "Mogul Stars",
        "address": "0xbd83010eb60f12112908774998f65761cf9f6f9a"
    },
    "STARSHIP": {
        "symbol": "STARSHIP",
        "decimals": 9,
        "name": "StarShip",
        "address": "0x52419258e3fa44deac7e670eadd4c892b480a805"
    },
    "START": {
        "symbol": "START",
        "decimals": 18,
        "name": "BSCstarter",
        "address": "0x31d0a7ada4d4c131eb612db48861211f63e57610"
    },
    "STAX": {
        "symbol": "STAX",
        "decimals": 18,
        "name": "StableX Token",
        "address": "0x0da6ed8b13214ff28e9ca979dd37439e8a88f6c4"
    },
    "STBU": {
        "symbol": "STBU",
        "decimals": 18,
        "name": "Stobox Token v.2",
        "address": "0xb0c4080a8fa7afa11a09473f3be14d44af3f8743"
    },
    "STC": {
        "symbol": "STC",
        "decimals": 18,
        "name": "Satoshi Island Coin",
        "address": "0x340724464cf51a551106cc6657606ee7d87b28b9"
    },
    "STEMX": {
        "symbol": "STEMX",
        "decimals": 18,
        "name": "STEMX",
        "address": "0x26734add0650719ea29087fe5cc0aab81b4f237d"
    },
    "STEP": {
        "symbol": "STEP",
        "decimals": 18,
        "name": "Step",
        "address": "0x465707181acba42ed01268a33f0507e320a154bd"
    },
    "STEPG": {
        "symbol": "STEPG",
        "decimals": 18,
        "name": "StepG Token",
        "address": "0x5e6d3bb496301ecdfa34fa1ed2d3bada250f0409"
    },
    "STG": {
        "symbol": "STG",
        "decimals": 18,
        "name": "StargateToken",
        "address": "0xb0d502e938ed5f4df2e681fe6e419ff29631d62b"
    },
    "STI": {
        "symbol": "STI",
        "decimals": 10,
        "name": "Seek Tiger",
        "address": "0x4f5f7a7dca8ba0a7983381d23dfc5eaf4be9c79a"
    },
    "stkBNB": {
        "symbol": "stkBNB",
        "decimals": 18,
        "name": "Staked BNB",
        "address": "0xc2e9d07f66a89c44062459a47a0d2dc038e4fb16"
    },
    "STKK": {
        "symbol": "STKK",
        "decimals": 4,
        "name": "Streakk",
        "address": "0x41fe2441c9eeab2158e29185d128ebab82aa8198"
    },
    "STM": {
        "symbol": "STM",
        "decimals": 18,
        "name": "Streamity",
        "address": "0x90df11a8cce420675e73922419e3f4f3fe13cccb"
    },
    "STN": {
        "symbol": "STN",
        "decimals": 18,
        "name": "Stretch Token",
        "address": "0x4bc99635f7cd965069ae7142d66784ea518995e3"
    },
    "STORE": {
        "symbol": "STORE",
        "decimals": 18,
        "name": "Bit Store Coin",
        "address": "0x65d9033cff96782394dab5dbef17fa771bbe1732"
    },
    "STORY": {
        "symbol": "STORY",
        "decimals": 18,
        "name": "Story",
        "address": "0x85ee8e3e0068edeeee960979958d7f61416a9d84"
    },
    "STRELKA AI": {
        "symbol": "STRELKA AI",
        "decimals": 18,
        "name": "Strelka AI",
        "address": "0xab3bcb0e39b505de2a3545ce721e117de75d1e1d"
    },
    "STRI": {
        "symbol": "STRI",
        "decimals": 18,
        "name": "STRITE Token",
        "address": "0x9b93c29595dd603f75854eba3c5f4ee078ee4454"
    },
    "STRIP": {
        "symbol": "STRIP",
        "decimals": 18,
        "name": "Strip Finance",
        "address": "0x0fe178b9a471b3698cb6fcb4625df9a756a2c55c"
    },
    "STRM": {
        "symbol": "STRM",
        "decimals": 18,
        "name": "Stream",
        "address": "0xc598275452fa319d75ee5f176fd3b8384925b425"
    },
    "STRX": {
        "symbol": "STRX",
        "decimals": 18,
        "name": "StrikeX",
        "address": "0xd6fdde76b8c1c45b33790cc8751d5b88984c44ec"
    },
    "STYL": {
        "symbol": "STYL",
        "decimals": 18,
        "name": "Stylike Governance",
        "address": "0xd1e756a5868fcf56a01befc41a8163a6b4f67f43"
    },
    "STZ": {
        "symbol": "STZ",
        "decimals": 18,
        "name": "99Starz",
        "address": "0x7fe378c5e0b5c32af2ecc8829bedf02245a0e4ef"
    },
    "STZU": {
        "symbol": "STZU",
        "decimals": 8,
        "name": "Shihtzu Exchange Token",
        "address": "0x31801b15215c021e7988fa0bc37dcfa6a303bd00"
    },
    "SUGAR": {
        "symbol": "SUGAR",
        "decimals": 18,
        "name": "SugarYield",
        "address": "0x57528b45134f09f2e0069334a36a7e14af74745f"
    },
    "SUI": {
        "symbol": "SUI",
        "decimals": 9,
        "name": "Salmonation",
        "address": "0x4841181ae4079072ebe83a29b718388a387169e3"
    },
    "SUPE": {
        "symbol": "SUPE",
        "decimals": 18,
        "name": "Supe Token",
        "address": "0xb972c4027818223bb7b9399b3ca3ca58186e1590"
    },
    "SUPER": {
        "symbol": "SUPER",
        "decimals": 18,
        "name": "SUPER-ERC20",
        "address": "0x51ba0b044d96c3abfca52b64d733603ccc4f0d4d"
    },
    "SURE": {
        "symbol": "SURE",
        "decimals": 18,
        "name": "inSure",
        "address": "0x9b17baadf0f21f03e35249e0e59723f34994f806"
    },
    "SUSHI": {
        "symbol": "SUSHI",
        "decimals": 18,
        "name": "SushiToken",
        "address": "0x947950bcc74888a40ffa2593c5798f11fc9124c4"
    },
    "Suter": {
        "symbol": "Suter",
        "decimals": 18,
        "name": "Suterusu",
        "address": "0x4cfbbdfbd5bf0814472ff35c72717bd095ada055"
    },
    "SWAMP": {
        "symbol": "SWAMP",
        "decimals": 18,
        "name": "Swampy",
        "address": "0xc5a49b4cbe004b6fd55b30ba1de6ac360ff9765d"
    },
    "SWAP": {
        "symbol": "SWAP",
        "decimals": 18,
        "name": "SafeSwap Token",
        "address": "0xe56a473043eaab7947c0a2408cea623074500ee3"
    },
    "SWAPZ": {
        "symbol": "SWAPZ",
        "decimals": 18,
        "name": "SWAPZ.app",
        "address": "0xd522a1dce1ca4b138dda042a78672307eb124cc2"
    },
    "SWASH": {
        "symbol": "SWASH",
        "decimals": 18,
        "name": "Swash Token",
        "address": "0x41065e3428188ba6eb27fbdde8526ae3af8e3830"
    },
    "SWEEP": {
        "symbol": "SWEEP",
        "decimals": 9,
        "name": "Sweeptoken",
        "address": "0x09c704c1eb9245af48f058878e72129557a10f04"
    },
    "SWFTC": {
        "symbol": "SWFTC",
        "decimals": 18,
        "name": "SwftCoin",
        "address": "0xe64e30276c2f826febd3784958d6da7b55dfbad3"
    },
    "SWG": {
        "symbol": "SWG",
        "decimals": 18,
        "name": "SWGToken",
        "address": "0xe792f64c582698b8572aaf765bdc426ac3aefb6b"
    },
    "SWI": {
        "symbol": "SWI",
        "decimals": 4,
        "name": "Swinca Coin",
        "address": "0x81372c18c87f6d2fe91f416d7c8a109cea48c332"
    },
    "SWINGBY": {
        "symbol": "SWINGBY",
        "decimals": 18,
        "name": "SWINGBY token",
        "address": "0x71de20e0c4616e7fcbfdd3f875d568492cbe4739"
    },
    "SwirlX": {
        "symbol": "SwirlX",
        "decimals": 18,
        "name": "SwirlToken",
        "address": "0x7dc3577681038522d796335e73f2efeccca1878d"
    },
    "SWTH": {
        "symbol": "SWTH",
        "decimals": 8,
        "name": "Switcheo Token",
        "address": "0x250b211ee44459dad5cd3bca803dd6a7ecb5d46c"
    },
    "SWU": {
        "symbol": "SWU",
        "decimals": 18,
        "name": "SMART WORLD UNION",
        "address": "0x958cc5ac2efa569cd9ad9b9b88245e1f038b02be"
    },
    "SXP": {
        "symbol": "SXP",
        "decimals": 18,
        "name": "Swipe",
        "address": "0x47bead2563dcbf3bf2c9407fea4dc236faba485a"
    },
    "SYL": {
        "symbol": "SYL",
        "decimals": 6,
        "name": "SYL",
        "address": "0x7e52a123ed6db6ac872a875552935fbbd2544c86"
    },
    "SYN": {
        "symbol": "SYN",
        "decimals": 18,
        "name": "Synapse",
        "address": "0xa4080f1778e69467e905b8d6f72f6e441f9e9484"
    },
    "SynapticAI": {
        "symbol": "SynapticAI",
        "decimals": 18,
        "name": "Synaptic AI",
        "address": "0x0a94ea47de185d6376db4cad70123ec8de4f2841"
    },
    "SYNOPTI": {
        "symbol": "SYNOPTI",
        "decimals": 18,
        "name": "Synopti",
        "address": "0x840590a04dd494c980d70a380e10bec739432a8a"
    },
    "T23": {
        "symbol": "T23",
        "decimals": 18,
        "name": "2023",
        "address": "0x897f2be515373cf1f899d864b5be2bd5efd4e653"
    },
    "TABOO": {
        "symbol": "TABOO",
        "decimals": 9,
        "name": "TABOO TOKEN",
        "address": "0x9abdba20edfba06b782126b4d8d72a5853918fd0"
    },
    "TAG": {
        "symbol": "TAG",
        "decimals": 18,
        "name": "TagCoin - TagProtocol Native Coin",
        "address": "0x717fb7b6d0c3d7f1421cc60260412558283a6ae5"
    },
    "TANK": {
        "symbol": "TANK",
        "decimals": 18,
        "name": "CryptoTanks",
        "address": "0x4444a19c8bb86e9bdbc023709a363bbce91af33e"
    },
    "TAO": {
        "symbol": "TAO",
        "decimals": 18,
        "name": "Fusotao Protocol",
        "address": "0x3cb1a1fac70f13a6a63914f2e9ad923cdb5ece3d"
    },
    "TAP": {
        "symbol": "TAP",
        "decimals": 18,
        "name": "TAP Coin",
        "address": "0x35bedbf9291b22218a0da863170dcc9329ef2563"
    },
    "TARO": {
        "symbol": "TARO",
        "decimals": 18,
        "name": "Taroverse Token",
        "address": "0x424aa711301c82252eccaccf01301ad7ad7b5d40"
    },
    "TAROT": {
        "symbol": "TAROT",
        "decimals": 18,
        "name": "Tarot",
        "address": "0xa8cd6e4bf45724d3ac27f9e31e47ba4e399a7b52"
    },
    "TAUM": {
        "symbol": "TAUM",
        "decimals": 18,
        "name": "Orbitau Taureum",
        "address": "0x02e22eb7f6e73ef313dd71248cd164b1bdc5aadd"
    },
    "TAUR": {
        "symbol": "TAUR",
        "decimals": 18,
        "name": "Marnotaur",
        "address": "0x19b99162adaab85134e781ac0048c275c31b205a"
    },
    "TBAC": {
        "symbol": "TBAC",
        "decimals": 8,
        "name": "BlockAura BEP",
        "address": "0x2326c7395d02a8c89a9d7a0b0c1cf159d49ce51c"
    },
    "TBC": {
        "symbol": "TBC",
        "decimals": 18,
        "name": "TeraBlock Token",
        "address": "0x9798df2f5d213a872c787bd03b2b91f54d0d04a1"
    },
    "TBCC": {
        "symbol": "TBCC",
        "decimals": 18,
        "name": "TBCC v2",
        "address": "0xf29480344d8e21efeab7fde39f8d8299056a7fea"
    },
    "TBS": {
        "symbol": "TBS",
        "decimals": 18,
        "name": "TLabs Token",
        "address": "0x45fffed8d9651fe9ea0321fcc9b15ee5e052a208"
    },
    "TC": {
        "symbol": "TC",
        "decimals": 4,
        "name": "TTcoin",
        "address": "0x659049786cb66e4486b8c0e0ccc90a5929a21162"
    },
    "TCG2": {
        "symbol": "TCG2",
        "decimals": 9,
        "name": "TCGCoin 2.0",
        "address": "0xf73d8276c15ce56b2f4aee5920e62f767a7f3aea"
    },
    "TCH": {
        "symbol": "TCH",
        "decimals": 18,
        "name": "TCH Token",
        "address": "0x5ecc4b299e23f526980c33fe35eff531a54aedb1"
    },
    "TCT": {
        "symbol": "TCT",
        "decimals": 18,
        "name": "Token Club",
        "address": "0xca0a9df6a8cad800046c1ddc5755810718b65c44"
    },
    "TDX": {
        "symbol": "TDX",
        "decimals": 18,
        "name": "Tidex Token",
        "address": "0x317eb4ad9cfac6232f0046831322e895507bcbeb"
    },
    "TED": {
        "symbol": "TED",
        "decimals": 18,
        "name": "Ted",
        "address": "0xa4a66d8a705260c8cb1ebb59224e018015294f48"
    },
    "Teddy V2": {
        "symbol": "Teddy V2",
        "decimals": 18,
        "name": "Teddy Doge V2",
        "address": "0xdb79c12d1d0670988a39b0e48b96e955ef922d24"
    },
    "TEM": {
        "symbol": "TEM",
        "decimals": 9,
        "name": "Templar Token",
        "address": "0x19e6bfc1a6e4b042fb20531244d47e252445df01"
    },
    "TENFI": {
        "symbol": "TENFI",
        "decimals": 18,
        "name": "TEN Finance",
        "address": "0xd15c444f1199ae72795eba15e8c1db44e47abf62"
    },
    "TERZ": {
        "symbol": "TERZ",
        "decimals": 18,
        "name": "SHELTERZ",
        "address": "0xcf3bb6ac0f6d987a5727e2d15e39c2d6061d5bec"
    },
    "TEX": {
        "symbol": "TEX",
        "decimals": 18,
        "name": "IotexPad",
        "address": "0x049dd7532148826cde956c7b45fec8c30b514052"
    },
    "TFI": {
        "symbol": "TFI",
        "decimals": 18,
        "name": "TrustFi Network Token",
        "address": "0x7565ab68d3f9dadff127f864103c8c706cf28235"
    },
    "TFLOW": {
        "symbol": "TFLOW",
        "decimals": 18,
        "name": "TradeFlow",
        "address": "0x00ee89f7f21b60b72dd5d4070a4310f796c38c32"
    },
    "TFS": {
        "symbol": "TFS",
        "decimals": 18,
        "name": "Fairspin Token",
        "address": "0xf4bea2c219eb95c6745983b68185c7340c319d9e"
    },
    "TFT": {
        "symbol": "TFT",
        "decimals": 7,
        "name": "TFT on BSC",
        "address": "0x8f0fb159380176d324542b3a7933f0c2fd0c2bbf"
    },
    "TGDAO": {
        "symbol": "TGDAO",
        "decimals": 18,
        "name": "TGDAO",
        "address": "0x46f275321107d7c49cf80216371abf1a1599c36f"
    },
    "TGR": {
        "symbol": "TGR",
        "decimals": 18,
        "name": "Tegro",
        "address": "0xd9780513292477c4039dfda1cfcd89ff111e9da5"
    },
    "THB": {
        "symbol": "THB",
        "decimals": 18,
        "name": "THUNDERBRAWL COIN",
        "address": "0xf7d9f74f02f258961f229f10666a1dba85d0529f"
    },
    "THC": {
        "symbol": "THC",
        "decimals": 18,
        "name": "Thetan Coin",
        "address": "0x24802247bd157d771b7effa205237d8e9269ba8a"
    },
    "THE": {
        "symbol": "THE",
        "decimals": 18,
        "name": "THENA",
        "address": "0xf4c8e32eadec4bfe97e0f595add0f4450a863a11"
    },
    "THG": {
        "symbol": "THG",
        "decimals": 18,
        "name": "Thetan Gem",
        "address": "0x9fd87aefe02441b123c3c32466cd9db4c578618f"
    },
    "THOREUM": {
        "symbol": "THOREUM",
        "decimals": 18,
        "name": "Thoreumv4 - Thoreum.AI",
        "address": "0xce1b3e5087e8215876af976032382dd338cf8401"
    },
    "TIFI": {
        "symbol": "TIFI",
        "decimals": 18,
        "name": "TiFi Token",
        "address": "0x17e65e6b9b166fb8e7c59432f0db126711246bc0"
    },
    "TIME": {
        "symbol": "TIME",
        "decimals": 8,
        "name": "ChronoTech Token",
        "address": "0x3b198e26e473b8fab2085b37978e36c9de5d7f68"
    },
    "TINC": {
        "symbol": "TINC",
        "decimals": 18,
        "name": "Tiny Coin",
        "address": "0x05ad6e30a855be07afa57e08a4f30d00810a402e"
    },
    "TINU": {
        "symbol": "TINU",
        "decimals": 9,
        "name": "Telegram Inu",
        "address": "0x4aa22532e3e8b051eae48e60c58426c8553d5df5"
    },
    "TIP": {
        "symbol": "TIP",
        "decimals": 18,
        "name": "SugarBounce",
        "address": "0x40f906e19b14100d5247686e08053c4873c66192"
    },
    "TIPO": {
        "symbol": "TIPO",
        "decimals": 18,
        "name": "TIPOToken",
        "address": "0x58b40ac5cbeeea651dc5512ea81a0bc8575f04a8"
    },
    "TITA": {
        "symbol": "TITA",
        "decimals": 18,
        "name": "Titan Hunters",
        "address": "0x0c1253a30da9580472064a91946c5ce0c58acf7f"
    },
    "TITI": {
        "symbol": "TITI",
        "decimals": 18,
        "name": "Titi Financial ",
        "address": "0xe618ef7c64afede59a81cef16d0161c914ebab17"
    },
    "TKB": {
        "symbol": "TKB",
        "decimals": 18,
        "name": "TokenBot",
        "address": "0x5655592badf214bbd520187de0a766cd7bd7c712"
    },
    "TKC": {
        "symbol": "TKC",
        "decimals": 18,
        "name": "The Kingdom Coin",
        "address": "0x06dc293c250e2fb2416a4276d291803fc74fb9b5"
    },
    "TKING": {
        "symbol": "TKING",
        "decimals": 18,
        "name": "Tiger King",
        "address": "0x9b4bdddaeb68d85b0848bab7774e6855439fd94e"
    },
    "TKO": {
        "symbol": "TKO",
        "decimals": 18,
        "name": "Tokocrypto Token",
        "address": "0x9f589e3eabe42ebc94a44727b3f3531c0c877809"
    },
    "TKP": {
        "symbol": "TKP",
        "decimals": 18,
        "name": "TOKPIE",
        "address": "0x7849ed1447250d0b896f89b58f3075b127ca29b3"
    },
    "TLC": {
        "symbol": "TLC",
        "decimals": 18,
        "name": "Trillioner",
        "address": "0x29a5daf6e3fdf964def07706ea1abee7ec03d021"
    },
    "TLM": {
        "symbol": "TLM",
        "decimals": 4,
        "name": "Alien Worlds Trilium",
        "address": "0x2222227e22102fe3322098e4cbfe18cfebd57c95"
    },
    "TLOS": {
        "symbol": "TLOS",
        "decimals": 18,
        "name": "pTokens TLOS",
        "address": "0xb6c53431608e626ac81a9776ac3e999c5556717c"
    },
    "TMG": {
        "symbol": "TMG",
        "decimals": 18,
        "name": "T-mac DAO",
        "address": "0x71b87be9ccbabe4f393e809dfc26df3c9720e0a2"
    },
    "TMON": {
        "symbol": "TMON",
        "decimals": 18,
        "name": "Two Monkey Juice Bar",
        "address": "0x2cd24aaf0aeabde7f830d6719eeb8eb3837712de"
    },
    "TMT": {
        "symbol": "TMT",
        "decimals": 18,
        "name": "TopManager Token",
        "address": "0x4803ac6b79f9582f69c4fa23c72cb76dd1e46d8d"
    },
    "TOKO": {
        "symbol": "TOKO",
        "decimals": 18,
        "name": "Tokoin",
        "address": "0x45f7967926e95fd161e56ed66b663c9114c5226f"
    },
    "TONCOIN": {
        "symbol": "TONCOIN",
        "decimals": 9,
        "name": "Wrapped TON Coin",
        "address": "0x76a797a59ba2c17726896976b7b3747bfd1d220f"
    },
    "TOOLS": {
        "symbol": "TOOLS",
        "decimals": 18,
        "name": "TOOLS",
        "address": "0x1311b352467d2b5c296881badea82850bcd8f886"
    },
    "TOON": {
        "symbol": "TOON",
        "decimals": 18,
        "name": "PontoonToken",
        "address": "0xaee433adebe0fbb88daa47ef0c1a513caa52ef02"
    },
    "TOR": {
        "symbol": "TOR",
        "decimals": 18,
        "name": "TOR",
        "address": "0x1d6cbdc6b29c6afbae65444a1f65ba9252b8ca83"
    },
    "TORN": {
        "symbol": "TORN",
        "decimals": 18,
        "name": "TornadoCash",
        "address": "0x1ba8d3c4c219b124d351f603060663bd1bcd9bbf"
    },
    "TOTEM": {
        "symbol": "TOTEM",
        "decimals": 18,
        "name": "Cryptotem",
        "address": "0x777994409c6b7e2393f6098a33a9cd8b7e9d0d28"
    },
    "TOTM": {
        "symbol": "TOTM",
        "decimals": 18,
        "name": "Totem Token",
        "address": "0x6ff1bfa14a57594a5874b37ff6ac5efbd9f9599a"
    },
    "TOWER": {
        "symbol": "TOWER",
        "decimals": 18,
        "name": "TOWER",
        "address": "0xe7c9c6bc87b86f9e5b57072f907ee6460b593924"
    },
    "TPAD": {
        "symbol": "TPAD",
        "decimals": 9,
        "name": "TrustPad",
        "address": "0xadcfc6bf853a0a8ad7f9ff4244140d10cf01363c"
    },
    "TPT": {
        "symbol": "TPT",
        "decimals": 4,
        "name": "TokenPocket Token",
        "address": "0xeca41281c24451168a37211f0bc2b8645af45092"
    },
    "TRAVA": {
        "symbol": "TRAVA",
        "decimals": 18,
        "name": "TravaFinance Token",
        "address": "0x0391be54e72f7e001f6bbc331777710b4f2999ef"
    },
    "TRAVEL": {
        "symbol": "TRAVEL",
        "decimals": 18,
        "name": "TravelCare",
        "address": "0x826e5ec70dbc5607ff9218011fbb97f9a8d97953"
    },
    "TRDC": {
        "symbol": "TRDC",
        "decimals": 18,
        "name": "traders coin",
        "address": "0x7e8db69dcff9209e486a100e611b0af300c3374e"
    },
    "TREES": {
        "symbol": "TREES",
        "decimals": 9,
        "name": "SAFETREES",
        "address": "0xd3b77ac07c963b8cead47000a5208434d9a8734d"
    },
    "TRIAS": {
        "symbol": "TRIAS",
        "decimals": 18,
        "name": "\bTrias Token",
        "address": "0xa4838122c683f732289805fc3c207febd55babdd"
    },
    "TRIVIA": {
        "symbol": "TRIVIA",
        "decimals": 3,
        "name": "Trivian Token",
        "address": "0xb465f3cb6aba6ee375e12918387de1eac2301b05"
    },
    "TRL": {
        "symbol": "TRL",
        "decimals": 18,
        "name": "Triall",
        "address": "0xe2eb47954e821dc94e19013677004cd59be0b17f"
    },
    "TRMX": {
        "symbol": "TRMX",
        "decimals": 4,
        "name": "TourismX Token",
        "address": "0xa6472bc7c0e2266034bb40edd8c6e8961cf45826"
    },
    "Troll": {
        "symbol": "Troll",
        "decimals": 9,
        "name": "Troll Face",
        "address": "0x52721d159cd90dd76014f73c1440e4ff983420ac"
    },
    "TRR": {
        "symbol": "TRR",
        "decimals": 18,
        "name": "TERRAN",
        "address": "0xbb95cc1c662d89822bda29d2e147b124406e6e42"
    },
    "TRUBGR": {
        "symbol": "TRUBGR",
        "decimals": 18,
        "name": "TruBadger",
        "address": "0xc003f5193cabe3a6cbb56948dfeaae2276a6aa5e"
    },
    "TruePNL": {
        "symbol": "TruePNL",
        "decimals": 18,
        "name": "PNL",
        "address": "0xb346c52874c7023df183068c39478c3b7b2515bc"
    },
    "TRUMPARMY": {
        "symbol": "TRUMPARMY",
        "decimals": 9,
        "name": "Trump Army",
        "address": "0x7361de48dde2d05e379d9e6641b7e7b2e323a464"
    },
    "TRUSTNFT": {
        "symbol": "TRUSTNFT",
        "decimals": 18,
        "name": "TrustNFT",
        "address": "0x08f725d2809fda409bc23493f3615a4c85a22d7d"
    },
    "TRUTH": {
        "symbol": "TRUTH",
        "decimals": 18,
        "name": "Truth Seekers",
        "address": "0x55a633b3fce52144222e468a326105aa617cc1cc"
    },
    "TRVL": {
        "symbol": "TRVL",
        "decimals": 18,
        "name": "TRVL",
        "address": "0x6a8fd46f88dbd7bdc2d536c604f811c63052ce0f"
    },
    "TRY": {
        "symbol": "TRY",
        "decimals": 18,
        "name": "TryHards",
        "address": "0x75d107de2217ffe2cd574a1b3297c70c8fafd159"
    },
    "TRYB": {
        "symbol": "TRYB",
        "decimals": 6,
        "name": "BiLira",
        "address": "0xc1fdbed7dac39cae2ccc0748f7a80dc446f6a594"
    },
    "TSX": {
        "symbol": "TSX",
        "decimals": 18,
        "name": "TradeStars TSX",
        "address": "0x270388e0ca29cfd7c7e73903d9d933a23d1bab39"
    },
    "TTAI": {
        "symbol": "TTAI",
        "decimals": 18,
        "name": "Trade Tech AI",
        "address": "0xd618ad98e6557532d3c65e88bf1ff765724f21c9"
    },
    "TTC": {
        "symbol": "TTC",
        "decimals": 18,
        "name": "Tao Te Ching ",
        "address": "0x152ad7dc399269fa65d19bd7a790ea8aa5b23dad"
    },
    "TTN": {
        "symbol": "TTN",
        "decimals": 9,
        "name": "TeleTreon",
        "address": "0x50a9eb8a53f2c2993f46b354bd5f24f1c880bf24"
    },
    "TTT": {
        "symbol": "TTT",
        "decimals": 18,
        "name": "TopTrade",
        "address": "0x2cb63fcd1380a8ad0ff5ba16ddcbdf4935154da8"
    },
    "TUP": {
        "symbol": "TUP",
        "decimals": 18,
        "name": "Tenup DAO Token",
        "address": "0x63eaeb6e33e11252b10553900a9f38a9ed172871"
    },
    "TUSD": {
        "symbol": "TUSD",
        "decimals": 18,
        "name": "TrueUSD",
        "address": "0x14016e85a25aeb13065688cafb43044c2ef86784"
    },
    "TWELVE": {
        "symbol": "TWELVE",
        "decimals": 18,
        "name": "Twelve Zodiac",
        "address": "0xbd6ceeef56985b608252c3651dd903a3fcc34910"
    },
    "TWT": {
        "symbol": "TWT",
        "decimals": 18,
        "name": "Trust Wallet",
        "address": "0x4b0f1812e5df2a09796481ff14017e6005508003"
    },
    "TXBIT": {
        "symbol": "TXBIT",
        "decimals": 18,
        "name": "Txbit Token",
        "address": "0x339fe932809e39a95b621a7f88bbf6c08eb6c978"
    },
    "TXL": {
        "symbol": "TXL",
        "decimals": 18,
        "name": "Tixl Token",
        "address": "0x1ffd0b47127fdd4097e54521c9e2c7f0d66aafc5"
    },
    "TXS": {
        "symbol": "TXS",
        "decimals": 9,
        "name": "XStudio",
        "address": "0xc042705c93525ae247c8998715e7942ef6135747"
    },
    "TYV": {
        "symbol": "TYV",
        "decimals": 8,
        "name": "TYVCOIN",
        "address": "0x90a8bbf934fde975555632addcb258e895c69de1"
    },
    'unshETH': {
        'symbol': 'unshETH',
        'decimals': 18,
        'name': 'unshETH Ether',
        'address': '0x0Ae38f7E10A43B5b2fB064B42a2f4514cbA909ef',
    },
    "U": {
        "symbol": "U",
        "decimals": 18,
        "name": "Unidef",
        "address": "0x89db9b433fec1307d3dc8908f2813e9f7a1d38f0"
    },
    "UBXS": {
        "symbol": "UBXS",
        "decimals": 6,
        "name": "UBXS Token",
        "address": "0x4f1960e29b2ca581a38c5c474e123f420f8092db"
    },
    "UCO": {
        "symbol": "UCO",
        "decimals": 18,
        "name": "UnirisToken",
        "address": "0xb001f1e7c8bda414ac7cf7ecba5469fe8d24b6de"
    },
    "UCON": {
        "symbol": "UCON",
        "decimals": 18,
        "name": "YouCoin",
        "address": "0x1f88e9956c8f8f64c8d5fef5ed8a818e2237112c"
    },
    "UFARM": {
        "symbol": "UFARM",
        "decimals": 18,
        "name": "UNIFARM Token",
        "address": "0x0a356f512f6fce740111ee04ab1699017a908680"
    },
    "UFI": {
        "symbol": "UFI",
        "decimals": 18,
        "name": "PureFi Token",
        "address": "0xe2a59d5e33c6540e18aaa46bf98917ac3158db0d"
    },
    "UFT": {
        "symbol": "UFT",
        "decimals": 18,
        "name": "UniLend Finance Token",
        "address": "0x2645d5f59d952ef2317c8e0aaa5a61c392ccd44d"
    },
    "ULAND": {
        "symbol": "ULAND",
        "decimals": 18,
        "name": "ULAND TOKEN",
        "address": "0x9789df6753b7f813a1c55ed20ecf83571dfde428"
    },
    "ULTRON": {
        "symbol": "ULTRON",
        "decimals": 18,
        "name": "Ultron Vault",
        "address": "0xd2ed1973d55488b7118ea81d5a30cd7b61c68a49"
    },
    "ULX": {
        "symbol": "ULX",
        "decimals": 18,
        "name": "Ultron",
        "address": "0xd983ab71a284d6371908420d8ac6407ca943f810"
    },
    "UMB": {
        "symbol": "UMB",
        "decimals": 18,
        "name": "Umbrella",
        "address": "0x846f52020749715f02aef25b5d1d65e48945649d"
    },
    "UMT": {
        "symbol": "UMT",
        "decimals": 18,
        "name": "UnityMeta Token",
        "address": "0xca861e289f04cb9c67fd6b87ca7eafa59192f164"
    },
    "UNB": {
        "symbol": "UNB",
        "decimals": 18,
        "name": "Unbound",
        "address": "0x301af3eff0c904dc5ddd06faa808f653474f7fcc"
    },
    "UNCX": {
        "symbol": "UNCX",
        "decimals": 18,
        "name": "UniCrypt on xDai on BSC",
        "address": "0x09a6c44c3947b69e2b45f4d51b67e6a39acfb506"
    },
    "UNFI": {
        "symbol": "UNFI",
        "decimals": 18,
        "name": "UNFI",
        "address": "0x728c5bac3c3e370e372fc4671f9ef6916b814d8b"
    },
    "UNI": {
        "symbol": "UNI",
        "decimals": 18,
        "name": "Uniswap",
        "address": "0xbf5140a22578168fd562dccf235e5d43a02ce9b1"
    },
    "UNO": {
        "symbol": "UNO",
        "decimals": 18,
        "name": "UnoRe",
        "address": "0x474021845c4643113458ea4414bdb7fb74a01a77"
    },
    "UNW": {
        "symbol": "UNW",
        "decimals": 18,
        "name": "Uniwhale Token",
        "address": "0x5b65cd9feb54f1df3d0c60576003344079f8dc06"
    },
    "URUS": {
        "symbol": "URUS",
        "decimals": 18,
        "name": "Aurox Token",
        "address": "0xc6dddb5bc6e61e0841c54f3e723ae1f3a807260b"
    },
    "USD+": {
        "symbol": "USD+",
        "decimals": 6,
        "name": "USD+",
        "address": "0xe80772eaf6e2e18b651f160bc9158b2a5cafca65"
    },
    "USDC": {
        "symbol": "USDC",
        "decimals": 18,
        "name": "USD Coin",
        "address": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"
    },
    "USDD": {
        "symbol": "USDD",
        "decimals": 18,
        "name": "Decentralized USD",
        "address": "0xd17479997f34dd9156deef8f95a52d81d265be9c"
    },
    "USDZ": {
        "symbol": "USDZ",
        "decimals": 9,
        "name": "ZEDXION",
        "address": "0x734d66f635523d7ddb7d2373c128333da313041b"
    },
    "USH": {
        "symbol": "USH",
        "decimals": 18,
        "name": "unshETHing_Token",
        "address": "0x91d6d6af7635b7b23a8ced9508117965180e2362"
    },
    "UST": {
        "symbol": "UST",
        "decimals": 18,
        "name": "Wrapped UST Token",
        "address": "0x23396cf899ca06c4472205fc903bdb4de249d6fc"
    },
    "USV": {
        "symbol": "USV",
        "decimals": 9,
        "name": "Universal Store of Value",
        "address": "0xaf6162dc717cfc8818efc8d6f46a41cf7042fcba"
    },
    "USX": {
        "symbol": "USX",
        "decimals": 18,
        "name": "dForce USD",
        "address": "0xb5102cee1528ce2c760893034a4603663495fd72"
    },
    "UT": {
        "symbol": "UT",
        "decimals": 18,
        "name": "Universal Token",
        "address": "0x39dc1f91fee49c03a0db558254707116101518bf"
    },
    "UTED": {
        "symbol": "UTED",
        "decimals": 18,
        "name": "UNITED",
        "address": "0x951df2682ff9a963c4243a38d3841c9ba471b8ae"
    },
    "UTU": {
        "symbol": "UTU",
        "decimals": 18,
        "name": "UTU Coin",
        "address": "0xed4bb33f20f32e989af975196e86019773a7cff0"
    },
    "UV": {
        "symbol": "UV",
        "decimals": 18,
        "name": "UnityVentures",
        "address": "0xb3a95bdbe4ac65b0628db1e6600f71ed59b89255"
    },
    "UVT": {
        "symbol": "UVT",
        "decimals": 18,
        "name": "Universe Token",
        "address": "0x196eb1d21c05cc265ea0a1479e924e7983467838"
    },
    "UW3S": {
        "symbol": "UW3S",
        "decimals": 18,
        "name": "Utility Web3Shot",
        "address": "0x961e149db8bfbdb318c182152725ac806d7be3f4"
    },
    "VAI": {
        "symbol": "VAI",
        "decimals": 18,
        "name": "VAI Stablecoin",
        "address": "0x4bd17003473389a42daf6a0a729f6fdb328bbbd7"
    },
    "VALAS": {
        "symbol": "VALAS",
        "decimals": 18,
        "name": "Valas Finance Protocol Token",
        "address": "0xb1ebdd56729940089ecc3ad0bbeeb12b6842ea6f"
    },
    "VANCAT": {
        "symbol": "VANCAT",
        "decimals": 9,
        "name": "VANCAT Token",
        "address": "0x0da1774e58ed28ff9749340f116055f8d836a7c8"
    },
    "vBUSD": {
        "symbol": "vBUSD",
        "decimals": 8,
        "name": "Venus BUSD",
        "address": "0x95c78222b3d6e262426483d42cfa53685a67ab9d"
    },
    "VCG": {
        "symbol": "VCG",
        "decimals": 18,
        "name": "VCGamers",
        "address": "0x1f36fb2d91d9951cf58ae4c1956c0b77e224f1e9"
    },
    "vDAI": {
        "symbol": "vDAI",
        "decimals": 8,
        "name": "Venus DAI",
        "address": "0x334b3ecb4dca3593bccc3c7ebd1a1c1d1780fbf1"
    },
    "VEED": {
        "symbol": "VEED",
        "decimals": 18,
        "name": "VEED",
        "address": "0x16fdd1edb14ac4012395a0617a682d81595db486"
    },
    "VELO": {
        "symbol": "VELO",
        "decimals": 18,
        "name": "VELO",
        "address": "0xf486ad071f3bee968384d2e39e2d8af0fcf6fd46"
    },
    "VEMP": {
        "symbol": "VEMP",
        "decimals": 18,
        "name": "vEmpire Gamer Token",
        "address": "0xedf3ce4dd6725650a8e9398e5c6398d061fa7955"
    },
    "VENT": {
        "symbol": "VENT",
        "decimals": 18,
        "name": "VENT [via ChainPort.io]",
        "address": "0x872d068c25511be88c1f5990c53eeffcdf46c9b4"
    },
    "VERA": {
        "symbol": "VERA",
        "decimals": 18,
        "name": "Vera",
        "address": "0x4a0a3902e091cdb3aec4279a6bfac50297f0a79e"
    },
    "VERVE": {
        "symbol": "VERVE",
        "decimals": 18,
        "name": "VERVETV.app",
        "address": "0x32561fa6d2d3e2191bf50f813df2c34fb3c89b62"
    },
    "VEST": {
        "symbol": "VEST",
        "decimals": 18,
        "name": "DAO Invest",
        "address": "0x873801ae2ff12d816db9a7b082f5796bec64c82c"
    },
    "VET": {
        "symbol": "VET",
        "decimals": 18,
        "name": "VeChain",
        "address": "0x6fdcdfef7c496407ccb0cec90f9c5aaa1cc8d888"
    },
    "VETTER": {
        "symbol": "VETTER",
        "decimals": 9,
        "name": "Vetter Token",
        "address": "0x6169b3b23e57de79a6146a2170980ceb1f83b9e0"
    },
    "VFOX": {
        "symbol": "VFOX",
        "decimals": 18,
        "name": "VFOX",
        "address": "0x4d61577d8fd2208a0afb814ea089fdeae19ed202"
    },
    "VGO": {
        "symbol": "VGO",
        "decimals": 8,
        "name": "Virgo Token",
        "address": "0xfb526228ff1c019e4604c7e7988c097d96bd5b70"
    },
    "VICS": {
        "symbol": "VICS",
        "decimals": 18,
        "name": "RoboFi Token",
        "address": "0x9bcab88763c33a95e73bc6dcf80fcf27a77090b2"
    },
    "VIM": {
        "symbol": "VIM",
        "decimals": 18,
        "name": "VicMove",
        "address": "0x5bcd91c734d665fe426a5d7156f2ad7d37b76e30"
    },
    "VINA": {
        "symbol": "VINA",
        "decimals": 18,
        "name": "Vicuna",
        "address": "0x61a802de6327a05dda95812ae1535109599f7df2"
    },
    "VINU": {
        "symbol": "VINU",
        "decimals": 18,
        "name": "Vita Inu",
        "address": "0xfebe8c1ed424dbf688551d4e2267e7a53698f0aa"
    },
    "VIP": {
        "symbol": "VIP",
        "decimals": 9,
        "name": "VIP TOKEN",
        "address": "0x6759565574de509b7725abb4680020704b3f404e"
    },
    "VITE": {
        "symbol": "VITE",
        "decimals": 18,
        "name": "Vite",
        "address": "0x2794dad4077602ed25a88d03781528d1637898b4"
    },
    "VİTY": {
        "symbol": "VİTY",
        "decimals": 18,
        "name": "VİTTEEY",
        "address": "0x311e85452ec46d03d056317b979d444ea717dc7e"
    },
    "VIVA": {
        "symbol": "VIVA",
        "decimals": 9,
        "name": "Viva Classic",
        "address": "0x32767ca0b39a1261e4ba392a605f7fab37d059c7"
    },
    "VIZSLASWAP": {
        "symbol": "VIZSLASWAP",
        "decimals": 18,
        "name": "VizslaSwap",
        "address": "0xadaae082237cb1772c9e079db95c117e6dd0c5af"
    },
    "vLINK": {
        "symbol": "vLINK",
        "decimals": 8,
        "name": "Venus LINK",
        "address": "0x650b940a1033b8a1b1873f78730fcfc73ec11f1f"
    },
    "VLK": {
        "symbol": "VLK",
        "decimals": 18,
        "name": "Vulkania",
        "address": "0x797bb0beea437d2762a755ea911c0046c1284568"
    },
    "VLX": {
        "symbol": "VLX",
        "decimals": 18,
        "name": "Velas",
        "address": "0xe9c803f48dffe50180bd5b01dc04da939e3445fc"
    },
    "VLXPAD": {
        "symbol": "VLXPAD",
        "decimals": 18,
        "name": "VELASPAD.io",
        "address": "0xb8e3bb633f7276cc17735d86154e0ad5ec9928c0"
    },
    "VMT": {
        "symbol": "VMT",
        "decimals": 18,
        "name": "Vemate",
        "address": "0xe615c5e7219f9801c3b75bc76e45a4dab3c38e51"
    },
    "VNW": {
        "symbol": "VNW",
        "decimals": 18,
        "name": "VNetwork",
        "address": "0xfa7d4d3fde48e7d70840b6947c4065f8fcfe796d"
    },
    "VOLT": {
        "symbol": "VOLT",
        "decimals": 9,
        "name": "Volt Inu",
        "address": "0x7db5af2b9624e1b3b4bb69d6debd9ad1016a58ac"
    },
    "VPP": {
        "symbol": "VPP",
        "decimals": 18,
        "name": "Virtue Player Points",
        "address": "0xe069af87450fb51fc0d0e044617f1c134163e591"
    },
    "VRGW": {
        "symbol": "VRGW",
        "decimals": 18,
        "name": "Virtual Reality Game World",
        "address": "0xfdd2374be7ae7a71138b9f6b93d9ef034a49edb6"
    },
    "VRT": {
        "symbol": "VRT",
        "decimals": 18,
        "name": "Venus Reward Token",
        "address": "0x5f84ce30dc3cf7909101c69086c50de191895883"
    },
    "VS": {
        "symbol": "VS",
        "decimals": 6,
        "name": "Vision",
        "address": "0xcd76bc49a69bcdc5222d81c18d4a04dc8a387297"
    },
    "VST": {
        "symbol": "VST",
        "decimals": 18,
        "name": "Voice Street Token",
        "address": "0xacf34edcc424128cccc730bf85cdaceebcb3eece"
    },
    "vSXP": {
        "symbol": "vSXP",
        "decimals": 8,
        "name": "Venus SXP",
        "address": "0x2ff3d0f6990a40261c66e1ff2017acbc282eb6d0"
    },
    "VT": {
        "symbol": "VT",
        "decimals": 18,
        "name": "Virtual Tourist Token",
        "address": "0xed66ec1acb7dbd0c01cccff33e3ff1f423057c21"
    },
    "VTG": {
        "symbol": "VTG",
        "decimals": 18,
        "name": "Victory Gem",
        "address": "0x8de5aa37a7c40a53062ead382b8eead3b08a7a46"
    },
    "vUSDC": {
        "symbol": "vUSDC",
        "decimals": 8,
        "name": "Venus USDC",
        "address": "0xeca88125a5adbe82614ffc12d0db554e2e2867c8"
    },
    "vUSDT": {
        "symbol": "vUSDT",
        "decimals": 8,
        "name": "Venus USDT",
        "address": "0xfd5840cd36d94d7229439859c0112a4185bc0255"
    },
    "vXRP": {
        "symbol": "vXRP",
        "decimals": 8,
        "name": "Venus XRP",
        "address": "0xb248a295732e0225acd3337607cc01068e3b9c10"
    },
    "vXVS": {
        "symbol": "vXVS",
        "decimals": 8,
        "name": "Venus XVS",
        "address": "0x151b1e2635a717bcdc836ecd6fbb62b674fe3e1d"
    },
    "WAG": {
        "symbol": "WAG",
        "decimals": 18,
        "name": "WAGYUSWAP.app",
        "address": "0x7fa7df4996ac59f398476892cfb195ed38543520"
    },
    "WAL": {
        "symbol": "WAL",
        "decimals": 18,
        "name": "WastedLands",
        "address": "0xd306c124282880858a634e7396383ae58d37c79c"
    },
    "WALBT": {
        "symbol": "WALBT",
        "decimals": 18,
        "name": "Wrapped AllianceBlock Token",
        "address": "0x42f3008f6945f052c31e7680f7f78c512099b904"
    },
    "wALV": {
        "symbol": "wALV",
        "decimals": 18,
        "name": "Alvey Chain",
        "address": "0x256d1fce1b1221e8398f65f9b36033ce50b2d497"
    },
    "WAM": {
        "symbol": "WAM",
        "decimals": 18,
        "name": "WAM",
        "address": "0xebbaeff6217d22e7744394061d874015709b8141"
    },
    "WANA": {
        "symbol": "WANA",
        "decimals": 18,
        "name": "Wanaka Farm",
        "address": "0x339c72829ab7dd45c3c52f965e7abe358dd8761e"
    },
    "WARS": {
        "symbol": "WARS",
        "decimals": 18,
        "name": "MetaWars",
        "address": "0x50e756a22ff5cee3559d18b9d9576bc38f09fa7c"
    },
    "WATCH": {
        "symbol": "WATCH",
        "decimals": 18,
        "name": "yieldwatch",
        "address": "0x7a9f28eb62c791422aa23ceae1da9c847cbec9b0"
    },
    "wBAN": {
        "symbol": "wBAN",
        "decimals": 18,
        "name": "Wrapped Banano",
        "address": "0xe20b9e246db5a0d21bf9209e4858bc9a3ff7a034"
    },
    "wBETH": {
        "symbol": "wBETH",
        "decimals": 18,
        "name": "Wrapped Binance Beacon ETH",
        "address": "0xa2e3356610840701bdf5611a53974510ae27e2e1"
    },
    "wBIS": {
        "symbol": "wBIS",
        "decimals": 8,
        "name": "Wrapped BIS",
        "address": "0x56672ecb506301b1e32ed28552797037c54d36a9"
    },
    "wBLK": {
        "symbol": "wBLK",
        "decimals": 18,
        "name": "Wrapped Blackcoin",
        "address": "0xd2cdfd5d26dfa1d11116b9ed7dbd7c6b88c6e1d3"
    },
    "WBM": {
        "symbol": "WBM",
        "decimals": 9,
        "name": "WB-Mining",
        "address": "0x19575b407e2dd49cb2ba46375a7fba37c8ec553a"
    },
    "wBTCZ": {
        "symbol": "wBTCZ",
        "decimals": 8,
        "name": "Wrapped BitcoinZ",
        "address": "0xcbbb3e5099f769f6d4e2b8b92dc0e268f7e099d8"
    },
    "WBYTZ": {
        "symbol": "WBYTZ",
        "decimals": 8,
        "name": "Wrapped BYTZ",
        "address": "0x586fc153cf7e9c029d8c30842c4cb6a86f03b816"
    },
    "WCHI": {
        "symbol": "WCHI",
        "decimals": 8,
        "name": "Wrapped CHI",
        "address": "0x22648c12acd87912ea1710357b1302c6a4154ebc"
    },
    "WCREDIT": {
        "symbol": "WCREDIT",
        "decimals": 18,
        "name": "Wrapped CREDIT on BSC",
        "address": "0xc9308bcf5fa46d728422753d2d5afbc5cdb66b03"
    },
    "WDF": {
        "symbol": "WDF",
        "decimals": 18,
        "name": "Wallet Defi",
        "address": "0xfc12242996ed64382286d765572f19e9b843f196"
    },
    "wDingocoin": {
        "symbol": "wDingocoin",
        "decimals": 8,
        "name": "Wrapped Dingocoin",
        "address": "0x9b208b117b2c4f76c1534b6f006b033220a681a4"
    },
    "wDZOO": {
        "symbol": "wDZOO",
        "decimals": 18,
        "name": "DegenZoo",
        "address": "0x56d06a78ef8e95d6043341f24759e2834be6f97b"
    },
    "we2net": {
        "symbol": "we2net",
        "decimals": 18,
        "name": "we2net",
        "address": "0x572c9ab47977d7d909572f3b8bce076a858a8763"
    },
    "WEAR": {
        "symbol": "WEAR",
        "decimals": 18,
        "name": "Metawear",
        "address": "0x9d39ef3bbca5927909dde44476656b81bbe4ee75"
    },
    "WEB3T": {
        "symbol": "WEB3T",
        "decimals": 18,
        "name": "WEB3TOOLS ECOSYSTEM",
        "address": "0x065a74c744eb69b4975629c1a89823c694d2efdb"
    },
    "WEB4": {
        "symbol": "WEB4",
        "decimals": 9,
        "name": "WEB4 AI",
        "address": "0xee7e8c85956d32c64bafdcded3f43b3c39b1ce2f"
    },
    "WebAI": {
        "symbol": "WebAI",
        "decimals": 18,
        "name": "Web AI",
        "address": "0x7c5e8a22a4e8f9da2797a9e30e9d64abf5493c43"
    },
    "WEC": {
        "symbol": "WEC",
        "decimals": 18,
        "name": "WholeEarthCoin from Mainnet",
        "address": "0x3623f2b63d8f50b477849d29e7c9a6625331e89d"
    },
    "WED": {
        "symbol": "WED",
        "decimals": 9,
        "name": "Wednesday Token",
        "address": "0xddbb3e6f8413d0e3adc700a731da304aec97bcbb"
    },
    "WEFIN": {
        "symbol": "WEFIN",
        "decimals": 8,
        "name": "Wrapped EFIN",
        "address": "0xae459484c895a335cec08058290d94551dbf5fbb"
    },
    "WEJS": {
        "symbol": "WEJS",
        "decimals": 18,
        "name": "Wrapped Enjinstarter",
        "address": "0x09f423ac3c9babbff6f94d372b16e4206e71439f"
    },
    "WELD": {
        "symbol": "WELD",
        "decimals": 18,
        "name": "Weld.Money",
        "address": "0x5b6ebb33eea2d12eefd4a9b2aeaf733231169684"
    },
    "WELT": {
        "symbol": "WELT",
        "decimals": 18,
        "name": "FABWELT",
        "address": "0x1785113910847770290f5f840b4c74fc46451201"
    },
    "WETH": {
        "symbol": "WETH",
        "decimals": 18,
        "name": "Wrapped Ether",
        "address": "0x4db5a66e937a9f4473fa95b1caf1d1e1d62e29ea"
    },
    "WEVER": {
        "symbol": "WEVER",
        "decimals": 9,
        "name": "Wrapped Ever",
        "address": "0x0a7e7d210c45c4abba183c1d0551b53ad1756eca"
    },
    "WEX": {
        "symbol": "WEX",
        "decimals": 18,
        "name": "WaultSwap",
        "address": "0xa9c41a46a6b3531d28d5c32f6633dd2ff05dfb90"
    },
    "WEYU": {
        "symbol": "WEYU",
        "decimals": 18,
        "name": "WEYU",
        "address": "0xfafd4cb703b25cb22f43d017e7e0d75febc26743"
    },
    "WGR": {
        "symbol": "WGR",
        "decimals": 18,
        "name": "BSC Wrapped Wagerr",
        "address": "0xdbf8265b1d5244a13424f13977723acf5395eab2"
    },
    "WGRLC": {
        "symbol": "WGRLC",
        "decimals": 8,
        "name": "Wrapped GRLC",
        "address": "0x7283dfa2d8d7e277b148cc263b5d8ae02f1076d3"
    },
    "WIN": {
        "symbol": "WIN",
        "decimals": 18,
        "name": "WINk",
        "address": "0xaef0d72a118ce24fee3cd1d43d383897d05b4e99"
    },
    "WING": {
        "symbol": "WING",
        "decimals": 9,
        "name": "Wing Token",
        "address": "0x3cb7378565718c64ab86970802140cc48ef1f969"
    },
    "WIRTUAL": {
        "symbol": "WIRTUAL",
        "decimals": 18,
        "name": "WIRTUAL",
        "address": "0xa19d3f4219e2ed6dc1cb595db20f70b8b6866734"
    },
    "WKC": {
        "symbol": "WKC",
        "decimals": 18,
        "name": "WIKI CAT",
        "address": "0x6ec90334d89dbdc89e08a133271be3d104128edb"
    },
    "WKD": {
        "symbol": "WKD",
        "decimals": 9,
        "name": "Wakanda Inu Token",
        "address": "0x5344c20fd242545f31723689662ac12b9556fc3d"
    },
    "WLX": {
        "symbol": "WLX",
        "decimals": 18,
        "name": "Wallax",
        "address": "0x1c8f79ef0a9502c382df9ed96e138613a814af19"
    },
    "WMATIC": {
        "symbol": "WMATIC",
        "decimals": 18,
        "name": "Wrapped Matic",
        "address": "0xc836d8dc361e44dbe64c4862d55ba041f88ddd39"
    },
    "WMX": {
        "symbol": "WMX",
        "decimals": 18,
        "name": "Wombex Token",
        "address": "0xa75d9ca2a0a1d547409d82e1b06618ec284a2ced"
    },
    "WNAV": {
        "symbol": "WNAV",
        "decimals": 8,
        "name": "Wrapped Navcoin",
        "address": "0xbfef6ccfc830d3baca4f6766a0d4aaa242ca9f3d"
    },
    "WNDR": {
        "symbol": "WNDR",
        "decimals": 8,
        "name": "Wonderman Token",
        "address": "0xdfd7b0dd7bf1012dfdf3307a964c36b972300ac8"
    },
    "WNK": {
        "symbol": "WNK",
        "decimals": 18,
        "name": "Winkies",
        "address": "0xb160a5f19ebccd8e0549549327e43ddd1d023526"
    },
    "WOD": {
        "symbol": "WOD",
        "decimals": 18,
        "name": "World of Defish",
        "address": "0x298632d8ea20d321fab1c9b473df5dbda249b2b6"
    },
    "WOJ": {
        "symbol": "WOJ",
        "decimals": 9,
        "name": "Wojak",
        "address": "0x55f96c7005d7c684a65ee653b07b5fe1507c56ab"
    },
    "WOL": {
        "symbol": "WOL",
        "decimals": 18,
        "name": "World Of Legends",
        "address": "0x5eeb28b5aef44b6664b342d23b1aadce84196386"
    },
    "WOM": {
        "symbol": "WOM",
        "decimals": 18,
        "name": "Wombat Token",
        "address": "0xad6742a35fb341a9cc6ad674738dd8da98b94fb1"
    },
    "WOO": {
        "symbol": "WOO",
        "decimals": 18,
        "name": "Wootrade Network",
        "address": "0x4691937a7508860f876c9c0a2a617e7d9e945d4b"
    },
    "WOOP": {
        "symbol": "WOOP",
        "decimals": 18,
        "name": "Woonkly Power",
        "address": "0x8b303d5bbfbbf46f1a4d9741e491e06986894e18"
    },
    "WOR": {
        "symbol": "WOR",
        "decimals": 18,
        "name": "WARRIOR",
        "address": "0xd6edbb510af7901b2c049ce778b65a740c4aeb7f"
    },
    "WOW": {
        "symbol": "WOW",
        "decimals": 18,
        "name": "WOWswap",
        "address": "0x4da996c5fe84755c80e108cf96fe705174c5e36a"
    },
    "WPKT": {
        "symbol": "WPKT",
        "decimals": 18,
        "name": "Wrapped PKT",
        "address": "0x1c25222994531c4ac35e4d94bbf7552c9aa92e32"
    },
    "wROSE": {
        "symbol": "wROSE",
        "decimals": 18,
        "name": "Wrapped ROSE",
        "address": "0x6c6d604d3f07abe287c1a3df0281e999a83495c0"
    },
    "WRX": {
        "symbol": "WRX",
        "decimals": 8,
        "name": "wazirx token",
        "address": "0x8e17ed70334c87ece574c9d537bc153d8609e2a3"
    },
    "WSB": {
        "symbol": "WSB",
        "decimals": 18,
        "name": "WSB Token",
        "address": "0x22168882276e5d5e1da694343b41dd7726eeb288"
    },
    "WSC": {
        "symbol": "WSC",
        "decimals": 18,
        "name": "WealthSecrets",
        "address": "0xb7dacf54a54bfea818f21472d3e71a89287841a7"
    },
    "WSG": {
        "symbol": "WSG",
        "decimals": 18,
        "name": "Wall Street Games",
        "address": "0xa58950f05fea2277d2608748412bf9f802ea4901"
    },
    "WSI": {
        "symbol": "WSI",
        "decimals": 18,
        "name": "WeSendit",
        "address": "0x837a130aed114300bab4f9f1f4f500682f7efd48"
    },
    "WSIGNA": {
        "symbol": "WSIGNA",
        "decimals": 8,
        "name": "Wrapped Signa",
        "address": "0x7b0e7e40ee4672599f7095d1ddd730b0805195ba"
    },
    "WSO": {
        "symbol": "WSO",
        "decimals": 18,
        "name": "Widi Soul",
        "address": "0xc19fe21b4ef356f2f65894392dde4252aa083605"
    },
    "WSPP": {
        "symbol": "WSPP",
        "decimals": 0,
        "name": "WolfSafePoorPeople",
        "address": "0x46d502fac9aea7c5bc7b13c8ec9d02378c33d36f"
    },
    "WSYS": {
        "symbol": "WSYS",
        "decimals": 18,
        "name": "Wrapped SYS",
        "address": "0x747b1223b23e53070c54df355fac2e198aa54708"
    },
    "WTF": {
        "symbol": "WTF",
        "decimals": 18,
        "name": "Waterfall Governance Token",
        "address": "0xd73f32833b6d5d9c8070c23e599e283a3039823c"
    },
    "WTWool": {
        "symbol": "WTWool",
        "decimals": 18,
        "name": "Wolf Town Wool",
        "address": "0xaa15535fd352f60b937b4e59d8a2d52110a419dd"
    },
    "WUDO": {
        "symbol": "WUDO",
        "decimals": 18,
        "name": "Wrapped Unido",
        "address": "0x70802af0ba10dd5bb33276b5b37574b6451db3d9"
    },
    "wUSDR": {
        "symbol": "wUSDR",
        "decimals": 9,
        "name": "Wrapped USDR",
        "address": "0x2952beb1326accbb5243725bd4da2fc937bca087"
    },
    "WWY": {
        "symbol": "WWY",
        "decimals": 18,
        "name": "WeWay Token",
        "address": "0x9ab70e92319f0b9127df78868fd3655fb9f1e322"
    },
    "wXRC": {
        "symbol": "wXRC",
        "decimals": 18,
        "name": "Wrapped xRhodium",
        "address": "0x8f0342bf1063b1d947b0f2cc611301d611ac3487"
    },
    "wZNN": {
        "symbol": "wZNN",
        "decimals": 8,
        "name": "Wrapped ZNN",
        "address": "0x84b174628911896a3b87fa6980d05dbc2ee74836"
    },
    "WZRD": {
        "symbol": "WZRD",
        "decimals": 18,
        "name": "Wizardia Token",
        "address": "0xfa40d8fc324bcdd6bbae0e086de886c571c225d4"
    },
    "X-AI": {
        "symbol": "X-AI",
        "decimals": 18,
        "name": "X Social",
        "address": "0x2eabcb730ca72f0afcbc9da24d105345cb0852aa"
    },
    "XCB": {
        "symbol": "XCB",
        "decimals": 18,
        "name": "CryptoBirdToken",
        "address": "0x9dcd6ab0511b2e72af3d088538d678bae9bbf552"
    },
    "XCN": {
        "symbol": "XCN",
        "decimals": 18,
        "name": "Chain",
        "address": "0x7324c7c0d95cebc73eea7e85cbaac0dbdf88a05b"
    },
    "XCT": {
        "symbol": "XCT",
        "decimals": 6,
        "name": "Citadel.one",
        "address": "0xe8670901e86818745b28c8b30b17986958fce8cc"
    },
    "XCUR": {
        "symbol": "XCUR",
        "decimals": 8,
        "name": "Curate",
        "address": "0xd52669712f253cd6b2fe8a8638f66ed726cb770c"
    },
    "XCV": {
        "symbol": "XCV",
        "decimals": 18,
        "name": "XCarnival",
        "address": "0x4be63a9b26ee89b9a3a13fd0aa1d0b2427c135f8"
    },
    "XDNA": {
        "symbol": "XDNA",
        "decimals": 18,
        "name": "extraDNA",
        "address": "0x80dba9c32b7ab5445e482387a5522e24c0ba4c24"
    },
    "XED": {
        "symbol": "XED",
        "decimals": 18,
        "name": "Exeedme",
        "address": "0x5621b5a3f4a8008c4ccdd1b942b121c8b1944f1f"
    },
    "XEND": {
        "symbol": "XEND",
        "decimals": 18,
        "name": "XEND",
        "address": "0x4a080377f83d669d7bb83b3184a8a5e61b500608"
    },
    "XEP": {
        "symbol": "XEP",
        "decimals": 8,
        "name": "Electra Protocol",
        "address": "0xb897d0a0f68800f8be7d69ffdd1c24b69f57bf3e"
    },
    "XETA": {
        "symbol": "XETA",
        "decimals": 18,
        "name": "XANA",
        "address": "0xbc7370641ddcf16a27eea11230af4a9f247b61f9"
    },
    "XFT": {
        "symbol": "XFT",
        "decimals": 18,
        "name": "Offshift ",
        "address": "0xe138c66982fd5c890c60b94fdba1747faf092c20"
    },
    "XGT": {
        "symbol": "XGT",
        "decimals": 18,
        "name": "Xion Global Token",
        "address": "0xc25af3123d2420054c8fcd144c21113aa2853f39"
    },
    "XIDO": {
        "symbol": "XIDO",
        "decimals": 18,
        "name": "XIDO FINANCE",
        "address": "0x3764bc0de9b6a68c67929130aaec16b6060cab8c"
    },
    "XIL": {
        "symbol": "XIL",
        "decimals": 18,
        "name": "XIL",
        "address": "0xf3be1a4a47576208c1592cc027087ce154b00672"
    },
    "XIV": {
        "symbol": "XIV",
        "decimals": 18,
        "name": "INVERSE",
        "address": "0x00518f36d2e0e514e8eb94d34124fc18ee756f10"
    },
    "XLD": {
        "symbol": "XLD",
        "decimals": 18,
        "name": "XcelDefi",
        "address": "0xc79d1fd14f514cd713b5ca43d288a782ae53eab2"
    },
    "XLN": {
        "symbol": "XLN",
        "decimals": 9,
        "name": "LunaOne",
        "address": "0x2e2ea48c9412e0abb2d6acccec571c6b6411725a"
    },
    "XMC": {
        "symbol": "XMC",
        "decimals": 18,
        "name": "X-MASK Coin",
        "address": "0xb0cb8dd3b2aa9558ba632a350e242f58d2e289b0"
    },
    "XMETA": {
        "symbol": "XMETA",
        "decimals": 18,
        "name": "TTX METAVERSE",
        "address": "0x9aab0a9b3a2f7cf669f1385c48e0a063b93834bb"
    },
    "XMS": {
        "symbol": "XMS",
        "decimals": 18,
        "name": "Mars Ecosystem Token",
        "address": "0x7859b01bbf675d67da8cd128a50d155cd881b576"
    },
    "XMT": {
        "symbol": "XMT",
        "decimals": 18,
        "name": "MetalSwap",
        "address": "0x582c12b30f85162fa393e5dbe2573f9f601f9d91"
    },
    "XNL": {
        "symbol": "XNL",
        "decimals": 18,
        "name": "Chronicle [via ChainPort.io]",
        "address": "0x5f26fa0c2ee5d3c0323d861d0c503f31ac212662"
    },
    "XP": {
        "symbol": "XP",
        "decimals": 18,
        "name": "PolkaFantasy",
        "address": "0x180cfbe9843d79bcafcbcdf23590247793dfc95b"
    },
    "XPNET": {
        "symbol": "XPNET",
        "decimals": 18,
        "name": "XP.network",
        "address": "0x8cf8238abf7b933bf8bb5ea2c7e4be101c11de2a"
    },
    "XPR": {
        "symbol": "XPR",
        "decimals": 4,
        "name": "Proton",
        "address": "0x5de3939b2f811a61d830e6f52d13b066881412ab"
    },
    "XPRESS": {
        "symbol": "XPRESS",
        "decimals": 18,
        "name": "XPRESS TOKEN",
        "address": "0xaa9826732f3a4973ff8b384b3f4e3c70c2984651"
    },
    "XPX": {
        "symbol": "XPX",
        "decimals": 6,
        "name": "XPX",
        "address": "0x6f3aaf802f57d045efdd2ac9c06d8879305542af"
    },
    "XROW": {
        "symbol": "XROW",
        "decimals": 18,
        "name": "XROW",
        "address": "0x7cc1c126be3128c1f0441a893cd6220498b27650"
    },
    "XRPC": {
        "symbol": "XRPC",
        "decimals": 18,
        "name": "Xrp Classic",
        "address": "0x30c54d82564aee6a56755f80aa4bbdf2e5093322"
    },
    "XRX": {
        "symbol": "XRX",
        "decimals": 18,
        "name": "REX",
        "address": "0xb25583e5e2db32b7fcbffe3f5e8e305c36157e54"
    },
    "XTM": {
        "symbol": "XTM",
        "decimals": 18,
        "name": "Torum",
        "address": "0xcd1faff6e578fa5cac469d2418c95671ba1a62fe"
    },
    "XTZ": {
        "symbol": "XTZ",
        "decimals": 18,
        "name": "Tezos Token",
        "address": "0x16939ef78684453bfdfb47825f8a5f714f12623a"
    },
    "XVS": {
        "symbol": "XVS",
        "decimals": 18,
        "name": "Venus",
        "address": "0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63"
    },
    "XWG": {
        "symbol": "XWG",
        "decimals": 18,
        "name": "XWG",
        "address": "0x6b23c89196deb721e6fd9726e6c76e4810a464bc"
    },
    "XWIN": {
        "symbol": "XWIN",
        "decimals": 18,
        "name": "xWIN Token",
        "address": "0xd88ca08d8eec1e9e09562213ae83a7853ebb5d28"
    },
    "XY": {
        "symbol": "XY",
        "decimals": 18,
        "name": "XY Token",
        "address": "0x666666661f9b6d8c581602aaa2f76cbead06c401"
    },
    "xYSL": {
        "symbol": "xYSL",
        "decimals": 18,
        "name": "xYSL token",
        "address": "0x0047a0deadafb7ee6b1a0d219e70fb6767057d93"
    },
    "YACHT": {
        "symbol": "YACHT",
        "decimals": 18,
        "name": "YachtingVerse",
        "address": "0x0f208f5ea1d4fbca61ac6b6754f765950d3840de"
    },
    "YAE": {
        "symbol": "YAE",
        "decimals": 18,
        "name": "Cryptonovae",
        "address": "0x4ee438be38f8682abb089f2bfea48851c5e71eaf"
    },
    "YAG": {
        "symbol": "YAG",
        "decimals": 18,
        "name": "Yaki Gold",
        "address": "0x2722c9db0fc6818dc9dd3a01254afc3804438b64"
    },
    "YAY": {
        "symbol": "YAY",
        "decimals": 18,
        "name": "YAY Games",
        "address": "0x524df384bffb18c0c8f3f43d012011f8f9795579"
    },
    "YCT": {
        "symbol": "YCT",
        "decimals": 18,
        "name": "YouClout",
        "address": "0x23e3981052d5280c658e5e18d814fa9582bfbc9e"
    },
    "YEL": {
        "symbol": "YEL",
        "decimals": 18,
        "name": "YEL Token",
        "address": "0xd3b71117e6c1558c1553305b44988cd944e97300"
    },
    "YEON": {
        "symbol": "YEON",
        "decimals": 8,
        "name": "YEON",
        "address": "0x84b1270f5a858dc25db8cc005fff27fbf6c8afd2"
    },
    "YES": {
        "symbol": "YES",
        "decimals": 18,
        "name": "YES WORLD",
        "address": "0xb9d35811424600fa9e8cd62a0471fbd025131cb8"
    },
    "YFI": {
        "symbol": "YFI",
        "decimals": 18,
        "name": "yearn.finance",
        "address": "0x88f1a5ae2a3bf98aeaf342d26b30a79438c9142e"
    },
    "YFIH2": {
        "symbol": "YFIH2",
        "decimals": 18,
        "name": "YFIH2",
        "address": "0xdcb624c870d73cdd0b3345762977cb14de598cd0"
    },
    "YFII": {
        "symbol": "YFII",
        "decimals": 18,
        "name": "YFII.finance Token",
        "address": "0x7f70642d88cf1c4a3a7abb072b53b929b653eda5"
    },
    "YFX": {
        "symbol": "YFX",
        "decimals": 18,
        "name": "YFX",
        "address": "0xf55a93b613d172b86c2ba3981a849dae2aecde2f"
    },
    "YIN": {
        "symbol": "YIN",
        "decimals": 18,
        "name": "YIN Finance",
        "address": "0x794baab6b878467f93ef17e2f2851ce04e3e34c8"
    },
    "YOCO": {
        "symbol": "YOCO",
        "decimals": 9,
        "name": "YoCoin",
        "address": "0xdd17629d05e068a9d118ee35d11101d4140d0586"
    },
    "YON": {
        "symbol": "YON",
        "decimals": 18,
        "name": "YES||NO",
        "address": "0xb8c3e8ff71513afc8cfb2dddc5a994a501db1916"
    },
    "YOOSHI": {
        "symbol": "YOOSHI",
        "decimals": 9,
        "name": "YOOSHI",
        "address": "0x02ff5065692783374947393723dba9599e59f591"
    },
    "YOSHI": {
        "symbol": "YOSHI",
        "decimals": 18,
        "name": "Yoshi.exchange",
        "address": "0x4374f26f0148a6331905edf4cd33b89d8eed78d1"
    },
    "YourWallet": {
        "symbol": "YourWallet",
        "decimals": 18,
        "name": "YourWallet",
        "address": "0x4aaf59dee18ecc1bbd2bf68b3f7ba3af47eb9cfc"
    },
    "YU": {
        "symbol": "YU",
        "decimals": 18,
        "name": "BOUNTYKINDS YU",
        "address": "0x3e098c23dcfbbe0a3f468a6bed1cf1a59dc1770d"
    },
    "YUSE": {
        "symbol": "YUSE",
        "decimals": 18,
        "name": "Yuse Token",
        "address": "0x8526ff6bbd8a976127443b1ce451ca1044aa3ce2"
    },
    "ZADA": {
        "symbol": "ZADA",
        "decimals": 18,
        "name": "Zada",
        "address": "0xfcadd830ff2d6cf3ad1681e1e8fc5ddce9d59e74"
    },
    "ZAFI": {
        "symbol": "ZAFI",
        "decimals": 18,
        "name": "ZakumiFi",
        "address": "0x2efdff1e566202f82e774bb7add18c56cbb9427d"
    },
    "ZAM": {
        "symbol": "ZAM",
        "decimals": 18,
        "name": "Zamzam",
        "address": "0xbbcf57177d8752b21d080bf30a06ce20ad6333f8"
    },
    "ZAMZAM": {
        "symbol": "ZAMZAM",
        "decimals": 18,
        "name": "ZAMZAM Token",
        "address": "0xa5e279e14efd60a8f29e5ac3b464e3de0c6bb6b8"
    },
    "ZAP": {
        "symbol": "ZAP",
        "decimals": 18,
        "name": "ZAP TOKEN",
        "address": "0xc5326b32e8baef125acd68f8bc646fd646104f1c"
    },
    "ZAX": {
        "symbol": "ZAX",
        "decimals": 9,
        "name": "ZILLION AAKAR XO",
        "address": "0x9a2478c4036548864d96a97fbf93f6a3341fedac"
    },
    "ZEC": {
        "symbol": "ZEC",
        "decimals": 18,
        "name": "Zcash Token",
        "address": "0x1ba42e5193dfa8b03d15dd1b86a3113bbbef8eeb"
    },
    "ZEE": {
        "symbol": "ZEE",
        "decimals": 18,
        "name": "ZeroSwapToken",
        "address": "0x44754455564474a89358b2c2265883df993b12f0"
    },
    "ZEFU": {
        "symbol": "ZEFU",
        "decimals": 18,
        "name": "Zenfuse Trading Platform Token (BSC)",
        "address": "0x23ec58e45ac5313bcb6681f4f7827b8a8453ac45"
    },
    "ZENIQ": {
        "symbol": "ZENIQ",
        "decimals": 18,
        "name": "ZENIQ",
        "address": "0x5b52bfb8062ce664d74bbcd4cd6dc7df53fd7233"
    },
    "ZENITH": {
        "symbol": "ZENITH",
        "decimals": 18,
        "name": "Zenith Coin",
        "address": "0x57c81885faad67fc4de892102f6fead3b9215f6b"
    },
    "ZEUM": {
        "symbol": "ZEUM",
        "decimals": 18,
        "name": "Colizeum",
        "address": "0x482e6bd0a178f985818c5dfb9ac77918e8412fba"
    },
    "ZFM": {
        "symbol": "ZFM",
        "decimals": 18,
        "name": "ZFM Coin",
        "address": "0xce6b8b2787c657f1b98b7a66b5b63178863fd719"
    },
    "ZGD": {
        "symbol": "ZGD",
        "decimals": 18,
        "name": "ZambesiGold",
        "address": "0xbf27da33a58de2bc6eb1c7dab6cf2e84e825d7dc"
    },
    "ZIBU": {
        "symbol": "ZIBU",
        "decimals": 18,
        "name": "Zibu",
        "address": "0x580e2b3170aa36e7018ead248298c8cc18b0f019"
    },
    "ZIL": {
        "symbol": "ZIL",
        "decimals": 12,
        "name": "Zilliqa",
        "address": "0xb86abcb37c3a4b64f74f59301aff131a1becc787"
    },
    "ZINU": {
        "symbol": "ZINU",
        "decimals": 9,
        "name": "ZINU",
        "address": "0x80640a39cfc2b1b7c792821c462376aa7083f5a8"
    },
    "ZIX": {
        "symbol": "ZIX",
        "decimals": 18,
        "name": "Coinzix Token",
        "address": "0x48077400faf11183c043feb5184a13ea628bb0db"
    },
    "ZLW": {
        "symbol": "ZLW",
        "decimals": 18,
        "name": "ZELWIN",
        "address": "0x5dd1e31e1a0e2e077ac98d2a4b781f418ca50387"
    },
    "ZMBE": {
        "symbol": "ZMBE",
        "decimals": 18,
        "name": "Zombie Token",
        "address": "0x50ba8bf9e34f0f83f96a340387d1d3888ba4b3b5"
    },
    "ZMN": {
        "symbol": "ZMN",
        "decimals": 18,
        "name": "ZMINE Token",
        "address": "0xfcb8a4b1a0b645e08064e05b98e9cc6f48d2aa57"
    },
    "ZNX": {
        "symbol": "ZNX",
        "decimals": 6,
        "name": "ZeNeX Coin",
        "address": "0xc2eb046621b59f604c7abdb1600d01636adc4fed"
    },
    "ZOA": {
        "symbol": "ZOA",
        "decimals": 18,
        "name": "ZOA",
        "address": "0xb2e841894b1c3d638948517f6234c6e06d3b8e1c"
    },
    "ZODI": {
        "symbol": "ZODI",
        "decimals": 18,
        "name": "Zodium",
        "address": "0x0cca2f5561bb0fca88e5b9b48b7fbf000349c357"
    },
    "ZOGI": {
        "symbol": "ZOGI",
        "decimals": 18,
        "name": "Zogi",
        "address": "0x41080ca7be4b3f0cacbd95164e9a56b582382caa"
    },
    "Zoo": {
        "symbol": "Zoo",
        "decimals": 18,
        "name": "ZooToken",
        "address": "0x1d229b958d5ddfca92146585a8711aecbe56f095"
    },
    "ZOON": {
        "symbol": "ZOON",
        "decimals": 18,
        "name": "CryptoZoon",
        "address": "0x9d173e6c594f479b4d47001f8e6a95a7adda42bc"
    },
    "ZUKI": {
        "symbol": "ZUKI",
        "decimals": 18,
        "name": "ZUKI MOBA",
        "address": "0xe81257d932280ae440b17afc5f07c8a110d21432"
    },
    "ZUM": {
        "symbol": "ZUM",
        "decimals": 9,
        "name": "ZumToken",
        "address": "0x54c2c07b3af037567269ad6a168d5bd527867b58"
    }
}
