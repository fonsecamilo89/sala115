# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'aula115'
copyright = '2026, Camilo Fonseca'
author = 'Camilo Fonseca'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_design"]

myst_enable_extensions = [
    "dollarmath", #ecuaciones matematicas con $
    "tasklist", # listas con casillas de verificacion
    "colon_fence", #bloques con ::: en vez de ```
    "attrs_inline", # para agregar atributos en linea ejemplo: IMAGENES
    "smartquotes", #comillas inteligentes
    "fieldlist" # listas de campos
]

myst_number_code_blocks = ["python"] # Numera bloques de código en los lenguajes especificados
myst_links_external_new_tab = True # Abre enlaces externos en una nueva pestaña
myst_enable_checkboxes = True # Habilita casillas de verificación en las listas de tareas
myst_heading_anchors = 3 # Genera enlaces ancla para los encabezados (niveles 1 a 3)

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for LaTeX output ------------------------------------------------

latex_engine = "lualatex"
latex_logo = "./_static/logo_light.png"
latex_documents = [
    ('index', 'aula115.tex', 'Libro didáctico para el estudiante', 'Julian Camilo Fonseca Romero', 'manual'),
]
text_add_secnumbers = False
latex_use_latex_multicolumn = True
latex_table_style = ['borderless', 'colorrows']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'
html_static_path = ['_static']
html_title = "aula 115"
# html_logo = './_static/logo_light.png'
html_css_files = [
    "css/custom.css",
]

pygments_style = "sphinx"
pygments_dark_style = "monokai"

html_theme_options = {
    "light_logo": "logo_light.png",
    "dark_logo": "logo_dark.png",
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-guilabel-text": "#FF0000",
        "color-brand-primary": "#265787",
        "sidebar-caption-font-size": "var(--font-size--normal)",
        "toc-font-size": "var(--font-size--small)",
        "admonition-font-size": "0.858rem"
    },
}

# html_theme_options = {
#     'logo_only': True,
# }

# html_theme_options = {
#     # if we have a html_logo below, this shows /only/ the logo with no title text
#     "logo_only": True,
#     # Collapse navigation (False makes it tree-like)
#     "collapse_navigation": False,
#     # Remove version and language picker beneath the title
#     "version_selector": False,
#     "language_selector": False,
#     'sticky_navigation': False
# }