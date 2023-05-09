# pylint: disable=line-too-long

import json
import logging
import sys
import traceback
from typing import Callable, List, Optional, Set, Type, Union

from credmark.cmf.engine.cache import ModelRunCache
from credmark.cmf.engine.errors import ModelRunRequestError
from credmark.cmf.engine.mocks import ModelMockException, ModelMockRunner
from credmark.cmf.engine.model_api import ModelApi
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.cmf.engine.web3_registry import Web3Registry
from credmark.cmf.model import Model
from credmark.cmf.model.context import ModelContext
from credmark.cmf.model.errors import (
    MaxModelRunDepthError,
    ModelBaseError,
    ModelCallStackEntry,
    ModelEngineError,
    ModelInputError,
    ModelInvalidStateError,
    ModelNotFoundError,
    ModelOutputError,
    ModelRunError,
    ModelTypeError,
    create_instance_from_error_dict,
)
from credmark.cmf.model.models import RunModelMethod
from credmark.cmf.types import (
    BlockNumber,
    BlockNumberOutOfRangeDetailDTO,
    BlockNumberOutOfRangeError,
)
from credmark.dto import DTOType, DTOValidationError, EmptyInput
from credmark.dto.encoder import json_dumps
from credmark.dto.transform import (
    DataTransformError,
    transform_data_for_dto,
    transform_dto_to_dict,
)

LEDGER_GET_LATEST_BLOCK_NUMBER_SLUG = 'ledger.block-number'
CHAIN_GET_LATEST_BLOCK_NUMBER_SLUG = 'chain.get-latest-block'


def extract_most_recent_run_model_traceback(exc_traceback, skip=1):
    # Extract "skip" most-recent group of frames before frames
    # in this file (or superclass context) until it comes back to
    # the context.
    context_files = set([__file__,
                         __file__.replace('credmark/cmf/engine/context',
                                          'credmark/cmf/model/context'),
                         __file__.replace('credmark/cmf/engine/context',
                                          'credmark/cmf/engine/model_api')])
    ptb = []
    in_other_file = False
    tb = traceback.extract_tb(exc_traceback)
    for frame in tb[::-1][:30]:  # reversed
        if frame.filename in context_files:
            if in_other_file and skip == 0:
                break
            in_other_file = False
        else:
            if not in_other_file:
                skip -= 1
            in_other_file = True
            if skip == 0:
                ptb.append(frame)
    return ''.join(traceback.format_list(ptb))


class EngineModelContext(ModelContext):
    # No doc string so it uses parent's

    # general logger:
    logger = logging.getLogger(__name__)
    # logger used for debugging models:
    debug_logger = logging.getLogger(f'{__name__}.debug')

    dev_mode = False
    test_mode = False
    max_run_depth = 25

    # map of slug to manifest, filled in lazily
    _model_manifest_map: dict[str, dict] = {}
    _model_underscore_manifest_map: dict[str, dict] = {}

    def reset_cache(self):
        self.__model_cache = ModelRunCache()

    @property
    def model_cache(self):
        return self.__model_cache

    @property
    def model_loader(self):
        return self.__model_loader

    @classmethod
    def _clear_model_manifest_maps(cls):
        cls._model_manifest_map.clear()
        cls._model_underscore_manifest_map.clear()

    # Set of model slugs to use the local version.
    # If set contains "-", no local models will be used.
    # If set contains "*", we favor using local version of all models.
    use_local_models_slugs: Set[str] = set()

    _model_run_listeners: List[Callable] = []

    _model_mock_runner: Union[ModelMockRunner, None] = None

    @classmethod
    def add_model_run_listener(cls, run_listener):
        cls._model_run_listeners.append(run_listener)

    @classmethod
    def notify_model_run(cls,
                         slug: str, version: Union[str, None],
                         chain_id: int, block_number: int,
                         input: Union[dict, DTOType],
                         output: Union[dict, DTOType, None],
                         error: Union[ModelBaseError, None]):
        for listener in cls._model_run_listeners:
            listener(slug, version, chain_id, block_number,
                     input, output, error)

    @classmethod
    def use_model_mock_runner(cls, model_mock_runner: Union[ModelMockRunner, None]):
        cls._model_mock_runner = model_mock_runner

    @classmethod
    def create_context(cls,  # pylint: disable=too-many-arguments,too-many-locals,too-many-branches
                       chain_id: int,
                       block_number: Union[dict, int, None],
                       model_loader: Union[ModelLoader,
                                           None] = None,
                       chain_to_provider_url: Union[dict[str,
                                                         str], None] = None,
                       api_url: Union[str, None] = None,
                       run_id: Union[str, None] = None,
                       depth: int = 0,
                       client: Union[str, None] = None,
                       console: bool = False,
                       use_local_models: Union[str, None] = None,
                       model_cache: Union[ModelRunCache,
                                          bool] = True):
        """
        Parameters:
            block_number: if None, latest block is used
            run_id (str | None): a string to identify a particular model run. It is
                same for any other models run from within a model.
        """

        if console:
            cls.dev_mode = True
            RunModelMethod.interactive_docs = True
            # Clear the previous context when we re-create context in the interactive console.
            ModelContext.set_current_context(None)

        if model_loader is None:
            model_loader = ModelLoader(['.'])

        api = ModelApi.api_for_url(api_url)

        web3_registry = Web3Registry(chain_to_provider_url)

        cls.use_local_models_slugs = set()
        if use_local_models is not None and len(use_local_models):
            local_model_slugs = use_local_models.split(',')
            if '-' not in local_model_slugs:
                cls.logger.debug(f'Using local models {local_model_slugs}')
            else:
                if len(local_model_slugs) > 1:
                    cls.logger.warning(f'Using no local models (conflicting args: {use_local_models})')
                else:
                    cls.logger.debug('Using no local models')
            cls.use_local_models_slugs.update(local_model_slugs)

        if cls.dev_mode and '-' not in cls.use_local_models_slugs:
            cls.use_local_models_slugs.update(
                model_loader.loaded_dev_model_slugs())
            cls.logger.debug('Using local models (requested + dev models): '
                             f'{cls.use_local_models_slugs}')

        if block_number is None:
            # Lookup latest block number if none specified
            block_number = cls.get_latest_block_number(api, chain_id)
            cls.logger.info(f'Using latest block number {block_number}')
        elif isinstance(block_number, dict):
            block_number = BlockNumber.from_dict(block_number)
        else:
            block_number = BlockNumber(block_number)

        if model_cache is True:
            _model_cache = ModelRunCache()
        elif model_cache is False:
            _model_cache = None
        else:
            _model_cache = model_cache

        context = EngineModelContext(
            chain_id, block_number, web3_registry,
            run_id, depth, model_loader, _model_cache, api, client,
            is_top_level=not console,
            parent_context=None)

        if console:
            context.is_active = True
            ModelContext.set_current_context(context)

        return context

    @classmethod
    def create_context_and_run_model(cls,  # pylint: disable=too-many-arguments,too-many-locals
                                     chain_id: int,
                                     block_number: Union[dict, int, None],
                                     model_slug: str,
                                     model_version: Union[str, None] = None,
                                     input: Union[dict, None] = None,
                                     model_loader: Union[ModelLoader,
                                                         None] = None,
                                     chain_to_provider_url: Union[dict[str,
                                                                       str], None] = None,
                                     api_url: Union[str, None] = None,
                                     run_id: Union[str, None] = None,
                                     depth: int = 0,
                                     client: Union[str, None] = None,
                                     use_local_models: Union[str, None] = None,
                                     model_cache: Union[ModelRunCache,
                                                        bool] = True):
        """
        Parameters:
            block_number: if None, latest block is used
            run_id (str | None): a string to identify a particular model run. It is
                same for any other models run from within a model.
        Catches all exceptions
        """
        context: Union[EngineModelContext, None] = None

        try:
            context = cls.create_context(chain_id,
                                         block_number,
                                         model_loader,
                                         chain_to_provider_url,
                                         api_url,
                                         run_id,
                                         depth,
                                         client,
                                         console=False,
                                         use_local_models=use_local_models,
                                         model_cache=model_cache)

            if input is None:
                input = {}

            response = cls.run_model_with_context(context,
                                                  model_slug,
                                                  model_version,
                                                  input)

        except Exception as e:
            err = ModelEngineError(str(e))
            response = {
                'slug': model_slug,
                'version': model_version,
                'chainId': chain_id,
                'blockNumber': block_number,
                'error': err.dict(),
                'dependencies': context.dependencies if context else {}}

        return response

    @classmethod
    def run_model_with_context(cls,
                               context: 'EngineModelContext',
                               model_slug: str,
                               model_version: Union[str, None],
                               input: Union[dict, DTOType],
                               transform_output_to_dict=True):
        chain_id = context.chain_id
        block_number = int(context.block_number)
        block_timestamp = context.block_number.timestamp if context.block_number.is_timestamp_loaded else None

        try:
            ModelContext.set_current_context(context)

            # We set the block_number in the context above so we pass in
            # None for block_number to the run_model method.
            result_tuple = context._run_model(  # pylint: disable=protected-access
                model_slug, input, None, model_version)

            output = result_tuple[2]
            if transform_output_to_dict:
                output = transform_data_for_dto(
                    output, None, model_slug, 'output')

            response = {
                'slug': result_tuple[0],
                'version': result_tuple[1],
                'chainId': chain_id,
                'blockNumber': block_number,
                'blockTimestamp': block_timestamp,
                'output': output,
                'dependencies': context.dependencies}

        except ModelBaseError as err:
            response = {
                'slug': model_slug,
                'version': model_version,
                'chainId': chain_id,
                'blockNumber': block_number,
                'blockTimestamp': block_timestamp,
                'error': err.dict(),
                'dependencies': context.dependencies if context else {}}
        except Exception as e:
            err = ModelEngineError(str(e))
            response = {
                'slug': model_slug,
                'version': model_version,
                'chainId': chain_id,
                'blockNumber': block_number,
                'blockTimestamp': block_timestamp,
                'error': err.dict(),
                'dependencies': context.dependencies if context else {}}
        finally:
            ModelContext.set_current_context(None)

        return response

    @classmethod
    def get_latest_block_number(cls, api: ModelApi, chain_id: int):
        if chain_id == 1:
            _s, _v, output, _e, _d = api.run_model(LEDGER_GET_LATEST_BLOCK_NUMBER_SLUG,
                                                   None, chain_id, 0, {}, raise_error_results=True)
            if output is None:
                raise Exception('Error response getting latest block number')
            number, timestamp = output['number'], output['timestamp']
        else:
            _s, _v, output, _e, _d = api.run_model(CHAIN_GET_LATEST_BLOCK_NUMBER_SLUG,
                                                   None, chain_id, 0, {}, raise_error_results=True)
            if output is None:
                raise Exception('Error response getting latest block number')
            number, timestamp = output['blockNumber'], output['timestamp']
        return BlockNumber(number, timestamp)

    def __init__(self,  # pylint: disable=too-many-arguments
                 chain_id: int,
                 block_number: Union[BlockNumber, int],
                 web3_registry: Web3Registry,
                 run_id: Union[str, None],
                 depth: int,
                 model_loader: ModelLoader,
                 model_cache: Optional[ModelRunCache],
                 api: Union[ModelApi, None],
                 client: Union[str, None] = None,
                 is_top_level: bool = False,
                 parent_context: Union[ModelContext, None] = None):
        if isinstance(block_number, int):
            block_number = BlockNumber(block_number)

        super().__init__(chain_id, block_number, web3_registry, parent_context)
        self.run_id = run_id
        self.__client = client
        self.__depth = depth
        self.__dependencies = {}
        self.__model_loader = model_loader
        self.__model_cache = model_cache
        self.__api = api
        self.__is_top_level = is_top_level
        self.is_active = False

    @property
    def dependencies(self):
        return self.__dependencies

    def _model_manifests(self, underscore_slugs=False):
        """
        Returns a map of slug to manifest for all models local
        and remote, which is lazily built for the class on the first call.
        """
        if len(self._model_manifest_map) == 0:
            manifests = self.__model_loader.loaded_model_manifests_with_class()
            for m in manifests:
                slug = m['slug']
                self._model_manifest_map[slug] = m
                self._model_underscore_manifest_map[slug.replace('-', '_')] = m

            if self.__api is not None:
                try:
                    deployed_manifests = self.__api.get_models()
                    for m in deployed_manifests:
                        m |= {'mclass': self.__model_loader.get_model_class(m['slug'], m['version'])}
                        slug = m['slug']
                        self._model_manifest_map[slug] = m
                        self._model_underscore_manifest_map[slug.replace(
                            '-', '_')] = m
                except Exception:
                    # Error will have been logged but we continue so things work offline
                    pass
        return self._model_underscore_manifest_map if underscore_slugs else self._model_manifest_map

    def _class_for_model(self, slug: str, version: Union[str, None] = None):
        return self.__model_loader.get_model_class(slug, version, False)

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

    def _force_local_model_for_slug(self, slug: str):
        return slug in self.use_local_models_slugs

    def _favor_local_model_for_slug(self, slug: str):
        return '*' in self.use_local_models_slugs or slug in self.use_local_models_slugs

    def _use_no_local_model(self):
        return '-' in self.use_local_models_slugs

    def run_model(self,
                  slug,
                  input=EmptyInput(),
                  return_type=None,
                  block_number: Union[BlockNumber, int, None] = None,
                  version=None,
                  local: bool = False,
                  ):
        """Run a model by slug and optional version.

        Parameters:
            slug (str): the slug of the model
            input (dict | DTO): an optional dictionary of
                  input data that will be passed to the model when it is run.
            block_number (int | None): optional block number to use as context.
                  If None, the block_number of the current context will be used.
            version (str | None): optional version of the model.
                  If version is None, the latest version of
                  the model is used.
            return_type (DTO Type | None): optional class to use for the
                  returned output data. If not specified, returned value is a dict.
                  If a DTO specified, the returned value will be an instance
                  of that class if the output data is compatible with it. If its not,
                  an exception will be raised.

        Returns:
            The output returned by the model's run() method as a dict
            or a DTO instance if return_type is specified.

        Raises:
            MissingModelError: if requested model is not available
            Exception on other errors
        """

        if block_number is not None and block_number > self.block_number:
            raise ModelInvalidStateError(
                f'Attempt to run model {slug} at context block {self.block_number} '
                f'with future block {block_number}')

        if isinstance(block_number, int):
            block_number = BlockNumber(block_number)

        res_tuple = self._run_model(slug, input, block_number, version, local)

        # The last item of the tuple is the output.
        output = res_tuple[-1]
        # Transform to the requested return type
        return transform_data_for_dto(output, return_type, slug, 'output')

    def set_current(self):
        ModelContext.set_current_context(self)

    def reload_model(self):
        self.__model_loader.reload()
        EngineModelContext._clear_model_manifest_maps()

    def add_model(self, mclass: Type[Model], replace=True):
        self.__model_loader.add_model(mclass, replace)
        EngineModelContext._clear_model_manifest_maps()

    def remove_model_by_slug(self, model_slug):
        self.__model_loader.remove_model_by_slug(model_slug)
        EngineModelContext._clear_model_manifest_maps()

    def _run_model(self,
                   slug: str,
                   input: Union[dict, DTOType],
                   block_number: Union[BlockNumber, None],
                   version: Union[str, None],
                   local: bool = False
                   ):

        mock_result = self._run_model_mock(slug, input, version)
        if isinstance(mock_result, str):
            slug = mock_result
        else:
            return mock_result

        is_cli = (self.dev_mode and not self.run_id) or self.test_mode
        is_top_level_inactive = self.__is_top_level and not self.is_active
        force_local = self._force_local_model_for_slug(slug)
        use_local = ((is_top_level_inactive or force_local or self.test_mode
                     or self._favor_local_model_for_slug(slug))
                     and not self._use_no_local_model())
        use_local = use_local or local
        # when using the cli, we allow running remote models as top level
        try_remote = not is_top_level_inactive or is_cli

        debug_log = self.debug_logger.isEnabledFor(logging.DEBUG)

        if debug_log:
            self.debug_logger.debug(
                f'Run model states: {self.dev_mode=}, {self.run_id=}, {self.test_mode=}, '
                f'{self._favor_local_model_for_slug(slug)=} {self._use_no_local_model()=}, '
                f'{self.is_active=}')
            self.debug_logger.debug(
                f'{is_cli=}, {is_top_level_inactive=}, {try_remote=}, {slug=}, '
                f'{force_local=}, {use_local=}, '
                f'{block_number=}')

        try:
            model_class = self.__model_loader.get_model_class(
                slug, version, force_local)
        except Exception:
            self.logger.error(
                f'Requested local model not found locally: slug {slug} '
                f'version {version if version is not None else "any"}')
            raise

        self.__depth += 1

        try:
            if self.__depth >= self.max_run_depth:
                raise MaxModelRunDepthError(f'Max model run depth hit {self.__depth}')

            return self._run_model_with_class(
                slug,
                input,
                block_number,
                version,
                model_class,
                use_local,
                try_remote)
        finally:
            self.__depth -= 1

    def _run_model_mock(self, slug, input, version):
        # Run a model mock if mock runner set.
        # Returns the mock result or a string for the slug
        # of the model to actually run.

        # Use mocks if set
        if EngineModelContext._model_mock_runner is not None:
            try:
                self.__depth += 1

                mock_input = transform_data_for_dto(input, None, slug, 'input')
                output = EngineModelContext._model_mock_runner.output_for_model(
                    slug, mock_input)  # type: ignore
                if isinstance(output, str):
                    # If a str, run model slug returned from mock
                    return output
                else:
                    if version is None:
                        version = '0.0'
                    self._add_dependency(slug, version, 1)
                    return slug, version, output
            except ModelMockException:
                # At the top level, we run the actual model if there is no mock
                if self.__depth > 1:
                    raise
            finally:
                self.__depth -= 1

        return slug

    def _run_model_with_class(self,  # pylint: disable=too-many-locals,too-many-arguments,too-many-branches
                              slug: str,
                              input: Union[dict, DTOType],
                              block_number: Union[BlockNumber, None],
                              version: Union[str, None],
                              model_class: Union[Type[Model], None],
                              use_local: bool,
                              try_remote: bool):

        api = self.__api

        debug_log = self.debug_logger.isEnabledFor(logging.DEBUG)

        if use_local and model_class is not None:
            slug, version, output = self._run_local_model_with_class(
                slug,
                input,
                block_number,
                version,
                model_class)

        elif try_remote and api is not None:
            run_block_number = block_number if block_number is not None else self.block_number

            try:
                if debug_log:
                    self.debug_logger.debug(
                        f"> Run API model '{slug}' input: {input} "
                        f"run_block_number: {run_block_number}")

                version_requested = version
                input_as_dict = transform_dto_to_dict(input)

                in_cache, cached_output = (
                    (None, ({}, None, {})) if self.__model_cache is None
                    else self.__model_cache.get(self.chain_id, int(run_block_number),
                                                slug, version_requested, input_as_dict))

                if in_cache is not None:
                    if debug_log:
                        self.debug_logger.debug(
                            f'cached from remote, {slug, version_requested, input_as_dict}')
                    output, error, dependencies = cached_output
                else:
                    # We pass depth - 1 which is the callers depth
                    # since we already incremented for this model run request
                    slug, version, output, error, dependencies = api.run_model(
                        slug, version, self.chain_id,
                        run_block_number,
                        input_as_dict,
                        self.run_id, self.__depth - 1, self.__client)

                    if self.__model_cache is not None:
                        self.__model_cache.put(self.chain_id,
                                               int(run_block_number),
                                               slug,
                                               version_requested,
                                               input_as_dict,
                                               output,
                                               dependencies,
                                               error)

                if dependencies:
                    self._add_dependencies(dependencies)

                # Any error raised will already have a call stack entry
                if error is not None:
                    if debug_log:
                        self.debug_logger.debug(
                            f"< Run API model '{slug}' error: {error} "
                            f"run_block_number: {run_block_number}")
                    raise create_instance_from_error_dict(error)

                EngineModelContext.notify_model_run(slug, version, self.chain_id,
                                                    run_block_number, input, output, error)

                if debug_log:
                    self.debug_logger.debug(
                        f"< Run API model '{slug}' output: {output} "
                        f"run_block_number: {run_block_number}")

            except ModelNotFoundError as err:
                # We always fallback to local if model not found on server.
                if model_class is not None and not self._use_no_local_model():
                    self.logger.debug(
                        f'Model {slug} not on server. Using local instead')
                    slug, version, output = self._run_local_model_with_class(
                        slug,
                        input,
                        block_number,
                        version,
                        model_class)
                else:
                    EngineModelContext.notify_model_run(slug, version, self.chain_id,
                                                        run_block_number, input, None, err)
                    raise
            except ModelBaseError as err:
                EngineModelContext.notify_model_run(slug, version, self.chain_id,
                                                    run_block_number, input, None, err)
                raise
            except Exception as exc:
                err = ModelRunError(str(exc))
                EngineModelContext.notify_model_run(slug, version, self.chain_id,
                                                    run_block_number, input, None, err)
                raise
        else:
            # No call stack item because model not run
            err = ModelNotFoundError.create(slug, version)
            self.logger.error(err)
            raise err

        return slug, version, output

    def enter(self, block_number):
        if block_number > self._block_number:
            raise BlockNumberOutOfRangeError(
                message=(
                    f'You can not enter a context with a larger block number ({block_number} > current {self._block_number})'),
                detail=BlockNumberOutOfRangeDetailDTO(
                    blockNumber=block_number,
                    maxBlockNumber=self._block_number))

        context = EngineModelContext(self.chain_id,
                                     block_number,
                                     self._web3_registry,
                                     self.run_id,
                                     self.__depth,
                                     self.__model_loader,
                                     self.__model_cache,
                                     self.__api,
                                     self.__client,
                                     parent_context=self)

        ModelContext.set_current_context(context)
        return context

    def _run_local_model_with_class(self,  # pylint: disable=too-many-locals,too-many-branches,too-many-statements
                                    slug: str,
                                    input: Union[dict, DTOType],
                                    block_number: Union[BlockNumber, None],
                                    version: Union[str, None],
                                    model_class: Type[Model]):

        debug_log = self.debug_logger.isEnabledFor(logging.DEBUG)

        if not self.is_active:
            # At top level, we use this context
            context = self
        else:
            # otherwise we create a new context
            if block_number is None:
                block_number = self.block_number

            context = EngineModelContext(self.chain_id,
                                         block_number,
                                         self._web3_registry,
                                         self.run_id,
                                         self.__depth,
                                         self.__model_loader,
                                         self.__model_cache,
                                         self.__api,
                                         self.__client,
                                         parent_context=self)

        original_input = input

        try:
            try:
                input = transform_data_for_dto(input, model_class.inputDTO, slug, 'input')
            except DataTransformError as err:
                # We convert to an input error here to distinguish
                # from output transform errors below
                raise ModelInputError(str(err))

            input_as_dict = transform_dto_to_dict(input)

            in_cache, cached_output = (
                (None, ({}, None, {})) if self.__model_cache is None
                else self.__model_cache.get(context.chain_id,
                                            int(context.block_number),
                                            model_class.slug,
                                            model_class.version,
                                            input_as_dict))
            if in_cache is not None:
                if debug_log:
                    self.debug_logger.debug(
                        f'cached from local {model_class.slug, model_class.version, input_as_dict}')
                output, _error, _dependencies = cached_output
            else:
                ModelContext.set_current_context(context)
                context.is_active = True

                # Errors in this section will add the callee
                # model to the call stack

                context.__dict__['original_input'] = original_input
                context.__dict__['slug'] = slug
                model = model_class(context)

                if debug_log:
                    self.debug_logger.debug(
                        f"> Run model '{slug}' input: {input} block_number: {block_number}")

                output = model.run(input)

                del context.__dict__['original_input']
                del context.__dict__['slug']

                try:
                    # transform to the defined outputDTO for validation of output
                    output = transform_data_for_dto(
                        output, model_class.outputDTO, slug, 'output')
                    if self.dev_mode:
                        # In dev mode we do a deep transform to dicts (convert all DTOs)
                        # We do this to ensure dev is same as production.
                        # Production mode will serialize all input and output.
                        output = json.loads(json_dumps(output))

                except DataTransformError as err:
                    raise ModelOutputError(str(err))

            EngineModelContext.notify_model_run(slug,
                                                model_class.version,
                                                context.chain_id,
                                                context.block_number,
                                                input,
                                                output,
                                                None)

            if debug_log:
                self.debug_logger.debug(
                    f"< Run model '{slug}' output: {output} block_number: {block_number}")

        except Exception as err:
            if slug == 'console':
                print(err, file=sys.stderr)
                raise err

            if isinstance(err, (DataTransformError, DTOValidationError)):
                # Transform error is a coding error in model just run
                err = ModelTypeError(str(err))
                trace = traceback.format_exc(limit=30)
                if debug_log:
                    self.debug_logger.debug(
                        f"< Run model '{slug}' error: {err} block_number: {block_number}")

            elif isinstance(err, ModelBaseError):
                _exc_type, _exc_value, exc_traceback = sys.exc_info()
                if isinstance(err, (ModelNotFoundError, ModelRunRequestError)):
                    trace = extract_most_recent_run_model_traceback(
                        exc_traceback, 2)
                else:
                    trace = extract_most_recent_run_model_traceback(
                        exc_traceback)

                # For errors that have specific detail classes, we
                # ensure detail is a dict (as it will be over the wire)
                # to make local-dev identical to production.
                err.transform_data_detail(None)

                if debug_log:
                    self.debug_logger.debug(
                        f"< Run model '{slug}' error: {err}")
            else:
                input_json = json_dumps(transform_data_for_dto(
                    input, None, slug, 'input'))
                err_msg = (f'Exception running model {slug}({input_json}) on '
                           f'chain {context.chain_id} '
                           f'block {context.block_number} ('
                           f'{context.block_number.timestamp_datetime:%Y-%m-%d %H:%M:%S}) '
                           f'with {err}')
                if self.dev_mode:
                    self.logger.exception(err_msg)
                elif debug_log:
                    self.debug_logger.debug(
                        f"< Run model '{slug}' error: {err_msg}")

                err = ModelRunError(err_msg)
                trace = traceback.format_exc(limit=30)

            # We add the model just run (or validated input for) to stack
            err.data.stack.insert(0,  # pylint:disable=no-member
                                  ModelCallStackEntry(
                                      slug=slug,
                                      version=model_class.version,
                                      chainId=context.chain_id,
                                      blockNumber=context.block_number,
                                      input=json_dumps(original_input),
                                      trace=trace if trace is not None else None))

            EngineModelContext.notify_model_run(slug, model_class.version, context.chain_id,
                                                context.block_number, input, None, err)
            raise err

        finally:
            context.is_active = False
            ModelContext.set_current_context(self)

            # If we ran with a different context, we add its deps
            if context != self:
                self._add_dependencies(context.dependencies)

            # Now we add dependency for this run
            version = model_class.version
            self._add_dependency(slug, version, 1)

        if in_cache is None and self.__model_cache is not None:
            output_as_dict = transform_dto_to_dict(output)
            self.__model_cache.put(context.chain_id,
                                   int(context.block_number),
                                   slug,
                                   version,
                                   input_as_dict,
                                   output_as_dict,
                                   self.dependencies,
                                   None)

        return slug, version, output
