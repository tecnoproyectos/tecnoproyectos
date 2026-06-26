:date: 2026-06-22
:modified: 2026-06-26
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Normas de edición
=================
Estas son las normas para editar los contenidos de la página web con 
el lenguaje reStructuredText.
Puedes aprender a utilizar este lenguaje de marcado con 
la :ref:`página de ejemplo de reStructuredText <restructuredtext>`.


Carpeta de proyecto
-------------------
Todos los archivos de un proyecto deben estar contenidos en una carpeta
con nombre del proyecto y las iniciales del creador.
  
Por ejemplo: arduino-ft, scratch-cpm, puente-fam
  
Si tienes dudas, contacta con el administrador de la web para que 
te asigne un directorio en el que comenzar a añadir contenidos.


Imágenes y documentos
---------------------
Todas las imágenes y archivos descargables deben empezar por el mismo
nombre de la carpeta en el que están contenidas. De esta forma ningún
archivo de todo el proyecto tendrá un nombre coincidente con el de 
otro proyecto distinto.
      
Por ejemplo imágenes o archivos pdf: arduino-ft-01.png, arduino-ft-guia.pdf


Página de índice
----------------
El primer archivo de contenidos dentro de la carpeta de un proyecto 
debe llamarse **index.rst** y debe contener una lista con todos los 
archivos de ese proyecto.
   
No está permitido hacer subniveles. Todos los archivos del proyecto
deben colgar del archivo principal index.rst.

Si necesitas separar proyectos, será necesario crear un proyecto nuevo
con un nuevo nombre.


Nombre de las páginas
---------------------
Los diferentes archivos de reStructuredText (\*.rst) de un proyecto,
que luego se convertirán en una página web, deben nombrarse con palabras
separadas por guiones altos que describan lo mejor posible el contenido
del archivo.
Se puede utilizar desde una palabra hasta tres palabras como máximo.
   
Ejemplos: pantalla-lcd.rst, entradas-analogicas.rst, disenio-papel.rst
   
No utilices tildes, eñes o diéresis ya que eso crearía problemas con
las páginas html generadas. La letra 'ñ' se puede sustituir por las
letras 'ni' y las tildes y diéresis no se ponen.
   
Intenta no numerar los archivos, porque las numeraciones se desordenan
al añadir contenido o al reordenar el contenido existente.


Subdirectorios
--------------
Se recomienda mantener todos los archivos \*.rst en el directorio raíz del 
proyecto y las imágenes en el subdirectorio _images.
   
Se puede crear otro subdirectorio más para las descargas: _downloads
   
Se recomienda no crear más subdirectorios para mantener limpio el 
proyecto y poder ver todos los archivos a la vez sin tener que navegar
por subdirectorios.


Codificación de los archivos
----------------------------
La codificación de los archivos de texto \*.rst deberá ser UTF-8
con BOM para que pueda soportar la edición de caracteres internacionales.
   
Se pueden utilizar emojis en el texto, pero al traducir la página web a
formato PDF, la mayoría se perderán.


Metadatos
---------
Es necesario añadir metadatos en la cabecera para indicar quién es el
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


Caracteres por línea
--------------------
Los archivos reStructuredText se pueden escribir con cualquier número de
columnas por cada línea de texto, pero se recomienda utilizar un límite
práctico de **75 caracteres por línea** como máximo para que las líneas
se puedan visualizar sin problemas en una pantalla estrecha.


Títulos
-------
Se recomienda realizar **un solo título principal** en cada página,
al comienzo de la página y subrayado con caracteres de igual::

   Título principal
   ================

Se pueden añadir subtítulos secundarios, subrayados con caracteres de
resta::

   Títulos secundarios
   -------------------
   Se pueden hacer muchos títulos secundarios en una página
   para organizar todo el contenido.

De forma excepcional se pueden añadir subtítulos de tercer nivel,
subrayados con caracteres de acentos circunflejos, aunque se desaconseja
porque puede generar confusión::

   Título de tercer nivel
   ^^^^^^^^^^^^^^^^^^^^^^
   Se desaconseja utilizar tantos niveles de títulos en una página.
   Es preferible separar los contenidos en páginas diferentes.

Los títulos deben ser breves para que los menús de navegación no se
saturen con frases largas. Lo ideal es utilizar una, dos o tres palabras
descriptivas y aportar una explicación mayor en el texto a continuación
del título.


Extensión de página
-------------------
Cada página de contenidos debería tener una extensión tal que se pueda 
estudiar y realizar sus ejercicios en una sesión de clase
(alrededor de 50 minutos).

Si es necesario separar contenidos para diferenciarlos (por ejemplo
separar circuitos en serie de circuitos en paralelo) lo ideal es que 
cada página contenga sus propios ejercicios y tareas y que se puedan 
hacer como mucho tres páginas por sesión de clase.


Ejemplos
--------
Puedes fijarte en cómo está escrito un proyecto ya existente para
tomarlo como referencia para escribir el tuyo.
   
Por ejemplo te puede servir de modelo estas mismas páginas que explican
`Cómo colaborar
<https://github.com/tecnoproyectos/tecnoproyectos/tree/main/source/colaborar-cp>`__
situado en la carpeta ``sources/colaborar-cp`` del repositorio.
