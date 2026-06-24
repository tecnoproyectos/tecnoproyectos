:date: 2026-06-23
:modified: 2026-06-23
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Práctica 01 — Paso 4: La función map(), traducir rangos
========================================================

Concepto: map()
----------------

``mouseX`` va de 0 (izquierda) a 400 (derecha, si el lienzo mide 400 px de
ancho). Pero el tamaño de una forma puede ir de 20 a 200, o un valor de
color va de 0 a 255. Necesitamos traducir un rango a otro. Para eso existe
``map()``:

.. code-block:: javascript

   // map(valor, inicio_original, fin_original, inicio_nuevo, fin_nuevo)
   // Ejemplo: si mouseX va de 0 a 400
   // y queremos que el tamaño vaya de 20 a 200
   tamaño = map(mouseX, 0, 400, 20, 200)

Puedes leerlo así: «si mouseX vale 0, tamaño vale 20; si mouseX vale 400,
tamaño vale 200; y cualquier valor intermedio se calcula
proporcionalmente».


Aplícalo a tu código
---------------------

.. code-block:: javascript

   function setup() {
     createCanvas(400, 600); // ancho x alto
   }

   function draw() {
     background(220);

     fill("Turquoise"); // color turquesa en inglés
     noStroke();

     // el tamaño depende de la posición horizontal del ratón
     let tamaño = map(mouseX, 0, 400, 20, 200);

     // posición del centro del círculo fija en el centro del lienzo
     ellipse(width / 2, height / 2, tamaño, tamaño);
   }


.. admonition:: width y height

   En lugar de escribir 400 y 600 (los valores concretos de tu lienzo),
   puedes usar las variables ``width`` y ``height`` que p5.js actualiza
   automáticamente. Así tu código funciona igual aunque cambies el tamaño
   del lienzo.
