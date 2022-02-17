from .base import Model

import sys
import types
import inspect
from typing import Union
from .errors import WrongModelMethodSignature

def it(slug: str,
        version: str,
        display_name: Union[str, None] = None,
        description: Union[str, None] = None):
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
                    'display_name': display_name,
                    'description': description,
                    'class': cls.__dict__['__module__'] + '.' + cls.__name__
                }
            }

            attr_name = '_manifest'
            def get_attr(self, attr_name = attr_name):
                return getattr(self, '_' + attr_name)
            attr_prop = property(get_attr, None)                
            setattr(cls, attr_name, attr_prop)
            setattr(cls, '_' + attr_name, attr_value)
            
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
                    try:
                        assert inspect.signature(Model.__dict__[method]) == inspect.signature(
                            mro_cls.__dict__[method])
                        break
                    except:
                        if mro_cls == cls:
                            msg = (f'Model {cls.__name__} does not define method '
                                   f'{method}{inspect.signature(cls.__dict__[method])} with '
                                   f'signature {inspect.signature(Model.__dict__[method])}')
                        else:
                            msg = (f'Model\'s parent {mro_cls.__name__} does not define '
                                   f'method {method}{inspect.signature(mro_cls.__dict__[method])} with '
                                   f'signature {inspect.signature(Model.__dict__[method])}')
                        raise WrongModelMethodSignature(msg)

                if not found_this_method:
                    raise WrongModelMethodSignature(
                        f'Model {cls.__name__} misses a method {method}() with signature {inspect.signature(Model.__dict__[method])}')

            return cls

        return wrapper

class ModIt(types.ModuleType):
    def __init__(self):
        types.ModuleType.__init__(self, __name__)
        # or super().__init__(__name__) for Python 3
        self.__dict__.update(sys.modules[__name__].__dict__)

    def __call__(self,
                 slug: str,
                 version: str,
                 display_name: Union[str, None] = None,
                 description: Union[str, None] = None):
    
        return it(slug, version, display_name, description)

# sys.modules[__name__] = ModIt()
