# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'bwForCluster NEMO'
copyright = '2021, eScience, Rechenzentrum, Albert-Ludwigs-Universität Freiburg'
author = 'Michael Janczyk (MJ), Jan Leendertse (JL), Dirk von Suchodoletz (DvS), Bernd Wiebelt (BW)'

# The full version, including alpha/beta/rc tags
release = '0.4.0'
version = '0.4.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'pydata_sphinx_theme',
    'sphinx_book_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_favicon = 'img/nemo-favicon.png'
html_logo = 'img/nemo-logo.png'
html_title = 'bwForCluster NEMO'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML sidebars
html_sidebars = {
    "**": ["my-sidebar-logo.html",
           "search-field.html",
           "my-sidebar-nav.html",
           "sbt-sidebar-footer.html"]
}

# Theme options
html_theme_options = {
    "repository_url": "https://github.com/nemo-cluster/nemo-docs",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "toc_title": "Inhalt",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_download_button": True,
}
