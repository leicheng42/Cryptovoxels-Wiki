import sphinx_rtd_theme
import myst_parser

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Voxels Wiki'
copyright = '2023, 雷电所 RaidenINST'
author = 'Lei Cheng'
release = '0.1'

master_doc = "index"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    # 'sphinx.ext.duration',
    # 'sphinx.ext.autosectionlabel',
    ]
# source_suffix = {'.rst': 'restructuredtext', '.txt': 'markdown', '.md': 'markdown',}

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/leicheng42/Cryptovoxels-Wiki",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_source_button": True,
    "home_page_in_toc": True,
    
}

html_logo = "imgs/logo.jpg"
html_title = "Voxels Wiki"
