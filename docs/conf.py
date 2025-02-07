# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Incase the project was not installed
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import teachopencadd
import sphinx_material

from datetime import datetime

# -- Project information -----------------------------------------------------

project = "TeachOpenCADD"
copyright = (
    f"2018-{datetime.now().year}, Volkamer Lab. Project structure based on the "
    "Computational Molecular Science Python Cookiecutter version 1.1"
)
author = "Volkamer Lab"

# The short X.Y version
version = teachopencadd.__version__.split("+")[0]
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx_material",
    "nbsphinx",
    "nbsphinx_link",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

autosummary_generate = True
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"
nbsphinx_codecell_lexer = "python"
highlight_language = "none"

# -- Options for HTML output -------------------------------------------------
# -- HTML theme settings ------------------------------------------------
html_short_title = "TeachOpenCADD"
html_show_sourcelink = True
html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}

html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"

# material theme options (see theme.conf for more information)
html_theme_options = {
    # "base_url": "http://bashtage.github.io/sphinx-material/",
    "repo_url": "https://github.com/volkamerlab/teachopencadd/",
    "repo_name": "TeachOpenCADD",
    "google_analytics_account": "G-Q6ZE82CNZB",
    "html_minify": False,
    "html_prettify": False,
    "css_minify": False,
    "logo_icon": "school",
    "repo_type": "github",
    "globaltoc_depth": 2,
    "color_primary": "teal",
    "color_accent": "cyan",
    "touch_icon": "images/apple-icon-152x152.png",
    "theme_color": "#2196f3",
    "master_doc": False,
    # "nav_title": "TeachOpenCADD",
    "nav_links": [
        {"href": "talktorials", "internal": True, "title": "Our talktorials"},
        {"href": "installing", "internal": True, "title": "Run locally"},
        {"href": "contribute", "internal": True, "title": "Development"},
        {"href": "contact", "internal": True, "title": "Contact"},
        {"href": "citation", "internal": True, "title": "Citation"},
        # {
        #     "href": "https://squidfunk.github.io/mkdocs-material/",
        #     "internal": False,
        #     "title": "Material for MkDocs",
        # },
    ],
    "heroes": {
        "index": "A teaching platform for computer-aided drug design",
        "customization": "Configuration options to personalize your site.",
    },
    "version_dropdown": False,
    # "version_json": "_static/versions.json",
    # "version_info": {
    #     "Release": "https://bashtage.github.io/sphinx-material/",
    #     "Development": "https://bashtage.github.io/sphinx-material/devel/",
    #     "Release (rel)": "/sphinx-material/",
    #     "Development (rel)": "/sphinx-material/devel/",
    # },
    "table_classes": ["plain"],
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "teachopencadddoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "teachopencadd.tex",
        "TeachOpenCADD Documentation",
        "teachopencadd",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "teachopencadd", "TeachOpenCADD Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "teachopencadd",
        "TeachOpenCADD Documentation",
        author,
        "teachopencadd",
        "A teaching platform for computer-aided drug design",
        "Miscellaneous",
    ),
]


# -- Extension configuration -------------------------------------------------

html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]
html_js_files = []


# -- Extension for opengraph -------------------------------------------------

ogp_site_url = "https://projects.volkamerlab.org/teachopencadd/"
ogp_image = "https://raw.githubusercontent.com/volkamerlab/teachopencadd/master/docs/_static/images/TeachOpenCADD_topics.png"
ogp_description_length = 300
ogp_type = "website"
