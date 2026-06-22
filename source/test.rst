:date: 2026-06-19
:modified: 2026-06-22
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

.. _test:

Página de test 
==============
Esta es una página que sirve de ejemplo de la mayoría de las funciones
útiles del lenguaje reStructuredText para Sphinx.
Con esta página se puede aprender a utilizar este lenguaje y se puede
comprobar el funcionamiento de los estilos aplicados por el tema Furo de
Sphinx.

`Documentación de reStructuredText para Sphinx.
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__


Párrafos
--------
Párrafo con texto *resaltado*, texto **resaltado fuerte** y texto en
``formato código``.

Párrafo segundo: Lorem ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat.

Párrafo tercero: Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
est laborum.


Listas
------
Lista numerada:

#. Primero
#. Segundo 
#. Tercero

Lista no numerada:

* Primero

  * Sub primero primero
  * Sub primero segundo
  
* Segundo
* Tercero

Término uno
  Descripción del término uno.
  
Término dos
  Descripción del término dos.
  
  Que puede tener varios párrafos.


Tablas
------

Tabla en forma de cuadrícula:

+---------------+---------------+---------------+
| Encabezado 1  | Encabezado 2  | Encabezado 3  |
+===============+===============+===============+
| Fila 1, col 1 | Fila 1, col 2 | Fila 1, col 3 |
+---------------+---------------+---------------+
| Fila 2, col 1 | Fila 2, col 2 | Fila 2, col 3 |
+---------------+---------------+---------------+


Tabla en forma de lista:

.. list-table:: tabla en forma de lista
   :name: tabla-lista
   :header-rows: 1
   :widths: auto
   :align: center

   * - Encabezado 1
     - Encabezado 2
     - Encabezado 3
     - Encabezado 4
   * - Fila 1, col 1
     - Fila 1, col 2
     - Fila 1, col 3
     - Fila 1, col 4
   * - Fila 2, col 1
     - Fila 2, col 2
     - Fila 2, col 3
     - Fila 2, col 4


Hipervínculos
-------------

`Enlace a una página de Wikipedia sobre Python
<https://es.wikipedia.org/wiki/Python>`__.

Enlace interno a la :ref:`página principal de contenidos <content>`.

:download:`Descarga de este texto fuente <test.rst>`.

Enlace a la :numref:`Tabla %s <tabla-lista>`.


Imágenes
--------

Ejemplo de imagen centrada en el medio de la página con título.
Al clicar sobre la imagen, se muestra en su tamaño real más grande:

.. figure:: test/flower.jpg
   :name: figura-flower
   :width: 360px
   :align: center
   
   Flor blanca.
   
   Imagen de `Siritas Keawnet <https://www.pexels.com/@sosassosay/>`__ en 
   `Pexels <https://www.pexels.com/photo/white-and-yellow-flower-in-tilt-shift-lens-3718388/>`__


Ejemplo de imagen a la derecha con texto alrededor.
Al clicar sobre la imagen se abre un enlace a Wikipedia:

.. figure:: test/flower.jpg
   :width: 360px
   :align: right
   :target: https://es.wikipedia.org/wiki/Flor
   
   Flor blanca.
   
   Imagen de `Siritas Keawnet <https://www.pexels.com/@sosassosay/>`__ en 
   `Pexels <https://www.pexels.com/photo/white-and-yellow-flower-in-tilt-shift-lens-3718388/>`__

Lorem ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
est laborum.


Advertencias
------------

.. tip::
   Esto es un consejo o truco que facilita el aprendizaje.
   Ayuda al estudiante a trabajar de forma más eficiente.

.. note::
   Esto es una aclaración, dato curioso o recordatorio importante.
   También se puede utilizar para conectar un tema con otro.


.. warning::
   Esta advertencia se usa para alertar sobre fallos típicos, 
   malentendidos o acciones que pueden estropear algo.

.. hint::
   :collapsible: closed
   
   Esta sugerencia o pista sirve para guiar al estudiante hacia la
   solución. Estimula el pensamiento crítico sin dar la respuesta
   directamente.
   Además se muestra inicialmente cerrada para no dar pistas antes
   de que el estudiante lo pida expresamente.


Consistencia
   Asigna siempre el mismo tipo de contenido al mismo bloque para que
   el estudiante asocie el color con el tipo de mensaje de forma
   automática.


Notas a pie de página
---------------------
Este texto necesita una aclaración mediante una nota al pie de página
con numeración automática [#f1]_. 

También puedes enlazar a otra nota a pie de página usando un nombre
identificativo o etiqueta [#nota_nombre]_.

Por otro lado, Sphinx es la herramienta estándar para generar
documentación de proyectos asociados a Python [#]_.


Fórmulas
--------
El generador de páginas estáticas Sphinx permite añadir fórmulas a la
documentación gracias al lenguaje LaTeX:

.. math::

   ax^2 + bx + c = 0

.. math::

   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}



Glosario de términos
--------------------

.. glossary::

   Sphinx
      Generador de documentación de código abierto escrito en **Python**.
      Convierte archivos de texto plano (usualmente en formato 
      *reStructuredText* o *Markdown*) en sitios web HTML estáticos,
      manuales en PDF, ePub y otros formatos.
      Es la herramienta estándar de la industria para documentar
      proyectos en el ecosistema Python.

   Furo
      Tema que define el aspecto visual y la estructura estética de la
      documentación generada por Sphinx. Es limpio, minimalista y 
      adaptable (*responsive*) diseñado específicamente para 
      proyectos de documentación de Sphinx. 
      Destaca por ofrecer navegación fluida tanto en pantallas móviles
      como de escritorio y soporte nativo para modos claro/oscuro.

   Python
      Lenguaje de programación de alto nivel, interpretado y
      multiparadigma. Es ampliamente conocido por su sintaxis limpia y
      legible, y funciona como la base tecnológica sobre la cual está
      construido y se ejecuta todo el sistema de Sphinx.


.. index:: reStructuredText

El lenguaje reStructuredText
----------------------------
Es un :index:`lenguaje de marcado ligero <reStructuredText>` diseñado 
específicamente para la comunidad de **Python**. Su objetivo principal
es facilitar la creación de documentos técnicos legibles tanto en su
formato de texto plano de origen como una vez procesados y compilados
por herramientas como **Sphinx**.




.. rubric:: Notas:

.. [#f1] Esta es la explicación de la primera nota al pie, numerada
   automáticamente.
.. [#nota_nombre] Esta nota se asocia mediante el texto de la etiqueta,
   pero Sphinx le asignará el número correlativo correcto.
.. [#] Sphinx transforma archivos reStructuredText en HTML, PDF y otros
   formatos.
