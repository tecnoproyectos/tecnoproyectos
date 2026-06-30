# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import time
import re
import json

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tecno Proyectos'
author = 'Equipo de Tecno Proyectos'
copyright = '%s, %s' % (time.strftime("%Y"), author)
release = time.strftime("%Y")
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.imgmath',
]

imgmath_font_size = 18
imgmath_image_format = 'svg'
imgmath_dvisvgm_args = ['--no-fonts', '--bbox=2pt']

source_suffix = {'.rst': 'restructuredtext'}
source_encoding = 'utf-8-sig'
master_doc = 'content'
exclude_patterns = []

numfig = True
numfig_format = {
    'figure': 'Figura %s',
    'table': 'Tabla %s',
    'code-block': 'Código %s',
}    

templates_path = ['_templates']
html_additional_pages = {
    'index': 'index.html',
}


language = 'es'
locale_dirs = ['../locale/']
gettext_compact = False
figure_language_filename = "{path}/{basename}.{language}{ext}"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_show_sphinx = False
html_title = project

html_context = {
    'metatags': ('<link rel="icon" sizes="192x192" href="_static/favicon-192.png" type="image/png">')
}

html_logo = '_static/favicon.png'

html_extra_path = ['_custom/extra']

html_static_path = ['_static']

html_favicon = '_custom/extra/favicon.ico'

html_theme = 'furo'
html_theme_options = {
}


#
# Add open-in-new-tab links in Sphinx HTML writer
# from: https://stackoverflow.com/questions/25583581/add-open-in-new-tab-links-in-sphinx-restructuredtext
#
from sphinx.writers.html import HTMLTranslator
from docutils import nodes
from docutils.nodes import Element

class PatchedHTMLTranslator(HTMLTranslator):

    def visit_reference(self, node: Element) -> None:
        atts = {'class': 'reference'}
        if node.get('internal') or 'refuri' not in node:
            atts['class'] += ' internal'
        else:
            atts['class'] += ' external'
            # ---------------------------------------------------------
            # Customize behavior (open in new tab, secure linking site)
            atts['target'] = '_blank'
            atts['rel'] = 'noopener noreferrer'
            # ---------------------------------------------------------
        if 'refuri' in node:
            atts['href'] = node['refuri'] or '#'
            if self.settings.cloak_email_addresses and atts['href'].startswith('mailto:'):
                atts['href'] = self.cloak_mailto(atts['href'])
                self.in_mailto = True
        else:
            assert 'refid' in node, \
                   'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts['class'] += ' image-reference'
        if 'reftitle' in node:
            atts['title'] = node['reftitle']
        if 'target' in node:
            atts['target'] = node['target']
        self.body.append(self.starttag(node, 'a', '', **atts))

        if node.get('secnumber'):
            self.body.append(('%s' + self.secnumber_suffix) %
                             '.'.join(map(str, node['secnumber'])))

#
# Add reStructuredText meta tags in Sphinx HTML JSON-LD
#
def add_rst_meta_tags(app, pagename, templatename, context, doctree):
    # 1. Obtener autor global    
    global_author = app.config.author
    
    # 2. Intentar obtener metadatos de varias fuentes (compatibilidad con traducciones)
    rst_meta = context.get('meta') or {}
    
    # Si viene de una traducción, a veces los metadatos están en las propiedades del documento
    if not rst_meta and app.env and pagename in app.env.metadata:
        rst_meta = app.env.metadata[pagename]

    # 3. Buscar el autor (insensible a mayúsculas/minúsculas por si la traducción cambia la clave)
    meta_author = global_author
    for key, value in rst_meta.items():
        if key.lower() == 'author':
            meta_author = value
            break
 
    # 4. Estructurar los datos de Schema
    raw_title = context.get('title', 'Picuino')
    clean_title = re.sub(r'<[^>]*>', '', raw_title)
    canonical_url = 'https://tecnoproyectos.github.io/' + pagename + '.html'
    schema_data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": clean_title,
        "author": {
            "@type": "Person",
            "name": meta_author,
        },
        "publisher": {
            "@type": "Organization",
            "name": "Tecno Proyectos",
            "url": "https://tecnoproyectos.github.io/",
            "logo": {
                "@type": "ImageObject",
                "url": "https://tecnoproyectos.github.io/favicon-192.png",
            }
        },
        "mainEntityOfPage": canonical_url,
    }

    # 5. Inyectar etiquetas <meta> para HTML
    if 'license_url' in rst_meta:
        schema_data["license"] = rst_meta.get("license_url") 

    if 'image' in rst_meta:
        schema_data["image"] = [ 'https://tecnoproyectos.github.io/_images/' + rst_meta.get("image") ] 

    creation_year = ''

    if 'date' in rst_meta:
        published_date = rst_meta.get("date") + 'T12:00:00+01:00'
        schema_data["datePublished"] = published_date
        context['metatags'] += f'<meta property="article:published_time" content="{published_date}" />\n'
        creation_year = rst_meta.get("date").split('-')[0].strip()

    if 'modified' in rst_meta:
        modified_date = rst_meta.get('modified') + 'T12:00:00+01:00'
        schema_data["dateModified"] = modified_date
        context['metatags'] += f'<meta property="article:modified_time" content="{modified_date}" />\n'

        modified_year = rst_meta.get("modified").split('-')[0].strip()
        if creation_year and creation_year != modified_year:
            creation_year = creation_year + '-' + modified_year
    
    # Inyectar el script en los metatags de la página
    schema_script = f"\n<script type=\"application/ld+json\">\n{json.dumps(schema_data, indent=2, ensure_ascii=False)}\n</script>\n"
    if 'metatags' in context:
        context['metatags'] += schema_script
    else:
        context['metatags'] = schema_script

    if creation_year:
        context['meta']['creation_year'] = creation_year


# Conectar las funciones al evento
def setup(app):
    app.set_translator('html', PatchedHTMLTranslator)
    app.connect('html-page-context', add_rst_meta_tags)
    app.add_css_file('custom.css')
