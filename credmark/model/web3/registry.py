
from typing import Union
from web3 import HTTPProvider, Web3


class Web3Registry:

    def __init__(self, chain_to_provider_url: Union[dict[str, str], None]):
        super().__init__()
        self.__chain_to_web3_provider: dict[int, HTTPProvider] = dict()
        self.__chain_to_provider_url = chain_to_provider_url if \
            chain_to_provider_url is not None else {}

    def web3_for_chain_id(self, chain_id: int):
        provider = self.__chain_to_web3_provider.get(chain_id)
        if provider is None:
            url = self.__chain_to_provider_url.get(str(chain_id))
            if url is None:
                raise Exception(f'No web3 provider url for chain id {chain_id}')
            provider = Web3.HTTPProvider(url)
            self.__chain_to_web3_provider[chain_id] = provider
        return Web3(provider)
