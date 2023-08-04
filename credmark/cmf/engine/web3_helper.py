import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Union

from web3 import AsyncWeb3, Web3
from web3._utils.rpc_abi import RPC
from web3.middleware.async_cache import async_construct_simple_cache_middleware
from web3.middleware.cache import construct_simple_cache_middleware
from web3.middleware.geth_poa import async_geth_poa_middleware, geth_poa_middleware


def inject_poa(web3: Union[AsyncWeb3, Web3]):
    if isinstance(web3, Web3):
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    else:
        web3.middleware_onion.inject(async_geth_poa_middleware, layer=0)
    return web3


SIMPLE_CACHE_RPC_CHAIN_ID = {
    RPC.web3_clientVersion,
    RPC.net_version,
    RPC.eth_chainId
}


def add_chain_id_cache(web3: Web3):
    cache_chain_id_middleware = construct_simple_cache_middleware(
        rpc_whitelist=SIMPLE_CACHE_RPC_CHAIN_ID
    )
    web3.middleware_onion.add(
        cache_chain_id_middleware,
        name="chain_id_cache"
    )


def add_chain_id_cache_async(web3: AsyncWeb3):
    try:
        asyncio.get_running_loop()
        # we need to create a separate thread so we can block before returning
        with ThreadPoolExecutor(1) as pool:
            cache_chain_id_middleware = pool.submit(
                lambda: asyncio.run(async_construct_simple_cache_middleware(
                    rpc_whitelist=SIMPLE_CACHE_RPC_CHAIN_ID
                ))
            ).result()
    except RuntimeError:
        # no event loop running
        cache_chain_id_middleware = asyncio.run(async_construct_simple_cache_middleware(
            rpc_whitelist=SIMPLE_CACHE_RPC_CHAIN_ID
        ))

    web3.middleware_onion.add(
        cache_chain_id_middleware,
        name="async_chain_id_cache"
    )
