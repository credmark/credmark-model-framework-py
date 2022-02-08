import logging
import os
from typing import Union, Type, List
from packaging import version
import yaml
from credmark.model import Model
from credmark.model.errors import MissingModelError


class ModelLoader:
    logger = logging.getLogger(__name__)

    def __init__(self, manifest_paths: Union[List[str], None] = None):
        '''
        manifest_paths is a list of paths to search for model manifest files.
        '''
        self.errors = []
        self.warnings = []

        # Map "name:version" to a model class
        self.__name_version_to_class_dict: dict[str, Type[Model]] = dict()

        # Map name to a sorted list of model versions
        self.__name_to_versions_dict: dict[str, List[version.Version]] = dict()

        self.__model_manifest_list: List[dict] = []

        if manifest_paths is not None:
            self._search_paths_for_manifest_files(manifest_paths)

    def clear(self):
        self.errors.clear()
        self.warnings.clear()
        self.__name_version_to_class_dict.clear()
        self.__name_to_versions_dict.clear()
        self.__model_manifest_list.clear()

    def log_errors(self):
        for e in self.errors:
            self.logger.error(e)
        for w in self.warnings:
            self.logger.warning(w)

    def has_errors_or_warnings(self):
        return len(self.errors) > 0 or len(self.warnings) > 0

    def loaded_model_versions(self):
        """Return a list of name:version strings of loaded models"""
        return list(self.__name_version_to_class_dict.keys())

    def loaded_model_version_lists(self):
        """Return a dict of model name to list of version strings"""
        return {k: [str(v) for v in vs] for k, vs in self.__name_to_versions_dict.items()}

    def loaded_model_manifests(self):
        return self.__model_manifest_list

    def _search_paths_for_manifest_files(self, paths: List[str]):
        for path in paths:
            self._search_path_for_manifest_files(path)

    def _search_path_for_manifest_files(self, path: str):
        if path.startswith('./'):
            path = path[2:]

        if os.path.isfile(path):
            if path.endswith('.yaml'):
                self._try_model_manifest(path)
        else:
            for root, _dirs, files in os.walk(path):
                for fname in files:
                    if fname.endswith('.yaml'):
                        self._try_model_manifest(os.path.join(root, fname))

    def _try_model_manifest(self, fpath: str):
        folder = os.path.dirname(fpath)
        try:
            manifest = self._load_yaml_file(fpath)
            if manifest is not None and 'credmark_model_manifest' in manifest:
                self._process_model_manifest(manifest, folder, fpath)
        except Exception as err:
            self.errors.append(
                f'Error loading manifest file {fpath}: {err}')

    def _load_yaml_file(self, path):
        with open(path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise Exception(f'Error loading yaml: {exc}')

    def _process_model_manifest(self, manifest, _root: str, fpath: str):
        models: list = manifest.get('models')

        if models is None:
            model = manifest.get('model')
            if model is not None:
                models = [model]

        if models is not None:
            for model in models:
                try:
                    self._process_model_manifest_entry(model)
                except Exception as err:
                    self.errors.append(
                        f'Error processing entry in manifest file {fpath}: {err}')

    def _process_model_manifest_entry(self, model_manifest):
        try:
            model_classname = model_manifest['class']
            model_name = model_manifest['name']
            # ensure version is a string
            model_version = model_manifest['version'] = str(
                model_manifest['version'])
        except KeyError as err:
            raise Exception(
                f'Missing field {err} for model {model_manifest.get("name", "<unknown>")}')

        mclass = None
        modulename, classname = model_classname = os.path.splitext(
            model_classname)
        if modulename and classname:
            mclass = self._load_module_class(modulename, classname[1:])
        else:
            raise Exception(
                f'Invalid model class "{model_classname}" for model {model_name}')

        if mclass is not None:
            mclass.name = model_name
            mclass.version = model_version
            self._add_model_class(mclass)
            self.__model_manifest_list.append(model_manifest)

    def _add_model_class(self, model_class: Type[Model]):
        name = model_class.name
        ver = model_class.version

        if name is None or ver is None:
            raise Exception(
                f'${model_class} must have name ({name}) and version ({ver}) set')

        try:
            pver = version.Version(ver)
        except version.InvalidVersion:
            raise Exception(f'${model_class} has invalid version ({ver})')

        name_ver = f'{name}:{ver}'
        if name_ver in self.__name_version_to_class_dict:
            raise Exception(
                f'Duplicate model name ({name}) and version ({ver}) found. Skipping duplicate.')

        self.logger.debug(f'Added model {name} {ver}')

        self.__name_version_to_class_dict[f'{name}:{ver}'] = model_class

        verlist = self.__name_to_versions_dict.get(name)
        if verlist is not None:
            verlist.append(pver)
            verlist.sort()
        else:
            self.__name_to_versions_dict[name] = [pver]

    def _load_module_class(self, modulename, name):
        """ Import a named object from a module in the context of this function.
        """
        try:
            module = __import__(modulename, globals(), locals(), [name])
            mclass = vars(module)[name]
        except (ImportError, KeyError) as err:
            raise Exception(
                f'Error importing class {name} from module {modulename}: {err}')
        return mclass

    def get_model_class(self, name: str, ver: Union[str, None], raise_on_not_found: bool = True):
        """Get a model class by name and optional version.

        Parameters:
            name (str): name of the model
            ver (str | None): [OPTIONAL] version of the model.
                    If None, the latest version is used.
            raise_on_not_found (bool): If true, raises an error if
                    model class not found. Default true.

        Returns:
            Model class.

        Raises:
            MissingModelError if model is not found if raise_on_not_found is True
        """
        model_class = None

        if not ver:
            # Get the latest version
            verlist = self.__name_to_versions_dict.get(name)
            if verlist is not None:
                ver = verlist[-1].public

        if ver:
            model_class = self.__name_version_to_class_dict.get(
                f'{name}:{ver}')

        if model_class is None and raise_on_not_found:
            err = MissingModelError(name, ver)
            self.logger.error(err)
            raise err

        return model_class
