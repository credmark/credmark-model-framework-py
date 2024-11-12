# pylint: disable=invalid-name, non-ascii-name
from enum import IntEnum
from itertools import chain
from typing import Any, DefaultDict, Generic, Iterable, TypeVar, Union


class Network(IntEnum):
    Mainnet = 1
    Optimism = 10
    BSC = 56
    BSCTestnet = 97
    xDai = 100
    Polygon = 137
    Oasys = 248
    Fantom = 250
    Base = 8453
    ArbitrumOne = 42161
    Avalanche = 43114
    Linea = 59144
    Sepolia = 11155111

    def __str__(self):
        return str(self.value)

    @property
    def chain_id(self):
        return self.value

    @property
    def has_ledger(self):
        return self in [
            Network.Mainnet,
            Network.BSC,
            Network.Polygon,
            Network.ArbitrumOne,
            Network.Optimism,
            Network.Avalanche,
            Network.Base,
            Network.Oasys,
            Network.Linea,
        ]

    @property
    def has_dex_price(self):
        return False

    @property
    def has_node(self):
        return self in [
            Network.Mainnet,
            Network.BSC,
            Network.Polygon,
            Network.ArbitrumOne,
            Network.Optimism,
            Network.Avalanche,
            Network.Fantom,
            Network.Base,
            Network.Oasys,
            Network.Linea,
        ]

    @property
    def is_testnet(self):
        return self in [
            Network.Sepolia,
            Network.BSCTestnet,
        ]

    @property
    def uses_geth_poa(self):
        return self in [
            Network.BSC,
            Network.Polygon,
            Network.Optimism,
            Network.Avalanche,
            Network.Oasys,
            Network.Linea,
        ]

    @classmethod
    def parse_network(cls, n: Any) -> "Network":
        if isinstance(n, str):
            if not n.isdigit():
                raise KeyError(f"Network {n} is not a valid network")
            n = int(n)
        if isinstance(n, int):
            n = Network(n)

        return n


NetworkKey = Union[Network, str, int]
T = TypeVar("T")
_T = TypeVar("_T")


class NetworkDict(DefaultDict[Network, T], Generic[T]):
    """
    A dictionary with network as key. It implements a defaultdict to make it easier
    to provide default values for missing networks. Key can be Network enum, int or int as str.

    ```
    d = NetworkDict(list, {
        Network.Mainnet: [1, 2, 3],
        Network.Sepolia: [4, 5, 6],
    })

    print(d[Network.Mainnet]) # [1, 2, 3]
    print(d[1]) # [1, 2, 3]
    print(d["1"]) # [1, 2, 3]

    print(d[Network.Optimism]) # []
    d[Network.Optimism].append(10)
    print(d[Network.Optimism]) # [10]
    ```
    """

    @staticmethod
    def _process_args(mapping=(), **kwargs):
        if hasattr(mapping, "items"):
            mapping = mapping.items()

        return ((Network.parse_network(k), v) for k, v in chain(mapping, kwargs.items()))

    def __setitem__(self, k: NetworkKey, v: T):
        super().__setitem__(Network.parse_network(k), v)

    def __getitem__(self, k: NetworkKey):
        return super().__getitem__(Network.parse_network(k))

    def __delitem__(self, k: NetworkKey):
        super().__delitem__(Network.parse_network(k))

    def __contains__(self, k: NetworkKey):
        return super().__contains__(Network.parse_network(k))

    def __missing__(self, k: NetworkKey):
        return super().__missing__(Network.parse_network(k))

    def get(self, k: NetworkKey, default: Union[T, _T] = None) -> Union[T, _T]:
        return super().get(Network.parse_network(k), default)

    def pop(self, k: NetworkKey, default: Union[T, _T] = None) -> Union[T, _T]:
        return super().pop(Network.parse_network(k), default)

    def setdefault(self, k: NetworkKey, v: T):
        super().setdefault(Network.parse_network(k), v)

    def update(self, mapping: Iterable[tuple[NetworkKey, T]] = (), **kwargs):
        print("update")
        super().update(self._process_args(mapping, **kwargs))

    @classmethod
    def fromkeys(cls, keys: Iterable[NetworkKey], v: _T = None) -> "NetworkDict[_T]":
        raise Exception("fromkeys is incompatible with defaultdict")


CREDMARK_PUBLIC_PROVIDERS = {
    str(Network.Mainnet): "https://nodes.credmark.com/1",
    str(Network.Optimism): "https://nodes.credmark.com/10",
    str(Network.BSC): "https://nodes.credmark.com/56",
    str(Network.Polygon): "https://nodes.credmark.com/137",
    str(Network.Fantom): "https://nodes.credmark.com/250",
    str(Network.ArbitrumOne): "https://nodes.credmark.com/42161",
    str(Network.Avalanche): "https://nodes.credmark.com/43114",
    str(Network.Base): "https://base.llamarpc.com",
    str(Network.Linea): "https://1rpc.io/linea",
    str(Network.Oasys): "https://rpc.mainnet.oasys.games",
    str(Network.Sepolia): "https://1rpc.io/sepolia",
}
