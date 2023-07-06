from typing import Union
from web3.middleware.geth_poa import geth_poa_middleware, async_geth_poa_middleware
from web3 import AsyncWeb3, Web3

def inject_poa(web3: Union[AsyncWeb3, Web3]):
    if isinstance(web3, Web3):
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    else:
        web3.middleware_onion.inject(async_geth_poa_middleware, layer=0)
    return web3
