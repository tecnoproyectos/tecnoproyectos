:date: 2026-06-25
:modified: 2026-06-25
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Hazlo tuyo y entrega
=====================
.. parsed-literal::

  Paso 4/4 de práctica 2 "Partículas conectadas"

El programa está completo. Ahora es tu turno de tomar decisiones para
diferenciarlo. Aquí tienes ideas ordenadas de menor a mayor dificultad.


Color
------

Cambia el fondo a negro y las partículas a blanco: las líneas de conexión
quedan con un aspecto completamente distinto:

.. code-block:: javascript

   background(0);
   fill(255);
   stroke(255);

Para añadir color a las partículas puedes usar el modo HSB que viste en
`Paso 6/8 (práctica1 Lienzo interactivo) — Cambio de color <cambio-color.html>`_. Asigna a cada
partícula un tono aleatorio al inicializarla y úsalo al dibujarla.

Haz que las líneas sean más transparentes cuanto mayor sea la distancia
entre las partículas. El cuarto parámetro de ``stroke()`` es el alfa
(0 = transparente, 255 = opaco):

.. code-block:: javascript

   stroke(0, map(d, 0, dMin, 200, 0));

.. warning::
  Vigila dónde colocar cada línea de código

Movimiento autónomo
--------------------

Puedes usar ``frameCount`` con ``sin()`` para hacer que las partículas
«palpiten», variando su tamaño de forma cíclica. Es el mismo recurso que
viste en `Paso 8/8 — Entrega y reto extra <entrega.html>`_ de la
práctica 1:

.. figure::
  _images/javascript-eg-208.png
  :width: 600px
  :align: center

.. code-block:: javascript

   // El tamaño oscila entre 4 y 12 píxeles de forma continua
   let pulso = map(sin(frameCount * 0.05), -1, 1, 4, 12);
   circle(px[i], py[i], pulso);

Varía ``dMin`` con la posición horizontal del ratón para que las líneas
de conexión cambien en tiempo real:

.. code-block:: javascript

   dMin = map(mouseX, 0, width, 30, 200);


Interacción con el teclado
---------------------------

Añade la función ``keyPressed()`` para que al pulsar una tecla todas las
partículas vuelvan al centro con velocidades nuevas, como si se
regeneraran:

.. figure::
  _images/javascript-eg-209.png
  :width: 400px
  :align: center


Mientras no se pulse ninguna tecla, las partículas siguen moviéndose
con normalidad. Al pulsar cualquier tecla, se reinician desde el centro.


Entrega
--------

Cuando tu composición esté terminada:

* Guarda el proyecto en el editor (necesitas cuenta para guardarlo online).
* Copia el enlace del proyecto (botón Share en el editor).
* Entrega el enlace respondiendo a las preguntas de esta ficha:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - Título de tu composición
     -
   * - ¿Hasta qué paso llegaste?
     -
   * - ¿Qué efecto produce cambiar dMin? Describe un valor concreto que hayas probado.
     -
   * - ¿Qué variación añadiste respecto al programa base?
     -
   * - ¿Qué fue lo más difícil de esta práctica?
     -
   * - ¿Qué añadirías si tuvieras más tiempo?
     -


Resumen de lo aprendido en esta práctica
-----------------------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Elemento
     - Para qué sirve
   * - ``let px = []``
     - Declara un array vacío para guardar una lista de valores.
   * - ``px[i]``
     - Accede al elemento i del array (el índice empieza en 0).
   * - ``for (let i = 0; i < nb; i = i + 1)``
     - Repite el bloque nb veces, con i tomando los valores 0, 1, 2...
   * - ``if (x < 0 || x > width)``
     - Ejecuta el bloque si x sale por cualquiera de los dos bordes.
   * - ``random(a, b)``
     - Devuelve un número aleatorio entre a y b.
   * - ``dist(x1, y1, x2, y2)``
     - Calcula la distancia en píxeles entre dos puntos.
   * - For anidado
     - Un bucle for dentro de otro: compara cada partícula con todas las demás.
   * - ``keyPressed()``
     - Función que se ejecuta automáticamente al pulsar cualquier tecla.
