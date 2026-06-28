"""
Lee los datos de los proyectos de Procomún desde un archivo YAML
y genera una página reStructuredText para Sphinx con todos los 
datos leídos.
"""

import os
import re
import jinja2
import yaml
import datetime

rst_file = 'procomun.rst'

rst_template = """:date: 2026-06-26
:modified: {{ modified }}
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

:no-search:


Recursos de Procomún
====================
`Procomún <https://procomun.intef.es/>`__
es una red y repositorio de Recursos Educativos Abiertos (REA)
impulsada por el Ministerio de Educación de España a través del INTEF.
Es un espacio colaborativo donde los docentes pueden buscar, descargar,
modificar y compartir materiales de enseñanza de acceso libre.


Recursos de Tecnología
----------------------

{% for r in recursos %}
#. `{{r['title']}}
   <{{r['url']}}>`__

   {{r['date']}} {{r['author']}}
{%- endfor %}

"""


def main():
    recursos_eso = read_yaml('procomun_eso.yaml')
    recursos_bach = read_yaml('procomun_bach.yaml')
    recursos = sort_list(recursos_eso + recursos_bach)
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    template = jinja2.Template(rst_template)
    result = template.render(recursos=recursos, modified=today)
    with open(rst_file, 'w', encoding='utf-8') as fo:
        fo.write(result)
    

def save_yaml(yaml_file, data):
    with open(yaml_file, 'w', encoding='utf-8') as fo:
        yaml.dump(data, fo, allow_unicode=True, sort_keys=False, default_flow_style=False)


def read_yaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as fi:
        data = yaml.safe_load(fi)
    return data


def sort_list(recursos_list):
    # Create index (date + id) and delete duplicates
    recursos_dict = {}
    for r in recursos_list:
        r_index = r['date'] + r['id']
        if r_index in recursos_dict:
            if not r['tags'] in recursos_dict[r_index]['tags']:
                recursos_dict[r_index]['tags'].append(r['tags'])
        else:
            recursos_dict[r_index] = r
            recursos_dict[r_index]['tags'] = [r['tags']]    
    # Sort
    keys = sorted(recursos_dict.keys(), reverse=True)
    recursos_sorted = [recursos_dict[i] for i in keys]
    return recursos_sorted


main()
