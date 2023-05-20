from web3.middleware.geth_poa import geth_poa_middleware


def inject_poa(web3):
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return web3
