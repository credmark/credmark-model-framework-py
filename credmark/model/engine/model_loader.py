import logging
import os
import re
from typing import Union, Type, List
from packaging import version
import yaml
from credmark.model import Model
from credmark.model.errors import MissingModelError
from requests.structures import CaseInsensitiveDict


class ModelLoader:
    logger = logging.getLogger(__name__)

    max_slug_length = 64
    model_slug_re = re.compile(r'^([A-Za-z0-9]+\-)*[A-Za-z0-9]+$')

    def validate_model_slug(self, slug: str):
        if self.model_slug_re.match(slug) is None or len(slug) > self.max_slug_length:
            raise Exception(
                f'Invalid model slug "{slug}". '
                'Slugs must start and end with a letter or number and may contain hyphens.')
        if len(slug) > self.max_slug_length:
            raise Exception(
                f'Invalid model slug "{slug}". '
                'Slugs must be not more than {self.max_slug_length} characters.')

    def __init__(self, manifest_paths: Union[List[str], None] = None):
        '''
        manifest_paths is a list of paths to search for model manifest files.
        '''
        self.errors = []
        self.warnings = []

        # Map "slug:version" to a model class
        self.__slug_version_to_class_dict: CaseInsensitiveDict[Type[Model]] = CaseInsensitiveDict()

        # Map slug to a sorted list of model versions
        self.__slug_to_versions_dict: CaseInsensitiveDict[List[version.Version]] = CaseInsensitiveDict(
        )

        self.__model_manifest_list: List[dict] = []

        if manifest_paths is not None:
            self._search_paths_for_manifest_files(manifest_paths)

    def clear(self):
        self.errors.clear()
        self.warnings.clear()
        self.__slug_version_to_class_dict.clear()
        self.__slug_to_versions_dict.clear()
        self.__model_manifest_list.clear()

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
            if manifest is not None and 'credmarkModelManifest' in manifest:
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
            model_slug = model_manifest['slug']
            self.validate_model_slug(model_slug)
            model_classname = model_manifest['class']
            # ensure version is a string
            model_version = model_manifest['version'] = str(
                model_manifest['version'])
        except KeyError as err:
            raise Exception(
                f'Missing field {err} for model {model_manifest.get("slug", "<unknown>")}')

        mclass = None
        modulename, classname = model_classname = os.path.splitext(
            model_classname)
        if modulename and classname:
            mclass = self._load_module_class(modulename, classname[1:])
        else:
            raise Exception(
                f'Invalid model class "{model_classname}" for model {model_slug}')

        if mclass is not None:
            mclass.slug = model_slug
            mclass.version = model_version
            self._add_model_class(mclass)
            self.__model_manifest_list.append(model_manifest)

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

        slug_ver = f'{slug}:{ver}'
        if slug_ver in self.__slug_version_to_class_dict:
            raise Exception(
                f'Duplicate model slug ({slug}) and version ({ver}) found. Skipping duplicate.')

        self.logger.debug(f'Added model {slug} {ver}')

        self.__slug_version_to_class_dict[f'{slug}:{ver}'] = model_class

        verlist = self.__slug_to_versions_dict.get(slug)
        if verlist is not None:
            verlist.append(pver)
            verlist.sort()
        else:
            self.__slug_to_versions_dict[slug] = [pver]

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
            MissingModelError if model is not found if raise_on_not_found is True
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
            err = MissingModelError(slug, ver)
            self.logger.error(err)
            raise err

        return model_class
