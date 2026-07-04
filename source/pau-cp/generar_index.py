"""
Convierte el listado de todos los archivos PDF de este directorio
en una tabla de reStructuredText
"""

import os
import re
import jinja2
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


'''


comunidades = [
   ['andalucia',   'Andalucía'],
   ['aragon',      'Aragón'],
   ['asturias',    'Asturias'],
   ['baleares',    'Baleares'],
   ['canarias',    'Canarias'],
   ['cantabria',   'Cantabria'],
   ['clm',         'Castilla la Mancha'],
   ['cyl',         'Castilla y León'],
   ['catalunya',   'Cataluña'],
   ['valencia',    'Comunidad Valenciana'],
   ['extremadura', 'Extremadura'],
   ['galicia',     'Galicia'],
   ['madrid',      'Madrid'],
   ['murcia',      'Murcia'],
   ['navarra',     'Navarra'],
   ['paisvasco',   'País Vasco'],
   ['rioja',       'Rioja'],
   ]


materias = [
    ['tein', 'Tecnología e Ingeniería II'],
    ]


tipo_examenes = [
    ['ordinaria', 'Ordinaria'],
    ['extra', 'Extraordinaria'],
    ['modelo', 'Modelo'],
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
                  ['examen', True],                  
                  ])
    database_tein = select(database, 'materia', 'tein')
    content = render_table(database_tein)
    write_file('index.rst', content)
    input('Press Enter')


def extract(database, field, reverse=False):
    return sorted(list({fila.get(field) for fila in database}), reverse=reverse)


def select(database, field, value):
    return [fila for fila in database if fila.get(field) == value]


def render_table(database):
    comunidades = extract(database, 'comunidad')
    cursos = extract(database, 'curso', reverse=True)
    table = [table_header]
    table.append(
        'Tecnología e Ingeniería II\n' +
        '--------------------------\n' +
        '.. list-table:: Exámenes PAU\n' +
        '   :header-rows: 1\n' +
        '   :align: left\n' +
        '\n' 
        )

    # Encabezados de la tabla
    table.append('   * - Comunidad\n')
    for curso in cursos:
        table.append(f'     - { curso }\n')

    # Tabla de contenidos
    for comunidad in comunidades:
        comunidad_name = rename_comunidad(comunidad)
        table.append(f'   * - { comunidad_name }\n')
        database_comunidad = select(database, 'comunidad', comunidad)
        for curso in cursos:
            db = select(database_comunidad, 'curso', curso)
            if len(db):
                ex = db[0]
                table.append(f"     - `{ ex['examen'] }\n")
                table.append(f"       </static/pau/{ ex['file_name'] }>`__\n")
            else:
                table.append(f"     -\n")              
            for ex in db[1:]:
                table.append("\n")
                table.append(f"       `{ ex['examen'] }\n")
                table.append(f"       </static/pau/{ ex['file_name'] }>`__\n")
    return ''.join(table)


def database_sort(database, fields):
    for field in reversed(fields):
        database.sort(key=itemgetter(field[0]), reverse=field[1])
    return database


def extract_fields(file_names):
    database = []
    for file_name in file_names:
        comunidad = file_name.split('-')[1]
        materia = file_name.split('-')[2]
        curso = file_name.split('-')[3]
        curso = f'20{curso[:2]}-{curso[2:]}'
        examen = read_tipo_examen(file_name[:-4].split('-')[4:])
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


def rename_materia(file_name):
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
