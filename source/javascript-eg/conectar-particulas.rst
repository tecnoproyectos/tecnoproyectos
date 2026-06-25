:date: 2026-06-25
:modified: 2026-06-25
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Conectamos partículas: dist() y for anidado
============================================
.. parsed-literal::

  Paso 3/4 de práctica 2 "Partículas conectadas"

Las partículas ya se mueven y rebotan. Ahora vamos a dibujar una línea
entre cada dos partículas que estén cerca. Para eso necesitamos dos cosas:
la función ``dist()`` y un **bucle for dentro de otro bucle for**.


dist(): la distancia entre dos puntos
--------------------------------------

``dist(x1, y1, x2, y2)`` es una función de p5.js que devuelve la distancia
en píxeles entre los puntos (x1, y1) y (x2, y2). Calcula internamente lo
mismo que el teorema de Pitágoras, pero sin que tengamos que escribirlo:

.. code-block:: javascript

   let d = dist(px[i], py[i], px[j], py[j]);
   // d es la distancia en píxeles entre la partícula i y la partícula j


El for anidado: comparar cada partícula con todas las demás
------------------------------------------------------------

Para comprobar si dos partículas están cerca necesitamos compararlas
de dos en dos. Eso requiere un bucle dentro de otro: el exterior recorre
la primera partícula (``i``), y el interior recorre la segunda (``j``).
En lenguaje natural: «para cada partícula i, compruebo su distancia con
cada partícula j»:

.. code-block:: javascript

   let dMin = 100; // distancia máxima para trazar una línea

   for (let i = 0; i < nb; i = i + 1) {
     for (let j = 0; j < nb; j = j + 1) {
       let d = dist(px[i], py[i], px[j], py[j]);
       if (d < dMin) {
         line(px[i], py[i], px[j], py[j]);
       }
     }
   }

Este bloque va dentro de ``draw()``, después del bucle que mueve y
dibuja las partículas.


El programa completo
---------------------

.. code-block:: javascript

   let nb   = 50;
   let px   = [];
   let py   = [];
   let pvx  = [];
   let pvy  = [];
   let dMin = 100;

   function setup() {
     createCanvas(windowWidth, windowHeight);
     for (let i = 0; i < nb; i = i + 1) {
       px[i]  = width / 2;
       py[i]  = height / 2;
       pvx[i] = random(-3, 3);
       pvy[i] = random(-3, 3);
     }
   }

   function draw() {
     background(255);
     // Mover y dibujar partículas
     noStroke();
     fill(0);
     for (let i = 0; i < nb; i = i + 1) {
       px[i] = px[i] + pvx[i];
       py[i] = py[i] + pvy[i];
       if (px[i] < 0 || px[i] > width)  { pvx[i] = -pvx[i]; }
       if (py[i] < 0 || py[i] > height) { pvy[i] = -pvy[i]; }
       circle(px[i], py[i], 6);
     }
     // Conectar partículas cercanas
     stroke(0);
     for (let i = 0; i < nb; i = i + 1) {
       for (let j = 0; j < nb; j = j + 1) {
         let d = dist(px[i], py[i], px[j], py[j]);
         if (d < dMin) {
           line(px[i], py[i], px[j], py[j]);
         }
       }
     }
   }

.. admonition:: Nota de rendimiento

   Con ``nb = 50`` partículas, el bucle anidado realiza 50 × 50 = 2.500
   comparaciones por fotograma. Si aumentas ``nb`` a 200 o más y el
   programa va lento, reduce ``nb`` o ``dMin``.

.. admonition:: Experimenta

   Prueba a cambiar ``dMin`` a 50 y luego a 200. ¿Qué efecto tiene sobre
   la red de conexiones?
