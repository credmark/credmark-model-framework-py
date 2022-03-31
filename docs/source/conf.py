# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Source code dir relative to this file
sys.path.insert(1, os.path.abspath('../ext'))  # Source code dir relative to this file

project = 'Credmark Model Framework'
copyright = '2022, Credmark'
author = 'Credmark'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    # We use credmark_autosummary instead of sphinx.ext.autosummary
    # 'sphinx.ext.autosummary',
    'credmark_autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    # 'sphinx_autodoc_typehints', # causes problems with pydantic and forward refs
    'sphinx.ext.napoleon',
    'sphinxcontrib.autodoc_pydantic',
    'myst_parser',
]

myst_enable_extensions = [
    'deflist',
    'colon_fence',
]

autosummary_generate = True  # Set to True to generate new rst files.
autosummary_imported_members = False

# "class" shows class doc only, "both" will Add __init__ doc (ie. params) to class summaries
autoclass_content = "class"
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)
autodoc_inherit_docstrings = False  # If no docstring, inherit from base class
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints
autodoc_typehints = "description"  # Sphinx-native method. Not as good as sphinx_autodoc_typehints
add_module_names = False  # Remove namespaces from class/method signatures

autodoc_pydantic_model_show_json = True
autodoc_pydantic_field_doc_policy = 'both'  # 'docstring' | 'description' | 'both'
autodoc_pydantic_model_hide_paramlist = False
autodoc_pydantic_model_signature_prefix = 'DTO class'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 10,  # sidebar maxdepth, -1 infinite
    'includehidden': False,  # default is True

}

html_css_files = ["readthedocs-custom.css"]  # Override some CSS settings

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'
