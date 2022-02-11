from typing import Union
import inspect
# from functools import wraps

from .base import Model
from .errors import WriteModelManifestError, WrongModelMethodSignature

# TODO:
# 1. dectorator uses doc string to retrive manifests, instead of passing attributes via function


def manifest_v1(slug: str,
                version=Union[str, None],
                display_name=Union[str, None],
                description=Union[str, None]):

    def wrapper(cls):
        attr_value = {
            'credmarkModelManifest': 'v1',
            'model': {
                'slug': slug,
                'version': version,
                'display_name': display_name,
                'description': description,
                'class': cls.__dict__['__module__'] + '.' + cls.__name__
            }
        }

        attr_name = '_manifest'

        def getAttr(self, attr_name=attr_name):
            return getattr(self, '_' + attr_name)

        def setAttr(self, _value, attr_name=attr_name):
            raise WriteModelManifestError(f'Model {attr_name} is read-only')
        prop = property(getAttr, setAttr)
        setattr(cls, attr_name, prop)
        setattr(cls, '_' + attr_name, attr_value)

        # Checks for the class
        # 1. it need to be inherited from Model class
        def is_parent(child, parent):
            found = parent in child.__bases__
            if found:
                return True
            else:
                return True in [is_parent(pp, parent) for pp in child.__bases__]
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
                else:
                    found_this_method = True
                    try:
                        assert inspect.signature(Model.__dict__[method]) == inspect.signature(
                            mro_cls.__dict__[method])
                    except:
                        if mro_cls == cls:
                            raise WrongModelMethodSignature(
                                f'Model {cls.__name__} does not define method {method}{inspect.signature(cls.__dict__[method])} with signature {inspect.signature(Model.__dict__[method])}')
                        else:
                            raise WrongModelMethodSignature(
                                f'Model\'s parent {mro_cls.__name__} does not define method {method}{inspect.signature(mro_cls.__dict__[method])} with signature {inspect.signature(Model.__dict__[method])}')
                    break
            if not found_this_method:
                raise WrongModelMethodSignature(
                    f'Model {cls.__name__} misses a method {method}() with signature {inspect.signature(Model.__dict__[method])}')

        return cls

    return wrapper
