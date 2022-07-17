# System
from enum import IntEnum


class Network(IntEnum):
    #pylint: disable=invalid-name, non-ascii-name
    Mainnet = 1
    Rinkeby = 4
    Görli = 5
    Kovan = 42
    BSC = 56
    BSCTestnet = 97
    xDai = 100
