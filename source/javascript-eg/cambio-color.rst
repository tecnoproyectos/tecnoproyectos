:date: 2026-06-23
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Modos de color: RGB y HSB
=========================
.. parsed-literal::
  
  Paso 6/8 de práctica 1 "Lienzo interactivo"

Color dinámico con map()
------------------------
Igual que hemos traducido la posición del ratón al tamaño de una forma,
podemos traducirla a los valores de un color. Si usamos ``mouseX`` para el
tono y ``mouseY`` para el brillo, el color de la forma cambia mientras
movemos el ratón.

Hay dos formas habituales de manejar el color en p5.js. Te presentamos las
dos para que elijas la que te resulte más intuitiva.


Opción 1: modo RGB (Rojo, Verde, Azul)
---------------------------------------

Es el modo por defecto. Cada canal va de 0 a 255:

.. code-block:: javascript

   // mouseX controla el R (rojo)
   // mouseY controla el canal B (azul)
   let rojo = map(mouseX, 0, width,  0, 255);
   let azul = map(mouseY, 0, height, 0, 255);

   fill(rojo, 50, azul);


Opción 2: modo HSB (Tono, Saturación, Brillo)
-----------------------------------------------

HSB es más intuitivo para crear degradados de color. El tono (hue) va de
0 a 360 y recorre el arco iris. Para usarlo hay que activarlo con
``colorMode()`` en ``setup()``:

.. code-block:: javascript

   function setup() {
     createCanvas(400, 600);
     colorMode(HSB, 360, 100, 100); // Hue (tono), Saturación, Brillo
   }

   function draw() {
     background(220);

     // mouseX controla el tono
     let tono = map(mouseX, 0, width, 0, 360);

     fill(tono, 80, 90); // ahora en modo HSB
     noStroke();
     ellipse(width / 2, height / 2, 150, 150); // radio fijo
   }

Prueba ambas opciones y quédate con la que más te guste. No hay una
respuesta correcta.


.. admonition:: colorMode()

   Los posibles parámetros de ``colorMode()``, y de cualquier otra función
   de p5.js, están ampliamente descritos en la 
   `documentación oficial de p5.js <https://p5js.org/reference/>`__.

   Es buena práctica recurrir a ella siempre que quieras aprender más.
