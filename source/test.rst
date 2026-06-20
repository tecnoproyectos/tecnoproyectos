:date: 2026-06-19
:modified: 2026-06-19
:author: Carlos Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/
:tocdepth: 1

.. _test:

Página de test 
==============
Esta es una página que sirve de ejemplo de la mayoría de las funciones
útiles del lenguaje reStructuredText para Sphinx.
Con esta página se puede aprender a utilizar este lenguaje y se puede
comprobar el funcionamiento de los estilos aplicados por el tema de Sphinx.

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

Término
  Descripción del término.
  
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
   :widths: 20 40 40
   :header-rows: 1
   :align: center

   * - Encabezado 1
     - Encabezado 2
     - Encabezado 3
   * - Fila 1, col 1
     - Fila 1, col 2
     - Fila 1, col 3
   * - Fila 2, col 1
     - Fila 2, col 2
     - Fila 2, col 3


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