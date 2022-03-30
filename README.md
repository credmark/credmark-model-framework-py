# credmark-model-framework-py

This repo contains the code for the `credmark-model-framework` python package.

For a Quickstart guide and a detailed description of all components, see the instructions [here](https://github.com/credmark/credmark-models-py/blob/main/README.md).

## Install

```
pip install git+https://github.com/credmark/credmark-model-framework-py.git@main
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

### Details

The docs are using sphinx with the `autosummary` extension.
This automatically generates docs for the files in the package and puts the generated files in `docs/source/reference`. This folder is not stored in git.

Note that it currently doesn't seem to crawl folders that are namespace modules (ie folders without a `__init__.py` file.)
