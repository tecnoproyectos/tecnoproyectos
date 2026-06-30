"""
Lee de la web de Procomún todos los proyectos de Tecnología
para la ESO y para Bachillerato y escribe los datos de forma
ordenada en un archivo de texto con formato YAML.
"""

import os
import re
import time
import requests
from bs4 import BeautifulSoup
import yaml

url_procomun = 'https://procomun.intef.es'
url_search_tecnoeso = url_procomun + '/search-full?f%5B0%5D=knowledgearea_keyword%3ATecnolog%C3%ADas&f%5B1%5D=learningcontext_keyword%3AEducaci%C3%B3n%20Secundaria%20Obligatoria'
url_search_tecnobach = url_procomun + '/search-full?f%5B0%5D=knowledgearea_keyword%3ATecnolog%C3%ADas&f%5B1%5D=learningcontext_keyword%3ABachillerato'

# Headers para simular un navegador real y evitar bloqueos por seguridad
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def main():
    recursos_eso = crawl_web(url_search_tecnoeso, tags='ESO')
    save_yaml('procomun_eso.yaml', recursos_eso)

    recursos_bach = crawl_web(url_search_tecnobach, tags='Bach')
    save_yaml('procomun_bach.yaml', recursos_bach)


def save_yaml(yaml_file, data):
    with open(yaml_file, 'w', encoding='utf-8') as fo:
        yaml.dump(data, fo, allow_unicode=True, sort_keys=False, default_flow_style=False)


def crawl_web(url, maxdepth=200, tags=''):
    recursos_list = []
    counter = 0
    while counter < maxdepth:
        new_url, recursos = buscar_enlaces(url, tags)
        recursos_list = recursos_list + recursos
        counter += 1
        if new_url:
            print(f'-------- Page {counter} -----------')
            print('Crawled:', url)
            time.sleep(3)
            url = new_url
        else:
            break
    return recursos_list


def buscar_enlaces(url_base, tags=''):
    recursos_list = []
    response = requests.get(url_base, headers=HEADERS, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        recursos = soup.select('li.recurso')
        for recurso in recursos:
            try: 
                link = recurso.select_one('h2 a')
                titulo = limpiar_titulo(link.get_text(strip=True))
                url_resource = link.get('href')
                procomun_id = url_resource.split('/')[-1]
                date = traduce_date(recurso.select_one('div.metas time').get_text(strip=True))
                author = limpiar_nombre(recurso.select_one('div.metas span.autor a').get_text(strip=True))
            
                print(f'> {titulo}\n  {procomun_id}\n  {date}\n  {author}')
                recursos_list.append({
                    'title' : titulo,
                    'url': url_procomun + url_resource,
                    'id': procomun_id,
                    'date': date,
                    'author': author,
                    'tags': tags,
                    })
            except:
                print('Error procesando recurso')
                
        nodo_siguiente = soup.select_one('li.pager__item--next a')
        if nodo_siguiente:
            link = nodo_siguiente.get('href')
            url_siguiente_pagina = f"https://procomun.intef.es/search-full{link}"
            return url_siguiente_pagina, recursos_list
        else:
            return None, recursos_list
    else:
        print('No responde: ', url_base)
        return None, recursos_list


def traduce_date(date):
    if date:
        dia, mes, anio = date.split('/')
        return(f'{anio}-{mes}-{dia}')
    return ''


def limpiar_titulo(title):
    title = re.sub('TÍTULO:', '', title)
    title = re.sub('[\n\r\t ]+', ' ', title)
    return title.strip()


def limpiar_nombre(author):
    author = author.title()
    author = re.sub('\\.', '. ', author)
    author = re.sub(' De ', ' de ', author)
    author = re.sub(' Del ', ' del ', author)
    author = re.sub(' La ', ' la ', author)
    author = re.sub('Mª', 'María', author)
    author = re.sub('Maríajosé', 'María José', author)
    author = re.sub('[ \t\n\r]+', ' ', author)
    return author.strip()


main()
