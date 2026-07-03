"""
Convierte el listado de todos los archivos PDF de este directorio
en una tabla de reStructuredText
"""

import os
import re
from operator import itemgetter


table_header = ''':date: 2026-07-03
:modified: 2026-07-03
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Exámenes PAU
============
Exámenes de las Pruebas de Acceso a la Universidad de las materias
de Bachillerato relacionadas con Tecnología.


.. list-table:: Exámenes PAU
   :header-rows: 1
   :widths: 15 15 80
   :align: left

   * - Comunidad
     - Curso
     - Materia - Examen
'''


comunidades = [
   ['andalucia',     'Andalucía'],
   ['aragon',        'Aragón'],
   ['asturias',      'Asturias'],
   ['baleares',      'Baleares'],
   ['canarias',      'Canarias'],
   ['Cantabria',     'Cantabria'],
   ['castillalamancha', 'Castilla la Mancha'],
   ['castillayleon', 'Castilla y León'],
   ['catalunya',     'Cataluña'],
   ['catalunya',     'Cataluña'],
   ['valencia',      'Comunidad Valenciana'],
   ['extremadura',   'Extremadura'],
   ['galicia',       'Galicia'],
   ['madrid',        'Madrid'],
   ['murcia',        'Murcia'],
   ['navarra',       'Navarra'],
   ['paisvasco',     'País Vasco'],
   ['rioja',         'Rioja'],
   ]


materias = [
    ['tein', 'Tecnología e Ingeniería II'],
    ]


tipo_examenes = [
    ['extra', 'Extraordinaria'],
    ['modelo', 'Modelo'],
    ['ordinaria', 'Ordinaria'],
    ['coincide', 'Coincidentes'],
    ['solucion', 'Soluciones'],
    ]


def main():
    table = [table_header]
    file_names = read_file_names('../../../static/pau')
    database = extract_fields(file_names)
    database_sort(database, [
                  ['comunidad', False],
                  ['materia', False],
                  ['curso', True],
                  ['examen', False],                  
                  ])
    content = render_table(database)
    write_file('index.rst', content)
    input('Press Enter')


def render_table(database):
    table = [table_header]
    for f in database:
        table.append(f"   * - { f['comunidad'] }\n" +
           f"     - { f['curso'] }\n" +
           f"     - `{ f['materia'] } - { f['examen'] }\n" +
           f"       </static/pau/{ f['file_name'] }>`__\n")
    return ''.join(table)


def database_sort(database, fields):
    for field in reversed(fields):
        database.sort(key=itemgetter(field[0]), reverse=field[1])
    return database


def extract_fields(file_names):
    database = []
    for file_name in file_names:
        comunidad = rename_comunidad(file_name.split('-')[1])
        materia = read_materia(file_name.split('-')[2])
        curso = file_name.split('-')[3]
        curso = f'20{curso[:2]}-{curso[2:]}'
        examen = read_tipo_examen(file_name.split('-')[4:])
        database.append({
            'file_name': file_name,
            'comunidad': comunidad,
            'materia': materia,
            'curso': curso,
            'examen': examen,
            })
    return database

    
def write_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as fo:
        fo.write(data)


def read_tipo_examen(tipos):
    for i in range(len(tipos)):
        tipos[i] = tipos[i].capitalize()
        for tipo_examen in tipo_examenes:
            if re.search(tipo_examen[0], tipos[i], flags=re.IGNORECASE):
                tipos[i] = tipo_examen[1]
    return ' '.join(tipos)


def read_materia(file_name):
    for materia in materias:
        if re.search(materia[0], file_name):
            return materia[1]
    return 'No reconocida'


def rename_comunidad(text):
    for comunidad in comunidades:
        text = re.sub(comunidad[0], comunidad[1], text)
    return text


def read_file_names(path):
    file_names = [f for f in os.listdir(path) if f[-4:].lower() == '.pdf']
    return file_names


main()
