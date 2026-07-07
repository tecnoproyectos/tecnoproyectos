"""
Convierte el listado de todos los archivos PDF de este directorio
en una tabla de reStructuredText
"""

import os
import re
import jinja2
from operator import itemgetter


table_header = ''':date: 2026-07-03
:modified: 2026-07-07
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Exámenes PAU
============
Exámenes de las Pruebas de Acceso a la Universidad de las materias
de Bachillerato relacionadas con Tecnología.


'''


comunidades = [
   ['andalucia',   'Andalucía',
    'https://www.juntadeandalucia.es/economiaconocimientoempresasyuniversidad/sguit/?q=grados&d=g_b_examenes_anteriores.php'],
   ['aragon',      'Aragón',
    'https://academico.unizar.es/acceso-admision-grado/pau/exame'],
   ['asturias',    'Asturias',
    'https://www.uniovi.es/estudia/grados/sobrelosgrados/ebau/examenes'],
   ['baleares',    'Baleares',
    'https://estudis.uib.es/es/estudis-de-grau/Com-hi-pots-accedir/acces/batxiller/ModelsExamenPBAU/'],
   ['canarias',    'Canarias',
    'https://www.gobiernodecanarias.org/educacion/web/bachillerato/pau/pau/index.html'],
   ['cantabria',   'Cantabria',
    'http://web.unican.es/admision/acceso-a-estudios-de-grado/evaluacion-de-bachillerato-para-el-acceso-a-la-universidad'],
   ['catalunya',   'Cataluña',
    'http://www.selecat.cat/'],
   ['clm',         'Castilla la Mancha',
    'https://www.uclm.es/es/perfiles/preuniversitario/acceso/pau/modelosycriteriosdecorreccion'],
   ['cyl',         'Castilla y León',
    'https://pruebasdeacceso.uva.es/1.ebau/'],
   ['extremadura', 'Extremadura',
    'https://alumnado.unex.es/pau/'],
   ['galicia',     'Galicia',
    'https://www.ciug.gal/gal/pau'],
   ['madrid',      'Madrid',
    'https://www.ucm.es/pruebas-de-acceso'],
   ['murcia',      'Murcia',
    'https://www.um.es/web/estudios/acceso/estudiantes-bachillerato-y-ciclos-formativos'],
   ['navarra',     'Navarra',
    'https://www.unavarra.es/sites/estudios/acceso-y-admision/evau-para-estudiantes/desarrollo-de-las-pruebas.html'],
   ['paisvasco',   'País Vasco',
    'https://www.ehu.eus/es/web/unibertsitaterako-sarbidea/pruebas-de-acceso/examenes-de-cursos-anteriores/bachillerato-y-ciclos-formativos-de-grado-superior'],
   ['rioja',       'La Rioja',
    'https://www.unirioja.es/administracion-y-servicios/oficina-del-estudiante/ebau/examenes-y-criterios/'],
   ['uned',        'UNED',
    'https://unedasiss.uned.es/examenes'],
   ['valencia',    'Comunidad Valenciana',
    'https://universitats.gva.es/va/prova-acces-universitat-pau'],
   ]


materias = [
    ['tein', 'Tecnología e Ingeniería II'],
    ]


tipo_examenes = [
    ['ordinaria', 'Ordinaria'],
    ['extra',     'Extraordinaria'],
    ['modelo',    'Modelo'],
    ['coincide',  'Coincidentes'],
    ['solucion',  'Soluciones'],
    ]


orden_examenes = ['modelo', 'ordinaria', 'extra', 'criterios',
                  'titular', 'reserva', 'suplente', 'suplente1', 'suplente2']


def main():
    file_names = read_file_names('../../../static/pau')
    database = extract_fields(file_names)
    database_sort(database, [
                  ['comunidad', False],
                  ['materia', False],
                  ['curso', True],
                  ['examen', False],
                  ['examen_name', False],
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
    num_criterios = sum('criterios' in d['file_name'] for d in database)
    num_examenes = len(database) - num_criterios
    comunidades = extract(database, 'comunidad')
    cursos = extract(database, 'curso', reverse=True)
    table = [table_header]
    materia_name = rename_materia(database[0]['materia'])
    table.append(
        f'{ materia_name }\n' +
        '-' * len(materia_name) + '\n' +
        f'.. list-table:: { num_examenes } exámenes y { num_criterios } criterios PAU\n' +
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
        comunidad_link = linkto_comunidad(comunidad)
        table.append(f'   * - `{ comunidad_name }\n')
        table.append(f'       <{ comunidad_link }>`__\n')
        database_comunidad = select(database, 'comunidad', comunidad)
        for curso in cursos:
            db = select(database_comunidad, 'curso', curso)
            if len(db):
                exam = db[0]
                table.append(f"     - `{ exam['examen_name'] }\n")
                table.append(f"       </static/pau/{ exam['file_name'] }>`__\n")
            else:
                table.append(f"     -\n")
            for exam in db[1:]:
                table.append("\n")
                table.append(f"       `{ exam['examen_name'] }\n")
                table.append(f"       </static/pau/{ exam['file_name'] }>`__\n")
    return ''.join(table)


def criterio_ord_examen(item):
    valor = item['examen'][0]
    if valor in orden_examenes:
        return (0, orden_examenes.index(valor), valor)
    else:
        return (1, valor)


def database_sort(database, fields):
    for field in reversed(fields):
        if field[0] == 'examen':
            database.sort(key=criterio_ord_examen, reverse=field[1])
        else:
            database.sort(key=itemgetter(field[0]), reverse=field[1])
    return database


def extract_fields(file_names):
    database = []
    for file_name in file_names:
        comunidad = file_name.split('-')[1]
        materia = file_name.split('-')[2]
        curso = file_name.split('-')[3]
        curso = f'20{curso[:2]}-{curso[2:]}'
        examen = file_name[:-4].split('-')[4:]
        examen_name = read_tipo_examen(examen)
        database.append({
            'file_name': file_name,
            'comunidad': comunidad,
            'materia': materia,
            'curso': curso,
            'examen': examen,
            'examen_name': examen_name,
            })
    return database


def write_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as fo:
        fo.write(data)


def read_tipo_examen(tipos):
    name = []
    for tipo in tipos:
        tipo = tipo.capitalize()
        for tipo_examen in tipo_examenes:
            if re.search(tipo_examen[0], tipo, flags=re.IGNORECASE):
                tipo = tipo_examen[1]
        name.append(tipo)
    return ' '.join(name)


def rename_materia(file_name):
    for materia in materias:
        if re.search(materia[0], file_name):
            return materia[1]
    return 'No reconocida'


def rename_comunidad(text):
    for comunidad in comunidades:
        if re.search(comunidad[0], text):
            return comunidad[1]
    return text


def linkto_comunidad(text):
    for comunidad in comunidades:
        if re.search(comunidad[0], text):
            return comunidad[2]
    return text


def read_file_names(path):
    file_names = [f for f in os.listdir(path) if f[-4:].lower() == '.pdf']
    return file_names


main()
