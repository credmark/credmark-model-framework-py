from typing import Any, ClassVar, Union
import os
import logging
import requests
from urllib.parse import urljoin, quote
from credmark.model.engine.errors import MissingModelError, ModelRunRequestError

GATEWAY_API_URL = 'https://gateway.credmark.com'

RUN_MODEL_PATH = '/v1/model/run'
GET_MODELS_PATH = '/v1/models'
GET_MODEL_PATH_FORMAT = '/v1/models/{}'
GET_MODEL_DEPLOYMENTS_PATH_FORMAT = '/v1/models/{}/deployments'

RUN_REQUEST_TIMEOUT = 600

logger = logging.getLogger(__name__)


class ModelApi:

    _url_to_api: ClassVar = dict()

    @classmethod
    def api_for_url(cls, url: Union[str, None] = None):
        if url:
            if url.endswith(RUN_MODEL_PATH):
                url = url[:-(len(RUN_MODEL_PATH))]
        else:
            url = GATEWAY_API_URL

        api: ModelApi = cls._url_to_api.get(url)  # type: ignore
        if api is None:
            api_key = os.environ.get('CREDMARK_API_KEY')
            internal_api = url != GATEWAY_API_URL
            api = ModelApi(url, api_key, internal_api)
            cls._url_to_api[url] = api
        return api

    def __init__(self, url: str, api_key=None, internal_api=False):
        self.__url = url
        self.__internal_api = internal_api
        self.__api_key = api_key

    def _get(self, url):
        """
        Return JSON object or None if not found.
        Other errors raise
        """
        headers = {'Authorization': 'Bearer ' +
                   self.__api_key} if self.__api_key is not None else None
        resp = None

        try:
            resp = requests.get(url, headers=headers)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.ConnectionError as err:
            logger.error(
                f'Error running api request for {url}: {err}')
            raise
        except Exception as err:
            if resp is not None:
                if resp.status_code == 404:
                    return None
                else:
                    logger.error(f'Error api response {resp.text}')
            logger.error(
                f'Error running api request for {url}: {err}')
            raise
        finally:
            # Ensure the response is closed in case we ever don't
            # read the content.
            if resp is not None:
                resp.close()

    def get_models(self):
        url = urljoin(self.__url, GET_MODELS_PATH)
        models = self._get(url)
        return models if models is not None else []

    def get_model(self, slug: str):
        path = GET_MODEL_PATH_FORMAT.format(quote(slug))
        url = urljoin(self.__url, path)
        return self._get(url)

    def get_model_deployments(self, slug: str):
        path = GET_MODEL_DEPLOYMENTS_PATH_FORMAT.format(quote(slug))
        url = urljoin(self.__url, path)
        return self._get(url)

    def run_model(self,
                  slug: str,
                  version: Union[str, None],
                  chain_id: int,
                  block_number: int,
                  input: Union[dict, None],
                  run_id: Union[str, None] = None,
                  depth: Union[int, None] = None) -> \
            tuple[str, str, dict[str, Any], dict[str, Any]]:
        req = {
            'slug': slug,
            'chainId': chain_id,
            'blockNumber': block_number,
            'input': input if input is not None else {},
        }
        if version is not None:
            req['version'] = version
        if self.__internal_api:
            if run_id is not None:
                req['runId'] = run_id
            if depth is not None:
                req['depth'] = depth

        headers = {'Authorization': 'Bearer ' +
                   self.__api_key} if self.__api_key is not None else None
        resp = None
        resp_obj = None
        url = urljoin(self.__url, RUN_MODEL_PATH)
        try:
            resp = requests.post(url, json=req, headers=headers, timeout=RUN_REQUEST_TIMEOUT)
            resp.raise_for_status()
            resp_obj = resp.json()
            return resp_obj['slug'], resp_obj['version'], \
                resp_obj['output'], resp_obj['dependencies']
        except requests.exceptions.ConnectionError as err:
            logger.error(
                f'Error running api request for {slug} {self.__url}: {err}')
            error_result = {
                "statusCode": 503,
                "error": "Model runner unavailable",
                "message": f'Unable to reach model runner for model {slug}'
            }
            raise ModelRunRequestError(
                'Model run request error', error_result)
        except Exception as err:
            logger.error(
                f'Error running api request for {slug} {self.__url}: {err}')
            if resp is not None:
                logger.error(f'Error api response {resp.text}')
                if resp.status_code == 404:
                    raise MissingModelError(
                        slug, version, 'Model not found from api')
                else:
                    try:
                        error_result = resp.json()
                    except Exception:
                        error_result = {
                            "statusCode": resp.status_code,
                            "error": "Model run error",
                            "message": resp.text
                        }
                    raise ModelRunRequestError(
                        'Model run request error', error_result)
            raise err
        finally:
            # Ensure the response is closed in case we ever don't
            # read the content.
            if resp is not None:
                resp.close()
