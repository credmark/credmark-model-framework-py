
import os
import json
from typing import Union
from web3 import HTTPProvider, WebsocketProvider, Web3


class Web3Registry:

    # Cache of urls to providers that are reused
    # We don't cache chainId to providers because that
    # can change from request to request when running in a lambda
    _url_to_web3_provider: dict[str, Union[HTTPProvider, WebsocketProvider]] = {}

    @classmethod
    def web3_for_provider_url(cls, provider_url: str):
        provider = cls._url_to_web3_provider.get(provider_url)
        if provider is None:
            if provider_url.startswith('http'):
                provider = Web3.HTTPProvider(provider_url)
            elif provider_url.startswith('ws'):
                provider = Web3.WebsocketProvider(provider_url)
            else:
                raise Exception(f'Unknown prefix for Web3 provider {provider_url}')
            cls._url_to_web3_provider[provider_url] = provider
        # create a new web3 instance with cached provider
        return Web3(provider)

    @staticmethod
    def load_providers_from_env():
        providers_json = os.environ.get('CREDMARK_WEB3_PROVIDERS')
        if providers_json:
            try:
                chain_to_provider_url: dict = json.loads(providers_json)
            except Exception as err:
                raise Exception(f'Error parsing JSON in env var CREDMARK_WEB3_PROVIDERS: {err}')
        else:
            chain_to_provider_url = {}

        key_prefix = 'CREDMARK_WEB3_PROVIDER_CHAIN_ID_'
        for key, val in os.environ.items():
            if key.startswith(key_prefix):
                chain_to_provider_url[key.replace(key_prefix, '')] = val

        return chain_to_provider_url

    def __init__(self, chain_to_provider_url: Union[dict[str, str], None]):
        super().__init__()
        self.__chain_to_provider_url = chain_to_provider_url if \
            chain_to_provider_url is not None else {}

    def web3_for_chain_id(self, chain_id: int):
        url = self.__chain_to_provider_url.get(str(chain_id))
        if url is None:
            raise Exception(f'No web3 provider url for chain id {chain_id}')
        return self.web3_for_provider_url(url)
