# -*- coding: utf-8 -*-
"""
   Read all js files of this directory and write out a image file
   with the highlighted code.
   
   ----------------------------------------------------------------
   Dependencies:
   Python 3.14
   python -m pip install pygments
   font: 'DejaVu Sans Mono'

   ----------------------------------------------------------------
   Copyright (c) 2026 by Carlos Félix Pardo Martín <carlos (at) picuino.com>
   License GPL v3  <https://www.gnu.org/licenses/gpl-3.0.html>
   
   This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License
   version 3 as published by the Free Software Foundation.

"""

import os
import pathlib
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from pygments.styles import get_all_styles


visual_style = 'friendly'       # Ejemplos: 'friendly', 'monokai', 'native'
font_name = 'DejaVu Sans Mono'  # Necesitas tener la fuente instalada en tu sistema
font_size = 16
line_numbers = False
force_write = False


def main():
    language = 'javascript'
    lexer = get_lexer_by_name(language, stripall=True)
    filenames = [f for f in os.listdir('.') if f[-3:] == '.js']
    for filename in filenames:
        image_name = filename[:-3] + '.png'
        if force_write or file_newer(filename, image_name):
            source_code = read_file(filename)
            image_data = generate_image(source_code, lexer)
            write_bin_file(image_name, image_data)
            print(f'Image: {image_name}')
    input('Press Enter')



def file_newer(file_org, file_dst):
   mtime_org = pathlib.Path(file_org)
   mtime_dst = pathlib.Path(file_dst)
   if not mtime_dst.exists() \
      or mtime_org.stat().st_mtime > mtime_dst.stat().st_mtime:
      return True
   return False


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as fi:
        data = fi.read()
    return data


def write_bin_file(filename, data):
    with open(filename, 'wb') as fo:
        fo.write(data)
    

def generate_image(source_code, lexer):
    formatter = ImageFormatter(
        font_name=font_name,
        font_size=font_size,
        style=visual_style,
        line_numbers=line_numbers,
    )
    return highlight(source_code, lexer, formatter)


main()
