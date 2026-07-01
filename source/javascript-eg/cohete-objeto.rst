:date: 2026-06-28
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Cohete: objeto literal
======================

.. parsed-literal::

   Paso 1/5 de práctica 3 "Fuegos artificiales"

En esta práctica vas a crear una simulación de fuegos artificiales
interactivos. Cada vez que hagas clic en el lienzo, un cohete saldrá
disparado desde ese punto, subirá frenado por la gravedad y explotará en
una lluvia de chispas de colores que se desvanecen poco a poco.

El programa introduce un concepto nuevo: el **objeto literal**. Verás por
qué agrupar propiedades relacionadas en un objeto hace el código más claro,
y lo compararás directamente con el estilo de variables sueltas que ya
conoces.

.. note::

   Este tutorial presupone que conoces ``setup()``, ``draw()``,
   ``background()``, ``circle()``, ``stroke()``, ``fill()``, ``random()``
   y el bucle ``for``. También necesitarás el concepto de array de la
   práctica 2. Si alguno de estos puntos te resulta poco familiar,
   repásalo antes de continuar.


Un cohete con variables sueltas
--------------------------------

Empezamos con lo más sencillo: un único cohete que sube desde el centro
del lienzo. Tiene posición (``x``, ``y``) y velocidad (``vx``, ``vy``).
La gravedad se simula sumando un pequeño valor positivo a ``vy`` en cada
fotograma: el cohete va frenando, se detiene y luego cae.

.. figure::
   _images/javascript-eg-301.png
   :width: 600px
   :align: center


Ejecuta el código. El cohete sube, frena y empieza a caer. La gravedad
es ese ``0.1`` que se suma a ``vy`` en cada fotograma.

.. admonition:: Experimenta

   Cambia el valor de ``vy`` inicial de ``random(-20, -5)`` a
   ``random(-8, -5)``. ¿A qué altura llega el cohete?
   Prueba también a cambiar la gravedad de ``0.1`` a ``0.05`` y a
   ``0.2`` y observa cómo varía la trayectoria.


El cohete como objeto literal
------------------------------

En `la práctica anterior Partículas conectadas <particula-rebotando>`_,
usábamos **arrays paralelos** para guardar los datos de
cada partícula: un array para ``x``, otro para ``y``, otro para ``vx``,
otro para ``vy``. El índice ``i`` relacionaba los datos que pertenecían
a la misma partícula.

Un **objeto literal** agrupa todas las propiedades relacionadas bajo un
mismo nombre. Se escribe entre llaves ``{ }``, separando cada propiedad
con coma. Compara los dos estilos:

.. code-block:: javascript

   // Con variables sueltas (lo que conocemos de prácticas anteriores)
   let x, y, vx, vy;

   // Con un objeto literal: todas las propiedades agrupadas
   let cohete = {
     x:  width / 2,
     y:  height,
     vx: random(-2, 2),
     vy: random(-10, -5)
   };

Para acceder a una propiedad se usa la **notación de punto**:
``cohete.x``, ``cohete.vy``, etc.
 
En setup() podemos crear y definir valor para las propiedades que necesitemos para cohete.
Aquí está el programa completo reescrito con el objeto:

.. figure::
   _images/javascript-eg-302.png
   :width: 600px
   :align: center



.. admonition:: ¿Qué ha cambiado?

   El resultado en pantalla es idéntico al programa anterior. Lo que ha
   cambiado es la organización del código: ahora ``x``, ``y``, ``vx`` y
   ``vy`` están agrupadas en el objeto ``cohete``. Esto no parece una
   gran ventaja con un único cohete, pero en el paso 4, cuando tengamos
   varios, la diferencia será evidente.
