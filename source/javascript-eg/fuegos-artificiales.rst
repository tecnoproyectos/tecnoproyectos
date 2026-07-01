:date: 2026-06-28
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Fuegos artificiales: mousePressed() y funciones auxiliares
==========================================================

.. parsed-literal::

   Paso 4/5 de práctica 3 "Fuegos artificiales"

El programa del paso anterior funciona, pero ``draw()`` empieza a ser
largo y difícil de leer: la lógica de crear chispas y la de moverlas
están mezcladas en el mismo bloque. Antes de añadir más cohetes, vamos
a **limpiar el código** extrayendo esa lógica a funciones auxiliares.
Verás que un código más limpio es también más fácil de ampliar.


Extraer funciones: explotar() y gestionarChispas()
----------------------------------------------------

Creamos dos funciones auxiliares. Cada una recibe un cohete como
parámetro (llamado ``c`` dentro de la función) y trabaja con sus
propiedades:

.. figure::
   _images/javascript-eg-310.png
   :width: 400px
   :align: center

.. note::

  Localiza en el código que tenías antes de estas funciones 
  y que ahora está dentro de ellas. Sustituye ese código 
  por una llamada a la función correspondiente.

Ahora ``draw()`` queda mucho más corto y legible: solo describe el
flujo general, sin entrar en detalles.


Varios cohetes con mousePressed()
----------------------------------

Con el código limpio, dar el salto a varios cohetes es sencillo.
Cambiamos ``cohete`` por un array ``cohetes = []``. La función
``mousePressed()`` añade un cohete nuevo en cada clic. ``draw()``
los gestiona todos con un bucle ``for``:

.. admonition:: Array de objetos frente a arrays paralelos

   En la práctica 2 teníamos ``px[]``, ``py[]``, ``pvx[]``, ``pvy[]``
   y el índice ``i`` relacionaba los datos de la misma partícula.
   Aquí cada cohete lleva consigo todos sus datos agrupados:
   ``cohetes[i].x``, ``cohetes[i].vy``, ``cohetes[i].chispas``...
   Al añadir una propiedad nueva — por ejemplo un tipo de explosión —
   solo hay que añadirla al objeto, sin crear un array paralelo nuevo.


El setup y draw 
---------------

.. figure::
   _images/javascript-eg-311.png
   :width: 400px
   :align: center


.. admonition:: Fíjate en ===

   ``c.chispas.length === 0`` usa triple igual. En JavaScript ``===``
   compara valor **y tipo** a la vez, mientras que ``==`` solo compara
   el valor y puede dar resultados inesperados. Es buena práctica usar
   siempre ``===`` para comparar.
