# pylint:disable=too-many-lines

OPTIMISM_TOKENS = {
    "BTC": {
        "symbol": "BTC",
        "decimals": 8,
        "name": "Bitcoin",
        "address": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "set_loaded": True,
    },
    "ETH": {
        "symbol": "ETH",
        "decimals": 18,
        "name": "Ethereum",
        # "address": "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000",
        "address": "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
        "set_loaded": True,
        "is_native_token": True
    },
    "USDC": {
        "symbol": "USDC",
        "decimals": 6,
        "name": "USD Coin",
        "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607"
    },
    "WBTC": {
        "symbol": "WBTC",
        "decimals": 8,
        "name": "Wrapped BTC",
        "address": "0x68f180fcce6836688e9084f035309e29bf0a2095"
    },
    "DAI": {
        "symbol": "DAI",
        "decimals": 18,
        "name": "Dai Stablecoin",
        "address": "0xda10009cbd5d07dd0cecc66161fc93d7c9000da1"
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
    },
    "CRV": {
        "symbol": "CRV",
        "decimals": 18,
        "name": "Curve DAO Token",
        "address": "0x0994206dfe8de6ec6920ff4d779b0d950605fb53"
    },
    "THALES": {
        "symbol": "THALES",
        "decimals": 18,
        "name": "Thales DAO Token",
        "address": "0x217d47011b23bb961eb6d93ca9945b7501a5bb11"
    },
    "USDT": {
        "symbol": "USDT",
        "decimals": 6,
        "name": "Tether USD",
        "address": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58"
    },
    ###
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
    "AMKT": {
        "symbol": "AMKT",
        "decimals": 18,
        "name": "Alongside Crypto Market Index",
        "address": "0xc27d9bc194a648fe3069955a5126699c4e49351c"
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
    "BitBTC": {
        "symbol": "BitBTC",
        "decimals": 18,
        "name": "BitBTC",
        "address": "0xc98b98d17435aa00830c87ea02474c5007e1f272"
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
    "BUILD": {
        "symbol": "BUILD",
        "decimals": 18,
        "name": "Build Token",
        "address": "0xe4de4b87345815c71aa843ea4841bcdc682637bb"
    },
    "BUSD": {
        "symbol": "BUSD",
        "decimals": 18,
        "name": "BUSD Token",
        "address": "0x9c9e5fd8bbc25984b178fdce6117defa39d2db39"
    },
    "cbETH": {
        "symbol": "cbETH",
        "decimals": 18,
        "name": "Coinbase Wrapped Staked ETH",
        "address": "0xaddb6a0412de1ba0f936dcaeb8aaa24578dcf3b2"
    },
    "COLLAB": {
        "symbol": "COLLAB",
        "decimals": 18,
        "name": "Collab.Land",
        "address": "0x8b21e9b7daf2c4325bf3d18c1beb79a347fe902a"
    },
    "CTSI": {
        "symbol": "CTSI",
        "decimals": 18,
        "name": "Cartesi Token",
        "address": "0xec6adef5e1006bb305bb1975333e8fc4071295bf"
    },
    "DAI+": {
        "symbol": "DAI+",
        "decimals": 18,
        "name": "DAI+",
        "address": "0x970d50d09f3a656b43e11b0d45241a84e3a6e011"
    },
    "DCN": {
        "symbol": "DCN",
        "decimals": 0,
        "name": "Dentacoin",
        "address": "0x1da650c3b2daa8aa9ff6f661d4156ce24d08a062"
    },
    "DF": {
        "symbol": "DF",
        "decimals": 18,
        "name": "dForce",
        "address": "0x9e5aac1ba1a2e6aed6b32689dfcf62a509ca96f3"
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
    "EQZ": {
        "symbol": "EQZ",
        "decimals": 18,
        "name": "Equalizer",
        "address": "0x81ab7e0d570b01411fcc4afd3d50ec8c241cb74b"
    },
    "ERN": {
        "symbol": "ERN",
        "decimals": 18,
        "name": "Ethos Reserve Note",
        "address": "0xc5b001dc33727f8f26880b184090d3e252470d45"
    },
    "EST": {
        "symbol": "EST",
        "decimals": 18,
        "name": "Erica Social Token",
        "address": "0x7b0bcc23851bbf7601efc9e9fe532bf5284f65d3"
    },
    "fBOMB": {
        "symbol": "fBOMB",
        "decimals": 18,
        "name": "Fantom Bomb",
        "address": "0x74ccbe53f77b08632ce0cb91d3a545bf6b8e0979"
    },
    "FRAX": {
        "symbol": "FRAX",
        "decimals": 18,
        "name": "Frax",
        "address": "0x2e3d870790dc77a83dd1d18184acc7439a53f475"
    },
    "frxETH": {
        "symbol": "frxETH",
        "decimals": 18,
        "name": "Frax Ether",
        "address": "0x6806411765af15bddd26f8f544a34cc40cb9838b"
    },
    "FXS": {
        "symbol": "FXS",
        "decimals": 18,
        "name": "Frax Share",
        "address": "0x67ccea5bb16181e7b4109c9c2143c24a1c2205be"
    },
    "GTC": {
        "symbol": "GTC",
        "decimals": 18,
        "name": "Gitcoin",
        "address": "0x1eba7a6a72c894026cd654ac5cdcf83a46445b08"
    },
    "GYSR": {
        "symbol": "GYSR",
        "decimals": 18,
        "name": "Geyser",
        "address": "0x117cfd9060525452db4a34d51c0b3b7599087f05"
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
    "LIZ": {
        "symbol": "LIZ",
        "decimals": 18,
        "name": "Theranos Coin",
        "address": "0x3bb4445d30ac020a84c1b5a8a2c6248ebc9779d0"
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
    "MTA": {
        "symbol": "MTA",
        "decimals": 18,
        "name": "Meta",
        "address": "0x929b939f8524c3be977af57a4a0ad3fb1e374b50"
    },
    "NFTE": {
        "symbol": "NFTE",
        "decimals": 18,
        "name": "NFTEarth",
        "address": "0xc96f4f893286137ac17e07ae7f217ffca5db3ab6"
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
        "address": "0x39fde572a18448f8139b7788099f0a0740f51205"
    },
    "OK": {
        "symbol": "OK",
        "decimals": 18,
        "name": "Okcash",
        "address": "0xd3ac016b1b8c80eeadde4d186a9138c9324e4189"
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
    "POOL": {
        "symbol": "POOL",
        "decimals": 18,
        "name": "PoolTogether",
        "address": "0x395ae52bb17aef68c2888d941736a71dc6d4e125"
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
    "PSP": {
        "symbol": "PSP",
        "decimals": 18,
        "name": "ParaSwap",
        "address": "0xd3594e879b358f430e20f82bea61e83562d49d48"
    },
    "RADIO": {
        "symbol": "RADIO",
        "decimals": 18,
        "name": "RadioShack Token",
        "address": "0xf899e3909b4492859d44260e1de41a9e663e70f5"
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
    "ROOBEE": {
        "symbol": "ROOBEE",
        "decimals": 18,
        "name": "ROOBEE",
        "address": "0xb12c13e66ade1f72f71834f2fc5082db8c091358"
    },
    "SARCO": {
        "symbol": "SARCO",
        "decimals": 18,
        "name": "Sarcophagus",
        "address": "0x7c6b91d9be155a6db01f749217d76ff02a7227f2"
    },
    "sBTC": {
        "symbol": "sBTC",
        "decimals": 18,
        "name": "Synth sBTC",
        "address": "0x298b9b95708152ff6968aafd889c6586e9169f1d"
    },
    "sETH": {
        "symbol": "sETH",
        "decimals": 18,
        "name": "Synth sETH",
        "address": "0xe405de8f52ba7559f9df3c368500b6e6ae6cee49"
    },
    "sfrxETH": {
        "symbol": "sfrxETH",
        "decimals": 18,
        "name": "Staked Frax Ether",
        "address": "0x484c2d6e3cdd945a8b2df735e079178c1036578c"
    },
    "sLINK": {
        "symbol": "sLINK",
        "decimals": 18,
        "name": "Synth sLINK",
        "address": "0xc5db22719a06418028a40a9b5e9a7c02959d0d08"
    },
    "SLM": {
        "symbol": "SLM",
        "decimals": 18,
        "name": "SoliMax",
        "address": "0xd652776de7ad802be5ec7bebfafda37600222b48"
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
    "SPANK": {
        "symbol": "SPANK",
        "decimals": 18,
        "name": "SPANK",
        "address": "0xcfd1d50ce23c46d3cf6407487b2f8934e96dc8f9"
    },
    "SUKU": {
        "symbol": "SUKU",
        "decimals": 18,
        "name": "SUKU",
        "address": "0xef6301da234fc7b0545c6e877d3359fe0b9e50a4"
    },
    "sUSD": {
        "symbol": "sUSD",
        "decimals": 18,
        "name": "Synth sUSD",
        "address": "0x8c6f28f2f1a3c87f0f938b96d27520d9751ec8d9"
    },
    "SUSHI": {
        "symbol": "SUSHI",
        "decimals": 18,
        "name": "SushiToken",
        "address": "0x3eaeb77b03dbc0f6321ae1b72b2e9adb0f60112b"
    },
    "SYN": {
        "symbol": "SYN",
        "decimals": 18,
        "name": "Synapse",
        "address": "0x5a5fff6f753d7c11a56a52fe47a177a87e431655"
    },
    "TAROT": {
        "symbol": "TAROT",
        "decimals": 18,
        "name": "Tarot",
        "address": "0x375488f097176507e39b9653b88fdc52cde736bf"
    },
    "TheDAO": {
        "symbol": "TheDAO",
        "decimals": 16,
        "name": "TheDAO",
        "address": "0xd8f365c2c85648f9b89d9f1bf72c0ae4b1c36cfd"
    },
    "TRB": {
        "symbol": "TRB",
        "decimals": 18,
        "name": "Tellor",
        "address": "0xaf8ca653fa2772d58f4368b0a71980e9e3ceb888"
    },
    "TUSD": {
        "symbol": "TUSD",
        "decimals": 18,
        "name": "TrueUSD",
        "address": "0xcb59a0a753fdb7491d5f3d794316f1ade197b21e"
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
    "UNIDX": {
        "symbol": "UNIDX",
        "decimals": 18,
        "name": "UniDex",
        "address": "0x5d47baba0d66083c52009271faf3f50dcc01023c"
    },
    "USD+": {
        "symbol": "USD+",
        "decimals": 6,
        "name": "USD+",
        "address": "0x73cb180bf0521828d8849bc8cf2b920918e23032"
    },
    "USDD": {
        "symbol": "USDD",
        "decimals": 18,
        "name": "Decentralized USD",
        "address": "0x7113370218f31764c1b6353bdf6004d86ff6b9cc"
    },
    "UST": {
        "symbol": "UST",
        "decimals": 6,
        "name": "UST (Wormhole)",
        "address": "0xba28feb4b6a6b81e3f26f08b83a19e715c4294fd"
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
    "WAD": {
        "symbol": "WAD",
        "decimals": 18,
        "name": "WardenSwap",
        "address": "0x703d57164ca270b0b330a87fd159cfef1490c0a5"
    },
    "WALBT": {
        "symbol": "WALBT",
        "decimals": 18,
        "name": "Wrapped AllianceBlock Token",
        "address": "0x276cf9e7a43d1b9422decd1f1d2608f3d588caad"
    },
    "wTBT": {
        "symbol": "wTBT",
        "decimals": 18,
        "name": "wTBT(Bridge Token)",
        "address": "0xdb4ea87ff83eb1c80b8976fc47731da6a31d35e5"
    },
    "wUSDR": {
        "symbol": "wUSDR",
        "decimals": 9,
        "name": "Wrapped USDR",
        "address": "0x340fe1d898eccaad394e2ba0fc1f93d27c7b717a"
    },
    "XCHF": {
        "symbol": "XCHF",
        "decimals": 18,
        "name": "CryptoFranc",
        "address": "0xe4f27b04cc7729901876b44f4eaa5102ec150265"
    },
    "ZRX": {
        "symbol": "ZRX",
        "decimals": 18,
        "name": "0x Protocol Token",
        "address": "0xd1917629b3e6a72e6772aab5dbe58eb7fa3c2f33"
    }
}
