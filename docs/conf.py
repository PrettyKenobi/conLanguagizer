# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# on_rtd = os.environ.get('READTHEDOCS') == 'True'
# if on_rtd:
#     plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
# else:
#     cwd = os.getcwd()
#     plantuml = 'java -jar %s' % os.path.join(cwd, "utils/plantuml_beta.jar")

# # If we are running on windows, we need to manipulate the path,
# # otherwise plantuml will have problems.
# if os.name == "nt":
#     plantuml = plantuml.replace("/", "\\")
#     plantuml = plantuml.replace("\\", "\\\\")

# plantuml_output_format = 'png'


# -- Project information -----------------------------------------------------

project = 'conLanguagizer'
copyright = '2020, Ken Bonnstetter'
author = 'Ken Bonnstetter'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx_js' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Suffix(es) for source file names
source_suffix = ['.rst', '.md']

# Which version of sphinx to use
needs_sphinx = '3.1'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nature'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Other options ----------------------------------------------------------

primary_domain = 'js'

rst_prolog = """
.. |cla| replace:: ClangBook
"""
