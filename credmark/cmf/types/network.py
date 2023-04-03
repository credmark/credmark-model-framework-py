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

    def __str__(self):
        return str(self.value)


CREDMARK_PUBLIC_PROVIDERS = {
    str(Network.Mainnet): "https://nodes.credmark.com/1",
    str(Network.Optimism): "https://nodes.credmark.com/10",
    str(Network.BSC): "https://nodes.credmark.com/56",
    str(Network.Polygon): "https://nodes.credmark.com/137",
    str(Network.Fantom): "https://nodes.credmark.com/250",
    str(Network.ArbitrumOne): "https://nodes.credmark.com/42161",
    str(Network.Avalanche): "https://nodes.credmark.com/43114",
}
