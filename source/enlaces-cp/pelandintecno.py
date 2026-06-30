import os
import re
import yaml
import jinja2
import time
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


url_base = 'https://pelandintecno.blogspot.com'
years = [f'{i:04d}' for i in range(2026, 2026+1)]
months = [f'{i:02d}' for i in range(1, 12+1)]


def main():
   database = read_database('pelandintecno.yaml')

   read_new_posts(database)

   database = remove_duplicated(database)
   
   database.sort(key=lambda reg: reg['date'], reverse=True)

   write_database('pelandintecno.yaml', database)

   new_database = clasifica(database)
   wc = words(new_database[-1][1])
   rst_data = render_template('pelandintecno.txt', new_database)
   write('pelandintecno.rst', rst_data)


def remove_duplicated(database):
   database_dict = {}
   for register in database:
      url = register['url']
      if url in database_dict:
         continue
      database_dict[url] = {
         'date': register['date'],
         'title': register['title'] }
   new_database = []
   for url in database_dict:
      entry = {
         'date': database_dict[url]['date'],
         'title': database_dict[url]['title'],
         'url': url }
      new_database.append(entry)
   return new_database


def words(database):
   wc = {}
   for web in database:
      words = re.split('[\s\.,:0-9\-#/]+', web['title'])
      for word in words:
         if word in wc and word:
            wc[word] += 1
         else:
            wc[word] = 1

   wc = [w for w in wc.items()]
   wc.sort(key=lambda x: x[1])
   return wc


def clasifica(database):
   clasificacion = [
      ['Dibujo', 'trazado|Expresión gráfica|acotación|vistas|perspectivas|ángulos|geométrico'
                 '|escuadra y cartabón|División de un segmento|acotar|acotación'
                 '|comunicación gráfica'],
      ['Mecanismos', 'relaciones de transmisión|palancas|engranajes|poleas|mecanismos'
                     '|biela|manivela|máquina|Tornillo sin fin|relación de transmisión'],
      ['Estructuras', 'Estructuras|resonancia|tacoma|cúpulas|arquitectura|torsión'
                      '|Arco|Kinetic|esfuerzos|pirámides|puente de Trajano|puente de papel'
                      '|torre de Pisa|arquitectónico|cúpula|estructurales|ingeniería civil'
                      '|bridge|tuneladoras|catedral|Skyscraper'],
      ['Diseño 3D', ' 3D|BlocksCAD|OpenSCAD|SketchUp'],
      ['Energía', 'Energía|enegía|fusion|eólica|mareomotriz|nuclear|consumo eléctrico|termosolar'
                  '|vapor|petróleo|motor|ENERGÉTICO|Chernobyl|combustible|chimenea solar'
                  '|aerogeneradores' ],
      ['Materiales', 'plástico|cemento|madera|metal|pétreos|cerámicos|polímeros'
                     '|fabricación del? papel|acero|moldeo|bronce|Titanio'
                     '|alto horno|Papel tissue|Niquel'],
      ['Electricidad', 'Nikola|Tesla|eléctric|electricidad|serie|paralelo|cortocircuito|circuitos'
                       '|resistencias|diferencial|magnetotérmico|circuito|ELECTRIC|Relé'
                       '|bombilla|Ohm|polímetro'],
      ['Micro:bit', 'micro:bit|microbit'],
      ['Electrónica', 'protoboard|electrónica|electrónicos|microchips|condensadores'
                      '|puertas lógicas|semiconductores|Karnaugh|lógicas|diodos'
                      '|Electronics|LÓGICA BINARIA|Moore|LED|unión PN|Transistor'
                      '|Tablas de verdad|Binario y Hexadecimal|condensador'],
      ['El proceso tecnológico', 'Proceso tecnológico'],
      ['Taller', 'seguridad|taller|Señales:|herramientas|Henry Ford|Torres de espagueti'],
      ['Historia de la Tecnología', 'Historia de la tecnología'],
      ['Neumática e hidráulica', 'neumática|hidráulic|FluidSim|válvulas distribuidoras'],
      ['Internet', 'internet|Redes Sociales|netiqueta|Netetiquetas|funciona una red|funciona un wiki'
                   '|twitter'],
      ['Proyectos', 'proyecto|proceso|TANGRAM'],
      ['Historia', 'Historia|revolución industrial'],
      ['Mujer', 'mujer|niña|Curie'],
      ['Leonardo', 'leonardo'],
      ['Vídeos y animaciones', 'v[ií]deos|infograf[íi]a|animaciones|Home: la película'
                               '|documental'],
      ['Ciencia', 'ciencia'],
      ['GIMP', 'gimp'],
      ['Hojas de Cálculo', 'hojas de cálculo'],
      ['Ordenadores', 'ordenador|computación|Turing|Scratch|Assembler|periféricos|linux'
                      '|inkscape|libre office writer'],
      ]

   new_database = []
   for titulo, pattern in clasificacion:
      for i in range(len(database)):
         web = database[i]
         if re.search(pattern, web['title'], flags=re.I) and not 'selected' in web:
            database[i]['selected'] = True
            append(new_database, titulo, web)

   titulo = 'Varios'
   for i in range(len(database)):
      web = database[i]
      if not 'selected' in web:
         append(new_database, titulo, web)
         
   return new_database


def append(database, titulo, web):
   for field in database:
      if field[0] == titulo:
         field[1].append(web)
         return
   database.append([titulo, [web]])   
   

def read_new_posts(database):
   new_data = False
   for year in years:
      for month in months:
         url = '{0}/{1}/{2}/'.format(url_base, year, month)
         print(f'Download: {url}')
         time.sleep(2)
         html = download(url)
         for title in get_titles(url, html):
            page = {
               'date': f'{year}-{month}',
               'title': title[1],
               'url': title[0],
            }
            if not database_exists(database, page):
               print(f'   New page: {page["title"]}')
               new_data = True
               database.append(page)
   return new_data


def render_template(filename, database):
   environment = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
   template = environment.get_template(filename)
   rst_data = template.render(database = database)
   return rst_data


def database_exists(database, page):
   for register in database:
      if register['url'] == page['url']:
         return True
   return False


def read(filename):
   with open(filename, 'r', encoding='utf-8-sig') as fi:
      data = fi.read()
   return data


def read_database(fname):
   try:
      data = yaml.load(read(fname), Loader=yaml.Loader)
   except:
      data = []
   return data


def write(filename, data):
   with open(filename, 'w', encoding='utf-8') as fo:
      fo.write(data)


def write_database(fname, database):
   yaml_txt = yaml.dump(database, default_flow_style=False, allow_unicode=True)
   write(fname, yaml_txt)

   
def get_titles(url, html):
   soup = BeautifulSoup(html, 'html.parser')
   for header3 in soup.find_all('h3'):
      if 'entry-title' in header3.get('class'):
         title = header3.text.strip()
         for link in header3.find_all('a'):
            url_link = link['href']
         yield url_link, title


def download(url):
   return requests.get(url).text


main()
