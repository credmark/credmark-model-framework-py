from typing import Any, ClassVar, Union
import os
import logging
import requests
import json
from urllib.parse import urljoin, quote
from credmark.dto.encoder import json_dumps
from credmark.cmf.engine.errors import ModelRunRequestError
from credmark.cmf.model.errors import ModelBaseError, ModelNotFoundError, \
    create_instance_from_error_dict

GATEWAY_API_URL = 'https://gateway.credmark.com'

RUN_MODEL_PATH = '/v1/model/run'
GET_MODELS_PATH = '/v1/models'
GET_MODEL_PATH_FORMAT = '/v1/models/{}'
GET_MODEL_DEPLOYMENTS_PATH_FORMAT = '/v1/models/{}/deployments'

RUN_REQUEST_TIMEOUT = 600

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
            internal_api = url != GATEWAY_API_URL
            api = ModelApi(url, api_key, internal_api)
            cls._url_to_api[url] = api
        return api

    def __init__(self, url: str, api_key=None, internal_api=False):
        self.__url = url
        self.__internal_api = internal_api
        self.__api_key = api_key
        self.__session = requests.Session()

    def _get(self, url):
        """
        Return JSON object or None if not found.
        Other errors raise
        """
        headers = {'Authorization': 'Bearer ' +
                   self.__api_key} if self.__api_key is not None else None
        resp = None

        try:
            resp = self.__session.get(url, headers=headers)
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
                  input: Union[dict, None],
                  run_id: Union[str, None] = None,
                  depth: Union[int, None] = None) -> \
            tuple[str, str, dict[str, Any], dict[str, Any]]:

        # We use json_dumps to ensure any DTOs embedded in a dict
        # are serialized properly. If we just set the input in the
        # req object and let requests serializes, any embedded DTOs
        # would fail.
        input_json = json_dumps(input) if input is not None else '{}'

        req = {
            'slug': slug,
            'chainId': chain_id,
            'blockNumber': block_number,
            'input': json.loads(input_json),
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
            resp = self.__session.post(url, json=req, headers=headers, timeout=RUN_REQUEST_TIMEOUT)
            resp.raise_for_status()
            resp_obj = resp.json()

            err_obj = resp_obj.get('error')
            if err_obj is not None:
                raise create_instance_from_error_dict(err_obj)

            return resp_obj['slug'], resp_obj['version'], \
                resp_obj['output'], resp_obj['dependencies']
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
