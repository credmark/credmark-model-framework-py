import inspect
import logging
import re
from abc import abstractmethod
from copy import deepcopy
from typing import List, Literal, Tuple, Type, Union

from credmark.cmf.engine.cache import CachePolicy
from credmark.cmf.types import BlockNumber
from credmark.cmf.types.series import BlockSeries, ImmutableOutput
from credmark.dto import DTOType, DTOTypesTuple, EmptyInput
from credmark.dto.transform import transform_data_for_dto

from .context import ModelContext
from .errors import ModelBaseError, ModelDataErrorDTO, ModelDefinitionError


class MissingModelBaseClass(ModelDefinitionError):
    pass


class WrongModelMethodSignature(ModelDefinitionError):
    pass


class InvalidModelCacheKey(ModelDefinitionError):
    pass


class InvalidModelSlug(ModelDefinitionError):
    pass


DICT_SCHEMA = {"title": "Object", "type": "object", "properties": {}}

# We could probably get the input and output DTOs from
# the run() method signature instead of passing them as params to
# the decorator but there may be reasons why they want to use
# different types and the DTOs are used to document the schema.

MAX_SLUG_LENGTH = 64
model_slug_re = re.compile(
    r'^(([A-Za-z0-9]+\-)*[A-Za-z0-9]+\.)?([A-Za-z0-9]+\-)*[A-Za-z0-9]+$')


class ModelErrorDesc:
    """
    Model error description base class.
    """
    @abstractmethod
    def schema(self, slug: str, include_definitions=True) -> dict:
        pass


class ModelDataErrorDesc(ModelErrorDesc):
    """
    A description of ModelDataErrors raised by a model.

    Contains the list of possible codes and their descriptions.
    """

    def __init__(self, description: Union[str, None] = None, code: Union[str, None] = None,
                 code_desc: Union[str, None] = None,
                 codes: Union[List[Tuple[str, str]], List[str], None] = None):
        """
        Create a description of a ModelDataError.

        Args:
        description: Description of the error
        code: Error code
        code_desc: Description of error code
        codes: List of tuples `(code, code_description)`
        """
        self.description = description if description is not None else 'ModelDataError'
        self.codes: List[Tuple[str, str]] = []
        if codes is not None:
            for ct in codes:
                self.codes.append(ct if isinstance(ct, tuple) else (ct, ct))
        if code is not None:
            self.codes.append((code, code_desc)
                              if code_desc is not None else (code, code))
        self.codes.sort()

    def schema(self, slug: str, include_definitions=True):
        """
        Returns a schema for the base object without the definitions.
        """
        schema = deepcopy(ModelDataErrorDTO.schema())
        schema['title'] = f'ModelDataError_{slug.replace(".","_").replace("-", "_")}'
        schema['description'] = self.description
        schema['properties']['type']['description'] = "ModelDataError"
        code_prop = schema['properties']['code']
        del code_prop['default']
        code_prop['enum'] = [ct[0] for ct in self.codes]
        code_desc_list = [f"\'{ct[0]}\' - {ct[1]}" for ct in self.codes]
        code_prop['description'] = f'Code values: {"; ".join(code_desc_list)}'
        required = schema['required']
        if 'code' not in required:
            required.append('code')
        if not include_definitions:
            del schema['definitions']
        return schema


def create_error_schema_for_error_descs(slug: str,
                                        errors: Union[List[ModelErrorDesc], ModelErrorDesc, None]):
    try:
        base_error_schema = ModelBaseError.base_error_schema()

        if isinstance(errors, ModelErrorDesc):
            errors = [errors]

        if errors is None or len(errors) == 0:
            return base_error_schema
        else:
            general_error = deepcopy(base_error_schema)
            definitions = general_error['definitions']
            del general_error['definitions']
            definitions[general_error['title']] = general_error
            combined_schema = {
                'title': f'ModelErrors_{slug.replace(".","_").replace("-", "_")}',
                'oneOf': [{'$ref': f'#/definitions/{general_error["title"]}'}],
                'definitions': definitions
            }
            oneOf = combined_schema['oneOf']
            for i, err_desc in enumerate(errors):
                schema = err_desc.schema(slug, False)
                title = schema["title"]
                if title in definitions:
                    # handle name clash
                    title = f'{title}_{i+1}'
                    schema['title'] = title
                oneOf.append({'$ref': f'#/definitions/{title}'})
                definitions[title] = schema
            return combined_schema

    except Exception as err:
        raise ModelDefinitionError(
            f'Exception processing "errors" in model {slug} describe(): {err}') from None


def validate_model_slug(slug: str, prefix: Union[str, None] = None):
    if prefix is not None and not slug.startswith(prefix):
        raise InvalidModelSlug(
            f'Slug for model {slug} must start with "{prefix}"')

    if model_slug_re.match(slug) is None or len(slug) > MAX_SLUG_LENGTH:
        quoted_prefix = f'"{prefix}"' if prefix else ''
        raise InvalidModelSlug(
            f'Invalid model slug "{slug}". '
            f'Following the prefix {quoted_prefix}' if prefix else 'Following a prefix and dot'
            ', slugs must start and end with a letter or number and may contain hyphens.')
    if len(slug) > MAX_SLUG_LENGTH:
        raise InvalidModelSlug(
            f'Invalid model slug "{slug}". '
            'Slugs must be not more than {MAX_SLUG_LENGTH} characters.')


def _describe(*,
              slug: str,
              version: str,
              display_name: Union[str, None] = None,
              description: Union[str, None] = None,
              developer: Union[str, None] = None,
              category: Union[str, None] = None,
              subcategory: Union[str, None] = None,
              tags: Union[list[str], None] = None,
              cache: CachePolicy = CachePolicy.FULL,
              input: Union[Type[DTOType], Type[dict]] = EmptyInput,
              output: Union[Type[DTOType], Type[dict], None] = None,
              errors: Union[List[ModelErrorDesc], ModelErrorDesc, None] = None):
    def wrapper(cls_in):  # pylint:disable=too-many-branches
        def is_parent(child, parent):
            found = parent in child.__bases__
            return found or True in [is_parent(pp, parent) for pp in child.__bases__]

        if cache is CachePolicy.INCREMENTAL:
            base_cls = IncrementalModel
            if not is_parent(cls_in, IncrementalModel):
                raise MissingModelBaseClass("A model with incremental cache policy should inherit "
                                            "from IncrementalModel imported from "
                                            "credmark.cmf.model.")
        elif cache is CachePolicy.IMMUTABLE:
            base_cls = ImmutableModel
            if not is_parent(cls_in, ImmutableModel):
                raise MissingModelBaseClass("A model with immutable cache policy should inherit "
                                            "from ImmutableModel imported from "
                                            "credmark.cmf.model.")
        else:
            base_cls = Model
            if not is_parent(cls_in, Model):
                raise MissingModelBaseClass("A model should inherit from Model "
                                            "imported from credmark.cmf.model.")

        cls = cls_in

        mod_parts = cls.__dict__['__module__'].split('.')
        if len(mod_parts) > 1 and mod_parts[1] == 'contrib':
            validate_model_slug(slug, 'contrib.')
        else:
            validate_model_slug(slug)

        # 2. has abstract functions as defined in the Model class
        method_list = [method for method in dir(base_cls)
                       if method.startswith('__') is False and
                       method in base_cls.__dict__ and
                       '__isabstractmethod__' in base_cls.__dict__[method].__dict__ and
                       base_cls.__dict__[method].__isabstractmethod__]

        for method in method_list:
            found_this_method = False
            for mro_cls in cls.__mro__:
                if mro_cls is base_cls or method not in mro_cls.__dict__:
                    continue

                found_this_method = True

                # Since the run method is overloaded, the signatures won't match exactly.
                # TODO: Add parameter and return value type compatibility check
                break

            if not found_this_method:
                raise WrongModelMethodSignature(
                    f'Model {cls.__name__} misses a method {method}() with signature {inspect.signature(base_cls.__dict__[method])}')  # pylint: disable=line-too-long

        model_desc = description
        if model_desc is None:
            model_desc = cls.__doc__.strip() if cls.__doc__ is not None else None

        attr_value = {
            'credmarkModelManifest': 'v1',
            'model': {
                'slug': slug,
                'version': version,
                'displayName': display_name,
                'description': model_desc,
                'developer': developer if developer is not None else '',
                'category': category,
                'subcategory': subcategory,
                'tags': tags,
                'cache': cache,
                'input': input.schema()
                if input is not None and issubclass(input, DTOTypesTuple)
                else DICT_SCHEMA,
                'output': output.schema()
                if output is not None and issubclass(output, DTOTypesTuple)
                else DICT_SCHEMA,
                'error': create_error_schema_for_error_descs(slug, errors),
                'class': cls.__dict__['__module__'] + '.' + cls.__name__,
            }
        }

        attr_name = '_manifest'

        def get_attr(self, attr_name=attr_name):
            return getattr(self, '_' + attr_name)
        attr_prop = property(get_attr, None)
        setattr(cls, attr_name, attr_prop)
        setattr(cls, '_' + attr_name, attr_value)

        cls.slug = slug
        cls.version = version
        cls.inputDTO = input
        cls.outputDTO = output

        return cls

    return wrapper


class BaseModel:
    # These class variables will be set automatically by
    # the loader or decorator
    slug: str
    version: str
    _manifest: dict
    inputDTO: Union[Type[DTOType], None]
    outputDTO: Union[Type[DTOType], None]

    def __init__(self, context: "ModelContext"):
        self.context = context
        # Configure our logger.
        self.logger = logging.getLogger(
            'credmark.cmf.model.{0}'.format(self.slug))
        self.init()

    def init(self):
        """
        Subclasses may override this method to do
        any model instance initiation.
        """

    def convert_dict_to_dto(self,
                            data: dict,
                            dto_class: Type[DTOType]):
        """
        A model can call this method to convert a dict
        of data in a known format into a DTO instance.
        """
        return transform_data_for_dto(data, dto_class, self.slug, 'transform')


class Model(BaseModel):
    """
    The base model class.

    Models should subclass this class and override the
    run() method. They may also override init().

    Available instance variables:

    - ``logger`` - a logger for messages related to the model
    - ``context`` - a ``ModelContext`` instance
    """

    @classmethod
    def describe(cls,
                 *,
                 slug: str,
                 version: str,
                 display_name: Union[str, None] = None,
                 description: Union[str, None] = None,
                 developer: Union[str, None] = None,
                 category: Union[str, None] = None,
                 subcategory: Union[str, None] = None,
                 tags: Union[list[str], None] = None,
                 cache: Literal[CachePolicy.FULL,
                                CachePolicy.SKIP,
                                CachePolicy.IGNORE_BLOCK,
                                CachePolicy.OFF_CHAIN] = CachePolicy.FULL,
                 input: Union[Type[DTOType], Type[dict]] = EmptyInput,
                 output: Union[Type[DTOType], Type[dict], None] = None,
                 errors: Union[List[ModelErrorDesc],
                               ModelErrorDesc, None] = None):
        """
        Decorator for credmark.cmf.model.Model subclasses to describe the model.

        Example usage::

            from credmark.cmf.model import Model

            @Model.describe(slug='example.echo',
                            version='1.0',
                            display_name='Echo',
                            description="A test model to echo the message property sent in input.",
                            developer="my_username",
                            category="financial",
                            input=EchoDto,
                            output=EchoDto)
            class EchoModel(Model):


        Parameters:
            slug: slug (short unique name) for the model. Can contain alpha-numeric and
                  and underscores. Contributor slugs must start with ``"contrib."``
                  Once submitted, the model slug cannot be changed.
            version: version string, ex. ``"1.0"``. The version number can be incremented
                  when the model code is updated.
            display_name: Name for the model
            description: Description of the model. If description is not set,
                        the doc string (``__doc__``) of the model class is used instead.
            developer: Name or nickname of the developer
            category: Category of the model (ex. "financial", "protocol" etc.)
            subcategory: Optional subcategory (ex. "aave")
            tags: optional list of string tags describing the model
            input: Type that model uses as input; a ``DTO`` subclass or dict.
                   Defaults to ``EmptyInput`` object.
            output: Type that the model run returns; a ``DTO`` subclass or dict.
                   Defaults to None which will provide no output schema.
            errors: If the model raises ``ModelDataError``, set this to a configured
                   ``ModelDataErrorDesc`` instance (or a list of instances) describing the
                   errors. Defaults to None.
        """
        return _describe(
            slug=slug,
            version=version,
            display_name=display_name,
            description=description,
            developer=developer,
            category=category,
            subcategory=subcategory,
            tags=tags,
            cache=cache,
            input=input,
            output=output,
            errors=errors,
        )

    @abstractmethod
    def run(self, input: Union[dict, DTOType]) -> Union[dict, DTOType]:
        """
        Subclasses **must** override this method to perform the work
        of running the model.

        Model instances may be reused so keep in mind that run()
        may be called multiple times. If you are using global
        data structures, make sure they are reset or cleared
        after each model run.
        """


class IncrementalModel(BaseModel):
    """
    Use `IncrementalModel` for models that only append to output with new blocks.
    Behind the scenes it uses `CachePolicy.INCREMENTAL` cache.
    These models should always return a BlockSeries. Use additional `from_block` arg
    in run method to only return BlockSeries for `from_block` -> `context.block`.
    """
    @classmethod
    def describe(cls,
                 *,
                 slug: str,
                 version: str,
                 display_name: Union[str, None] = None,
                 description: Union[str, None] = None,
                 developer: Union[str, None] = None,
                 category: Union[str, None] = None,
                 subcategory: Union[str, None] = None,
                 tags: Union[list[str], None] = None,
                 input: Union[Type[DTOType], Type[dict]] = EmptyInput,
                 output: Union[Type[BlockSeries], None] = BlockSeries,
                 errors: Union[List[ModelErrorDesc],
                               ModelErrorDesc, None] = None):
        """
        Decorator for credmark.cmf.model.IncrementalModel subclasses to describe the model.

        It shall return a parameterized class of `BlockSeries`.

        Example usage::

            from credmark.cmf.model import IncrementalModel
            from credmark.cmf.types.series import BlockSeries

            @IncrementalModel.describe(slug='example.echo-inc',
                            version='1.0',
                            display_name='Echo',
                            description="A test model to echo the message property sent in input.",
                            developer="my_username",
                            category="financial",
                            input=EchoDto,
                            output=BlockSeries[int])
            class EchoModel(IncrementalModel):
                def run(self, input: EchoDto, from_block: BlockNumber) -> BlockSeries[int]:
                    return BlockSeries(series=[
                        BlockSeriesRow(
                            blockNumber=0,
                            blockTimestamp=0,
                            sampleTimestamp=0,
                            output=1
                        ),
                        BlockSeriesRow(
                            blockNumber=1,
                            blockTimestamp=1,
                            sampleTimestamp=1,
                            output=2
                        ),
                    ])


        Parameters:
            slug: slug (short unique name) for the model. Can contain alpha-numeric and
                  and underscores. Contributor slugs must start with ``"contrib."``
                  Once submitted, the model slug cannot be changed.
            version: version string, ex. ``"1.0"``. The version number can be incremented
                  when the model code is updated.
            display_name: Name for the model
            description: Description of the model. If description is not set,
                        the doc string (``__doc__``) of the model class is used instead.
            developer: Name or nickname of the developer
            category: Category of the model (ex. "financial", "protocol" etc.)
            subcategory: Optional subcategory (ex. "aave")
            tags: optional list of string tags describing the model
            input: Type that model uses as input; a ``DTO`` subclass or dict.
                   Defaults to ``EmptyInput`` object.
            output: Type that the model run returns; a ``BlockSeries`` subclass.
            errors: If the model raises ``ModelDataError``, set this to a configured
                   ``ModelDataErrorDesc`` instance (or a list of instances) describing the
                   errors. Defaults to None.
        """
        return _describe(
            slug=slug,
            version=version,
            display_name=display_name,
            description=description,
            developer=developer,
            category=category,
            subcategory=subcategory,
            tags=tags,
            cache=CachePolicy.INCREMENTAL,
            input=input,
            output=output,
            errors=errors,
        )

    @abstractmethod
    def run(self, input: Union[dict, DTOType], from_block: BlockNumber) -> BlockSeries[DTOType]:
        ...


class ImmutableModel(BaseModel):
    """
    Subclass with `ImmutableModel` for models whose result is only available after a particular
    block and will not change for the future block numbers.

    It shall return a derived class of `ImmutableOutput` with field firstResultBlockNumber set.

    For blocks before which data is unavailable, the model should throw ModelDataError.
    Behind the scenes it uses `CachePolicy.IMMUTABLE` cache.
    """
    @classmethod
    def describe(cls,
                 *,
                 slug: str,
                 version: str,
                 display_name: Union[str, None] = None,
                 description: Union[str, None] = None,
                 developer: Union[str, None] = None,
                 category: Union[str, None] = None,
                 subcategory: Union[str, None] = None,
                 tags: Union[list[str], None] = None,
                 input: Union[Type[DTOType], Type[dict]] = EmptyInput,
                 output: Union[Type[ImmutableOutput], None] = ImmutableOutput,
                 errors: Union[List[ModelErrorDesc],
                               ModelErrorDesc, None] = None):
        """
        Decorator for credmark.cmf.model.ImmutableModel subclasses to describe the model.

        Example usage::

            from credmark.cmf.model import ImmutableModel
            from credmark.cmf.types.series import ImmutableOutput

            @ImmutableModel.describe(slug='example.echo-imm',
                            version='1.0',
                            display_name='Echo',
                            description="A test model to echo the message property sent in input.",
                            developer="my_username",
                            category="financial",
                            input=EchoDto,
                            output=ImmutableOutput)
            class EchoModel(ImmutableModel):
                def run(self, input: EchoDto, from_block: BlockNumber) -> ImmutableOutput:
                    return ImmutableOutput(
                    ...


        Parameters:
            slug: slug (short unique name) for the model. Can contain alpha-numeric and
                  and underscores. Contributor slugs must start with ``"contrib."``
                  Once submitted, the model slug cannot be changed.
            version: version string, ex. ``"1.0"``. The version number can be incremented
                  when the model code is updated.
            display_name: Name for the model
            description: Description of the model. If description is not set,
                        the doc string (``__doc__``) of the model class is used instead.
            developer: Name or nickname of the developer
            category: Category of the model (ex. "financial", "protocol" etc.)
            subcategory: Optional subcategory (ex. "aave")
            tags: optional list of string tags describing the model
            input: Type that model uses as input; a ``DTO`` subclass or dict.
                   Defaults to ``EmptyInput`` object.
            output: Type that the model run returns; a ``ImmutableOutput`` subclass.
            errors: If the model raises ``ModelDataError``, set this to a configured
                   ``ModelDataErrorDesc`` instance (or a list of instances) describing the
                   errors. Defaults to None.
        """
        return _describe(
            slug=slug,
            version=version,
            display_name=display_name,
            description=description,
            developer=developer,
            category=category,
            subcategory=subcategory,
            tags=tags,
            cache=CachePolicy.IMMUTABLE,
            input=input,
            output=output,
            errors=errors,
        )

    @abstractmethod
    def run(self, input: Union[dict, DTOType]) -> ImmutableOutput:
        ...
