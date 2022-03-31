# credmark_autosummary

`credmark_autosummary` is a modified version of the Sphinx ext `sphinx.ext.autosummary`.

Specifically, it adds support for pydantic models and is used in combination with `autodoc_pydantic`.

It uses all the same settings as `sphinx.ext.autosummary` so it's a drop-in replacement. It simply adds support for `pydantic_models` and `pydantic_settings` lists in module templates.

To use it, replace `'sphinx.ext.autosummary'` in your `conf.py` `extensions` with `'credmark_autosummary'` and make sure the `credmark_autosummary` is in your python path.
