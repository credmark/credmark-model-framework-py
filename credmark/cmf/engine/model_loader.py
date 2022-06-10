import logging
import os
import sys
import importlib
import importlib.util
import inspect
import json
from typing import Set, Union, Type, List
from packaging import version
from requests.structures import CaseInsensitiveDict
from credmark.cmf.model import Model
from credmark.cmf.engine.errors import ModelManifestWriteError
from credmark.cmf.model.errors import ModelNotFoundError
from credmark.cmf.model import validate_model_slug

# "Dev models" are models that are implemented on the server
# but we have a local version used for development (dev_mode).
# Typically they are models that call other models and they run
# locally so they can call other local-only models.

DEV_MODELS_PATHS = ['cmf/engine/dev_models/series_models.py',
                    'cmf/engine/dev_models/console.py']


class ModelLoader:
    logger = logging.getLogger(__name__)

    def __init__(self,
                 model_paths: Union[List[str], None] = None,
                 manifest_file: Union[str, None] = None,
                 load_dev_models=False):
        '''
        model_paths is a list of paths to search for model manifest files.
        '''
        self._model_paths = model_paths
        self._load_dev_models = load_dev_models

        if not isinstance(model_paths, list):
            raise Exception('model_paths needs to be a list of paths')

        self.errors = []
        self.warnings = []

        # Map "slug:version" to a model class
        self.__slug_version_to_class_dict: CaseInsensitiveDict[Type[Model]] = CaseInsensitiveDict(  # pylint: disable=line-too-long
        )

        # Map slug to a sorted list of model versions
        self.__slug_to_versions_dict: CaseInsensitiveDict[List[version.Version]] = CaseInsensitiveDict(  # pylint: disable=line-too-long
        )

        self.__model_manifest_list: List[dict] = []

        self.manifest_file = manifest_file

        self.__loading_dev_models = False
        self.__dev_model_slugs: Set[str] = set()

        if manifest_file is not None and os.path.isfile(manifest_file):
            self.logger.debug(f'Loading manifest from {manifest_file}')
            manifest = self._load_json_file(manifest_file)
            if manifest is not None and 'credmarkModelManifest' in manifest:
                self._process_model_manifest(manifest, None, None)
        else:
            if model_paths is not None:
                self.logger.debug(f'Loading manifest from model_paths: {model_paths}')
                self._search_paths_for_model_files(model_paths)

        if load_dev_models:  # pylint: disable=too-many-nested-blocks
            self.logger.debug('Loading dev models')
            cmf_spec = importlib.util.find_spec("credmark")
            if cmf_spec is not None:
                cmf_paths = cmf_spec.submodule_search_locations
                if cmf_paths is not None:
                    for dev_models_path in DEV_MODELS_PATHS:
                        for cmf_path in cmf_paths:
                            dev_model_fpath = os.path.join(cmf_path, dev_models_path)
                            if os.path.isfile(dev_model_fpath):
                                self.__loading_dev_models = True
                                self._try_model_module(cmf_path, dev_model_fpath)
                                self.__loading_dev_models = False
                                break

        self.__model_manifest_list.sort(key=lambda m: m['slug'])

    def reload(self):
        self.__init__(self._model_paths, self.manifest_file, self._load_dev_models)

    def clear(self):
        self.errors.clear()
        self.warnings.clear()
        self.__slug_version_to_class_dict.clear()
        self.__slug_to_versions_dict.clear()
        self.__model_manifest_list.clear()
        self.__dev_model_slugs.clear()

    def log_errors(self):
        for e in self.errors:
            self.logger.error(e)
        for w in self.warnings:
            self.logger.warning(w)

    def has_errors_or_warnings(self):
        return len(self.errors) > 0 or len(self.warnings) > 0

    def loaded_model_versions(self):
        """Return a list of slug:version strings of loaded models"""
        return list(self.__slug_version_to_class_dict.keys())

    def loaded_model_version_lists(self):
        """Return a dict of model slug to list of version strings"""
        return {k: [str(v) for v in vs] for k, vs in self.__slug_to_versions_dict.items()}

    def loaded_model_manifests(self):
        return self.__model_manifest_list

    def loaded_dev_model_slugs(self):
        return self.__dev_model_slugs

    def _search_paths_for_model_files(self, paths: List[str]):
        for path in paths:
            self._search_path_for_model_files(path)

    def _search_path_for_model_files(self, path: str):
        if path.startswith('./'):
            path = path[2:]

        if os.path.isfile(path):
            if path.endswith('.py'):
                self._try_model_module(os.path.dirname(path), path)
        else:
            for root, _dirs, files in os.walk(path):
                for fname in files:
                    if fname.endswith('.py'):
                        self._try_model_module(path, os.path.join(root, fname))

    def _load_module_with_path(self, base_path, fpath):
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        parent_path = os.path.abspath(os.path.join(base_path, '..'))
        add_path = False
        if parent_path not in sys.path:
            add_path = True
            sys.path.insert(0, parent_path)
        # fpath always ends with '.py'
        module_name = fpath[:-3].replace(parent_path + os.path.sep, '').replace('/', '.')
        spec = importlib.util.spec_from_file_location(module_name, fpath)
        if spec is None or spec.loader is None:
            raise Exception(f'Unable to load module from {fpath}')
        mod = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = mod
        spec.loader.exec_module(mod)
        if add_path:
            del sys.path[0]
        return module_name, mod

    def _try_model_module(self, base_path, fpath):
        module_name = ''
        try:
            module_name, mod = self._load_module_with_path(base_path, fpath)
            manifests = [v.__dict__['__manifest']
                         for k, v in mod.__dict__.items()
                         if inspect.isclass(v) and
                         '__manifest' in v.__dict__ and
                         'credmarkModelManifest' in v.__dict__['__manifest']]
            for manifest in manifests:
                self._process_model_manifest(manifest, base_path, fpath)
        except Exception as err:
            self.errors.append(
                f'Error loading manifest for module {module_name} in model file {fpath}: {err}')

    def _load_json_file(self, path):
        with open(path, "r") as stream:
            try:
                return json.load(stream)
            except Exception as exc:
                raise Exception(f'Error loading json manifest: {exc}')

    def _process_model_manifest(self, manifest, base_path, fpath):
        models: list = manifest.get('models')

        if models is None:
            model = manifest.get('model')
            if model is not None:
                models = [model]

        if models is not None:
            for model in models:
                try:
                    mclass = self._load_mclass(
                        model_manifest=model,
                        base_path=(model['class'].split('.')[0]
                                   if base_path is None else base_path),
                        fpath=(os.sep.join(model['class'].split('.')[:-1]) + '.py'
                               if fpath is None else fpath))
                    self._process_model_manifest_entry(model, mclass)
                except Exception as err:
                    self.errors.append(
                        f'Error processing entry in manifest file {fpath}: {err}')

    def _load_mclass(self, model_manifest, base_path, fpath):
        model_class = model_manifest['class']
        module_name, mod = self._load_module_with_path(base_path, fpath)
        mclass = vars(mod)[model_class.replace(module_name + '.', '')]

        return mclass

    def _process_model_manifest_entry(self, model_manifest, mclass):
        try:
            model_slug = model_manifest['slug']
            validate_model_slug(model_slug)
            # ensure version is a string
            _model_version = model_manifest['version'] = str(
                model_manifest['version'])
        except KeyError as err:
            raise Exception(
                f'Missing field {err} for model {model_manifest.get("slug", "<unknown>")}')

        if mclass is not None:
            self._add_model_class(mclass)
            self.__model_manifest_list.append(model_manifest)

    def add_model(self, model_class, replace=True):
        model_manifest = model_class.__dict__['__manifest']
        if 'credmarkModelManifest' not in model_manifest:
            raise Exception('credmarkModelManifest is missing')

        if replace:
            self.remove_model_by_slug(model_manifest['model']['slug'])
        self._process_model_manifest_entry(model_manifest['model'], model_class)

    def remove_model_by_slug(self, slug):
        keys_to_remove = [key for key in self.__slug_version_to_class_dict.keys()
                          if key.startswith(slug)]
        for key in keys_to_remove:
            del self.__slug_version_to_class_dict[key]

        if slug in self.__slug_to_versions_dict:
            self.__slug_to_versions_dict.pop(slug)

        for m in self.__model_manifest_list:
            if m['slug'] == slug:
                del m

    def _add_model_class(self, model_class: Type[Model]):
        slug = model_class.slug
        ver = model_class.version

        if slug is None or ver is None:
            raise Exception(
                f'${model_class} must have slug ({slug}) and version ({ver}) set')

        try:
            pver = version.Version(ver)
        except version.InvalidVersion:
            raise Exception(f'${model_class} has invalid version ({ver})')

        self._add_slug_version_model_class(slug, pver, model_class)

    def _add_slug_version_model_class(self,
                                      slug: str,
                                      ver: version.Version,
                                      model_class: Type[Model]):
        slug_ver = f'{slug}:{str(ver)}'

        existing_class = self.__slug_version_to_class_dict.get(slug_ver)
        if existing_class is not None and existing_class != model_class:
            raise Exception(
                f'Duplicate model slug ({slug}) and version ({ver}) found. Skipping duplicate.')

        self.logger.debug(
            f'Added {"dev " if self.__loading_dev_models else ""}model {slug} {str(ver)}')

        self.__slug_version_to_class_dict[slug_ver] = model_class

        verlist = self.__slug_to_versions_dict.get(slug)
        if verlist is not None:
            verlist.append(ver)
            verlist.sort()
        else:
            self.__slug_to_versions_dict[slug] = [ver]

        if self.__loading_dev_models:
            self.__dev_model_slugs.add(slug)

    def get_model_class(self, slug: str, ver: Union[str, None], raise_on_not_found: bool = True):
        """Get a model class by slug and optional version.

        Parameters:
            slug (str): slug of the model
            ver (str | None): [OPTIONAL] version of the model.
                    If None, the latest version is used.
            raise_on_not_found (bool): If true, raises an error if
                    model class not found. Default true.

        Returns:
            Model class.

        Raises:
            MissingModelError: if model is not found if raise_on_not_found is True
        """
        model_class = None

        if not ver:
            # Get the latest version
            verlist = self.__slug_to_versions_dict.get(slug)
            if verlist is not None:
                ver = verlist[-1].public

        if ver:
            model_class = self.__slug_version_to_class_dict.get(
                f'{slug}:{ver}')

        if model_class is None and raise_on_not_found:
            err = ModelNotFoundError.create(slug, ver)
            self.logger.error(err)
            raise err

        return model_class

    def write_manifest_file(self):
        manifest_file = self.manifest_file
        if manifest_file is None:
            return

        try:
            manifests = self.loaded_model_manifests()
            with open(manifest_file, 'w') as fp:
                try:
                    json.dump({'credmarkModelManifest': '1.0', 'models': manifests}, fp)
                    self.logger.info(f'Saved manifest to {manifest_file}')
                except:
                    err = ModelManifestWriteError(manifest_file)
                    self.logger.error(err)
                    raise err
        except Exception as err:
            self.logger.error(
                f'Error writing manifest file {manifest_file}: {err}')

    @classmethod
    def remove_manifest_file(cls, manifest_file):
        if manifest_file is None:
            return

        try:
            if os.path.isfile(manifest_file):
                os.remove(manifest_file)
                cls.logger.info(f'Removed manifest {manifest_file}')
        except Exception as err:
            cls.logger.error(
                f'Error removing manifest file {manifest_file}: {err}')
            raise err
