:date: 2026-06-22
:modified: 2026-06-22
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Colaboración con el proyecto
============================
En esta página se explicará cómo colaborar con este proyecto a través
de GitHub y qué normas seguir para mantener el estilo de la web homogéneo.


Normas de edición
-----------------
#. Todos los archivos de un proyecto deben estar contenidos en una carpeta
   con nombre del proyecto y las iniciales del creador.
  
   Por ejemplo: arduino-ft, scratch-cpm, puente-fam
  
   Si tienes dudas, contacta con el administrador de la web para que 
   te asigne un directorio en el que comenzar a añadir contenidos.

#. Todas las imágenes y archivos descargables deben empezar por el mismo
   nombre de la carpeta en el que están contenidas. De esta forma ningún
   archivo de todo el proyecto tendrá un nombre coincidente con el de 
   otro proyecto distinto.
      
   Por ejemplo imágenes o archivos pdf: arduino-ft-01.png, 
   arduino-ft-guia.pdf

#. El primer archivo de contenidos dentro de la carpeta de un proyecto 
   debe llamarse index.rst y debe contener una lista con todos los 
   archivos de ese proyecto.
   
   No está permitido hacer subniveles. Todos los archivos del proyecto
   deben colgar del archivo principal index.rst.

   Si necesitas separar proyectos, será necesario crear un proyecto nuevo
   con un nuevo nombre.

#. La codificación de los archivos rst deberá ser UTF-8 con BOM para que
   pueda soportar la edición de caracteres internacionales.
   
   Se pueden utilizar emojis en el texto, pero al traducir la página web a
   formato PDF, la mayoría se perderán.

#. Es necesario añadir metadatos en la cabecera para indicar quién es el
   autor del proyecto y qué licencia usa.
   Para dar coherencia a todo el sitio web y permitir la utilización de
   imágenes de Wikimedia y de herramientas como Fritzing, se recomienda
   encarecidamente mantener la licencia Creative Commons
   Attribution-ShareAlike 4.0.
   
   Los metadatos básicos de cabecera de todos los archivos rst serán::
   
      :date: 2026-06-22    (fecha de creación en formato año-mes-dia)
      :modified: 2026-06-22   (fecha de última modificación en formato año-mes-dia)
      :author: Nombre y apellido(s) del autor
      :license: Creative Commons Attribution-ShareAlike 4.0 International
      :license_url: https://creativecommons.org/licenses/by-sa/4.0/

#. Se recomienda mantener todos los archivos rst en el directorio raíz del 
   proyecto y las imágenes en el subdirectorio _images.
   
   Se puede crear otro directorio más para las descargas: _downloads
   
   Se recomienda no crear más subdirectorios para mantener limpio el 
   proyecto y poder ver todos los archivos a la vez sin tener que navegar
   por subdirectorios.

#. Las imágenes no deben tener un tamaño mayor de 500 kilobytes.
   Si hay imágenes de gran tamaño se recomienda crear un repositorio nuevo
   en GitHub para almacenarlas.
   Después se copiarán solo las imágenes imprescindibles en formato de
   tamaño y calidad reducidas en el proyecto para que el tamaño total de
   todo el sitio web se mantenga contenido.
   
   La herramienta estándar para reducir el tamaño y calidad de las
   imágenes es `ImageMagick <https://imagemagick.org/download/>`__
   
   La línea de comandos para reducir el tamaño de una imagen es::
      
      magick  image.jpg  -resize "1200x1200>" -quality 90 -strip   image-1200.jpg
   
   
   Donde image.jpg es la imagen original a reducir y 1200 es el tamaño en
   pixels de ancho o de alto (la mayor de las dos) de la imagen de salida.
   
   Para reducir a la vez el tamaño de muchas imágenes se utilizará la
   línea de comandos para Windows::
   
      for %i in (*.jpg) do magick "%i" -resize "1200x1200>" -quality 90 -strip "%~ni-1200.jpg"

   O su equivalente en Linux::

      for img in *.jpg; do
         magick "$img" -resize "1200x1200>" -quality 90 -strip "${img%.jpg}-1200.jpg"
      done
   
   
   