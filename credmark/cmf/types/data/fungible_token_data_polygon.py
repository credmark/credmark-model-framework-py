# pylint:disable=too-many-lines

POLYGON_TOKENS = {
    "ETH": {
        "symbol": "ETH",
        "decimals": 18,
        "name": "Ethereum",
        "address": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
        "set_loaded": True
    },
    "BTC": {
        "symbol": "BTC",
        "decimals": 8,
        "name": "Bitcoin",
        "address": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "set_loaded": True
    },
    "MATIC": {
        "symbol": "MATIC",
        "decimals": 18,
        "name": "Matic Token",
        "address": "0x0000000000000000000000000000000000001010",
        "is_native_token": True
    },
    "WMATIC": {
        "symbol": "WMATIC",
        "decimals": 18,
        "name": "Wrapped Matic",
        "address": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
    },
    "WBTC": {
        "symbol": "WBTC",
        "decimals": 8,
        "name": "(PoS) Wrapped BTC",
        "address": "0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"
    },
    "WETH": {
        "symbol": "WETH",
        "decimals": 18,
        "name": "Wrapped Ether",
        "address": "0x7ceb23fd6bc0add59e62ac25578270cff1b9f619"
    },
    ####
    "$ANRX": {
        "symbol": "$ANRX",
        "decimals": 18,
        "name": "AnRKey X (PoS)",
        "address": "0x554f074d9ccda8f483d1812d4874cbebd682644e"
    },
    "$DG": {
        "symbol": "$DG",
        "decimals": 18,
        "name": "decentral.games (PoS)",
        "address": "0x2a93172c8dccbfbc60a39d56183b7279a2f647b4"
    },
    "$KMC": {
        "symbol": "$KMC",
        "decimals": 18,
        "name": "$KMC",
        "address": "0x44d09156c7b4acf0c64459fbcced7613f5519918"
    },
    "$ZKP": {
        "symbol": "$ZKP",
        "decimals": 18,
        "name": "$ZKP Token",
        "address": "0x9a06db14d639796b25a6cec6a1bf614fd98815ec"
    },
    "0xBTC": {
        "symbol": "0xBTC",
        "decimals": 8,
        "name": "0xBitcoin Token",
        "address": "0x71b821aa52a49f32eed535fca6eb5aa130085978"
    },
    "1FLR": {
        "symbol": "1FLR",
        "decimals": 18,
        "name": "Flare Token",
        "address": "0x5f0197ba06860dac7e31258bdf749f92b6a636d4"
    },
    "1INCH": {
        "symbol": "1INCH",
        "decimals": 18,
        "name": "1Inch (PoS)",
        "address": "0x9c2c5fd7b07e95ee044ddeba0e97a665f142394f"
    },
    "AAA": {
        "symbol": "AAA",
        "decimals": 18,
        "name": "MoonRabbit",
        "address": "0x2ebd50ae084e71eed419cb6c620b3bbd3927bf7e"
    },
    "AAVE": {
        "symbol": "AAVE",
        "decimals": 18,
        "name": "Aave (PoS)",
        "address": "0xd6df932a45c0f255f85145f286ea0b292b21c90b"
    },
    "ABI": {
        "symbol": "ABI",
        "decimals": 9,
        "name": "Abachi",
        "address": "0x6d5f5317308c6fe7d6ce16930353a8dfd92ba4d7"
    },
    "ADDY": {
        "symbol": "ADDY",
        "decimals": 18,
        "name": "Adamant",
        "address": "0xc3fdbadc7c795ef1d6ba111e06ff8f16a20ea539"
    },
    "ADS": {
        "symbol": "ADS",
        "decimals": 11,
        "name": "Adshares (PoS)",
        "address": "0x598e49f01befeb1753737934a5b11fea9119c796"
    },
    "ADX": {
        "symbol": "ADX",
        "decimals": 18,
        "name": "AdEx Network (PoS)",
        "address": "0xdda7b23d2d72746663e7939743f929a3d85fc975"
    },
    "AGA": {
        "symbol": "AGA",
        "decimals": 4,
        "name": "AGA Token (PoS)",
        "address": "0x033d942a6b495c4071083f4cde1f17e986fe856c"
    },
    "agEUR": {
        "symbol": "agEUR",
        "decimals": 18,
        "name": "agEUR",
        "address": "0xe0b52e49357fd4daf2c15e02058dce6bc0057db4"
    },
    "AIDI": {
        "symbol": "AIDI",
        "decimals": 18,
        "name": "Aidi Finance",
        "address": "0xdfc2c4ce66561c3ee53dbea9ff78550f395a25e2"
    },
    "AIMX": {
        "symbol": "AIMX",
        "decimals": 18,
        "name": "Aimedis",
        "address": "0x33b6d77c607ea499ab5db7e2201c5a516a78a5db"
    },
    "ALCX": {
        "symbol": "ALCX",
        "decimals": 18,
        "name": "Alchemix (PoS)",
        "address": "0x95c300e7740d2a88a44124b424bfc1cb2f9c3b89"
    },
    "ALGB": {
        "symbol": "ALGB",
        "decimals": 18,
        "name": "Algebra",
        "address": "0x0169ec1f8f639b32eec6d923e24c2a2ff45b9dd6"
    },
    "ALI": {
        "symbol": "ALI",
        "decimals": 18,
        "name": "Artificial Liquid Intelligence Token",
        "address": "0xbfc70507384047aa74c29cdc8c5cb88d0f7213ac"
    },
    "ALM": {
        "symbol": "ALM",
        "decimals": 18,
        "name": "AliumToken on Polygon",
        "address": "0x1581929770be3275a82068c1135b6dd59c5334ed"
    },
    "ALN": {
        "symbol": "ALN",
        "decimals": 18,
        "name": "Aluna (PoS)",
        "address": "0xa8fcee762642f156b5d757b6fabc36e06b6d4a1a"
    },
    "ALPHA": {
        "symbol": "ALPHA",
        "decimals": 18,
        "name": "Aavegotchi ALPHA",
        "address": "0x6a3e7c3c6ef65ee26975b12293ca1aad7e1daed2"
    },
    "AMA": {
        "symbol": "AMA",
        "decimals": 18,
        "name": "AMAUROT",
        "address": "0x372246175d50db4fd42c2aba4e3292a0fe41ce2e"
    },
    "AMKT": {
        "symbol": "AMKT",
        "decimals": 18,
        "name": "Alongside Crypto Market Index (PoS)",
        "address": "0xb87904db461005fc716a6bf9f2d451c33b10b80b"
    },
    "ANKR": {
        "symbol": "ANKR",
        "decimals": 18,
        "name": "Ankr (PoS)",
        "address": "0x101a023270368c0d50bffb62780f4afd4ea79c35"
    },
    "ankrMATIC": {
        "symbol": "ankrMATIC",
        "decimals": 18,
        "name": "Ankr Staked MATIC",
        "address": "0x0e9b89007eee9c958c0eda24ef70723c2c93dd58"
    },
    "ANML": {
        "symbol": "ANML",
        "decimals": 18,
        "name": "Animal Concerts Token (PoS)",
        "address": "0xecc4176b90613ed78185f01bd1e42c5640c4f09d"
    },
    "ANT": {
        "symbol": "ANT",
        "decimals": 18,
        "name": "Aragon Network Token (PoS)",
        "address": "0x2b8504ab5efc246d0ec5ec7e74565683227497de"
    },
    "ANY": {
        "symbol": "ANY",
        "decimals": 18,
        "name": "Anyswap",
        "address": "0x6ab6d61428fde76768d7b45d8bfeec19c6ef91a8"
    },
    "APE": {
        "symbol": "APE",
        "decimals": 18,
        "name": "ApeCoin (PoS)",
        "address": "0xb7b31a6bc18e48888545ce79e83e06003be70930"
    },
    "ARIA20": {
        "symbol": "ARIA20",
        "decimals": 18,
        "name": "ARIANEE (PoS)",
        "address": "0x46f48fbdedaa6f5500993bede9539ef85f4bee8e"
    },
    "ARPA": {
        "symbol": "ARPA",
        "decimals": 18,
        "name": "ARPA Token (PoS)",
        "address": "0xee800b277a96b0f490a1a732e1d6395fad960a26"
    },
    "ASIA": {
        "symbol": "ASIA",
        "decimals": 18,
        "name": "ASIA COIN (PoS)",
        "address": "0x50bcbc40306230713239ae1bddd5eefeeaa273dc"
    },
    "ASK": {
        "symbol": "ASK",
        "decimals": 18,
        "name": "Permission Token",
        "address": "0xaa3717090cddc9b227e49d0d84a28ac0a996e6ff"
    },
    "ASTRAFER": {
        "symbol": "ASTRAFER",
        "decimals": 18,
        "name": "Astrafer",
        "address": "0xdfce1e99a31c4597a3f8a8945cbfa9037655e335"
    },
    "ATA": {
        "symbol": "ATA",
        "decimals": 18,
        "name": "Automata (PoS)",
        "address": "0x0df0f72ee0e5c9b7ca761ecec42754992b2da5bf"
    },
    "ATK": {
        "symbol": "ATK",
        "decimals": 18,
        "name": "Attack",
        "address": "0xf868939ee81f04f463010bc52eab91c0839ef08c"
    },
    "ATOM": {
        "symbol": "ATOM",
        "decimals": 6,
        "name": "Cosmos (PoS)",
        "address": "0xac51c4c48dc3116487ed4bc16542e27b5694da1b"
    },
    "AUDIO": {
        "symbol": "AUDIO",
        "decimals": 18,
        "name": "Audius (PoS)",
        "address": "0x5eb8d998371971d01954205c7afe90a7af6a95ac"
    },
    "AUDT": {
        "symbol": "AUDT",
        "decimals": 18,
        "name": "Auditchain",
        "address": "0x91c5a5488c0decde1eacd8a4f10e0942fb925067"
    },
    "AURUM": {
        "symbol": "AURUM",
        "decimals": 18,
        "name": "RaiderAurum",
        "address": "0x34d4ab47bee066f361fa52d792e69ac7bd05ee23"
    },
    "AVAX": {
        "symbol": "AVAX",
        "decimals": 18,
        "name": "Avalanche Token",
        "address": "0x2c89bbc92bd86f8075d1decc58c7f4e0107f286b"
    },
    "AX": {
        "symbol": "AX",
        "decimals": 18,
        "name": "AurusX",
        "address": "0x1a763170b96f23f15576d0fa0b2619d1254c437d"
    },
    "AXIA": {
        "symbol": "AXIA",
        "decimals": 18,
        "name": "Axia (axiaprotocol.io)",
        "address": "0x49690541e3f6e933a9aa3cffee6010a7bb5b72d7"
    },
    "AXL": {
        "symbol": "AXL",
        "decimals": 6,
        "name": "Axelar",
        "address": "0x6e4e624106cb12e168e6533f8ec7c82263358940"
    },
    "axlUSDC": {
        "symbol": "axlUSDC",
        "decimals": 6,
        "name": "Axelar Wrapped USDC",
        "address": "0x750e4c4984a9e0f12978ea6742bc1c5d248f40ed"
    },
    "AXN": {
        "symbol": "AXN",
        "decimals": 18,
        "name": "Axion",
        "address": "0x839f1a22a59eaaf26c85958712ab32f80fea23d9"
    },
    "AXS": {
        "symbol": "AXS",
        "decimals": 18,
        "name": "Axie Infinity Shard (PoS)",
        "address": "0x61bdd9c7d4df4bf47a4508c0c8245505f2af5b7b"
    },
    "AZUKI": {
        "symbol": "AZUKI",
        "decimals": 18,
        "name": "DokiDokiAzuki",
        "address": "0x7cdc0421469398e0f3aa8890693d86c840ac8931"
    },
    "B2M": {
        "symbol": "B2M",
        "decimals": 18,
        "name": "Bit2Me",
        "address": "0xe613a914bbb433855378183c3ab13003285da40a"
    },
    "BADGER": {
        "symbol": "BADGER",
        "decimals": 18,
        "name": "Badger (PoS)",
        "address": "0x1fcbe5937b0cc2adf69772d228fa4205acf4d9b2"
    },
    "BAKED": {
        "symbol": "BAKED",
        "decimals": 18,
        "name": "BakedToken (PoS)",
        "address": "0x32515ffdc3a84cfbf9ad4db14ef8f0a535c7afd6"
    },
    "BAL": {
        "symbol": "BAL",
        "decimals": 18,
        "name": "Balancer (PoS)",
        "address": "0x9a71012b13ca4d3d0cdc72a177df3ef03b0e76a3"
    },
    "BANANA": {
        "symbol": "BANANA",
        "decimals": 18,
        "name": "ApeSwapFinance Banana",
        "address": "0x5d47baba0d66083c52009271faf3f50dcc01023c"
    },
    "BANK": {
        "symbol": "BANK",
        "decimals": 18,
        "name": "Bankless Token (PoS)",
        "address": "0xdb7cb471dd0b49b29cab4a1c14d070f27216a0ab"
    },
    "BAT": {
        "symbol": "BAT",
        "decimals": 18,
        "name": "Basic Attention Token (PoS)",
        "address": "0x3cef98bb43d732e2f285ee605a8158cde967d219"
    },
    "BCMC": {
        "symbol": "BCMC",
        "decimals": 18,
        "name": "Blockchain Monster Coin",
        "address": "0xc10358f062663448a3489fc258139944534592ac"
    },
    "BCT": {
        "symbol": "BCT",
        "decimals": 18,
        "name": "Toucan Protocol: Base Carbon Tonne",
        "address": "0x2f800db0fdb5223b3c3f354886d907a671414a7f"
    },
    "BEAT": {
        "symbol": "BEAT",
        "decimals": 18,
        "name": "METABEAT",
        "address": "0xb78cf9ac0f47f1d69cba861deda29814d285c834"
    },
    "bECH": {
        "symbol": "bECH",
        "decimals": 18,
        "name": "Bridged Echelon",
        "address": "0xa3bac05723c35aa0b30ea63f5a5e9986465a9391"
    },
    "BETS": {
        "symbol": "BETS",
        "decimals": 18,
        "name": "BetSwirl Token",
        "address": "0x9246a5f10a79a5a939b0c2a75a3ad196aafdb43b"
    },
    "BIFI": {
        "symbol": "BIFI",
        "decimals": 18,
        "name": "beefy.finance",
        "address": "0xfbdd194376de19a88118e84e279b977f165d01b8"
    },
    "BLANK": {
        "symbol": "BLANK",
        "decimals": 18,
        "name": "GoBlank Token (PoS)",
        "address": "0xf4c83080e80ae530d6f8180572cbbf1ac9d5d435"
    },
    "BLKC": {
        "symbol": "BLKC",
        "decimals": 8,
        "name": "BlackHat",
        "address": "0x8626264b6a1b4e920905efd381002aba52ea0eea"
    },
    "BLOK": {
        "symbol": "BLOK",
        "decimals": 18,
        "name": "BLOK",
        "address": "0x229b1b6c23ff8953d663c4cbb519717e323a0a84"
    },
    "BNB": {
        "symbol": "BNB",
        "decimals": 18,
        "name": "Binance",
        "address": "0xa649325aa7c5093d12d6f98eb4378deae68ce23f"
    },
    "BNT": {
        "symbol": "BNT",
        "decimals": 18,
        "name": "Bancor Network Token (PoS)",
        "address": "0xc26d47d5c33ac71ac5cf9f776d63ba292a4f7842"
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
        "name": "bobcoin",
        "address": "0x590eb2920486486c2d9bb3eb651f73b81df87bcf"
    },
    "BOLLY": {
        "symbol": "BOLLY",
        "decimals": 18,
        "name": "Bollycoin (PoS)",
        "address": "0x7dc47cfb674beb5827283f6140f635680a5ce992"
    },
    "BOND": {
        "symbol": "BOND",
        "decimals": 18,
        "name": "BarnBridge Governance Token (PoS)",
        "address": "0xa041544fe2be56cce31ebb69102b965e06aace80"
    },
    "BONDLY": {
        "symbol": "BONDLY",
        "decimals": 18,
        "name": "Bondly (PoS)",
        "address": "0x64ca1571d1476b7a21c5aaf9f1a750a193a103c0"
    },
    "BONE": {
        "symbol": "BONE",
        "decimals": 18,
        "name": "Bone Token",
        "address": "0x6bb45ceac714c52342ef73ec663479da35934bf7"
    },
    "BOSON": {
        "symbol": "BOSON",
        "decimals": 18,
        "name": "Boson Token (PoS)",
        "address": "0x9b3b0703d392321ad24338ff1f846650437a43c9"
    },
    "BRIDGE": {
        "symbol": "BRIDGE",
        "decimals": 18,
        "name": "Cross-Chain Bridge Token",
        "address": "0x92868a5255c628da08f550a858a802f5351c5223"
    },
    "BS": {
        "symbol": "BS",
        "decimals": 18,
        "name": "BlackStallion",
        "address": "0x0c47298beee5203358e7bc30b9954b584361eab5"
    },
    "BUILD": {
        "symbol": "BUILD",
        "decimals": 18,
        "name": "Build Token",
        "address": "0xe94845ac6782a2e71c407abe4d5201445c26a62b"
    },
    "BULL": {
        "symbol": "BULL",
        "decimals": 18,
        "name": "Bullieverse",
        "address": "0x9f95e17b2668afe01f8fbd157068b0a4405cc08d"
    },
    "BURP": {
        "symbol": "BURP",
        "decimals": 18,
        "name": "Burp (PoS)",
        "address": "0x538d47d142f6993038a667e9d6210d3735749b36"
    },
    "BUSD": {
        "symbol": "BUSD",
        "decimals": 18,
        "name": "(PoS) Binance USD",
        "address": "0xdab529f40e671a1d4bf91361c21bf9f0c9712ab7"
    },
    "BWO": {
        "symbol": "BWO",
        "decimals": 18,
        "name": "Battle World",
        "address": "0xc1543024dc71247888a7e139c644f44e75e96d38"
    },
    "BYN": {
        "symbol": "BYN",
        "decimals": 18,
        "name": "Beyond Finance (PoS)",
        "address": "0x11602a402281974a70c2b4824d58ebede967e2be"
    },
    "C98": {
        "symbol": "C98",
        "decimals": 18,
        "name": "Coin98",
        "address": "0x77f56cf9365955486b12c4816992388ee8606f0e"
    },
    "CATHEON": {
        "symbol": "CATHEON",
        "decimals": 9,
        "name": "Catheon Gaming",
        "address": "0x7e7737c40878e720b32e7bc9cd096259f876d69f"
    },
    "CDT": {
        "symbol": "CDT",
        "decimals": 18,
        "name": "CheckDot",
        "address": "0x26c80854c36ff62bba7414a358c8c23bbb8dec39"
    },
    "CEL": {
        "symbol": "CEL",
        "decimals": 4,
        "name": "Celsius (PoS)",
        "address": "0xd85d1e945766fea5eda9103f918bd915fbca63e6"
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
        "name": "CyberFi Token (PoS)",
        "address": "0xecf8f2fa183b1c4d2a269bf98a54fce86c812d3e"
    },
    "CGG": {
        "symbol": "CGG",
        "decimals": 18,
        "name": "ChainGuardians Governance Token (PoS)",
        "address": "0x2ab4f9ac80f33071211729e45cfc346c1f8446d5"
    },
    "CGL": {
        "symbol": "CGL",
        "decimals": 18,
        "name": "Crypto Gladiator League",
        "address": "0x2627c26b33f5193da4adfb26df60202479ccd2d3"
    },
    "CGU": {
        "symbol": "CGU",
        "decimals": 8,
        "name": "Crypto Gaming United",
        "address": "0x709d140925272ee606825781b1bef7be6b1412cd"
    },
    "CHAIN": {
        "symbol": "CHAIN",
        "decimals": 18,
        "name": "Chain Games",
        "address": "0xd55fce7cdab84d84f2ef3f99816d765a2a94a509"
    },
    "CHAMP": {
        "symbol": "CHAMP",
        "decimals": 18,
        "name": "Ultimate Champions Token",
        "address": "0xed755dba6ec1eb520076cec051a582a6d81a8253"
    },
    "CHER": {
        "symbol": "CHER",
        "decimals": 18,
        "name": "Cherry Token",
        "address": "0x8f36cc333f55b09bb71091409a3d7ade399e3b1c"
    },
    "CHP": {
        "symbol": "CHP",
        "decimals": 18,
        "name": "CoinPoker Chips (PoS)",
        "address": "0x59b5654a17ac44f3068b3882f298881433bb07ef"
    },
    "CHZ": {
        "symbol": "CHZ",
        "decimals": 18,
        "name": "CHZ (PoS)",
        "address": "0xf1938ce12400f9a761084e7a80d37e732a4da056"
    },
    "CIOTX": {
        "symbol": "CIOTX",
        "decimals": 18,
        "name": "Crosschain IOTX",
        "address": "0x300211def2a644b036a9bdd3e58159bb2074d388"
    },
    "CIRUS": {
        "symbol": "CIRUS",
        "decimals": 18,
        "name": "Cirus (PoS)",
        "address": "0x2a82437475a60bebd53e33997636fade77604fc2"
    },
    "CIV": {
        "symbol": "CIV",
        "decimals": 18,
        "name": "Civilization (PoS)",
        "address": "0x42f6bdcfd82547e89f1069bf375aa60e6c6c063d"
    },
    "CLAM": {
        "symbol": "CLAM",
        "decimals": 9,
        "name": "Otter Clam",
        "address": "0xc250e9987a032acac293d838726c511e6e1c029d"
    },
    "CNTR": {
        "symbol": "CNTR",
        "decimals": 18,
        "name": "Centaur Token (PoS)",
        "address": "0xdae89da41a96956e9e70320ac9c0dd077070d3a5"
    },
    "COMBO": {
        "symbol": "COMBO",
        "decimals": 18,
        "name": "Furucombo (PoS)",
        "address": "0x6ddb31002abc64e1479fc439692f7ea061e78165"
    },
    "COMP": {
        "symbol": "COMP",
        "decimals": 18,
        "name": "(PoS) Compound",
        "address": "0x8505b9d2254a7ae468c0e9dd10ccea3a837aef5c"
    },
    "COR": {
        "symbol": "COR",
        "decimals": 18,
        "name": "Coreto (PoS)",
        "address": "0x4fdce518fe527439fe76883e6b51a1c522b61b7c"
    },
    "COT": {
        "symbol": "COT",
        "decimals": 18,
        "name": "CosplayToken (PoS)",
        "address": "0x8d520c8e66091cfd6743fe37fbe3a09505616c4b"
    },
    "COVAL": {
        "symbol": "COVAL",
        "decimals": 8,
        "name": "Circuits of Value V2",
        "address": "0x4597c8a59ab28b36840b82b3a674994a279593d0"
    },
    "CP": {
        "symbol": "CP",
        "decimals": 18,
        "name": "Cookies Protocol",
        "address": "0xf9d3d8b25b95bcda979025b74fdfa7ac3f380f9f"
    },
    "CPD": {
        "symbol": "CPD",
        "decimals": 18,
        "name": "Coinspaid (PoS)",
        "address": "0x1ce4a2c355f0dcc24e32a9af19f1836d6f4f98ae"
    },
    "CPR": {
        "symbol": "CPR",
        "decimals": 2,
        "name": "CIPHER",
        "address": "0xaa404804ba583c025fa64c9a276a6127ceb355c6"
    },
    "CRBN": {
        "symbol": "CRBN",
        "decimals": 18,
        "name": "Carbon (PoS)",
        "address": "0x89ef0900b0a6b5548ab2ff58ef588f9433b5fcf5"
    },
    "CRETA": {
        "symbol": "CRETA",
        "decimals": 18,
        "name": "CRETA TOKEN",
        "address": "0x202655af326de310491cb54f120e02ee0da92b55"
    },
    "CRI3X": {
        "symbol": "CRI3X",
        "decimals": 18,
        "name": "CRI3X",
        "address": "0x304243a820d4a3718becc89a3f33513586162cf0"
    },
    "CROWD": {
        "symbol": "CROWD",
        "decimals": 18,
        "name": "CrowdToken",
        "address": "0x483dd3425278c1f79f377f1034d9d2cae55648b6"
    },
    "CRV": {
        "symbol": "CRV",
        "decimals": 18,
        "name": "CRV (PoS)",
        "address": "0x172370d5cd63279efa6d502dab29171933a610af"
    },
    "CTSI": {
        "symbol": "CTSI",
        "decimals": 18,
        "name": "Cartesi Token (PoS)",
        "address": "0x2727ab1c2d22170abc9b595177b2d5c6e1ab7b7b"
    },
    "CUBIX": {
        "symbol": "CUBIX",
        "decimals": 18,
        "name": "CUBIX",
        "address": "0xa0e5c8b2b2e345c72f452880b2c164b944012907"
    },
    "CVC": {
        "symbol": "CVC",
        "decimals": 8,
        "name": "Civic (PoS)",
        "address": "0x66dc5a08091d1968e08c16aa5b27bac8398b02be"
    },
    "CVTX": {
        "symbol": "CVTX",
        "decimals": 18,
        "name": "CarrieVerse Token",
        "address": "0x40f97ec376ac1c503e755433bf57f21e3a49f440"
    },
    "CVX": {
        "symbol": "CVX",
        "decimals": 18,
        "name": "Convex Token (PoS)",
        "address": "0x4257ea7637c355f81616050cbb6a9b709fd72683"
    },
    "CXO": {
        "symbol": "CXO",
        "decimals": 18,
        "name": "CargoX Token (PoS)",
        "address": "0xf2ae0038696774d65e67892c9d301c5f2cbbda58"
    },
    "CYC": {
        "symbol": "CYC",
        "decimals": 18,
        "name": "Cyclone Protocol",
        "address": "0xcfb54a6d2da14abecd231174fc5735b4436965d8"
    },
    "DAFI": {
        "symbol": "DAFI",
        "decimals": 18,
        "name": "DAFI Token (PoS)",
        "address": "0x638df98ad8069a15569da5a6b01181804c47e34c"
    },
    "DAI": {
        "symbol": "DAI",
        "decimals": 18,
        "name": "(PoS) Dai Stablecoin",
        "address": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"
    },
    "DATA": {
        "symbol": "DATA",
        "decimals": 18,
        "name": "Streamr",
        "address": "0x3a9a81d576d83ff21f26f325066054540720fc34"
    },
    "DUSD": {
        "symbol": "DUSD",
        "decimals": 18,
        "name": "Davos.xyz USD",
        "address": "0xec38621e72d86775a89c7422746de1f52bba5320"
    },
    "DBD": {
        "symbol": "DBD",
        "decimals": 18,
        "name": "Day By Day Token (PoS)",
        "address": "0x72b9f88e822cf08b031c2206612b025a82fb303c"
    },
    "DEFIT": {
        "symbol": "DEFIT",
        "decimals": 18,
        "name": "Digital Fitness",
        "address": "0x428360b02c1269bc1c79fbc399ad31d58c1e8fda"
    },
    "DEFY": {
        "symbol": "DEFY",
        "decimals": 18,
        "name": "DEFY (PoS)",
        "address": "0xbf9f916bbda29a7f990f5f55c7607d94d7c3a60b"
    },
    "Deod": {
        "symbol": "Deod",
        "decimals": 18,
        "name": "Decentrawood",
        "address": "0xe77abb1e75d2913b2076dd16049992ffeaca5235"
    },
    "DEP": {
        "symbol": "DEP",
        "decimals": 18,
        "name": "DEAPCOIN (PoS)",
        "address": "0xd0ee109352c6116db0f17f4aa8519cdbfc7e7887"
    },
    "DERC": {
        "symbol": "DERC",
        "decimals": 18,
        "name": "DeRace Token",
        "address": "0xb35fcbcf1fd489fce02ee146599e893fdcdc60e6"
    },
    "DERI": {
        "symbol": "DERI",
        "decimals": 18,
        "name": "Deri (PoS)",
        "address": "0x3d1d2afd191b165d140e3e8329e634665ffb0e5e"
    },
    "DEUS": {
        "symbol": "DEUS",
        "decimals": 18,
        "name": "DEUS",
        "address": "0xde5ed76e7c05ec5e4572cfc88d1acea165109e44"
    },
    "DEXI": {
        "symbol": "DEXI",
        "decimals": 9,
        "name": "DEXIOPROTOCOL",
        "address": "0x65ba64899c2c7dbfdb5130e42e2cc56de281c78b"
    },
    "DF": {
        "symbol": "DF",
        "decimals": 18,
        "name": "dForce (PoS)",
        "address": "0x08c15fa26e519a78a666d19ce5c646d55047e0a3"
    },
    "DFX": {
        "symbol": "DFX",
        "decimals": 18,
        "name": "DFX Token (PoS)",
        "address": "0xe7804d91dfcde7f776c90043e03eaa6df87e6395"
    },
    "DFYN": {
        "symbol": "DFYN",
        "decimals": 18,
        "name": "DFYN Token (PoS)",
        "address": "0xc168e40227e4ebd8c1cae80f7a55a4f0e6d66c97"
    },
    "DG": {
        "symbol": "DG",
        "decimals": 18,
        "name": "Decentral Games (PoS)",
        "address": "0xef938b6da8576a896f6e0321ef80996f4890f9c4"
    },
    "DHT": {
        "symbol": "DHT",
        "decimals": 18,
        "name": "dHedge DAO Token (PoS)",
        "address": "0x8c92e38eca8210f4fcbf17f0951b198dd7668292"
    },
    "DHV": {
        "symbol": "DHV",
        "decimals": 18,
        "name": "DeHive.finance",
        "address": "0x5fcb9de282af6122ce3518cde28b7089c9f97b26"
    },
    "DIMO": {
        "symbol": "DIMO",
        "decimals": 18,
        "name": "Dimo",
        "address": "0xe261d618a959afffd53168cd07d12e37b26761db"
    },
    "DINO": {
        "symbol": "DINO",
        "decimals": 18,
        "name": "DinoSwap (PoS)",
        "address": "0xaa9654becca45b5bdfa5ac646c939c62b527d394"
    },
    "DMAGIC": {
        "symbol": "DMAGIC",
        "decimals": 18,
        "name": "Dark Magic",
        "address": "0x61daecab65ee2a1d5b6032df030f3faa3d116aa7"
    },
    "DMR": {
        "symbol": "DMR",
        "decimals": 18,
        "name": "Dreamr Platform Token (PoS)",
        "address": "0x955ce23f20217a6aa205620b40ede4c9e83d325f"
    },
    "DNXC": {
        "symbol": "DNXC",
        "decimals": 18,
        "name": "DinoX Coin",
        "address": "0xcaf5191fc480f43e4df80106c7695eca56e48b18"
    },
    "DODO": {
        "symbol": "DODO",
        "decimals": 18,
        "name": "DODO bird (PoS)",
        "address": "0xe4bf2864ebec7b7fdf6eeca9bacae7cdfdaffe78"
    },
    "DOG": {
        "symbol": "DOG",
        "decimals": 18,
        "name": "The Doge NFT",
        "address": "0xeee3371b89fc43ea970e908536fcddd975135d8a"
    },
    "DOM": {
        "symbol": "DOM",
        "decimals": 9,
        "name": "Dominium",
        "address": "0x0e2c818fea38e7df50410f772b7d59af20589a62"
    },
    "DOSE": {
        "symbol": "DOSE",
        "decimals": 18,
        "name": "DOSE",
        "address": "0x81382e9693de2afc33f69b70a6c12ca9b3a73f47"
    },
    "DPI": {
        "symbol": "DPI",
        "decimals": 18,
        "name": "DefiPulse Index (PoS)",
        "address": "0x85955046df4668e1dd369d2de9f3aeb98dd2a369"
    },
    "DRC": {
        "symbol": "DRC",
        "decimals": 0,
        "name": "Digital Reserve Currency (PoS)",
        "address": "0xfed16c746cb5bfed009730f9e3e6a673006105c7"
    },
    "DSF": {
        "symbol": "DSF",
        "decimals": 18,
        "name": "Dawn Star Token",
        "address": "0x095bc617b36ab227a379550633dfdcbf43f236f6"
    },
    "DSFR": {
        "symbol": "DSFR",
        "decimals": 4,
        "name": "DIGITAL SWISS FRANC",
        "address": "0xc45abe05e9db3739791d1dc1b1638be8ad68b10b"
    },
    "DSLA": {
        "symbol": "DSLA",
        "decimals": 18,
        "name": "DSLA (PoS)",
        "address": "0xa0e390e9cea0d0e8cd40048ced9fa9ea10d71639"
    },
    "DUCKIES": {
        "symbol": "DUCKIES",
        "decimals": 8,
        "name": "Yellow Duckies",
        "address": "0x18e73a5333984549484348a94f4d219f4fab7b81"
    },
    "DUX": {
        "symbol": "DUX",
        "decimals": 18,
        "name": "DUX",
        "address": "0x623ebda5fc6b271dd597e20ae99927ea9ef8515e"
    },
    "EAT": {
        "symbol": "EAT",
        "decimals": 18,
        "name": "Edge Activity Token",
        "address": "0x7c58d971a5dabd46bc85e81fdae87b511431452e"
    },
    "EDAT": {
        "symbol": "EDAT",
        "decimals": 18,
        "name": "EnviDa",
        "address": "0xdd9ba3b2571bea0854beb0508ce10fed0eca7e3e"
    },
    "EDG": {
        "symbol": "EDG",
        "decimals": 18,
        "name": "Edgeware",
        "address": "0x6e7118b82fb9608342c288a90eeb5e614aaee2e9"
    },
    "EGX": {
        "symbol": "EGX",
        "decimals": 6,
        "name": "ENEGRA",
        "address": "0x8db0a6d1b06950b4e81c4f67d1289fc7b9359c7f"
    },
    "ELAND": {
        "symbol": "ELAND",
        "decimals": 18,
        "name": "Etherland (PoS)",
        "address": "0xb0f61c597bbcc29f3f38396b01f9c0f0c2e8bff0"
    },
    "ELK": {
        "symbol": "ELK",
        "decimals": 18,
        "name": "Elk",
        "address": "0xeeeeeb57642040be42185f49c52f7e9b38f8eeee"
    },
    "ELON": {
        "symbol": "ELON",
        "decimals": 18,
        "name": "Dogelon (PoS)",
        "address": "0xe0339c80ffde91f3e20494df88d4206d86024cdf"
    },
    "eLunr": {
        "symbol": "eLunr",
        "decimals": 4,
        "name": "Ethereum-bridged Lunr Token",
        "address": "0xbbfe0b60de96a189bf09079de86a2db7bf0c7883"
    },
    "EMON": {
        "symbol": "EMON",
        "decimals": 18,
        "name": "EthermonToken",
        "address": "0xd6a5ab46ead26f49b03bbb1f9eb1ad5c1767974a"
    },
    "ENJ": {
        "symbol": "ENJ",
        "decimals": 18,
        "name": "Enjin Coin (PoS)",
        "address": "0x7ec26842f195c852fa843bb9f6d8b583a274a157"
    },
    "EPILLO": {
        "symbol": "EPILLO",
        "decimals": 18,
        "name": "EPILLO",
        "address": "0x7a6168e5a0ecc9841ad8fad20dcfcc4458fef0fb"
    },
    "eQUAD": {
        "symbol": "eQUAD",
        "decimals": 18,
        "name": "Quadrant Protocol",
        "address": "0xdab625853c2b35d0a9c6bd8e5a097a664ef4ccfb"
    },
    "EROWAN": {
        "symbol": "EROWAN",
        "decimals": 18,
        "name": "SifChain (erowan) (PoS)",
        "address": "0xa7051c5a22d963b81d71c2ba64d46a877fbc1821"
    },
    "ERR": {
        "symbol": "ERR",
        "decimals": 9,
        "name": "Coinerr",
        "address": "0xfb32513135e3267995268e3099d2b6114d20b6ed"
    },
    "ETH2x-FLI-P": {
        "symbol": "ETH2x-FLI-P",
        "decimals": 18,
        "name": "ETH 2x Flexible Leverage Index",
        "address": "0x3ad707da309f3845cd602059901e39c4dcd66473"
    },
    "ETHA": {
        "symbol": "ETHA",
        "decimals": 18,
        "name": "ETHA",
        "address": "0x59e9261255644c411afdd00bd89162d09d862e38"
    },
    "ETHM": {
        "symbol": "ETHM",
        "decimals": 18,
        "name": "Ethereum Meta",
        "address": "0x55b1a124c04a54eefdefe5fa2ef5f852fb5f2f26"
    },
    "EURe": {
        "symbol": "EURe",
        "decimals": 18,
        "name": "Monerium EUR emoney",
        "address": "0x18ec0a6e18e5bc3784fdd3a3634b31245ab704f6"
    },
    "EUROe": {
        "symbol": "EUROe",
        "decimals": 6,
        "name": "EUROe Stablecoin",
        "address": "0x820802fa8a99901f52e39acd21177b0be6ee2974"
    },
    "EURS": {
        "symbol": "EURS",
        "decimals": 2,
        "name": "STASIS EURS Token (PoS)",
        "address": "0xe111178a87a3bff0c8d18decba5798827539ae99"
    },
    "EVE": {
        "symbol": "EVE",
        "decimals": 18,
        "name": "EVE Exchange (PoS)",
        "address": "0xae29ac47a9e3b0a52840e547adf74b912999f7fc"
    },
    "EXN": {
        "symbol": "EXN",
        "decimals": 18,
        "name": "EXENO COIN",
        "address": "0x0c9b3ab1bd0cf0745625381f5c3aa1cd9bbc7abb"
    },
    "EZ": {
        "symbol": "EZ",
        "decimals": 18,
        "name": "EASY V2",
        "address": "0x34c1b299a74588d6abdc1b85a53345a48428a521"
    },
    "FACTR": {
        "symbol": "FACTR",
        "decimals": 18,
        "name": "Defactor (PoS)",
        "address": "0xe0bceef36f3a6efdd5eebfacd591423f8549b9d5"
    },
    "FBX": {
        "symbol": "FBX",
        "decimals": 18,
        "name": "FireBotToken",
        "address": "0xd125443f38a69d776177c2b9c041f462936f8218"
    },
    "FEAR": {
        "symbol": "FEAR",
        "decimals": 18,
        "name": "Fear NFTs (PoS)",
        "address": "0xa2ca40dbe72028d3ac78b5250a8cb8c404e7fb8c"
    },
    "FID": {
        "symbol": "FID",
        "decimals": 18,
        "name": "Fidira",
        "address": "0x9a4eb698e5de3d3df0a68f681789072de1e50222"
    },
    "FINT": {
        "symbol": "FINT",
        "decimals": 18,
        "name": "Fintropy",
        "address": "0xd0513db39d87e8825389feb10bd911dc53b3a153"
    },
    "FIS": {
        "symbol": "FIS",
        "decimals": 18,
        "name": "StaFi (PoS)",
        "address": "0x7a7b94f18ef6ad056cda648588181cda84800f94"
    },
    "FISH": {
        "symbol": "FISH",
        "decimals": 18,
        "name": "Fish",
        "address": "0x3a3df212b7aa91aa0402b9035b098891d276572b"
    },
    "FLAME": {
        "symbol": "FLAME",
        "decimals": 18,
        "name": "FireStarter",
        "address": "0x22e3f02f86bc8ea0d73718a2ae8851854e62adc5"
    },
    "FODL": {
        "symbol": "FODL",
        "decimals": 18,
        "name": "Fodl (PoS)",
        "address": "0x5314ba045a459f63906aa7c76d9f337dcb7d6995"
    },
    "FOOD": {
        "symbol": "FOOD",
        "decimals": 18,
        "name": "FoodChain Global",
        "address": "0x6f06e6bed64cf4c4187c06ee2a4732f6a171bc4e"
    },
    "FORT": {
        "symbol": "FORT",
        "decimals": 18,
        "name": "Forta",
        "address": "0x9ff62d1fc52a907b6dcba8077c2ddca6e6a9d3e1"
    },
    "FOUR": {
        "symbol": "FOUR",
        "decimals": 18,
        "name": "The 4th Pillar Token (PoS)",
        "address": "0x48cbc913de09317df2365e6827df50da083701d5"
    },
    "FOX": {
        "symbol": "FOX",
        "decimals": 18,
        "name": "FOX (PoS)",
        "address": "0x65a05db8322701724c197af82c9cae41195b0aa8"
    },
    "FRAX": {
        "symbol": "FRAX",
        "decimals": 18,
        "name": "Frax",
        "address": "0x45c32fa6df82ead1e2ef74d17b76547eddfaff89"
    },
    "FRM": {
        "symbol": "FRM",
        "decimals": 18,
        "name": "Ferrum Network Token",
        "address": "0xd99bafe5031cc8b345cb2e8c80135991f12d7130"
    },
    "frxETH": {
        "symbol": "frxETH",
        "decimals": 18,
        "name": "Frax Ether",
        "address": "0xee327f889d5947c1dc1934bb208a1e792f953e96"
    },
    "FSN": {
        "symbol": "FSN",
        "decimals": 18,
        "name": "Fusion",
        "address": "0x2bf9b864cdc97b08b6d79ad4663e71b8ab65c45c"
    },
    "FTM": {
        "symbol": "FTM",
        "decimals": 18,
        "name": "Fantom Token (PoS)",
        "address": "0xc9c1c1c20b3658f8787cc2fd702267791f224ce1"
    },
    "FTRB": {
        "symbol": "FTRB",
        "decimals": 18,
        "name": "Faith Tribe",
        "address": "0xc3f56d567e7663e8932e65d85ae4be7eb5575ca7"
    },
    "FUSE": {
        "symbol": "FUSE",
        "decimals": 18,
        "name": "Fuse",
        "address": "0xf915fdda4c882731c0456a4214548cd13a822886"
    },
    "fxPINE": {
        "symbol": "fxPINE",
        "decimals": 18,
        "name": "Pine Token (FXERC20)",
        "address": "0x612d833c0c7a54cdfbe9a4328b6d658020563ec0"
    },
    "FXS": {
        "symbol": "FXS",
        "decimals": 18,
        "name": "Frax Share",
        "address": "0x1a3acf6d19267e2d3e7f898f42803e90c9219062"
    },
    "FYN": {
        "symbol": "FYN",
        "decimals": 18,
        "name": "Affyn",
        "address": "0x3b56a704c01d650147ade2b8cee594066b3f9421"
    },
    "GAIA": {
        "symbol": "GAIA",
        "decimals": 18,
        "name": "GAIA Everworld",
        "address": "0x723b17718289a91af252d616de2c77944962d122"
    },
    "GAJ": {
        "symbol": "GAJ",
        "decimals": 18,
        "name": "PolyGaj Token",
        "address": "0xf4b0903774532aee5ee567c02aab681a81539e92"
    },
    "GAME": {
        "symbol": "GAME",
        "decimals": 18,
        "name": "GAME Credits",
        "address": "0x8d1566569d5b695d44a9a234540f68d393cdc40d"
    },
    "GAMER": {
        "symbol": "GAMER",
        "decimals": 18,
        "name": "GameStation",
        "address": "0x3f6b3595ecf70735d3f48d69b09c4e4506db3f47"
    },
    "GBYTE": {
        "symbol": "GBYTE",
        "decimals": 18,
        "name": "Imported GBYTE",
        "address": "0xab5f7a0e20b0d056aed4aa4528c78da45be7308b"
    },
    "GEL": {
        "symbol": "GEL",
        "decimals": 18,
        "name": "Gelato Network Token",
        "address": "0x15b7c0c907e4c6b9adaaaabc300c08991d6cea05"
    },
    "GEM": {
        "symbol": "GEM",
        "decimals": 18,
        "name": "NFTmall GEM Token",
        "address": "0x4a7b9a4589a88a06ca29f99556db08234078d727"
    },
    "GENE": {
        "symbol": "GENE",
        "decimals": 18,
        "name": "GenomesDAO (PoS)",
        "address": "0x34667ed7c36cbbbf2d5d5c5c8d6eb76a094edb9f"
    },
    "GENESIS": {
        "symbol": "GENESIS",
        "decimals": 18,
        "name": "Genesis",
        "address": "0x51869836681bce74a514625c856afb697a013797"
    },
    "GENI": {
        "symbol": "GENI",
        "decimals": 9,
        "name": "Genius",
        "address": "0x444444444444c1a66f394025ac839a535246fcc8"
    },
    "GEO$": {
        "symbol": "GEO$",
        "decimals": 18,
        "name": "GEOPOLY",
        "address": "0xf1428850f92b87e629c6f3a3b75bffbc496f7ba6"
    },
    "GET": {
        "symbol": "GET",
        "decimals": 18,
        "name": "GET Protocol (PoS)",
        "address": "0xdb725f82818de83e99f1dac22a9b5b51d3d04dd4"
    },
    "GFARM2": {
        "symbol": "GFARM2",
        "decimals": 18,
        "name": "Gains V2",
        "address": "0x7075cab6bcca06613e2d071bd918d1a0241379e2"
    },
    "GFC": {
        "symbol": "GFC",
        "decimals": 18,
        "name": "GCOIN",
        "address": "0x071ac29d569a47ebffb9e57517f855cb577dcc4c"
    },
    "GFI": {
        "symbol": "GFI",
        "decimals": 18,
        "name": "Gravity Finance",
        "address": "0x874e178a2f3f3f9d34db862453cd756e7eab0381"
    },
    "GFX": {
        "symbol": "GFX",
        "decimals": 18,
        "name": "GamyFi",
        "address": "0x65ad6a2288b2dd23e466226397c8f5d1794e58fc"
    },
    "GHST": {
        "symbol": "GHST",
        "decimals": 18,
        "name": "Aavegotchi GHST Token (PoS)",
        "address": "0x385eeac5cb85a38a9a07a70c73e0a3271cfb54a7"
    },
    "GIDDY": {
        "symbol": "GIDDY",
        "decimals": 18,
        "name": "Giddy Token",
        "address": "0x67eb41a14c0fe5cd701fc9d5a3d6597a72f641a6"
    },
    "GLCH": {
        "symbol": "GLCH",
        "decimals": 18,
        "name": "Glitch (PoS)",
        "address": "0xbe5cf150e1ff59ca7f2499eaa13bfc40aae70e78"
    },
    "GLM": {
        "symbol": "GLM",
        "decimals": 18,
        "name": "Golem Network Token (PoS)",
        "address": "0x0b220b82f3ea3b7f6d9a1d8ab58930c064a2b5bf"
    },
    "GLTR": {
        "symbol": "GLTR",
        "decimals": 18,
        "name": "GAX Liquidity Token Reward",
        "address": "0x3801c3b3b5c98f88a9c9005966aa96aa440b9afc"
    },
    "GM": {
        "symbol": "GM",
        "decimals": 8,
        "name": "GhostMarket Token",
        "address": "0x6a335ac6a3cdf444967fe03e7b6b273c86043990"
    },
    "GMEE": {
        "symbol": "GMEE",
        "decimals": 18,
        "name": "GAMEE",
        "address": "0xcf32822ff397ef82425153a9dcb726e5ff61dca7"
    },
    "GNOME": {
        "symbol": "GNOME",
        "decimals": 18,
        "name": "GenomesDAO Governance (PoS)",
        "address": "0x6e8a8726639d12935b3219892155520bdc57366b"
    },
    "GNS": {
        "symbol": "GNS",
        "decimals": 18,
        "name": "Gains Network",
        "address": "0xe5417af564e4bfda1c483642db72007871397896"
    },
    "GoC": {
        "symbol": "GoC",
        "decimals": 18,
        "name": "GoCrypto",
        "address": "0x4b85a666dec7c959e88b97814e46113601b07e57"
    },
    "gOHM": {
        "symbol": "gOHM",
        "decimals": 18,
        "name": "Governance OHM",
        "address": "0xd8ca34fd379d9ca3c6ee3b3905678320f5b45195"
    },
    "GOVI": {
        "symbol": "GOVI",
        "decimals": 18,
        "name": "GOVI (PoS)",
        "address": "0x43df9c0a1156c96cea98737b511ac89d0e2a1f46"
    },
    "GRT": {
        "symbol": "GRT",
        "decimals": 18,
        "name": "Graph Token (PoS)",
        "address": "0x5fe2b58c013d7601147dcdd68c143a77499f5531"
    },
    "GTON": {
        "symbol": "GTON",
        "decimals": 18,
        "name": "Graviton",
        "address": "0xf480f38c366daac4305dc484b2ad7a496ff00cea"
    },
    "GYSR": {
        "symbol": "GYSR",
        "decimals": 18,
        "name": "Geyser (PoS)",
        "address": "0xc48f61a288a08f1b80c2edd74652e1276b6a168c"
    },
    "H3RO3S": {
        "symbol": "H3RO3S",
        "decimals": 18,
        "name": "H3RO3S",
        "address": "0x480fd103973357266813ecfce9faababf3c4ca3a"
    },
    "HAKKA": {
        "symbol": "HAKKA",
        "decimals": 18,
        "name": "Hakka Finance",
        "address": "0x978338a9d2d0aa2ff388d3dc98b9bf25bff5efb4"
    },
    "HANZO": {
        "symbol": "HANZO",
        "decimals": 9,
        "name": "Hanzo",
        "address": "0x37eb60f78e06c4bb2a5f836b0fc6bccbbaa995b3"
    },
    "HEX": {
        "symbol": "HEX",
        "decimals": 8,
        "name": "HEX (PoS)",
        "address": "0x23d29d30e35c5e8d321e1dc9a8a61bfd846d4c5c"
    },
    "HMT": {
        "symbol": "HMT",
        "decimals": 18,
        "name": "Human Token (PoS)",
        "address": "0xc748b2a084f8efc47e086ccddd9b7e67aeb571bf"
    },
    "HNY": {
        "symbol": "HNY",
        "decimals": 18,
        "name": "HONEY",
        "address": "0x1fa2f83ba2df61c3d370071d61b17be01e224f3a"
    },
    "HOTCROSS": {
        "symbol": "HOTCROSS",
        "decimals": 18,
        "name": "Hot Cross Token (PoS)",
        "address": "0x3b737a181f7d2532cf49864f8050b3465a310593"
    },
    "HYVE": {
        "symbol": "HYVE",
        "decimals": 18,
        "name": "HYVE",
        "address": "0x61aee582896064ecd5d85d66a32ddeb5574a699d"
    },
    "ICE": {
        "symbol": "ICE",
        "decimals": 18,
        "name": "Decentral Games ICE",
        "address": "0xc6c855ad634dcdad23e64da71ba85b8c51e5ad7c"
    },
    "ICHI": {
        "symbol": "ICHI",
        "decimals": 18,
        "name": "ICHI",
        "address": "0x111111517e4929d3dcbdfa7cce55d30d4b6bc4d6"
    },
    "IDLE": {
        "symbol": "IDLE",
        "decimals": 18,
        "name": "Idle (PoS)",
        "address": "0xc25351811983818c9fe6d8c580531819c8ade90f"
    },
    "IDRT": {
        "symbol": "IDRT",
        "decimals": 6,
        "name": "Rupiah Token",
        "address": "0x554cd6bdd03214b10aafa3e0d4d42de0c5d2937b"
    },
    "IGG": {
        "symbol": "IGG",
        "decimals": 6,
        "name": "IG Gold (PoS)",
        "address": "0xe6fc6c7cb6d2c31b359a49a33ef08ab87f4de7ce"
    },
    "INDEX": {
        "symbol": "INDEX",
        "decimals": 18,
        "name": "Index (PoS)",
        "address": "0xfbd8a3b908e764dbcd51e27992464b4432a1132b"
    },
    "INF": {
        "symbol": "INF",
        "decimals": 18,
        "name": "Infam",
        "address": "0x000000ef379ee7f4c051f4b9af901a9219d9ec5c"
    },
    "INS": {
        "symbol": "INS",
        "decimals": 18,
        "name": "iNFTspaceToken",
        "address": "0xb988bd378a0754957d5d9471c96e0f8051645a26"
    },
    "INST": {
        "symbol": "INST",
        "decimals": 18,
        "name": "Instadapp (PoS)",
        "address": "0xf50d05a1402d0adafa880d36050736f9f6ee7dee"
    },
    "INSUR": {
        "symbol": "INSUR",
        "decimals": 18,
        "name": "InsurAce (PoS)",
        "address": "0x8a0e8b4b0903929f47c3ea30973940d4a9702067"
    },
    "IOEN": {
        "symbol": "IOEN",
        "decimals": 18,
        "name": "Internet of Energy Network",
        "address": "0xd0e9c8f5fae381459cf07ec506c1d2896e8b5df6"
    },
    "IOI": {
        "symbol": "IOI",
        "decimals": 6,
        "name": "IOI Token",
        "address": "0xaf24765f631c8830b5528b57002241ee7eef1c14"
    },
    "IOTX": {
        "symbol": "IOTX",
        "decimals": 18,
        "name": "IoTeX Network (PoS)",
        "address": "0xf6372cdb9c1d3674e83842e3800f2a62ac9f3c66"
    },
    "IQ": {
        "symbol": "IQ",
        "decimals": 18,
        "name": "Everipedia IQ (PoS)",
        "address": "0xb9638272ad6998708de56bbc0a290a1de534a578"
    },
    "IRON": {
        "symbol": "IRON",
        "decimals": 18,
        "name": "IRON Stablecoin",
        "address": "0xd86b5923f3ad7b585ed81b448170ae026c65ae9a"
    },
    "ISHND": {
        "symbol": "ISHND",
        "decimals": 18,
        "name": "Stronghands Finance",
        "address": "0x9e6b19874e97fe8e8cad77f2c0ab5e7a693e5dbf"
    },
    "ISKY": {
        "symbol": "ISKY",
        "decimals": 18,
        "name": "Skyblocks",
        "address": "0x5dfd5edfde4d8ec9e632dca9d09fc7e833f74210"
    },
    "ISLAMI": {
        "symbol": "ISLAMI",
        "decimals": 7,
        "name": "ISLAMICOIN",
        "address": "0x9c891326fd8b1a713974f73bb604677e1e63396d"
    },
    "ITSB": {
        "symbol": "ITSB",
        "decimals": 18,
        "name": "ITSBLOC",
        "address": "0x998013798440d44c1dd4c767bdd9580e16e46e28"
    },
    "IUX": {
        "symbol": "IUX",
        "decimals": 18,
        "name": "GeniuX",
        "address": "0x346404079b3792a6c548b072b9c4dddfb92948d5"
    },
    "IXT": {
        "symbol": "IXT",
        "decimals": 18,
        "name": "PlanetIX",
        "address": "0xe06bd4f5aac8d0aa337d13ec88db6defc6eaeefe"
    },
    "jEUR": {
        "symbol": "jEUR",
        "decimals": 18,
        "name": "Jarvis Synthetic Euro",
        "address": "0x4e3decbb3645551b8a19f0ea1678079fcb33fb4c"
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
        "address": "0x03cf5d93ca7c70ce0a21a09f4d70779d2c66b25a"
    },
    "JPYC": {
        "symbol": "JPYC",
        "decimals": 18,
        "name": "JPY Coin",
        "address": "0x431d5dff03120afa4bdf332c61a6e1766ef37bdb"
    },
    "JRT": {
        "symbol": "JRT",
        "decimals": 18,
        "name": "Jarvis Reward Token (PoS)",
        "address": "0x596ebe76e2db4470966ea395b0d063ac6197a8c5"
    },
    "KABY": {
        "symbol": "KABY",
        "decimals": 18,
        "name": "Kaby Arena",
        "address": "0x5198e7cc1640049de37d1bd10b03fa5a3afda120"
    },
    "KAMPAY": {
        "symbol": "KAMPAY",
        "decimals": 18,
        "name": "Kampay",
        "address": "0x39fc9e94caeacb435842fadedecb783589f50f5f"
    },
    "KANGAL": {
        "symbol": "KANGAL",
        "decimals": 18,
        "name": "Kangal",
        "address": "0x34f380a4e3389e99c0369264453523bbe5af7fab"
    },
    "KASTA": {
        "symbol": "KASTA",
        "decimals": 18,
        "name": "KastaToken",
        "address": "0x235737dbb56e8517391473f7c964db31fa6ef280"
    },
    "KAVA": {
        "symbol": "KAVA",
        "decimals": 6,
        "name": "Kava.io (PoS)",
        "address": "0x87d32f2c0a3d6d091772890c81e321026454a125"
    },
    "KEYFI": {
        "symbol": "KEYFI",
        "decimals": 18,
        "name": "KeyFi Token",
        "address": "0xd1a5f2a049343fc4d5f8d478f734eba51b22375e"
    },
    "KIT": {
        "symbol": "KIT",
        "decimals": 18,
        "name": "DexKit (PoS)",
        "address": "0x4d0def42cf57d6f27cd4983042a55dce1c9f853c"
    },
    "KLIMA": {
        "symbol": "KLIMA",
        "decimals": 9,
        "name": "Klima DAO",
        "address": "0x4e78011ce80ee02d2c3e649fb657e45898257815"
    },
    "KLX": {
        "symbol": "KLX",
        "decimals": 18,
        "name": "Kalima Token",
        "address": "0xcfb4c7f9b5f363ae162015479345cb2f0c76f3a9"
    },
    "KNC": {
        "symbol": "KNC",
        "decimals": 18,
        "name": "Kyber Network Crystal v2 (PoS)",
        "address": "0x1c954e8fe737f99f68fa1ccda3e51ebdb291948c"
    },
    "KNIGHT": {
        "symbol": "KNIGHT",
        "decimals": 18,
        "name": "Forest Knight",
        "address": "0x4455ef8b4b4a007a93daa12de63a47eeac700d9d"
    },
    "Knot": {
        "symbol": "Knot",
        "decimals": 18,
        "name": "Karmaverse Knot",
        "address": "0xb763f1177e9b2fb66fbe0d50372e3e2575c043e5"
    },
    "KOLnet": {
        "symbol": "KOLnet",
        "decimals": 18,
        "name": "KOLnet Token",
        "address": "0xfd195a17e2a60d248a7148a919c5166ae907479a"
    },
    "KOM": {
        "symbol": "KOM",
        "decimals": 8,
        "name": "Kommunitas",
        "address": "0xc004e2318722ea2b15499d6375905d75ee5390b8"
    },
    "KRIDA": {
        "symbol": "KRIDA",
        "decimals": 18,
        "name": "Krida Fans",
        "address": "0x3c5a5885f6ee4acc2597069fe3c19f49c6efba96"
    },
    "Krill": {
        "symbol": "Krill",
        "decimals": 18,
        "name": "Krill",
        "address": "0x05089c9ebffa4f0aca269e32056b1b36b37ed71b"
    },
    "KROM": {
        "symbol": "KROM",
        "decimals": 18,
        "name": "Kromatika (PoS)",
        "address": "0x14af1f2f02dccb1e43402339099a05a5e363b83c"
    },
    "KRW": {
        "symbol": "KRW",
        "decimals": 18,
        "name": "KROWN",
        "address": "0x6c3b2f402cd7d22ae2c319b9d2f16f57927a4a17"
    },
    "KZEN": {
        "symbol": "KZEN",
        "decimals": 18,
        "name": "Kaizen.Finance",
        "address": "0x4550003152f12014558e5ce025707e4dd841100f"
    },
    "LCD": {
        "symbol": "LCD",
        "decimals": 18,
        "name": "Lucidao",
        "address": "0xc2a45fe7d40bcac8369371b08419ddafd3131b4a"
    },
    "LDO": {
        "symbol": "LDO",
        "decimals": 18,
        "name": "Lido DAO Token (PoS)",
        "address": "0xc3c7d422809852031b44ab29eec9f1eff2a58756"
    },
    "LFG": {
        "symbol": "LFG",
        "decimals": 18,
        "name": "LFG Token [via ChainPort.io]",
        "address": "0x411be1e071675df40fe1c08ca760bb7aa707cedf"
    },
    "LFI": {
        "symbol": "LFI",
        "decimals": 18,
        "name": "LunaFi",
        "address": "0x77d97db5615dfe8a2d16b38eaa3f8f34524a0a74"
    },
    "LICP": {
        "symbol": "LICP",
        "decimals": 18,
        "name": "Liquid ICP",
        "address": "0x1b43b97094aa3c6cc678edb9e28ac67daaa7cc64"
    },
    "LIME": {
        "symbol": "LIME",
        "decimals": 18,
        "name": "iMe Lab",
        "address": "0x7f67639ffc8c93dd558d452b8920b28815638c44"
    },
    "LINK": {
        "symbol": "LINK",
        "decimals": 18,
        "name": "ChainLink Token",
        "address": "0x53e0bca35ec356bd5dddfebbd1fc0fd03fabad39"
    },
    "LKR": {
        "symbol": "LKR",
        "decimals": 18,
        "name": "Polkalokr",
        "address": "0xa5ff48e326958e0ce6fdf9518de561f2b5f57da3"
    },
    "LOPES": {
        "symbol": "LOPES",
        "decimals": 18,
        "name": "Lopes",
        "address": "0xcebdc775e9f18156ec2e04fb4150f1bc54de690f"
    },
    "lowb": {
        "symbol": "lowb",
        "decimals": 18,
        "name": "loser coin",
        "address": "0x1c0a798b5a5273a9e54028eb1524fd337b24145f"
    },
    "LPT": {
        "symbol": "LPT",
        "decimals": 18,
        "name": "Livepeer Token (PoS)",
        "address": "0x3962f4a0a0051dcce0be73a7e09cef5756736712"
    },
    "LUCHOW": {
        "symbol": "LUCHOW",
        "decimals": 18,
        "name": "LunaChow",
        "address": "0xc4bb7277a74678f053259cb1f96140347efbfd46"
    },
    "LUMIII": {
        "symbol": "LUMIII",
        "decimals": 18,
        "name": "LumiiiToken",
        "address": "0xed88227296943857409a8e0f15ad7134e70d0f73"
    },
    "LUNA": {
        "symbol": "LUNA",
        "decimals": 6,
        "name": "LUNA",
        "address": "0x9cd6746665d9557e1b9a775819625711d0693439"
    },
    "LUSD": {
        "symbol": "LUSD",
        "decimals": 18,
        "name": "LUSD Stablecoin (PoS)",
        "address": "0x23001f892c0c82b79303edc9b9033cd190bb21c7"
    },
    "LUXY": {
        "symbol": "LUXY",
        "decimals": 18,
        "name": "LUXY",
        "address": "0xd4945a3d0de9923035521687d4bf18cc9b0c7c2a"
    },
    "MABBC": {
        "symbol": "MABBC",
        "decimals": 8,
        "name": "Matic ABBC",
        "address": "0xe83ce6bfb580583bd6a62b4be7b34fc25f02910d"
    },
    "MAHA": {
        "symbol": "MAHA",
        "decimals": 18,
        "name": "MahaDAO (PoS)",
        "address": "0xedd6ca8a4202d4a36611e2fff109648c4863ae19"
    },
    "MANA": {
        "symbol": "MANA",
        "decimals": 18,
        "name": "(PoS) Decentraland MANA",
        "address": "0xa1c57f48f0deb89f569dfbe6e2b7f46d33606fd4"
    },
    "MASK": {
        "symbol": "MASK",
        "decimals": 18,
        "name": "Mask Network (PoS)",
        "address": "0x2b9e7ccdf0f4e5b24757c1e1a80e311e34cb10c7"
    },
    "MASQ": {
        "symbol": "MASQ",
        "decimals": 18,
        "name": "MASQ (PoS)",
        "address": "0xee9a352f6aac4af1a5b9f467f6a93e0ffbe9dd35"
    },
    "MaticX": {
        "symbol": "MaticX",
        "decimals": 18,
        "name": "Liquid Staking Matic (PoS)",
        "address": "0xfa68fb4628dff1028cfec22b4162fccd0d45efb6"
    },
    "MATRIX": {
        "symbol": "MATRIX",
        "decimals": 18,
        "name": "MatrixSwapToken (PoS)",
        "address": "0x211f4e76fcb811ed2b310a232a24b3445d95e3bc"
    },
    "MCASH": {
        "symbol": "MCASH",
        "decimals": 18,
        "name": "Monsoon Finance",
        "address": "0xa25610a77077390a75ad9072a084c5fbc7d43a0d"
    },
    "MCHC": {
        "symbol": "MCHC",
        "decimals": 18,
        "name": "MCHCoin (PoS)",
        "address": "0xee7666aacaefaa6efeef62ea40176d3eb21953b9"
    },
    "MCO2": {
        "symbol": "MCO2",
        "decimals": 18,
        "name": "Moss Carbon Credit (PoS)",
        "address": "0xaa7dbd1598251f856c12f63557a4c4397c253cea"
    },
    "MCRN": {
        "symbol": "MCRN",
        "decimals": 18,
        "name": "MacaronSwap Token",
        "address": "0xba25b552c8a098afdf276324c32c71fe28e0ad40"
    },
    "MEAN": {
        "symbol": "MEAN",
        "decimals": 6,
        "name": "MEAN",
        "address": "0x4867b60ad7c6adc98653f661f1aea31740986ba5"
    },
    "MEE": {
        "symbol": "MEE",
        "decimals": 18,
        "name": "MEE Governance Token",
        "address": "0xeb7eab87837f4dad1bb80856db9e4506fc441f3d"
    },
    "MEM": {
        "symbol": "MEM",
        "decimals": 18,
        "name": "Memecoin",
        "address": "0x42dbbd5ae373fea2fc320f62d44c058522bb3758"
    },
    "META": {
        "symbol": "META",
        "decimals": 8,
        "name": "ABCMETA Token",
        "address": "0xedcfb6984a3c70501baa8b7f5421ae795ecc1496"
    },
    "METAL": {
        "symbol": "METAL",
        "decimals": 18,
        "name": "METAL",
        "address": "0x200c234721b5e549c3693ccc93cf191f90dc2af9"
    },
    "METR": {
        "symbol": "METR",
        "decimals": 18,
        "name": "Metria",
        "address": "0x405ce8b2eaeea7d4ba5fc160848cb2a6569e03f0"
    },
    "MHUNT": {
        "symbol": "MHUNT",
        "decimals": 18,
        "name": "MetaShooter",
        "address": "0x61f95bd637e3034133335c1baa0148e518d438ad"
    },
    "MILK": {
        "symbol": "MILK",
        "decimals": 18,
        "name": "Milk",
        "address": "0x1599fe55cda767b1f631ee7d414b41f5d6de393d"
    },
    "MIM": {
        "symbol": "MIM",
        "decimals": 18,
        "name": "Magic Internet Money",
        "address": "0x49a0400587a7f65072c87c4910449fdcc5c47242"
    },
    "miMATIC": {
        "symbol": "miMATIC",
        "decimals": 18,
        "name": "miMATIC",
        "address": "0xa3fa99a148fa48d14ed51d610c367c61876997f1"
    },
    "MIMIR": {
        "symbol": "MIMIR",
        "decimals": 18,
        "name": "Mimir Token",
        "address": "0xd1790c5435b9fb7c9444c749cefe53d40d751eac"
    },
    "MITx": {
        "symbol": "MITx",
        "decimals": 18,
        "name": "Morpheus Infrastructure Token (PoS)",
        "address": "0x31042a4e66eda0d12143ffc8cc1552d611da4cba"
    },
    "MKR": {
        "symbol": "MKR",
        "decimals": 18,
        "name": "MAKER (PoS)",
        "address": "0x6f7c932e7684666c9fd1d44527765433e01ff61d"
    },
    "MLD": {
        "symbol": "MLD",
        "decimals": 18,
        "name": "Monolend",
        "address": "0x5d089336f95e649e491c054279d64a86565e8b25"
    },
    "MLN": {
        "symbol": "MLN",
        "decimals": 18,
        "name": "Melon Token (PoS)",
        "address": "0xa9f37d84c856fda3812ad0519dad44fa0a3fe207"
    },
    "MM": {
        "symbol": "MM",
        "decimals": 18,
        "name": "Million (PoS)",
        "address": "0x5647fe4281f8f6f01e84bce775ad4b828a7b8927"
    },
    "MMF": {
        "symbol": "MMF",
        "decimals": 18,
        "name": "Mad Meerkat Finance",
        "address": "0x22a31bd4cb694433b6de19e0acc2899e553e9481"
    },
    "MMO": {
        "symbol": "MMO",
        "decimals": 18,
        "name": "Mad Meerkat Optimizer",
        "address": "0x859a50979fdb2a2fd8ba1adcc66977c6f6b1cd5b"
    },
    "MNFT": {
        "symbol": "MNFT",
        "decimals": 18,
        "name": "MarvelousNFT (PoS)",
        "address": "0xd281af594cbb99e8469f3591d57a0c72eb725bdb"
    },
    "MNI": {
        "symbol": "MNI",
        "decimals": 18,
        "name": "MnI",
        "address": "0x1c5ea1a050633dd9136e42ce675211116f465692"
    },
    "MNTL": {
        "symbol": "MNTL",
        "decimals": 6,
        "name": "AssetMantle (PoS)",
        "address": "0x38a536a31ba4d8c1bcca016abbf786ecd25877e8"
    },
    "MOD": {
        "symbol": "MOD",
        "decimals": 18,
        "name": "MODEFI  (PoS)",
        "address": "0x8346ab8d5ea7a9db0209aed2d1806afa0e2c4c21"
    },
    "MODA": {
        "symbol": "MODA",
        "decimals": 18,
        "name": "moda",
        "address": "0x5e430f88d1be82eb3ef92b6ff06125168fd5dcf2"
    },
    "MOM": {
        "symbol": "MOM",
        "decimals": 18,
        "name": "MOM",
        "address": "0x4593b173439835ad8f4bb29210668e8fafb18f56"
    },
    "MOMA": {
        "symbol": "MOMA",
        "decimals": 18,
        "name": "MOchi MArket",
        "address": "0xe3ab61371ecc88534c522922a026f2296116c109"
    },
    "MONA": {
        "symbol": "MONA",
        "decimals": 18,
        "name": "Monavale",
        "address": "0x6968105460f67c3bf751be7c15f92f5286fd0ce5"
    },
    "MOONED": {
        "symbol": "MOONED",
        "decimals": 18,
        "name": "MoonEdge",
        "address": "0x7e4c577ca35913af564ee2a24d882a4946ec492b"
    },
    "MRST": {
        "symbol": "MRST",
        "decimals": 18,
        "name": "Mars Token",
        "address": "0x411bc96881a62572ff33c9d8ce60df99e3d96cd8"
    },
    "MS": {
        "symbol": "MS",
        "decimals": 18,
        "name": "Morphswap",
        "address": "0x476718ea98525f6eeba3689b321e709522ae0930"
    },
    "mSHEESHA": {
        "symbol": "mSHEESHA",
        "decimals": 18,
        "name": "SHEESHA POLYGON",
        "address": "0x88c949b4eb85a90071f2c0bef861bddee1a7479d"
    },
    "MSQ": {
        "symbol": "MSQ",
        "decimals": 18,
        "name": "MSQUARE",
        "address": "0x6a8ec2d9bfbdd20a7f5a4e89d640f7e7ceba4499"
    },
    "MSU": {
        "symbol": "MSU",
        "decimals": 18,
        "name": "MetaSoccer Universe",
        "address": "0xe8377a076adabb3f9838afb77bee96eac101ffb1"
    },
    "MTA": {
        "symbol": "MTA",
        "decimals": 18,
        "name": "Meta (PoS)",
        "address": "0xf501dd45a1198c2e1b5aef5314a68b9006d842e0"
    },
    "MTBC": {
        "symbol": "MTBC",
        "decimals": 18,
        "name": "Metabolic",
        "address": "0xfc541ec44a41974d76fc0b2f526cae781ffabaed"
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
        "address": "0xf5b9b4a0534cf508ab9953c64c5310dfa0b303a1"
    },
    "MV": {
        "symbol": "MV",
        "decimals": 18,
        "name": "Metaverse (PoS)",
        "address": "0xa3c322ad15218fbfaed26ba7f616249f7705d945"
    },
    "MVI": {
        "symbol": "MVI",
        "decimals": 18,
        "name": "Metaverse Index (PoS)",
        "address": "0xfe712251173a2cd5f5be2b46bb528328ea3565e1"
    },
    "MVX": {
        "symbol": "MVX",
        "decimals": 18,
        "name": "Metavault Trade",
        "address": "0x2760e46d9bb43dafcbecaad1f64b93207f9f0ed7"
    },
    "mXEN": {
        "symbol": "mXEN",
        "decimals": 18,
        "name": "XEN Crypto",
        "address": "0x2ab0e9e4ee70fff1fb9d67031e44f6410170d00e"
    },
    "MYST": {
        "symbol": "MYST",
        "decimals": 18,
        "name": "Mysterium (PoS)",
        "address": "0x1379e8886a944d2d9d440b3d88df536aea08d9f3"
    },
    "N1": {
        "symbol": "N1",
        "decimals": 18,
        "name": "NFTify",
        "address": "0xacbd826394189cf2623c6df98a18b41fc8ffc16d"
    },
    "NAKA": {
        "symbol": "NAKA",
        "decimals": 18,
        "name": "Nakamoto.Games",
        "address": "0x311434160d7537be358930def317afb606c0d737"
    },
    "NCT": {
        "symbol": "NCT",
        "decimals": 18,
        "name": "Toucan Protocol: Nature Carbon Tonne",
        "address": "0xd838290e877e0188a4a44700463419ed96c16107"
    },
    "NEST": {
        "symbol": "NEST",
        "decimals": 18,
        "name": "NEST",
        "address": "0x98f8669f6481ebb341b522fcd3663f79a3d1a6a7"
    },
    "NEX": {
        "symbol": "NEX",
        "decimals": 8,
        "name": "Nash Exchange Token (PoS)",
        "address": "0xa486c6bc102f409180ccb8a94ba045d39f8fc7cb"
    },
    "NEXM": {
        "symbol": "NEXM",
        "decimals": 8,
        "name": "Nexum Coin",
        "address": "0xc88640b734fea3b35c132fe757aeb5ca6c8cdc66"
    },
    "NEXO": {
        "symbol": "NEXO",
        "decimals": 18,
        "name": "Nexo (PoS)",
        "address": "0x41b3966b4ff7b427969ddf5da3627d6aeae9a48e"
    },
    "NFTY": {
        "symbol": "NFTY",
        "decimals": 18,
        "name": "NFTY Token",
        "address": "0xcc081220542a60a8ea7963c4f53d522b503272c1"
    },
    "NHT": {
        "symbol": "NHT",
        "decimals": 18,
        "name": "Neighbourhoods Token",
        "address": "0x84342e932797fc62814189f01f0fb05f52519708"
    },
    "NITRO": {
        "symbol": "NITRO",
        "decimals": 18,
        "name": "Nitro (PoS)",
        "address": "0x695fc8b80f344411f34bdbcb4e621aa69ada384b"
    },
    "NORD": {
        "symbol": "NORD",
        "decimals": 18,
        "name": "Nord Token (PoS)",
        "address": "0xf6f85b3f9fd581c2ee717c404f7684486f057f95"
    },
    "NPT": {
        "symbol": "NPT",
        "decimals": 18,
        "name": "NEOPIN Token",
        "address": "0x306ee01a6ba3b4a8e993fa2c1adc7ea24462000c"
    },
    "NSDX": {
        "symbol": "NSDX",
        "decimals": 18,
        "name": "NASDEX Token",
        "address": "0xe8d17b127ba8b9899a160d9a07b69bca8e08bfc6"
    },
    "NSFW": {
        "symbol": "NSFW",
        "decimals": 18,
        "name": "Pleasure Coin",
        "address": "0x8f006d1e1d9dc6c98996f50a4c810f17a47fbf19"
    },
    "NTIC": {
        "symbol": "NTIC",
        "decimals": 18,
        "name": "Entice Coin",
        "address": "0x8c9bac920cd9cf8c61f7fa4f34f43c572d040f61"
    },
    "NTVRK": {
        "symbol": "NTVRK",
        "decimals": 18,
        "name": "NETVRK [via ChainPort.io]",
        "address": "0x73a4dc4215dc3eb6aae3c7aafd2514cb34e5d983"
    },
    "NVT": {
        "symbol": "NVT",
        "decimals": 8,
        "name": "NVT",
        "address": "0x0fdb676775cc91042501c0c14ae5b2b5166b24d9"
    },
    "NXD": {
        "symbol": "NXD",
        "decimals": 18,
        "name": "Nexus Dubai",
        "address": "0x228b5c21ac00155cf62c57bcc704c0da8187950b"
    },
    "NXRA": {
        "symbol": "NXRA",
        "decimals": 18,
        "name": "AllianceBlock Nexera Token",
        "address": "0x644192291cc835a93d6330b24ea5f5fedd0eef9e"
    },
    "NXTT": {
        "symbol": "NXTT",
        "decimals": 18,
        "name": "NextEarthToken",
        "address": "0x0d0b8488222f7f83b23e365320a4021b12ead608"
    },
    "O3": {
        "symbol": "O3",
        "decimals": 18,
        "name": "O3 Swap Token",
        "address": "0xee9801669c6138e84bd50deb500827b776777d28"
    },
    "OATH": {
        "symbol": "OATH",
        "decimals": 18,
        "name": "Oath Token",
        "address": "0xc2c52ff5134596f5ff1b1204d3304228f2432836"
    },
    "oAUTO": {
        "symbol": "oAUTO",
        "decimals": 18,
        "name": "Orbit Bridge Polygon AUTOv2",
        "address": "0x7f426f6dc648e50464a0392e60e1bb465a67e9cf"
    },
    "OCAVU": {
        "symbol": "OCAVU",
        "decimals": 18,
        "name": "Ocavu Network Token",
        "address": "0xf796969fa47fb0748c80b8b153cbb895e88cbd54"
    },
    "ODDZ": {
        "symbol": "ODDZ",
        "decimals": 18,
        "name": "OddzToken",
        "address": "0x4e830f67ec499e69930867f9017aeb5b3f629c73"
    },
    "OGN": {
        "symbol": "OGN",
        "decimals": 18,
        "name": "OriginToken (PoS)",
        "address": "0xa63beffd33ab3a2efd92a39a7d2361cee14ceba8"
    },
    "OJA": {
        "symbol": "OJA",
        "decimals": 18,
        "name": "Ojamu",
        "address": "0x26373ec913876c9e6d38494dde458cb8649cb30c"
    },
    "OK": {
        "symbol": "OK",
        "decimals": 18,
        "name": "Okcash",
        "address": "0xd3ac016b1b8c80eeadde4d186a9138c9324e4189"
    },
    "OKLP": {
        "symbol": "OKLP",
        "decimals": 18,
        "name": "OkLetsPlay",
        "address": "0x5d48a5e5a3e737322ae27e25897f1c9e19ecc941"
    },
    "OM": {
        "symbol": "OM",
        "decimals": 18,
        "name": "MANTRA DAO (PoS)",
        "address": "0xc3ec80343d2bae2f8e680fdadde7c17e71e114ea"
    },
    "OMEN": {
        "symbol": "OMEN",
        "decimals": 18,
        "name": "Augury Finance",
        "address": "0x76e63a3e7ba1e2e61d3da86a87479f983de89a7e"
    },
    "OMG": {
        "symbol": "OMG",
        "decimals": 18,
        "name": "OMGToken (PoS)",
        "address": "0x62414d03084eeb269e18c970a21f45d2967f0170"
    },
    "OMMI": {
        "symbol": "OMMI",
        "decimals": 18,
        "name": "OMMNIVERSE",
        "address": "0xbc2659ead8d2d13a157a75bfc5acc156e1ea06df"
    },
    "ONSTON": {
        "symbol": "ONSTON",
        "decimals": 18,
        "name": "ONSTON",
        "address": "0xa4ce4a467e51aefec683a649c3f14427f104667f"
    },
    "OOE": {
        "symbol": "OOE",
        "decimals": 18,
        "name": "OpenOcean",
        "address": "0x9d5565da88e596730522cbc5a918d2a89dbc16d9"
    },
    "OPCT": {
        "symbol": "OPCT",
        "decimals": 18,
        "name": "Opacity (PoS)",
        "address": "0xce6bf09e5c7a3e65b84f88dcc6475c88d38ba5ef"
    },
    "ORARE": {
        "symbol": "ORARE",
        "decimals": 18,
        "name": "One Rare Token",
        "address": "0xff2382bd52efacef02cc895bcbfc4618608aa56f"
    },
    "ORB": {
        "symbol": "ORB",
        "decimals": 18,
        "name": "OrbCity",
        "address": "0x20c750c57c3bc5145af4b7a33d4fb66a8e79fe05"
    },
    "ORBS": {
        "symbol": "ORBS",
        "decimals": 18,
        "name": "Orbs (PoS)",
        "address": "0x614389eaae0a6821dc49062d56bda3d9d45fa2ff"
    },
    "ORE": {
        "symbol": "ORE",
        "decimals": 18,
        "name": "pTokens ORE (PoS)",
        "address": "0xd52f6ca48882be8fbaa98ce390db18e1dbe1062d"
    },
    "ORION": {
        "symbol": "ORION",
        "decimals": 18,
        "name": "Orion Money Token",
        "address": "0x5e0294af1732498c77f8db015a2d52a76298542b"
    },
    "OVR": {
        "symbol": "OVR",
        "decimals": 18,
        "name": "OVR (PoS)",
        "address": "0x1631244689ec1fecbdd22fb5916e920dfc9b8d30"
    },
    "OWL": {
        "symbol": "OWL",
        "decimals": 18,
        "name": "OwlDAO token",
        "address": "0x9085b4d52c3e0b8b6f9af6213e85a433c7d76f19"
    },
    "PAINT": {
        "symbol": "PAINT",
        "decimals": 18,
        "name": "Paint",
        "address": "0x7c28f627ea3aec8b882b51eb1935f66e5b875714"
    },
    "PAXG": {
        "symbol": "PAXG",
        "decimals": 18,
        "name": "Paxos Gold (PoS)",
        "address": "0x553d3d295e0f695b9228246232edf400ed3560b5"
    },
    "PAXW": {
        "symbol": "PAXW",
        "decimals": 18,
        "name": "pax.world",
        "address": "0xc79ae93d9c215eaa8c8da5c77e465bac7de28891"
    },
    "PBR": {
        "symbol": "PBR",
        "decimals": 18,
        "name": "PolkaBridge",
        "address": "0x0d6ae2a429df13e44a07cd2969e085e4833f64a0"
    },
    "PCR": {
        "symbol": "PCR",
        "decimals": 18,
        "name": "Paycer",
        "address": "0xa6083abe845fbb8649d98b8586cbf50b7f233612"
    },
    "PERI": {
        "symbol": "PERI",
        "decimals": 18,
        "name": "Peri Finance Token",
        "address": "0xdc0e17eae3b9651875030244b971fa0223a1764f"
    },
    "PET": {
        "symbol": "PET",
        "decimals": 18,
        "name": "Poodl Exchange Token",
        "address": "0xb7486718ea21c79bbd894126f79f504fd3625f68"
    },
    "pGOB": {
        "symbol": "pGOB",
        "decimals": 18,
        "name": "Goons of Balatroon",
        "address": "0x16d63619cd67b15ff822bfeb60388a226d2e452b"
    },
    "PGX": {
        "symbol": "PGX",
        "decimals": 18,
        "name": "Pegaxy Stone",
        "address": "0xc1c93d475dc82fe72dbc7074d55f5a734f8ceeae"
    },
    "pHBD": {
        "symbol": "pHBD",
        "decimals": 3,
        "name": "Polygon HBD",
        "address": "0x6d969cea201e427d2875724fd4e8044833fbc7f4"
    },
    "PICKLE": {
        "symbol": "PICKLE",
        "decimals": 18,
        "name": "PickleToken (PoS)",
        "address": "0x2b88ad57897a8b496595925f43048301c37615da"
    },
    "PIVN": {
        "symbol": "PIVN",
        "decimals": 18,
        "name": "PIVN",
        "address": "0x38a232cabb8a7f745c7d6e0a5bf300e3499aa8a6"
    },
    "PKTK": {
        "symbol": "PKTK",
        "decimals": 18,
        "name": "Peak Token",
        "address": "0x55bb4d4b4545a886df159354e5fa5791c2d13496"
    },
    "PLA": {
        "symbol": "PLA",
        "decimals": 18,
        "name": "PlayDapp Token (PoS)",
        "address": "0x8765f05adce126d70bcdf1b0a48db573316662eb"
    },
    "PLOT": {
        "symbol": "PLOT",
        "decimals": 18,
        "name": "PlotX",
        "address": "0xe82808eaa78339b06a691fd92e1be79671cad8d3"
    },
    "PMON": {
        "symbol": "PMON",
        "decimals": 18,
        "name": "Polychain Monsters",
        "address": "0x1796ae0b0fa4862485106a0de9b654efe301d0b2"
    },
    "POLI": {
        "symbol": "POLI",
        "decimals": 18,
        "name": "Polinate (PoS)",
        "address": "0x6fb54ffe60386ac33b722be13d2549dd87bf63af"
    },
    "POLX": {
        "symbol": "POLX",
        "decimals": 18,
        "name": "Polylastic",
        "address": "0x187ae45f2d361cbce37c6a8622119c91148f261b"
    },
    "polyBUNNY": {
        "symbol": "polyBUNNY",
        "decimals": 18,
        "name": "Polygon BUNNY Token",
        "address": "0x4c16f69302ccb511c5fac682c7626b9ef0dc126a"
    },
    "POLYCUB": {
        "symbol": "POLYCUB",
        "decimals": 18,
        "name": "PolyCub",
        "address": "0x7cc15fef543f205bf21018f038f591c6bada941c"
    },
    "PolyDoge": {
        "symbol": "PolyDoge",
        "decimals": 18,
        "name": "PolyDoge",
        "address": "0x8a953cfe442c5e8855cc6c61b1293fa648bae472"
    },
    "POLYPAD": {
        "symbol": "POLYPAD",
        "decimals": 18,
        "name": "POLYPAD.com",
        "address": "0x30ea765d4dda26e0f89e1b23a7c7b2526b7d29ec"
    },
    "POOL": {
        "symbol": "POOL",
        "decimals": 18,
        "name": "PoolTogether (PoS)",
        "address": "0x25788a1a171ec66da6502f9975a15b609ff54cf6"
    },
    "POP": {
        "symbol": "POP",
        "decimals": 18,
        "name": "Popcorn (PoS)",
        "address": "0xc5b57e9a1e7914fda753a88f24e5703e617ee50c"
    },
    "PORTX": {
        "symbol": "PORTX",
        "decimals": 18,
        "name": "ChainPort Token [via ChainPort.io]",
        "address": "0x189586b5f6317538ae50c20a976597da38984a24"
    },
    "PPAY": {
        "symbol": "PPAY",
        "decimals": 18,
        "name": "Plasma (PoS)",
        "address": "0x08158a6b5d4018340387d1a302f882e98a8bc5b4"
    },
    "PPRCY": {
        "symbol": "PPRCY",
        "decimals": 8,
        "name": "Wrapped PRCY",
        "address": "0xdfc3829b127761a3218bfcee7fc92e1232c9d116"
    },
    "PROPEL": {
        "symbol": "PROPEL",
        "decimals": 18,
        "name": "Propel",
        "address": "0xe0ce60af0850bf54072635e66e79df17082a1109"
    },
    "PROS": {
        "symbol": "PROS",
        "decimals": 18,
        "name": "Prosper",
        "address": "0x6109cb051c5c64093830121ed76272ab04bbdd7c"
    },
    "PRXY": {
        "symbol": "PRXY",
        "decimals": 18,
        "name": "Proxy",
        "address": "0xab3d689c22a2bb821f50a4ff0f21a7980dcb8591"
    },
    "PS1": {
        "symbol": "PS1",
        "decimals": 18,
        "name": "PolysportsToken",
        "address": "0x32cd1bcb75473845b5d1db6ece60aec6e41d8518"
    },
    "PSP": {
        "symbol": "PSP",
        "decimals": 18,
        "name": "ParaSwap (PoS)",
        "address": "0x42d61d766b85431666b39b89c43011f24451bff6"
    },
    "PUSD": {
        "symbol": "PUSD",
        "decimals": 18,
        "name": "PUSD",
        "address": "0x9af3b7dc29d3c4b1a5731408b6a9656fa7ac3b72"
    },
    "PYM": {
        "symbol": "PYM",
        "decimals": 18,
        "name": "Playermon",
        "address": "0x0bd49815ea8e2682220bcb41524c0dd10ba71d41"
    },
    "PYQ": {
        "symbol": "PYQ",
        "decimals": 18,
        "name": "PYQ",
        "address": "0x5a3064cbdccf428ae907796cf6ad5a664cd7f3d8"
    },
    "PYR": {
        "symbol": "PYR",
        "decimals": 18,
        "name": "PYR Token",
        "address": "0x430ef9263e76dae63c84292c3409d61c598e9682"
    },
    "QI": {
        "symbol": "QI",
        "decimals": 18,
        "name": "Qi Dao",
        "address": "0x580a84c73811e1839f75d86d75d88cca0c241ff4"
    },
    "QUICK": {
        "symbol": "QUICK",
        "decimals": 18,
        "name": "QuickSwap",
        "address": "0xb5c064f955d8e7f38fe0460c556a72987494ee17"
    },
    "QUIDD": {
        "symbol": "QUIDD",
        "decimals": 18,
        "name": "QUIDD",
        "address": "0x123706cdd8e60324e610e9a2cc7012d0f45a5b8e"
    },
    "RADIO": {
        "symbol": "RADIO",
        "decimals": 18,
        "name": "RadioShack Token",
        "address": "0x613a489785c95afeb3b404cc41565ccff107b6e0"
    },
    "RAI": {
        "symbol": "RAI",
        "decimals": 18,
        "name": "Rai Reflex Index (PoS)",
        "address": "0x00e5646f60ac6fb446f621d146b6e1886f002905"
    },
    "RAIDER": {
        "symbol": "RAIDER",
        "decimals": 18,
        "name": "RaiderToken",
        "address": "0xcd7361ac3307d1c5a46b63086a90742ff44c63b3"
    },
    "RAZOR": {
        "symbol": "RAZOR",
        "decimals": 18,
        "name": "RAZOR (PoS)",
        "address": "0xc91c06db0f7bffba61e2a5645cc15686f0a8c828"
    },
    "RBC": {
        "symbol": "RBC",
        "decimals": 18,
        "name": "Rubic (PoS)",
        "address": "0xc3cffdaf8f3fdf07da6d5e3a89b8723d5e385ff8"
    },
    "RBLS": {
        "symbol": "RBLS",
        "decimals": 8,
        "name": "Rebel Bots Token",
        "address": "0xe26cda27c13f4f87cffc2f437c5900b27ebb5bbb"
    },
    "RBW": {
        "symbol": "RBW",
        "decimals": 18,
        "name": "Rainbow Token",
        "address": "0x431cd3c9ac9fc73644bf68bf5691f4b83f9e104f"
    },
    "ReelT": {
        "symbol": "ReelT",
        "decimals": 8,
        "name": "Reel Token",
        "address": "0x19ccfe396006ffe7a92ab667b0ef90ce61b66f9f"
    },
    "RELAY": {
        "symbol": "RELAY",
        "decimals": 18,
        "name": "Relay Token",
        "address": "0x904371845bc56dcbbcf0225ef84a669b2fd6bd0d"
    },
    "renBTC": {
        "symbol": "renBTC",
        "decimals": 8,
        "name": "renBTC",
        "address": "0xdbf31df14b66535af65aac99c32e9ea844e14501"
    },
    "renDOGE": {
        "symbol": "renDOGE",
        "decimals": 8,
        "name": "renDOGE",
        "address": "0xce829a89d4a55a63418bcc43f00145adef0edb8e"
    },
    "REQ": {
        "symbol": "REQ",
        "decimals": 18,
        "name": "Request",
        "address": "0xb25e20de2f2ebb4cffd4d16a55c7b395e8a94762"
    },
    "REVV": {
        "symbol": "REVV",
        "decimals": 18,
        "name": "REVV",
        "address": "0x70c006878a5a50ed185ac4c87d837633923de296"
    },
    "RGP": {
        "symbol": "RGP",
        "decimals": 18,
        "name": "RigelToken",
        "address": "0x4af5ff1a60a6ef6c7c8f9c4e304cd9051fca3ec0"
    },
    "RIA": {
        "symbol": "RIA",
        "decimals": 18,
        "name": "Calvaria: Duels of Eternity",
        "address": "0xf9cea445c2ac1668f50caa2c2924f93606a4a37d"
    },
    "RIC": {
        "symbol": "RIC",
        "decimals": 18,
        "name": "Ricochet",
        "address": "0x263026e7e53dbfdce5ae55ade22493f828922965"
    },
    "RICE": {
        "symbol": "RICE",
        "decimals": 18,
        "name": "RICE",
        "address": "0x60138efceb1f7d8e10c8cb89bb61bbdbeebb4ffc"
    },
    "RISE": {
        "symbol": "RISE",
        "decimals": 18,
        "name": "EverRise",
        "address": "0xc17c30e98541188614df99239cabd40280810ca3"
    },
    "RNDR": {
        "symbol": "RNDR",
        "decimals": 18,
        "name": "Render Token",
        "address": "0x61299774020da444af134c82fa83e3810b309991"
    },
    "ROLL": {
        "symbol": "ROLL",
        "decimals": 18,
        "name": "Polyroll Token",
        "address": "0xc68e83a305b0fad69e264a1769a0a070f190d2d6"
    },
    "ROND": {
        "symbol": "ROND",
        "decimals": 18,
        "name": "ROND Coin",
        "address": "0x204820b6e6feae805e376d2c6837446186e57981"
    },
    "ROOBEE": {
        "symbol": "ROOBEE",
        "decimals": 18,
        "name": "ROOBEE",
        "address": "0xfafa220145dfa5c3ec85b6fa8a75aee2451cde5e"
    },
    "ROUTE (PoS)": {
        "symbol": "ROUTE (PoS)",
        "decimals": 18,
        "name": "Route",
        "address": "0x16eccfdbb4ee1a85a33f3a9b21175cd7ae753db4"
    },
    "ROY": {
        "symbol": "ROY",
        "decimals": 18,
        "name": "Royale",
        "address": "0x68ee0d0aad9e1984af85ca224117e4d20eaf68be"
    },
    "ROYA": {
        "symbol": "ROYA",
        "decimals": 18,
        "name": "Royale (PoS)",
        "address": "0x0bd820ad2d7ab7305b5c9538ba824c9b9beb0561"
    },
    "Runy": {
        "symbol": "Runy",
        "decimals": 18,
        "name": "Runy",
        "address": "0x578fee9def9a270c20865242cfd4ff86f31d0e5b"
    },
    "RVF": {
        "symbol": "RVF",
        "decimals": 18,
        "name": "Rocket Vault (PoS)",
        "address": "0x2ce13e4199443fdfff531abb30c9b6594446bbc7"
    },
    "RVLT": {
        "symbol": "RVLT",
        "decimals": 18,
        "name": "Revolt 2 Earn",
        "address": "0xf0f9d895aca5c8678f706fb8216fa22957685a13"
    },
    "SAFLE": {
        "symbol": "SAFLE",
        "decimals": 18,
        "name": "Safle",
        "address": "0x04b33078ea1aef29bf3fb29c6ab7b200c58ea126"
    },
    "SALE": {
        "symbol": "SALE",
        "decimals": 18,
        "name": "DxSale.Network (PoS)",
        "address": "0x8f6196901a4a153d8ee8f3fa779a042f6092d908"
    },
    "SAND": {
        "symbol": "SAND",
        "decimals": 18,
        "name": "SAND",
        "address": "0xbbba073c31bf03b8acf7c28ef0738decf3695683"
    },
    "SAVG": {
        "symbol": "SAVG",
        "decimals": 18,
        "name": "SAVAGE Token",
        "address": "0x981aecc6eb4d382b96a02b75e931900705e95a31"
    },
    "SD": {
        "symbol": "SD",
        "decimals": 18,
        "name": "Stader (PoS)",
        "address": "0x1d734a02ef1e1f5886e66b0673b71af5b53ffa94"
    },
    "Serum": {
        "symbol": "Serum",
        "decimals": 0,
        "name": "Karmaverse Zombie Serum",
        "address": "0x623a1350f6b749575f92ea54d0f745f9f07d3665"
    },
    "SFL": {
        "symbol": "SFL",
        "decimals": 18,
        "name": "Sunflower Land",
        "address": "0xd1f9c58e33933a993a3891f8acfe05a68e1afc05"
    },
    "sfrxETH": {
        "symbol": "sfrxETH",
        "decimals": 18,
        "name": "Staked Frax Ether",
        "address": "0x6d1fdbb266fcc09a16a22016369210a15bb95761"
    },
    "SG": {
        "symbol": "SG",
        "decimals": 18,
        "name": "SocialGood (PoS)",
        "address": "0x79375c41d88f839f551457145066096c5c8944bc"
    },
    "SHA": {
        "symbol": "SHA",
        "decimals": 18,
        "name": "Safe Haven Token",
        "address": "0x534f39c5f4df9cb13e16b24ca07c7c8c0e2eadb7"
    },
    "SHIB": {
        "symbol": "SHIB",
        "decimals": 18,
        "name": "SHIBA INU (PoS)",
        "address": "0x6f8a06447ff6fcf75d803135a7de15ce88c1d4ec"
    },
    "SKP": {
        "symbol": "SKP",
        "decimals": 18,
        "name": "SKY PLAY",
        "address": "0x4c665bbafd28ec9e5d792345f470ebfca21e3d15"
    },
    "SKRT": {
        "symbol": "SKRT",
        "decimals": 18,
        "name": "Sekuritance (PoS)",
        "address": "0xe51e88dd08499762b8e4eb3a9f3da9b8e79608c3"
    },
    "SLP": {
        "symbol": "SLP",
        "decimals": 0,
        "name": "Smooth Love Potion (PoS)",
        "address": "0x0c7304fbaf2a320a1c50c46fe03752722f729946"
    },
    "SMT": {
        "symbol": "SMT",
        "decimals": 18,
        "name": "Swarm Markets",
        "address": "0xe631dabef60c37a37d70d3b4f812871df663226f"
    },
    "SNG": {
        "symbol": "SNG",
        "decimals": 18,
        "name": "Synergy Land Token",
        "address": "0xad9f61563b104281b14322fec8b42eb67711bf68"
    },
    "SNK": {
        "symbol": "SNK",
        "decimals": 18,
        "name": "Snook",
        "address": "0x689f8e5913c158ffb5ac5aeb83b3c875f5d20309"
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
        "name": "Synthetix Network Token (PoS)",
        "address": "0x50b728d8d964fd00c2d0aad81718b71311fef68a"
    },
    "SOL": {
        "symbol": "SOL",
        "decimals": 9,
        "name": "Wrapped SOL",
        "address": "0xd93f7e271cb87c23aaa73edc008a79646d1f9912"
    },
    "SOLAR": {
        "symbol": "SOLAR",
        "decimals": 18,
        "name": "Dawn Star Share",
        "address": "0xf8eed914a0bacaf30c13420989bb7c81b75d833a"
    },
    "SPACE": {
        "symbol": "SPACE",
        "decimals": 18,
        "name": "Space Token",
        "address": "0xb53ec4ace420a62cfb75afdeba600d284777cd65"
    },
    "SPADE": {
        "symbol": "SPADE",
        "decimals": 18,
        "name": "PolygonFarm Finance",
        "address": "0xf5ea626334037a2cf0155d49ea6462fddc6eff19"
    },
    "SPN": {
        "symbol": "SPN",
        "decimals": 18,
        "name": "Sportzchain",
        "address": "0xa3c53b53fe43083aa31c6f32ffe90c4d91b44391"
    },
    "SPORT": {
        "symbol": "SPORT",
        "decimals": 18,
        "name": "Sport",
        "address": "0x503836c8c3a453c57f58cc99b070f2e78ec14fc0"
    },
    "SSGTx": {
        "symbol": "SSGTx",
        "decimals": 18,
        "name": "SafeSwap",
        "address": "0xd0cfd20e8bbdb7621b705a4fd61de2e80c2cd02f"
    },
    "STACK": {
        "symbol": "STACK",
        "decimals": 18,
        "name": "StackOS",
        "address": "0x980111ae1b84e50222c8843e3a7a038f36fecd2b"
    },
    "START": {
        "symbol": "START",
        "decimals": 18,
        "name": "BSCstarter",
        "address": "0x6ccf12b480a99c54b23647c995f4525d544a7e72"
    },
    "STBU": {
        "symbol": "STBU",
        "decimals": 18,
        "name": "Stobox Token v.2",
        "address": "0xcf403036bc139d30080d2cf0f5b48066f98191bb"
    },
    "STG": {
        "symbol": "STG",
        "decimals": 18,
        "name": "StargateToken",
        "address": "0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590"
    },
    "stMATIC": {
        "symbol": "stMATIC",
        "decimals": 18,
        "name": "Staked MATIC (PoS)",
        "address": "0x3a58a54c066fdc0f2d55fc9c89f0415c92ebf3c4"
    },
    "STND": {
        "symbol": "STND",
        "decimals": 18,
        "name": "Standard",
        "address": "0x08be454de533509e8832b257116c5506e55b0b64"
    },
    "STORJ": {
        "symbol": "STORJ",
        "decimals": 8,
        "name": "StorjToken (PoS)",
        "address": "0xd72357daca2cf11a5f155b9ff7880e595a3f5792"
    },
    "STZ": {
        "symbol": "STZ",
        "decimals": 18,
        "name": "99Starz",
        "address": "0x2c92a8a41f4b806a6f6f1f7c9d9dec78dcd8c18e"
    },
    "SUPER": {
        "symbol": "SUPER",
        "decimals": 18,
        "name": "SuperFarm (PoS)",
        "address": "0xa1428174f516f527fafdd146b883bb4428682737"
    },
    "SURE": {
        "symbol": "SURE",
        "decimals": 18,
        "name": "inSure (PoS)",
        "address": "0xf88332547c680f755481bf489d890426248bb275"
    },
    "SUSHI": {
        "symbol": "SUSHI",
        "decimals": 18,
        "name": "SushiToken (PoS)",
        "address": "0x0b3f868e0be5597d5db7feb59e1cadbb0fdda50a"
    },
    "SWAP": {
        "symbol": "SWAP",
        "decimals": 18,
        "name": "TrustSwap Token (PoS)",
        "address": "0x3809dcdd5dde24b37abe64a5a339784c3323c44f"
    },
    "SWASH": {
        "symbol": "SWASH",
        "decimals": 18,
        "name": "Swash Token",
        "address": "0xba3cb8329d442e6f9eb70fafe1e214251df3d275"
    },
    "SWAY": {
        "symbol": "SWAY",
        "decimals": 18,
        "name": "Sway Social Protocol",
        "address": "0x262b8aa7542004f023b0eb02bc6b96350a02b728"
    },
    "SWP": {
        "symbol": "SWP",
        "decimals": 18,
        "name": "Stepwatch Paradise",
        "address": "0xabede05598760e399ed7eb24900b30c51788f00f"
    },
    "SX": {
        "symbol": "SX",
        "decimals": 18,
        "name": "SportX (PoS)",
        "address": "0x840195888db4d6a99ed9f73fcd3b225bb3cb1a79"
    },
    "SYN": {
        "symbol": "SYN",
        "decimals": 18,
        "name": "Synapse",
        "address": "0xf8f9efc0db77d8881500bb06ff5d6abc3070e695"
    },
    "TCGC": {
        "symbol": "TCGC",
        "decimals": 18,
        "name": "TCGCoin (PoS)",
        "address": "0x44acd96620b708162af4a90524f29a6839675533"
    },
    "TECH": {
        "symbol": "TECH",
        "decimals": 18,
        "name": "Cryptomeda",
        "address": "0x6286a9e6f7e745a6d884561d88f94542d6715698"
    },
    "TEL": {
        "symbol": "TEL",
        "decimals": 2,
        "name": "Telcoin (PoS)",
        "address": "0xdf7837de1f2fa4631d716cf2502f8b230f1dcc32"
    },
    "TETU": {
        "symbol": "TETU",
        "decimals": 18,
        "name": "TETU Reward Token",
        "address": "0x255707b70bf90aa112006e1b07b9aea6de021424"
    },
    "THALES": {
        "symbol": "THALES",
        "decimals": 18,
        "name": "Thales DAO Token (PoS)",
        "address": "0x692c44990e4f408ba0917f5c78a83160c1557237"
    },
    "TITAN": {
        "symbol": "TITAN",
        "decimals": 18,
        "name": "IRON Titanium Token",
        "address": "0xaaa5b9e6c589642f98a1cda99b9d024b8407285a"
    },
    "TKB": {
        "symbol": "TKB",
        "decimals": 18,
        "name": "TokenBot",
        "address": "0x0c5f149362ca17eac5d18e6912ab4f5aeabf88e6"
    },
    "TNDR": {
        "symbol": "TNDR",
        "decimals": 18,
        "name": "Thunder Token",
        "address": "0x29e3e6ad4eeadf767919099ee23c907946435a70"
    },
    "TNGBL": {
        "symbol": "TNGBL",
        "decimals": 18,
        "name": "Tangible",
        "address": "0x49e6a20f1bbdfeec2a8222e052000bbb14ee6007"
    },
    "TNT": {
        "symbol": "TNT",
        "decimals": 18,
        "name": "Travel and Tourism token",
        "address": "0x25c498781ca536547b147e2199f572e5393d36f0"
    },
    "TOTEM": {
        "symbol": "TOTEM",
        "decimals": 6,
        "name": "TOTEM",
        "address": "0x1adcef5c780d8895ac77e6ee9239b4b3ecb76da2"
    },
    "TOWER": {
        "symbol": "TOWER",
        "decimals": 18,
        "name": "TOWER",
        "address": "0x2bc07124d8dac638e290f401046ad584546bc47b"
    },
    "TRACE": {
        "symbol": "TRACE",
        "decimals": 18,
        "name": "Trace Network",
        "address": "0x4287f07cbe6954f9f0decd91d0705c926d8d03a4"
    },
    "TRADE": {
        "symbol": "TRADE",
        "decimals": 18,
        "name": "Polytrade (PoS)",
        "address": "0x692ac1e363ae34b6b489148152b12e2785a3d8d6"
    },
    "TRB": {
        "symbol": "TRB",
        "decimals": 18,
        "name": "Tellor Tributes (PoS)",
        "address": "0xe3322702bedaaed36cddab233360b939775ae5f1"
    },
    "TRC": {
        "symbol": "TRC",
        "decimals": 18,
        "name": "TRACER Token",
        "address": "0x5c3e6447d97fe80a9818ef3fe14a2bf5bb83e0b8"
    },
    "TRY": {
        "symbol": "TRY",
        "decimals": 18,
        "name": "TryHards",
        "address": "0xefee2de82343be622dcb4e545f75a3b9f50c272d"
    },
    "TRYB": {
        "symbol": "TRYB",
        "decimals": 6,
        "name": "BiLira (PoS)",
        "address": "0x4fb71290ac171e1d144f7221d882becac7196eb5"
    },
    "TUSD": {
        "symbol": "TUSD",
        "decimals": 18,
        "name": "TrueUSD (PoS)",
        "address": "0x2e1ad108ff1d8c782fcbbb89aad783ac49586756"
    },
    "TUT": {
        "symbol": "TUT",
        "decimals": 18,
        "name": "Tutellus token",
        "address": "0x12a34a6759c871c4c1e8a0a42cfc97e4d7aaf68d"
    },
    "TXL": {
        "symbol": "TXL",
        "decimals": 18,
        "name": "Tixl Token",
        "address": "0x8eef5a82e6aa222a60f009ac18c24ee12dbf4b41"
    },
    "UBT": {
        "symbol": "UBT",
        "decimals": 8,
        "name": "Unibright (PoS)",
        "address": "0x7fbc10850cae055b27039af31bd258430e714c62"
    },
    "UCO": {
        "symbol": "UCO",
        "decimals": 18,
        "name": "UnirisToken (PoS)",
        "address": "0x3c720206bfacb2d16fa3ac0ed87d2048dbc401fc"
    },
    "UFARM": {
        "symbol": "UFARM",
        "decimals": 18,
        "name": "UNIFARM Token (PoS)",
        "address": "0xa7305ae84519ff8be02484cda45834c4e7d13dd6"
    },
    "UFI": {
        "symbol": "UFI",
        "decimals": 18,
        "name": "PureFi Token (PoS)",
        "address": "0x3c205c8b3e02421da82064646788c82f7bd753b9"
    },
    "UFT": {
        "symbol": "UFT",
        "decimals": 18,
        "name": "UniLend Finance Token (PoS)",
        "address": "0x5b4cf2c120a9702225814e18543ee658c5f8631e"
    },
    "ULT": {
        "symbol": "ULT",
        "decimals": 18,
        "name": "Shardus (PoS)",
        "address": "0xf0059cc2b3e980065a906940fbce5f9db7ae40a7"
    },
    "ULX": {
        "symbol": "ULX",
        "decimals": 18,
        "name": "Ultron",
        "address": "0xfa5d5dd2517ee9c1419534a16b132adde2e3d948"
    },
    "UM": {
        "symbol": "UM",
        "decimals": 18,
        "name": "Continuum",
        "address": "0x3b1a0c9252ee7403093ff55b4a5886d49a3d837a"
    },
    "UMA": {
        "symbol": "UMA",
        "decimals": 18,
        "name": "UMA Voting Token v1 (PoS)",
        "address": "0x3066818837c5e6ed6601bd5a91b0762877a6b731"
    },
    "UMMA": {
        "symbol": "UMMA",
        "decimals": 18,
        "name": "UMMA Token",
        "address": "0x36596a1dc57c695bed1a063470a7802797dca133"
    },
    "UNB": {
        "symbol": "UNB",
        "decimals": 18,
        "name": "Unbound",
        "address": "0xd81f558b71a5323e433729009d55159955f8a7f9"
    },
    "UNI": {
        "symbol": "UNI",
        "decimals": 18,
        "name": "Uniswap (PoS)",
        "address": "0xb33eaad8d922b1083446dc23f610c2567fb5180f"
    },
    "UNIC": {
        "symbol": "UNIC",
        "decimals": 18,
        "name": "UNIC",
        "address": "0x21ce5251d47aa72d2d1dc849b1bcce14d2467d1b"
    },
    "UNIM": {
        "symbol": "UNIM",
        "decimals": 18,
        "name": "Unicorn Milk",
        "address": "0x64060ab139feaae7f06ca4e63189d86adeb51691"
    },
    "UPO": {
        "symbol": "UPO",
        "decimals": 18,
        "name": "UpOnly",
        "address": "0x9dbfc1cbf7a1e711503a29b4b5f9130ebeccac96"
    },
    "USD+": {
        "symbol": "USD+",
        "decimals": 6,
        "name": "USD+",
        "address": "0x236eec6359fb44cce8f97e99387aa7f8cd5cde1f"
    },
    "USDC": {
        "symbol": "USDC",
        "decimals": 6,
        "name": "USD Coin (PoS)",
        "address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
    },
    "USDT": {
        "symbol": "USDT",
        "decimals": 6,
        "name": "(PoS) Tether USD",
        "address": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
    },
    "UST": {
        "symbol": "UST",
        "decimals": 18,
        "name": "Wrapped UST Token (PoS)",
        "address": "0x692597b009d13c4049a947cab2239b7d6517875f"
    },
    "USV": {
        "symbol": "USV",
        "decimals": 9,
        "name": "Universal Store of Value",
        "address": "0xac63686230f64bdeaf086fe6764085453ab3023f"
    },
    "USX": {
        "symbol": "USX",
        "decimals": 18,
        "name": "dForce USD",
        "address": "0xcf66eb3d546f0415b368d98a95eaf56ded7aa752"
    },
    "VATRENI": {
        "symbol": "VATRENI",
        "decimals": 18,
        "name": "Vatreni Token",
        "address": "0xd60deba014459f07bbcc077a5b817f31dafd5229"
    },
    "VEE": {
        "symbol": "VEE",
        "decimals": 18,
        "name": "BLOCKv Token (PoS)",
        "address": "0xf1c1a3c2481a3a8a3f173a9ab5ade275292a6fa3"
    },
    "VENT": {
        "symbol": "VENT",
        "decimals": 18,
        "name": "VENT [via ChainPort.io]",
        "address": "0xf21441f9ec4c1fe69cb7cf186eceab31af2b658d"
    },
    "VERSE": {
        "symbol": "VERSE",
        "decimals": 18,
        "name": "Shibaverse",
        "address": "0xa1388e73c51b37383b1ab9dce8317ef5a0349cc5"
    },
    "VEST": {
        "symbol": "VEST",
        "decimals": 18,
        "name": "DAO Invest (PoS)",
        "address": "0x381caf412b45dac0f62fbeec89de306d3eabe384"
    },
    "VHC": {
        "symbol": "VHC",
        "decimals": 18,
        "name": "Vault Hill City (PoS)",
        "address": "0x51b5619f5180e333d18b6310c8d540aea43a0371"
    },
    "VINU": {
        "symbol": "VINU",
        "decimals": 18,
        "name": "Vita Inu",
        "address": "0xafcdd4f666c84fed1d8bd825aa762e3714f652c9"
    },
    "VOXEL": {
        "symbol": "VOXEL",
        "decimals": 18,
        "name": "VOXEL Token",
        "address": "0xd0258a3fd00f38aa8090dfee343f10a9d4d30d3f"
    },
    "VP": {
        "symbol": "VP",
        "decimals": 11,
        "name": "Vortex Protocol",
        "address": "0xf46cb10e8c5fb9368bbf497a3176b80c0af66d44"
    },
    "VSP": {
        "symbol": "VSP",
        "decimals": 18,
        "name": "VesperToken (PoS)",
        "address": "0x09c5a4bca808bd1ba2b8e6b3aaf7442046b4ca5b"
    },
    "W$C": {
        "symbol": "W$C",
        "decimals": 18,
        "name": "World$tateCoin",
        "address": "0x77a6f2e9a9e44fd5d5c3f9be9e52831fc1c3c0a0"
    },
    "WALBT": {
        "symbol": "WALBT",
        "decimals": 18,
        "name": "Wrapped AllianceBlock Token",
        "address": "0x35b2ece5b1ed6a7a99b83508f8ceeab8661e0632"
    },
    "wBAN": {
        "symbol": "wBAN",
        "decimals": 18,
        "name": "Wrapped Banano",
        "address": "0xe20b9e246db5a0d21bf9209e4858bc9a3ff7a034"
    },
    "WBNB": {
        "symbol": "WBNB",
        "decimals": 18,
        "name": "Wrapped BNB",
        "address": "0xecdcb5b88f8e3c15f95c720c51c71c9e2080525d"
    },
    "WCHI": {
        "symbol": "WCHI",
        "decimals": 8,
        "name": "Wrapped CHI (PoS)",
        "address": "0xe79feaaa457ad7899357e8e2065a3267ac9ee601"
    },
    "WEB3": {
        "symbol": "WEB3",
        "decimals": 18,
        "name": "Arch Ethereum Web3 (PoS)",
        "address": "0xbcd2c5c78000504efbc1ce6489dfcac71835406a"
    },
    "WELT": {
        "symbol": "WELT",
        "decimals": 18,
        "name": "FABWELT",
        "address": "0x23e8b6a3f6891254988b84da3738d2bfe5e703b9"
    },
    "WIFI": {
        "symbol": "WIFI",
        "decimals": 18,
        "name": "WiFi Map",
        "address": "0xe238ecb42c424e877652ad82d8a939183a04c35f"
    },
    "WLD": {
        "symbol": "WLD",
        "decimals": 18,
        "name": "wLitiDAO",
        "address": "0xa936e1f747d14fc30d08272d065c8aef4ab7f810"
    },
    "WNT": {
        "symbol": "WNT",
        "decimals": 18,
        "name": "Wicrypt Network Token",
        "address": "0x82a0e6c02b91ec9f6ff943c0a933c03dbaa19689"
    },
    "WOLF": {
        "symbol": "WOLF",
        "decimals": 9,
        "name": "moonwolf.io",
        "address": "0x8f18dc399594b451eda8c5da02d0563c0b2d0f16"
    },
    "WOMBAT": {
        "symbol": "WOMBAT",
        "decimals": 18,
        "name": "Wombat",
        "address": "0x0c9c7712c83b3c70e7c5e11100d33d9401bdf9dd"
    },
    "WOO": {
        "symbol": "WOO",
        "decimals": 18,
        "name": "Wootrade Network (PoS)",
        "address": "0x1b815d120b3ef02039ee11dc2d33de7aa4a8c603"
    },
    "WOOFY": {
        "symbol": "WOOFY",
        "decimals": 12,
        "name": "Woofy",
        "address": "0xd0660cd418a64a1d44e9214ad8e459324d8157f1"
    },
    "WORK": {
        "symbol": "WORK",
        "decimals": 18,
        "name": "The Employment Commons Work Token (PoS)",
        "address": "0x6002410dda2fb88b4d0dc3c1d562f7761191ea80"
    },
    "WOW": {
        "symbol": "WOW",
        "decimals": 18,
        "name": "WOWswap",
        "address": "0x855d4248672a1fce482165e8dbe1207b94b1968a"
    },
    "wPPC": {
        "symbol": "wPPC",
        "decimals": 6,
        "name": "WrappedPeercoin",
        "address": "0x91e7e32c710661c44ae44d10aa86135d91c3ed65"
    },
    "WRLD": {
        "symbol": "WRLD",
        "decimals": 18,
        "name": "NFT Worlds",
        "address": "0xd5d86fc8d5c0ea1ac1ac5dfab6e529c9967a45e9"
    },
    "WRX": {
        "symbol": "WRX",
        "decimals": 8,
        "name": "Wazirx (PoS)",
        "address": "0x72d6066f486bd0052eefb9114b66ae40e0a6031a"
    },
    "WSPP": {
        "symbol": "WSPP",
        "decimals": 18,
        "name": "WolfSafePoorPeople",
        "address": "0x46d502fac9aea7c5bc7b13c8ec9d02378c33d36f"
    },
    "wstETH": {
        "symbol": "wstETH",
        "decimals": 18,
        "name": "Wrapped liquid staked Ether 2.0 (PoS)",
        "address": "0x03b54a6e9a984069379fae1a4fc4dbae93b3bccd"
    },
    "WUBQ": {
        "symbol": "WUBQ",
        "decimals": 18,
        "name": "Wrapped Ubiq",
        "address": "0xb1c5c9b97b35592777091cd34ffff141ae866abd"
    },
    "wUSDR": {
        "symbol": "wUSDR",
        "decimals": 9,
        "name": "Wrapped USDR",
        "address": "0xaf0d9d65fc54de245cda37af3d18cbec860a4d4b"
    },
    "XBLL": {
        "symbol": "XBLL",
        "decimals": 18,
        "name": "Bull",
        "address": "0x8110706a399d457d67b7a2b7636482b4bfcebb21"
    },
    "XCAD": {
        "symbol": "XCAD",
        "decimals": 18,
        "name": "XCAD Token (PoS)",
        "address": "0xa55870278d6389ec5b524553d03c04f5677c061e"
    },
    "XCASH": {
        "symbol": "XCASH",
        "decimals": 18,
        "name": "X-Cash (PoS)",
        "address": "0x03678f2c2c762dc63c2bb738c3a837d366eda560"
    },
    "XDAO": {
        "symbol": "XDAO",
        "decimals": 18,
        "name": "XDAO",
        "address": "0x71eeba415a523f5c952cc2f06361d5443545ad28"
    },
    "xDG": {
        "symbol": "xDG",
        "decimals": 18,
        "name": "Decentral Games Governance (PoS)",
        "address": "0xc6480da81151b2277761024599e8db2ad4c388c8"
    },
    "XED": {
        "symbol": "XED",
        "decimals": 18,
        "name": "Exeedme (PoS)",
        "address": "0x2fe8733dcb25bfbba79292294347415417510067"
    },
    "XEND": {
        "symbol": "XEND",
        "decimals": 18,
        "name": "XEND",
        "address": "0x86775d0b80b3df266af5377db34ba8f318d715ec"
    },
    "XGEM": {
        "symbol": "XGEM",
        "decimals": 18,
        "name": "Exchange Genesis Ethlas Medium",
        "address": "0x02649c1ff4296038de4b9ba8f491b42b940a8252"
    },
    "XIDR": {
        "symbol": "XIDR",
        "decimals": 6,
        "name": "XIDR",
        "address": "0x2c826035c1c36986117a0e949bd6ad4bab54afe2"
    },
    "XMT": {
        "symbol": "XMT",
        "decimals": 18,
        "name": "MetalSwap",
        "address": "0xadbe0eac80f955363f4ff47b0f70189093908c04"
    },
    "XP": {
        "symbol": "XP",
        "decimals": 18,
        "name": "PolkaFantasy",
        "address": "0x180cfbe9843d79bcafcbcdf23590247793dfc95b"
    },
    "XSGD": {
        "symbol": "XSGD",
        "decimals": 6,
        "name": "XSGD",
        "address": "0xdc3326e71d45186f113a2f448984ca0e8d201995"
    },
    "XTM": {
        "symbol": "XTM",
        "decimals": 18,
        "name": "Torum (PoS)",
        "address": "0xe1c42be9699ff4e11674819c1885d43bd92e9d15"
    },
    "XWIN": {
        "symbol": "XWIN",
        "decimals": 18,
        "name": "xWIN Token",
        "address": "0x6cd6cb131764c704ba9167c29930fbdc38901ab7"
    },
    "XY": {
        "symbol": "XY",
        "decimals": 18,
        "name": "XY Token",
        "address": "0x55555555a687343c6ce28c8e1f6641dc71659fad"
    },
    "YAE": {
        "symbol": "YAE",
        "decimals": 18,
        "name": "Cryptonovae",
        "address": "0x4ee438be38f8682abb089f2bfea48851c5e71eaf"
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
        "name": "(PoS) yearn.finance",
        "address": "0xda537104d6a5edd53c6fbba9a898708e465260b6"
    },
    "YFII": {
        "symbol": "YFII",
        "decimals": 18,
        "name": "YFII.finance (PoS)",
        "address": "0xb8cb8a7f4c2885c03e57e973c74827909fdc2032"
    },
    "YLD": {
        "symbol": "YLD",
        "decimals": 18,
        "name": "Yield (PoS)",
        "address": "0x4cebdbcb286101a17d3ea1f7fe7bbded2b2053dd"
    },
    "YVS": {
        "symbol": "YVS",
        "decimals": 18,
        "name": "YVS.Finance (PoS)",
        "address": "0xb565cf70613ca464d68427106af80c67a8e4b801"
    },
    "ZED": {
        "symbol": "ZED",
        "decimals": 18,
        "name": "ZED RUN",
        "address": "0x5ec03c1f7fa7ff05ec476d19e34a22eddb48acdc"
    },
    "ZEE": {
        "symbol": "ZEE",
        "decimals": 18,
        "name": "ZeroSwapToken",
        "address": "0xfd4959c06fbcc02250952daebf8e0fb38cf9fd8c"
    },
    "ZEXI": {
        "symbol": "ZEXI",
        "decimals": 18,
        "name": "ZEXICON",
        "address": "0x0c93709c4389b6eebdb0a4d3d60092bb61446382"
    },
    "ZRO": {
        "symbol": "ZRO",
        "decimals": 18,
        "name": "ZROToken",
        "address": "0x6acda5e7eb1117733dc7cb6158fc67f226b32022"
    },
    "ZRX": {
        "symbol": "ZRX",
        "decimals": 18,
        "name": "0x Protocol Token (PoS)",
        "address": "0x5559edb74751a0ede9dea4dc23aee72cca6be3d5"
    }
}
