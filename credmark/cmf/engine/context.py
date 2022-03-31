import json
import logging
import traceback
import sys
from typing import Type, Union
from credmark.dto.encoder import json_dumps
from credmark.cmf.model import Model
from credmark.cmf.model.context import ModelContext
from credmark.cmf.engine.errors import ModelNotFoundError, ModelRunRequestError
from credmark.cmf.model.errors import MaxModelRunDepthError, ModelBaseError, \
    ModelEngineError, ModelInputError, ModelInvalidStateError, ModelOutputError, \
    ModelRunError, ModelCallStackEntry, ModelTypeError
from credmark.cmf.engine.model_api import ModelApi
from credmark.cmf.engine.model_loader import ModelLoader
from credmark.dto.transform import DataTransformError, transform_data_for_dto
from credmark.cmf.engine.web3 import Web3Registry
from credmark.dto import DTO, EmptyInput, DTOValidationError
from credmark.cmf.model.slugs import CoreModels


def extract_most_recent_run_model_traceback(exc_traceback, skip=1):
    # Extract "skip" most-recent group of frames before frames
    # in this file (or superclass context) until it comes back to
    # the context.
    context_files = set([__file__,
                         __file__.replace('credmark/model/engine/context',
                                          'credmark/model/context'),
                         __file__.replace('credmark/model/engine/context',
                                          'credmark/model/engine/model_api')])
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

    logger = logging.getLogger(__name__)

    dev_mode = False
    max_run_depth = 20

    @classmethod
    def create_context_and_run_model(cls,  # pylint: disable=too-many-arguments,too-many-locals
                                     chain_id: int,
                                     block_number: Union[int, None],
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
            block_number: if None, latest block is used
            run_id (str | None): a string to identify a particular model run. It is
                same for any other models run from within a model.
        Catches all exceptions
        """
        context: Union[EngineModelContext, None] = None
        try:
            if model_loader is None:
                model_loader = ModelLoader(['.'])

            api = ModelApi.api_for_url(api_url)

            web3_registry = Web3Registry(chain_to_provider_url)

            if block_number is None:
                # Lookup latest block number if none specified
                block_number = cls.get_latest_block_number(api, chain_id)
                cls.logger.info(f'Using latest block number {block_number}')

            context = EngineModelContext(
                chain_id, block_number, web3_registry,
                run_id, depth, model_loader, api, True)

            if input is None:
                input = {}

            ModelContext._current_context = context

            # We set the block_number in the context above so we pass in
            # None for block_number to the run_model method.
            result_tuple = context._run_model(
                model_slug, input, None, model_version)

            output = result_tuple[2]
            output_as_dict = transform_data_for_dto(output, None, model_slug, 'output')

            response = {
                'slug': result_tuple[0],
                'version': result_tuple[1],
                'output': output_as_dict,
                'dependencies': context.dependencies}
            return response
        except ModelBaseError as err:
            response = {
                'slug': model_slug,
                'version': model_version,
                'error': err.dict(),
                'dependencies': context.dependencies if context else {}}
        except Exception as e:
            err = ModelEngineError(str(e))
            response = {
                'slug': model_slug,
                'version': model_version,
                'error': err.dict(),
                'dependencies': context.dependencies if context else {}}
        finally:
            ModelContext._current_context = None
        return response

    @classmethod
    def get_latest_block_number(cls, api: ModelApi, chain_id: int):
        _s, _v, output, _d = api.run_model(CoreModels.latest_block_number,
                                           None, chain_id, 0, {})
        block_number: int = output['blockNumber']
        return block_number

    def __init__(self,  # pylint: disable=too-many-arguments
                 chain_id: int,
                 block_number: int,
                 web3_registry: Web3Registry,
                 run_id: Union[str, None],
                 depth: int,
                 model_loader: ModelLoader,
                 api: Union[ModelApi, None],
                 is_top_level: bool = False):
        super().__init__(chain_id, block_number, web3_registry)
        self.run_id = run_id
        self.__depth = depth
        self.__dependencies = {}
        self.__model_loader = model_loader
        self.__api = api
        self.__is_top_level = is_top_level
        self.is_active = False

    @property
    def dependencies(self):
        return self.__dependencies

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
                  slug,
                  input=EmptyInput(),
                  return_type=None,
                  block_number=None,
                  version=None,
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
            MissingModelError if requested model is not available
            Exception on other errors
        """

        if block_number is not None and block_number > self.block_number:
            raise ModelInvalidStateError(
                f'Attempt to run model {slug} at context block {self.block_number} '
                f'with future block {block_number}')

        res_tuple = self._run_model(slug, input, block_number, version)

        # The last item of the tuple is the output.
        output = res_tuple[-1]
        # Transform to the requested return type
        return transform_data_for_dto(output, return_type, slug, 'output')

    def _run_model(self,
                   slug: str,
                   input: Union[dict, DTO],
                   block_number: Union[int, None],
                   version: Union[str, None]
                   ):

        is_cli = self.dev_mode and not self.run_id
        is_top_level_inactive = self.__is_top_level and not self.is_active
        try_local = is_top_level_inactive or self.dev_mode
        try_remote = not is_top_level_inactive or is_cli

        api = self.__api

        if try_local:
            # We raise an exception for missing class if no api
            raise_on_missing = api is None
            model_class = self.__model_loader.get_model_class(
                slug, version, raise_on_missing)
        else:
            model_class = None

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
                try_remote)
        finally:
            self.__depth -= 1

    def _run_model_with_class(self,  # pylint: disable=too-many-locals,too-many-branches,too-many-statements
                              slug: str,
                              input: Union[dict, DTO],
                              block_number: Union[int, None],
                              version: Union[str, None],
                              model_class: Union[Type[Model], None],
                              try_remote: bool):

        api = self.__api

        if model_class is not None:

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
                                             api
                                             )

            try:

                try:
                    input = transform_data_for_dto(input, model_class.inputDTO, slug, 'input')
                except DataTransformError as err:
                    # We convert to an input error here to distinguish
                    # from output transform errors below
                    raise ModelInputError(str(err))

                ModelContext._current_context = context
                context.is_active = True

                # Errors in this section will add the callee
                # model to the call stack

                model = model_class(context)

                output = model.run(input)

                try:
                    # transform to the defined outputDTO for validation of output
                    output = transform_data_for_dto(output, model_class.outputDTO, slug, 'output')
                    if self.dev_mode:
                        # In dev mode we do a deep transform to dicts (convert all DTOs)
                        # We do this to ensure dev is same as production.
                        # Production mode will serialize all input and output.
                        output = json.loads(json_dumps(output))
                except DataTransformError as err:
                    raise ModelOutputError(str(err))

            except Exception as err:
                if isinstance(err, (DataTransformError, DTOValidationError)):
                    # Transform error is a coding error in model just run
                    err = ModelTypeError(str(err))
                    trace = traceback.format_exc(limit=30)
                elif isinstance(err, ModelBaseError):
                    _exc_type, _exc_value, exc_traceback = sys.exc_info()
                    if isinstance(err, (ModelNotFoundError, ModelRunRequestError)):
                        trace = extract_most_recent_run_model_traceback(exc_traceback, 2)
                    else:
                        trace = extract_most_recent_run_model_traceback(exc_traceback)

                    # For errors that have specific detail classes, we
                    # ensure detail is a dict (as it will be over the wire)
                    # to make local-dev identical to production.
                    err.transform_data_detail(None)
                else:
                    if self.dev_mode:
                        self.logger.exception(f'Exception running model {slug}: {err}')
                    err = ModelRunError(f'Exception running model {slug}: {err}')
                    trace = traceback.format_exc(limit=30)
                # We add the model just run (or validated input for) to stack
                err.data.stack.insert(0,
                                      ModelCallStackEntry(
                                          slug=slug,
                                          version=model_class.version,
                                          chainId=context.chain_id,
                                          blockNumber=context.block_number,
                                          trace=trace[:1000] if trace is not None else None))
                raise err

            finally:
                context.is_active = False
                ModelContext._current_context = self

                # If we ran with a different context, we add its deps
                if context != self:
                    self._add_dependencies(context.dependencies)

                # Now we add dependency for this run
                version = model_class.version
                self._add_dependency(slug, version, 1)

        elif try_remote and api is not None:
            # Any error raised will already have a call stack entry
            slug, version, output, dependencies = api.run_model(
                slug, version, self.chain_id,
                block_number if block_number is not None else self.block_number,
                input if input is None or isinstance(input, dict) else input.dict(),
                self.run_id, self.__depth)
            if dependencies:
                self._add_dependencies(dependencies)
        else:
            # No call stack item because model not run
            err = ModelNotFoundError.create(slug, version)
            self.logger.error(err)
            raise err

        return slug, version, output
