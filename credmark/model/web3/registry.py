
import os
import json
from typing import Union
from web3 import HTTPProvider, Web3


class Web3Registry:

    @staticmethod
    def load_providers_from_env():
        providers_json = os.environ.get('CREDMARK_WEB3_PROVIDERS')
        if providers_json:
            try:
                chain_to_provider_url = json.loads(providers_json)
            except Exception as err:
                raise Exception(f'Error parsing JSON in env var CREDMARK_WEB3_PROVIDERS: {err}')
        else:
            chain_to_provider_url = {}

        key_prefix = 'CREDMARK_WEB3_PROVIDER_CHAINID_'
        for key, val in os.environ.items():
            if key.startswith(key_prefix):
                chain_to_provider_url[key.replace(key_prefix, '')] = val

        return chain_to_provider_url

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
