import io
from typing import Type, Union, overload, Optional

from credmark.dto import DTO, DTOType, DTOTypesTuple, EmptyInput

from .print import print_manifest_description

from credmark.cmf.model.errors import ModelInputError


class RunModelMethod:
    # This class is used interally by the context.

    # A run model method is callable (where the prefix is the actual
    # model name) or called with a method name (where prefix is the
    # dot prefix of the model name.)

    # If this is set to true for the class, the doc string
    # for an instance will be set to the model schema doc
    interactive_docs = False

    def __init__(self, context, prefix: str, block_number: Union[int, None] = None,
                 local: bool = False, input: Union[None, DTO] = None):
        self.__context = context
        self.__prefix = prefix
        self.__block_number = block_number
        self.__local = local
        self.__input = input

        if self.interactive_docs:
            # In interactive mode, we set the docstring to the
            # manifest doc for the model
            manifest = self.__context._model_manifests(True).get(prefix)
            if manifest is not None:
                doc = io.StringIO()
                print_manifest_description(manifest, doc)
                self.__doc__ = doc.getvalue()
                doc.close()
            else:
                slugs = [s for s in self.__context._model_manifests(True).keys()
                         if s.startswith(prefix)]
                slugs.sort()
                self.__doc__ = f'Run a model.\n\nAvailable models: {", ".join(slugs)}'

    # run a model. args can be a positional DTO or dict or kwargs
    @overload
    def __call__(self,
                 input: Union[DTOType, dict, None] = None,
                 return_type: Union[dict, None] = None,
                 version: Union[str, None] = None,
                 **kwargs) -> dict:
        ...

    @overload
    def __call__(self,
                 input: Union[DTOType, dict, None] = None,
                 return_type: Type[DTOType] = EmptyInput,
                 version: Union[str, None] = None,
                 **kwargs) -> DTOType:
        ...

    def __call__(self,
                 input: Union[DTOType, dict, None] = None,
                 return_type: Union[dict, Type[DTOType], None] = None,
                 version: Union[str, None] = None,
                 **kwargs) -> Union[dict, DTOType]:

        model_input = {}
        if self.__input is not None:
            if isinstance(self.__input, DTOTypesTuple):
                model_input = self.__input.dict()
            elif isinstance(self.__input, dict):
                model_input = self.__input

        if isinstance(input, DTOTypesTuple):
            input = model_input | input.dict() | kwargs
        elif isinstance(input, dict):
            input = model_input | input | kwargs
        elif input is not None:
            raise ModelInputError(
                f'You shall not send non-DTO/non-dict ({input=}) as input to model.')
        else:
            input = model_input | kwargs

        return self.__context.run_model(
            f"{self.__prefix.replace('_', '-')}",
            input,
            block_number=self.__block_number,
            version=version,
            return_type=return_type,
            local=self.__local)

    # Handle method calls where the prefix is the dot prefix of a model name
    def __getattr__(self, __name: str):
        if self.interactive_docs:
            model_manifests: dict = self.__context._model_manifests(True)
            # If prefix matches a complete slug we allow access to
            # manifest fields and model class properties.
            if self.__prefix in model_manifests:
                if __name in model_manifests[self.__prefix]:
                    return model_manifests[self.__prefix][__name]
                else:
                    # mclass = self.__context._class_for_model(self.__prefix.replace('_', '-'))
                    mclass = model_manifests[self.__prefix.replace('_', '-')]['mclass']
                    if mclass is not None:
                        mclassdict = vars(mclass)
                        if __name in mclassdict:
                            return mclassdict[__name]

        return RunModelMethod(
            self.__context,
            f"{self.__prefix}.{__name}",
            block_number=self.__block_number,
            local=self.__local,
            input=self.__input)

    def __dir__(self):
        if self.interactive_docs:
            # For ipython tab-complete
            model_manifests: dict = self.__context._model_manifests(True)

            if self.__prefix in model_manifests:
                # mclass = self.__context._class_for_model(self.__prefix.replace('_', '-'))
                mclass = model_manifests[self.__prefix.replace('_', '-')]['mclass']
                fields = list(model_manifests[self.__prefix].keys())
                if mclass is not None:
                    # allow autocomplete for some model class properties
                    fields.extend(['inputDTO', 'outputDTO'])
                fields.sort()
                return fields

            prefix = self.__prefix + '.'
            prefix_len = len(prefix)
            slugs = [s[prefix_len:]
                     for s in self.__context._model_manifests(True).keys() if s.startswith(prefix)]
            slugs.sort()
            return slugs
        else:
            return super().__dir__()


class Models:
    """
    """

    def __init__(self, context, block_number: Union[int, None] = None, local: bool = False,
                 input: Union[None, DTO] = None):
        self.__context = context
        self.__block_number = block_number
        self.__local = local
        self.__input = input

    def __getattr__(self, __name: str) -> RunModelMethod:
        return RunModelMethod(self.__context, __name, block_number=self.__block_number,
                              local=self.__local, input=self.__input)

    def __call__(self, block_number=None, local: bool = False, slug: Optional[str] = None):
        if slug:
            return RunModelMethod(self.__context, slug, block_number=self.__block_number,
                                  local=self.__local, input=self.__input)
        else:
            return self.__class__(self.__context, block_number=block_number, local=local,
                                  input=self.__input)

    def __dir__(self):
        if RunModelMethod.interactive_docs:
            # For ipython tab-complete
            slugs = [k for k, v in self.__context._model_manifests(True).items()
                     if self.__input is None or isinstance(self.__input, v['mclass'].inputDTO)]
            slugs.sort()
            return slugs
        else:
            return super().__dir__()

    def reload(self):
        if RunModelMethod.interactive_docs:
            self.__context._model_reload()  # pylint: disable=protected-access
