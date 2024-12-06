import os
import sys
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))
import sphinx_rtd_theme
project = 'Sphinx-Tutorial'
copyright = '2020, Sooftware'
author = 'Sooftware'
version = ''
release = '0.0'
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    "sphinx_rtd_theme",
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'recommonmark'
]
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'Sphinx-Tutorialdoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'Sphinx-Tutorial.tex', 'Sphinx-Tutorial Documentation',
     'Sooftware', 'manual'),
]
man_pages = [
    (master_doc, 'sphinx-tutorial', 'Sphinx-Tutorial Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'Sphinx-Tutorial', 'Sphinx-Tutorial Documentation',
     author, 'Sphinx-Tutorial', 'One line description of project.',
     'Miscellaneous'),
]
epub_title = project
epub_exclude_files = ['search.html']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', 'https://docs.python.org/3/objects.inv'),
}
todo_include_todos = True