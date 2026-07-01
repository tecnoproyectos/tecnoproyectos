:date: 2026-06-23
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Interacción: mouseX y mouseY
============================
.. parsed-literal::
  
  Paso 4/8 de práctica 1 "Lienzo interactivo"

Variables del sistema
---------------------
p5.js actualiza automáticamente dos variables especiales en cada fotograma:

* ``mouseX`` — contiene la posición horizontal del ratón en el lienzo
  (en píxeles)
* ``mouseY`` — contiene la posición vertical del ratón en el lienzo
  (en píxeles)

Puedes usar estas variables en cualquier parte de ``draw()``. Como
``draw()`` se ejecuta continuamente, el valor cambia con el ratón y el
resultado se actualiza en tiempo real.


Haz que la forma siga al ratón
------------------------------

Sustituye las coordenadas fijas de ``ellipse()`` por ``mouseX`` y
``mouseY``:

.. code-block:: javascript

   function setup() {
     createCanvas(400, 600); // ancho x alto
   }

   function draw() {
     background(220);

     fill("Crimson"); // color carmesí en inglés
     noStroke();
     ellipse(mouseX, mouseY, 80, 80); // X e Y del centro son las del ratón
   }

Mueve el ratón por el lienzo. El círculo te sigue. Esto ocurre porque
``draw()`` redibuja el lienzo 60 veces por segundo usando el valor
actualizado de ``mouseX`` y ``mouseY``.
