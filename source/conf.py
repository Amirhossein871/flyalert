import sys
import os

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../flyalert"))

project = 'FlyAlert'
copyright = '2025, Amirhossein Bohlouli'
author = 'Amirhossein Bohlouli'
release = '1.0.0'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme"
]
html_theme = "sphinx_rtd_theme"

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']
