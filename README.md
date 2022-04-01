# credmark-model-framework-py

This repo contains the code for the `credmark-model-framework` python package.

For a Quickstart guide and a detailed description of all components, see the instructions [here](https://github.com/credmark/credmark-models-py/blob/main/README.md).

## Install

```
pip install git+https://github.com/credmark/credmark-model-framework-py.git@main
```

## Releasing a Version

- Update the version in `setup.py`, update `HISTORY.rst`, and git commit the changes.

- Tag in git, replacing the version string:

```bash
git tag -a "0.1.0" -m "Version 0.1.0"
git push origin "0.1.0"
```

## Build During Development

```
python setup.py sdist
```

## Tests

Run tests with:

```
python -m unittest discover tests
```

## Docs

You can run docs locally.

- Create a virtual env

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install packages:

```bash
pip install -r requirements.txt
pip install -r docs/requirements.txt
pip install sphinx-rtd-theme
```

- Build docs

```bash
cd docs
make html
```

- View docs

Open `docs/build/html/index.html` in a browser

### Editing Docs

Sphinx is configured to use markdown or rst. The files are in `docs/source`. Nothing in the `docs/source/reference` folder should be edited since it's auto-generated. New md/rst files can be added to the source folder and then referenced in the `index.md` toctree.

The napoleon extension is installed so you can use the Google style docstrings described at [https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html).

### Details

#### credmark_autosummary

The docs are using sphinx with the `credmark_autosummary` extension. This is a modified version of `sphinx.ext.autosummary`. It is used to automatically generate reference docs for the files in the package.

Unfortunately `sphinx.ext.autosummary` has some issues:

- It currently doesn't seem to crawl folders that are namespace modules (ie folders without a `__init__.py` file.) This isn't really a problem right now and in fact, we use it to avoid generating docs for the `engine` folder.

- It doesn't work well with `sphinxcontrib.autodoc_pydantic` which is another extension we use for pydantic BaseModel subclasses. The `credmark_autosummary` extension handles the pydantic object types properly.

- Doesn't have fine control over showing/hiding superclass methods and attributes in a class.

#### Pydantic Generics

The `autodoc_pydantic` doesn't seem to handle models with generics properly so building the docs will generate many warnings (and some errors `Content block expected for the "raw" directive; none found`) related to generic DTOs. The docs for specific generic types won't be generated but they will be listed in the module DTO list.

#### Custom Templates

We also use custom autosummary templates that use the `toctree` so the full module tree is navigable.

The templates are based on https://github.com/sphinx-doc/sphinx/issues/7912 extended for pydantic_model types.
