import logging
import os
from typing import Union
from credmark.model import ModelContext
from credmark.model.errors import MaxModelRunDepthError
from credmark.model.engine.model_api import ModelApi
from credmark.model.engine.model_loader import ModelLoader


class EngineModelContext(ModelContext):
    logger = logging.getLogger(__name__)

    max_run_depth = 20

    @classmethod
    def create_context_and_run_model(cls,
                                     chain_id: int,
                                     block_number: int,
                                     model_name: str,
                                     model_version: Union[str, None] = None,
                                     input: Union[dict, None] = None,
                                     model_loader: Union[ModelLoader,
                                                         None] = None,
                                     provider_url: Union[str, None] = None,
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

        # If we have an api url or a key, we use the api
        api_key = os.environ.get('CREDMARK_API_KEY')
        api = ModelApi(api_url, api_key) if api_url or api_key else None

        context = EngineModelContext(
            chain_id, block_number, provider_url, run_id, depth, model_loader, api)

        # We set the block_number in the context so we pass in
        # None for block_number to the run_model method.
        result_tuple = context._run_model(
            model_name, input, None, model_version)
        response = {
            'name': result_tuple[0],
            'version': result_tuple[1],
            'result': result_tuple[2],
            'dependencies': context.__dependencies}
        return response

    def __init__(self,
                 chain_id: int,
                 block_number: int,
                 provider_url: Union[str, None],
                 run_id: Union[str, None],
                 depth: int,
                 model_loader: ModelLoader,
                 api: Union[ModelApi, None]):
        super().__init__(chain_id, block_number, provider_url)
        self.run_id = run_id
        self.__depth = depth
        self.__dependencies = {}
        self.__model_loader = model_loader
        self.__api = api

    def _add_dependency(self, name: str, version: str):
        ver = self.__dependencies.get(name)
        if ver is None:
            self.__dependencies[name] = version
        elif isinstance(ver, list):
            # list will be very short so not worth using a set
            if version not in ver:
                ver.append(version)
        else:
            self.__dependencies[name] = [ver, version]

    def _add_dependencies(self, dep_dict: dict):
        for name, version in dep_dict.items():
            if name not in self.__dependencies:
                self.__dependencies[name] = version
            elif isinstance(version, list):
                for ver in version:
                    self._add_dependency(name, ver)
            else:
                self._add_dependency(name, version)

    def run_model(self,
                  name: str,
                  input: Union[dict, None] = None,
                  block_number: Union[int, None] = None,
                  version: Union[str, None] = None
                  ):
        res_tuple = self._run_model(name, input, block_number, version)
        return res_tuple[2]

    def _run_model(self,
                   name: str,
                   input: Union[dict, None],
                   block_number: Union[int, None],
                   version: Union[str, None]
                   ):
        api = self.__api

        # We raise an exception for missing class
        # if we have no api or this is a top-level run.
        model_class = self.__model_loader.get_model_class(
            name, version, self.__api is None or self.__depth == 0)

        self.__depth += 1
        if self.__depth >= self.max_run_depth:
            raise MaxModelRunDepthError('Max model run depth')

        if model_class is not None:
            current_block_number = self.block_number

            if block_number is not None:
                self.block_number = self.web3.eth.default_block = block_number

            model = model_class(self)
            result = model.run(input)

            version = model_class.version
            self._add_dependency(name, version)

            if block_number is not None:
                self.block_number = self.web3.eth.default_block = current_block_number
        else:
            # api is not None here or get_model_class() would have
            # raised an error
            assert api is not None
            name, version, result, dependencies = api.run_model(
                name, version, self.chain_id,
                block_number if block_number is not None else self.block_number,
                input, self.run_id, self.__depth)
            if dependencies:
                self._add_dependencies(dependencies)

        self.__depth -= 1

        return name, version, result
