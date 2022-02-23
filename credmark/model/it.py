from credmark.types.dto import DTO
from .base import Model
import sys
import types
import inspect
from typing import Type, Union
from .errors import WrongModelMethodSignature

DICT_SCHEMA_JSON = '{"title": "Object", "type": "object", "properties": {}}'

# We could probably get the input and output DTOs from
# the run() method signature instead of passing them as params to
# the decorator but there may be reasons why they want to use
# different types and the DTOs are used to document the schema.


def it(slug: str,   # pylint: disable=locally-disabled, invalid-name
        version: str,
        tags: Union[list[str], None] = None,
        display_name: Union[str, None] = None,
        description: Union[str, None] = None,
        input: Union[Type[DTO], None] = None,
        output: Union[Type[DTO], None] = None):
    def wrapper(cls_in):
        def is_parent(child, parent):
            found = parent in child.__bases__
            return found or True in [is_parent(pp, parent) for pp in child.__bases__]

        if not is_parent(cls_in, Model):
            cls = type(cls_in.__name__, (Model, *cls_in.__bases__), dict(cls_in.__dict__))
        else:
            cls = cls_in

        attr_value = {
            'credmarkModelManifest': 'v1',
            'model': {
                'slug': slug,
                'version': version,
                'tags': tags,
                'display_name': display_name,
                'description': description,
                'input': input.schema_json() if input is not None and issubclass(input, DTO)
                else DICT_SCHEMA_JSON,
                'output': output.schema_json() if output is not None and issubclass(output, DTO)
                else DICT_SCHEMA_JSON,
                'class': cls.__dict__['__module__'] + '.' + cls.__name__
            }
        }

        attr_name = '_manifest'

        def get_attr(self, attr_name=attr_name):
            return getattr(self, '_' + attr_name)
        attr_prop = property(get_attr, None)
        setattr(cls, attr_name, attr_prop)
        setattr(cls, '_' + attr_name, attr_value)

        setattr(cls, 'slug', slug)
        setattr(cls, 'version', version)
        setattr(cls, 'inputDTO', input)
        setattr(cls, 'outputDTO', output)

        # Checks for the class
        # 1. it need to be inherited from Model class
        assert is_parent(cls, Model)

        # 2. has abstract functions as defined in the Model class
        method_list = [method for method in dir(Model)
                       if method.startswith('__') is False and
                       '__isabstractmethod__' in Model.__dict__[method].__dict__ and
                       Model.__dict__[method].__isabstractmethod__]

        for method in method_list:
            found_this_method = False
            for mro_cls in cls.__mro__:
                if method not in mro_cls.__dict__:
                    continue

                found_this_method = True

                # Since the run method is overloaded, the signatures won't match exactly.
                # TODO: Add parameter and return value type compatibility check
                break

            if not found_this_method:
                raise WrongModelMethodSignature(
                    f'Model {cls.__name__} misses a method {method}() with signature {inspect.signature(Model.__dict__[method])}')  # pylint: disable=line-too-long

        return cls

    return wrapper


class ModIt(types.ModuleType):
    def __init__(self):
        types.ModuleType.__init__(self, __name__)
        # or super().__init__(__name__) for Python 3
        self.__dict__.update(sys.modules[__name__].__dict__)

    def __call__(self, *args, **kwargs):
        return it(*args, *kwargs)

# sys.modules[__name__] = ModIt()
