import sys
import os

this_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(this_dir, "_ext"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.extlinks",
    "gmadocs",
    "jsapi",
]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["css/extra.css"]

exclude_patterns = [
    "_build/**",
    ".sphinx-build/**",
    "_templates/**",
    "_ext/**",
    "README.rst",
]

extlinks = {
    "glge": ("http://www.glge.org/api-docs/?url=/symbols/GLGE.%s.html", "GLGE.")
}

master_doc = "index"
source_suffix = ".rst"
smart_quotes = True

pygments_style = "pastie"

copyright = "2019, delfick"
project = "GammaJS"

version = "0.1"
release = "0.1"
