#pylint: disable=invalid-name, non-ascii-name
from enum import IntEnum


class Network(IntEnum):
    Mainnet = 1
    Ropsten = 3
    Rinkeby = 4
    Görli = 5
    Optimism = 10
    Kovan = 42
    BSC = 56
    BSCTestnet = 97
    xDai = 100
    Polygon = 137
    Fantom = 250
    ArbitrumOne = 42161
    Avalanche = 43114
