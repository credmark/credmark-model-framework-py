from typing import Union
import logging
import requests
from credmark.model.errors import MissingModelError, ModelRunRequestError

RUN_MODEL_API_URL = 'https://gateway.credmark.com/v0/models/run'

logger = logging.getLogger(__name__)


class ModelApi:

    def __init__(self, url=None, api_key=None):
        if url:
            self.__url = url
            self.__internal_api = True
        else:
            self.__url = RUN_MODEL_API_URL
            self.__internal_api = False

        self.__api_key = api_key

    def run_model(self,
                  slug: str,
                  version: Union[str, None],
                  chain_id: int,
                  block_number: int,
                  input=Union[dict, None],
                  run_id: Union[str, None] = None,
                  depth: Union[int, None] = None):
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

        try:
            resp = requests.post(self.__url, json=req, headers=headers)
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
