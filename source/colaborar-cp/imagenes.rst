:date: 2026-06-22
:modified: 2026-06-26
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Fotografías e imágenes
======================
En este apartado se explican los formatos de imagen, tamaños y 
forma de atribuir correctamente el material externo.

Formatos de imagen
------------------
Se recomienda utilizar solo dos formatos de imagen:

* **JPG**: para fotografías o imágenes con degradados y multitud de
  colores.

* **PNG**: para el resto de imágenes como capturas de pantalla, gráficos
  imágenes prediseñadas, capturas de texto, etc.
     
Ante la duda, lo mejor es guardar la imagen en **formato PNG**, puesto
que este formato no pierde calidad y se puede convertir fácilmente a JPG
posteriormente, mientras que las imágenes JPG pierden calidad y no
pueden convertirse posteriormente a PNG porque ocupan un tamaño
excesivo.


Ancho de imagen
---------------
El ancho de las imágenes debe ser suficientemente grande como para que
la imagen no pierda detalles, pero no innecesariamente grande para que 
el archivo ocupe un tamaño limitado.

Tamaños habituales de imágenes grandes para el formato web pueden ir desde
los 800 pixel de ancho de una visualización a pantalla grande, hasta los
1200 pixel que permiten ampliar aun más la imagen sin pérdida de calidad.

Las imágenes pequeñas pueden tener desde 120 pixel de ancho para pequeños
iconos hasta los 640 pixel de ancho para imágenes que ocupen casi toda la
pantalla en ordenadores personales.


Tamaño de archivo
-----------------
Los archivos de fotografías e imágenes no deben tener un tamaño mayor
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


Atribución de autoría
---------------------
Las imágenes suelen ser el contenido en el que más se utilizan recursos
de otras personas y es sumamente importante realizar una atribución de
autoría correcta.

Lo ideal es utilizar imágenes con la misma licencia que los recursos
de esta web (por defecto es Creative Commons Atribución Compartir-Igual
4.0) como lo son casi todas las imágenes de Wikimedia.

También se pueden utilizar imágenes con otras licencias, siempre
que sean compatibles con la licencia anterior, como las imágenes de stock
de `Pexels <https://www.pexels.com/es-es/license/>`__
o de `Pixabay <https://pixabay.com/service/license-summary/>`__.

La forma de atribuir correctamente la autoría es añadir los siguientes
elementos:

* **Título**: El nombre original de la imagen, si tiene.

* **Autor**: El nombre o seudónimo del creador, enlazado a su perfil
  si es posible.

* **Fuente**: Un enlace directo a donde está publicada la obra original.

* **Licencia**: El nombre de la licencia (CC BY-SA 4.0) enlazado a su
  texto legal.

* **Cambios**: Una declaración explícita si has adaptado o modificado la
  obra original.

Ejemplo práctico de código reStructuredText de una imagen con atribución::

   .. figure:: _images/hardware-cp-placa-base.jpg
      :align: center
      :width: 480px

      Placa base ASRock A70GXH-128M de 2012.

      `Evan-Amos <https://commons.wikimedia.org/wiki/File:A790GXH-128M-Motherboard.jpg>`__,
      `CC BY-SA 3.0 Unported <https://creativecommons.org/licenses/by-sa/3.0/deed.en>`__,
      vía Wikimedia Commons.
      Imagen original recortada.
