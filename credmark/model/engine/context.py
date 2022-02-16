import logging
import os
from typing import Union
from credmark.model import ModelContext
from credmark.model.errors import MaxModelRunDepthError
from credmark.model.engine.model_api import ModelApi
from credmark.model.engine.model_loader import ModelLoader
from credmark.model.web3 import Web3Registry


class EngineModelContext(ModelContext):
    logger = logging.getLogger(__name__)

    dev_mode = False
    max_run_depth = 20

    @classmethod
    def create_context_and_run_model(cls,
                                     chain_id: int,
                                     block_number: int,
                                     model_slug: str,
                                     model_version: Union[str, None] = None,
                                     input: Union[dict, None] = None,
                                     model_loader: Union[ModelLoader,
                                                         None] = None,
                                     chain_to_provider_url: Union[dict[str, str], None] = None,
                                     api_url: Union[str, None] = None,
                                     run_id: Union[str, None] = None,
                                     depth: int = 0):
        """
        Parameters:
            run_id (str | None): a string to identify a particular model run. It is
                same for any other models run from within a model.

        """
        if model_loader is None:
            model_loader = ModelLoader(['.'])

        api_key = os.environ.get('CREDMARK_API_KEY')
        # If we have an api url or a key, we create the api
        # TODO: When public api is available, we will always create the api
        api = ModelApi(api_url, api_key) if api_url or api_key else None

        web3_registry = Web3Registry(chain_to_provider_url)

        context = EngineModelContext(
            chain_id, block_number, web3_registry, run_id, depth, model_loader, api)

        # We set the block_number in the context so we pass in
        # None for block_number to the run_model method.
        result_tuple = context._run_model(
            model_slug, input, None, model_version)
        response = {
            'slug': result_tuple[0],
            'version': result_tuple[1],
            'output': result_tuple[2],
            'dependencies': context.__dependencies}
        return response

    def __init__(self,
                 chain_id: int,
                 block_number: int,
                 web3_registry: Web3Registry,
                 run_id: Union[str, None],
                 depth: int,
                 model_loader: ModelLoader,
                 api: Union[ModelApi, None]):
        super().__init__(chain_id, block_number, web3_registry)
        self.run_id = run_id
        self.__depth = depth
        self.__dependencies = {}
        self.__model_loader = model_loader
        self.__api = api

    def _add_dependency(self, slug: str, version: str, count: int):
        versions = self.__dependencies.get(slug)
        if versions is None:
            self.__dependencies[slug] = {version: count}
        else:
            if version in versions:
                versions[version] += count
            else:
                versions[version] = count

    def _add_dependencies(self, dep_dict: dict):
        for slug, versions in dep_dict.items():
            if slug not in self.__dependencies:
                self.__dependencies[slug] = versions
            else:
                for version, count in versions.items():
                    self._add_dependency(slug, version, count)

    def run_model(self,
                  slug: str,
                  input: Union[dict, None] = None,
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None
                  ):
        res_tuple = self._run_model(slug, input, block_number, version)
        return res_tuple[2]

    def _run_model(self,
                   slug: str,
                   input: Union[dict, None],
                   block_number: Union[int, None],
                   version: Union[str, None]
                   ):
        api = self.__api

        # We raise an exception for missing class
        # if we have no api or this is a top-level run.
        model_class = self.__model_loader.get_model_class(
            slug, version, self.__api is None or
            (self.__depth == 0 and not self.dev_mode))

        self.__depth += 1
        if self.__depth >= self.max_run_depth:
            raise MaxModelRunDepthError('Max model run depth')

        if model_class is not None:
            saved_block_number = self.block_number
            saved_web3 = self._web3

            if block_number is not None:
                self.block_number = block_number
            self._web3 = None

            model = model_class(self)
            output = model.run(input)

            version = model_class.version
            self._add_dependency(slug, version, 1)

            if block_number is not None:
                self.block_number = saved_block_number
            self._web3 = saved_web3

        else:
            # api is not None here or get_model_class() would have
            # raised an error
            assert api is not None
            slug, version, output, dependencies = api.run_model(
                slug, version, self.chain_id,
                block_number if block_number is not None else self.block_number,
                input, self.run_id, self.__depth)
            if dependencies:
                self._add_dependencies(dependencies)

        self.__depth -= 1

        return slug, version, output