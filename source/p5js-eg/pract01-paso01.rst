:date: 2026-06-23
:modified: 2026-06-23
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Práctica 01 — Paso 1: La estructura base, setup() y draw()
===========================================================

Concepto: el bucle de dibujo
------------------------------

Todo programa en p5.js tiene dos funciones principales que ya estarán
escritas cuando abras el editor:

.. code-block:: javascript

   function setup() {
     // se ejecuta UNA SOLA VEZ al inicio del programa
   }

   function draw() {
     // se ejecuta CONTINUAMENTE, muchas veces por segundo
   }

Puedes imaginarlo como una película de dibujos animados: ``setup()`` prepara
el estudio de animación, y ``draw()`` dibuja cada fotograma, uno tras otro,
muy rápido. Por defecto p5.js dibuja unos 60 fotogramas por segundo.


Tu primer lienzo
-----------------

Dentro de ``setup()`` vamos a crear el lienzo con ``createCanvas()``. Los
dos números son el ancho y el alto en píxeles:

.. code-block:: javascript

   function setup() {
     createCanvas(400, 600); // ancho x alto
   }

   function draw() {
     background(220); // fondo gris claro
   }

Escribe esto en el editor y pulsa el botón ▶ (Play). Deberías ver un
rectángulo gris. Si lo ves, ¡todo funciona correctamente!


.. admonition:: ¿Qué hace background()?

   ``background()`` rellena todo el lienzo con un color. Si le pasas un
   solo número entre 0 y 255, obtienes un tono de gris: 0 es negro puro y
   255 es blanco puro. Si no pones ``background()`` en ``draw()``, las
   formas que dibujes se acumularán unas sobre otras y verás un rastro.
