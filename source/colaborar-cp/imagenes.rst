:date: 2026-06-22
:modified: 2026-06-24
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Fotografías e imágenes
======================
#. Se recomienda utilizar solo dos formatos de imagen:

   * **JPG**: para fotografías o imágenes con degradados y multitud de
     colores.
   * **PNG**: para el resto de imágenes como capturas de pantalla, gráficos
     imágenes prediseñadas, capturas de texto, etc.
     
   Ante la duda, lo mejor es guardar la imagen en **formato PNG**, puesto
   que este formato no pierde calidad y se puede convertir fácilmente a JPG
   posteriormente, mientras que las imágenes JPG pierden calidad y no
   pueden convertirse posteriormente a PNG porque ocupan un tamaño
   excesivo.

#. El tamaño de las imágenes debe ser suficientemente grande como para que
   la imagen no pierda detalles, pero no innecesariamente grande para que 
   el archivo no ocupe un tamaño excesivo.
     
#. Los archivos de fotografías e imágenes no deben tener un tamaño mayor
   de 500 kilobytes.

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
