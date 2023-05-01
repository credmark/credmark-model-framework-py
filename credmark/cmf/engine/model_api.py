# pylint: disable=line-too-long

import logging
import os
from typing import Any, ClassVar, Union
from urllib.parse import quote, urljoin

import requests
from requests.adapters import HTTPAdapter, Retry

from credmark.cmf.engine.errors import ModelRunRequestError
from credmark.cmf.model.errors import ModelBaseError, create_instance_from_error_dict
from credmark.cmf.types import BlockNumber
from credmark.dto.encoder import json_dumps

GATEWAY_API_URL = 'https://gateway.credmark.com'
STAGING_GATEWAY_API_URL = 'https://gateway.staging.credmark.com'
CREDMARK_API_KEY = 'caprod_oOYBsqWiapsxNdScXRtt0VMHteLxRqC6jfB-FZ5AXMoLQtz0zjGrrsjf8xbDNNlc'

RUN_MODEL_PATH = '/v1/model/run'
GET_MODELS_PATH = '/v1/models'
GET_MODEL_PATH_FORMAT = '/v1/models/{}'
GET_MODEL_DEPLOYMENTS_PATH_FORMAT = '/v1/models/{}/deployments'

RUN_REQUEST_TIMEOUT = 1800

logger = logging.getLogger(__name__)


class ModelApi:

    _url_to_api: ClassVar = {}

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
            if not api_key and url == GATEWAY_API_URL:
                api_key = CREDMARK_API_KEY
            internal_api = url not in [
                GATEWAY_API_URL, STAGING_GATEWAY_API_URL]
            api = ModelApi(url, api_key, internal_api)
            cls._url_to_api[url] = api
        return api

    def __init__(self, url: str, api_key=None, internal_api=False):
        self.__url = url
        self.__internal_api = internal_api
        self.__session = requests.Session()
        self.__session.headers.update(
            {'User-Agent': 'credmark-model-framework'})
        if api_key is not None:
            self.__session.headers.update(
                {'Authorization': 'Bearer ' + api_key})

        retries = Retry(total=5, backoff_factor=1, allowed_methods=False,
                        status_forcelist=[429, 502], respect_retry_after_header=True)
        self.__session.mount('http://', HTTPAdapter(max_retries=retries))
        self.__session.mount('https://', HTTPAdapter(max_retries=retries))

    def _get(self, url):
        """
        Return JSON object or None if not found.
        Other errors raise
        """
        resp = None

        try:
            resp = self.__session.get(url)
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

    def run_model(self,  # pylint: disable=too-many-arguments,too-many-locals,too-many-branches
                  slug: str,
                  version: Union[str, None],
                  chain_id: int,
                  block_number: int,
                  input_jsonify: dict,
                  run_id: Union[str, None] = None,
                  depth: Union[int, None] = None,
                  client: Union[str, None] = None,
                  raise_error_results=False) -> tuple[
            str, str,
            Union[dict[str, Any], None],
            Union[dict[str, Any], None],
            dict[str, Any]
    ]:

        req = {
            'slug': slug,
            'chainId': chain_id,
            'blockNumber': int(block_number),
            'input': input_jsonify,
        }
        if version is not None:
            req['version'] = version
        if self.__internal_api:
            if isinstance(block_number, BlockNumber) and block_number.is_timestamp_loaded:
                req['blockNumber'] = block_number.dict()
            if run_id is not None:
                req['runId'] = run_id
            if depth is not None:
                req['depth'] = depth
            if client is not None:
                req['client'] = client

        resp = None
        resp_obj = None
        url = urljoin(self.__url, RUN_MODEL_PATH)

        try:
            resp = self.__session.post(
                url,
                data=json_dumps(req),
                headers={'Content-Type': 'application/json'},
                timeout=RUN_REQUEST_TIMEOUT)
            resp.raise_for_status()
            resp_obj = resp.json()

            if raise_error_results:
                err_obj = resp_obj.get('error')
                if err_obj is not None:
                    raise create_instance_from_error_dict(err_obj)

            if 'output' not in resp_obj and 'error' not in resp_obj:
                raise ModelRunRequestError(
                    f'Model {slug} run request response missing both output and error', str(201))

            return resp_obj['slug'], resp_obj['version'], resp_obj.get('output'), resp_obj.get('error'), resp_obj['dependencies']

        except requests.exceptions.ConnectionError as err:
            logger.error(
                f'Error running api request for {slug} {self.__url}: {err}')
            raise ModelRunRequestError(
                f'Unable to reach model runner for model {slug}', '503')
        except ModelBaseError:
            raise
        except Exception as err:
            logger.error(
                f'Error running api request for {slug} {self.__url}: {err}')
            if resp is not None:
                logger.error(f'Error api response {resp.text}')

                try:
                    error_result = resp.json()
                except Exception:
                    raise ModelRunRequestError(
                        f'Model run error response: {resp.text}', str(resp.status_code))

                raise ModelRunRequestError(
                    str(error_result.get('message', 'Error response from runner api')),
                    str(error_result.get('statusCode', 500)),
                )

            raise ModelRunRequestError(
                f'Model run request error: {str(err)}', str(503))
        finally:
            # Ensure the response is closed in case we ever don't
            # read the content.
            if resp is not None:
                resp.close()
