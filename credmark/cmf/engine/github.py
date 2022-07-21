import logging

import requests

logger = logging.getLogger(__name__)

GITHUB_API_TAGS_URL = 'https://api.github.com/repos/credmark/credmark-model-framework-py/tags'


def get_latest_cmf_version_tag():
    tag = None

    try:
        response = requests.get(GITHUB_API_TAGS_URL)
        response.raise_for_status()
        tag_list = response.json()
        if len(tag_list):
            tag = tag_list[0]['name']
    except Exception as err:
        logger.error(
            f'Error getting latest cmf version from {GITHUB_API_TAGS_URL}: {err}')

    return tag
