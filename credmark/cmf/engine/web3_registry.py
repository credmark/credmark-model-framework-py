
import json
import os
from typing import Optional, Union

from web3 import AsyncHTTPProvider, HTTPProvider, Web3, WebsocketProvider

from credmark.cmf.engine.web3 import inject_poa
from credmark.cmf.types.network import CREDMARK_PUBLIC_PROVIDERS, Network


class Web3Registry:

    # Cache of urls to providers that are reused
    # We don't cache chainId to providers because that
    # can change from request to request when running in a lambda
    _url_to_web3_provider: dict[tuple[str, bool],
                                Union[HTTPProvider, WebsocketProvider, AsyncHTTPProvider]] = {}

    @classmethod
    def web3_for_provider_url(cls, provider_url: str, chain_id: int, use_async: bool,
                              request_kwargs: Optional[dict] = None):
        if request_kwargs is None:
            request_kwargs = {}
        provider = cls._url_to_web3_provider.get((provider_url, use_async))
        if provider is None:
            if provider_url.startswith('http'):
                if use_async:
                    provider = Web3.AsyncHTTPProvider(provider_url, **request_kwargs)
                else:
                    provider = Web3.HTTPProvider(provider_url, **request_kwargs)
            elif provider_url.startswith('ws'):
                if use_async:
                    raise Exception('Async WebsocketProvider not supported')

                provider = Web3.WebsocketProvider(provider_url, **request_kwargs)
            else:
                raise Exception(
                    f'Unknown prefix for Web3 provider {provider_url}')
            cls._url_to_web3_provider[(provider_url, use_async)] = provider

        w3 = Web3(provider)  # type: ignore

        if chain_id in [Network.Rinkeby,
                        Network.BSC,
                        Network.Polygon,
                        Network.Optimism,
                        Network.Avalanche]:
            return inject_poa(w3)
        else:
            return w3

    @staticmethod
    def load_providers_from_env():
        providers_json = os.environ.get('CREDMARK_WEB3_PROVIDERS')
        if providers_json:
            try:
                chain_to_provider_url: dict = json.loads(providers_json)
            except Exception as err:
                raise Exception(
                    f'Error parsing JSON in env var CREDMARK_WEB3_PROVIDERS: {err}') from None
        else:
            chain_to_provider_url = {}

        key_prefix = 'CREDMARK_WEB3_PROVIDER_CHAIN_ID_'
        for key, val in os.environ.items():
            if key.startswith(key_prefix):
                chain_to_provider_url[key.replace(key_prefix, '')] = val

        return chain_to_provider_url

    def __init__(self, chain_to_provider_url: Optional[dict[str, str]]):
        super().__init__()
        self.__chain_to_provider_url = CREDMARK_PUBLIC_PROVIDERS
        if chain_to_provider_url:
            self.__chain_to_provider_url.update(chain_to_provider_url)

    # pylint:disable=line-too-long
    def web3_for_chain_id(self, chain_id: int):
        url = self.__chain_to_provider_url.get(str(chain_id))
        if url is None:
            raise Exception(
                f'No web3 provider url for chain id {chain_id}. '
                "In .env file or environment, set CREDMARK_WEB3_PROVIDERS as {'1':'https://web3-node-provider-url'}.")
        return self.web3_for_provider_url(url, chain_id, False)

    def web3_async_for_chain_id(self, chain_id: int):
        url = self.__chain_to_provider_url.get(str(chain_id))
        if url is None:
            raise Exception(
                f'No web3 provider url for chain id {chain_id}. '
                "In .env file or environment, set CREDMARK_WEB3_PROVIDERS as {'1':'https://web3-node-provider-url'}.")
        return self.web3_for_provider_url(url, chain_id, True)
