:date: 2026-06-25
:modified: 2026-06-25
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Partícula rebotando: variables, random() e if
==============================================
.. parsed-literal::

  Paso 1/4 de práctica 2 "Partículas conectadas"

En esta práctica vas a crear una simulación de partículas en movimiento
que se conectan entre sí cuando están cerca. El resultado es una red
animada que cambia continuamente, similar a las visualizaciones que
aparecen en fondos de pantalla o en gráficos de datos en movimiento.

Empezamos con lo más sencillo: **una única partícula** que se desplaza
por el lienzo y rebota en los bordes.

.. note::

   Este tutorial presupone que conoces ``setup()``, ``draw()``,
   ``background()``, ``circle()``, ``stroke()``, ``fill()`` y ``random()``.
   Si alguno de estos conceptos te resulta poco familiar, repasa la
   práctica 1 antes de continuar.


Posición y velocidad
---------------------

La partícula tiene cuatro variables: su posición (``x``, ``y``) y su
velocidad (``vx``, ``vy``). En cada fotograma sumamos la velocidad a la
posición, y la partícula se desplaza:

.. code-block:: javascript

   // Variables globales: posición y velocidad de una partícula
   let x, y;
   let vx, vy;

   function setup() {
     createCanvas(windowWidth, windowHeight);
     // Posición inicial: centro del lienzo
     x = width / 2;
     y = height / 2;
     // Velocidad inicial aleatoria (entre -3 y 3 píxeles por fotograma)
     vx = random(-3, 3);
     vy = random(-3, 3);
   }

   function draw() {
     background(255);
     // Mover la partícula sumando la velocidad a la posición
     x = x + vx;
     y = y + vy;
     // Dibujar la partícula
     noStroke();
     fill(0);
     circle(x, y, 6);
   }

Ejecuta el código. Verás una partícula que sale disparada en una
dirección aleatoria... y desaparece por el borde. Necesitamos que rebote.


El rebote con if
-----------------

Para que la partícula rebote invertimos su velocidad cuando toca un borde.
Si sale por la derecha (``x > width``), ``vx`` se vuelve negativa y la
partícula empieza a moverse hacia la izquierda. Es como una pelota que
choca contra una pared:

.. code-block:: javascript

   function draw() {
     background(255);
     // Mover
     x = x + vx;
     y = y + vy;
     // Rebotar al tocar los bordes
     if (x < 0 || x > width)  { vx = -vx; }
     if (y < 0 || y > height) { vy = -vy; }
     // Dibujar
     noStroke();
     fill(0);
     circle(x, y, 6);
   }

Ahora la partícula rebota indefinidamente sin salirse del lienzo.

.. admonition:: ¿Qué hace el operador ||?

   ``||`` significa «o». La condición ``x < 0 || x > width`` se lee:
   «si x es menor que 0 **o** x es mayor que el ancho del lienzo».
   Basta con que una de las dos sea verdadera para que se ejecute
   lo que hay dentro de las llaves.


.. admonition:: Experimenta

   Prueba a cambiar el rango de ``random(-3, 3)`` a ``random(-8, 8)``.
   ¿Qué efecto tiene sobre el movimiento?
   ¿Y si usas ``random(1, 3)`` sin valores negativos?
