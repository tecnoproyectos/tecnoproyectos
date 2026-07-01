:date: 2026-06-23
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Esctructura: setup() y draw()
=============================
.. parsed-literal::
  
  Paso 2/8 de práctica 1 "Lienzo interactivo"

En esta práctica veremos cómo usar las funciones setup() y draw().


El bucle de dibujo
------------------

Todo programa en p5.js tiene dos funciones principales que ya estarán
escritas cuando abras el `editor p5js <https://editor.p5js.org/>`_:

.. figure:: _images/javascript-eg-21.png

Puedes imaginarlo como una película de dibujos animados: ``setup()``
prepara el estudio de animación, y ``draw()`` dibuja cada fotograma,
uno tras otro, muy rápido. Por defecto p5.js dibuja unos 60 fotogramas
por segundo.


Tu primer lienzo
-----------------

Dentro de ``setup()`` vamos a crear el lienzo con ``createCanvas()``. Los
dos números son el ancho y el alto en píxeles:

.. figure:: _images/javascript-eg-22.png

Escribe esto en el `editor p5js <https://editor.p5js.org/>`_ y pulsa el
botón ▶ (Play). Deberías ver un rectángulo gris.
Si lo ves, ¡todo funciona correctamente!


.. admonition:: ¿Qué hace background()?

   ``background()`` rellena todo el lienzo con un color. Si le pasas un
   solo número entre 0 y 255, obtienes un tono de gris: 0 es negro puro y
   255 es blanco puro. Si no pones ``background()`` en ``draw()``, las
   formas que dibujes se acumularán unas sobre otras y verás un rastro.

