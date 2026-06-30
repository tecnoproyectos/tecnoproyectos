:date: 2026-06-28
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Hazlo tuyo: fuegos artificiales
===============================

.. parsed-literal::

   Paso 5/5 de práctica 3 "Fuegos artificiales"

El programa está completo. Ahora es tu turno de tomar decisiones para
diferenciarlo. Ordena las ideas de menor a mayor dificultad.


Color
------

El código ya usa ``colorMode(HSB)``. Experimenta con los valores de
saturación y brillo de cada chispa para conseguir efectos distintos:
chispas pálidas (baja saturación) o muy brillantes (brillo 100).

Haz que las chispas cambien de tono según su vida, usando ``map()``
como viste en la práctica 1 `Color que cambia con el ratón <cambio-color>`_:

.. code-block:: javascript

   // El tono va del naranja (30) al rojo (0) conforme la chispa se apaga
   let tonoChispa = map(ch.vida, 0, 255, 0, 60);
   stroke(tonoChispa, 90, 100, ch.vida);


Comportamiento
---------------

Cambia el fondo de ``background(0, 0, 0, 40)`` a
``background(240, 30, 10, 40)`` para un cielo oscuro con toque azulado.

Haz que la potencia del cohete dependa de la posición vertical del clic:
cuanto más abajo hagas clic, más sube el cohete:

.. code-block:: javascript

   vy: map(mouseY, 0, height, -4, -10)

Lanza un cohete automáticamente cada 90 fotogramas, además de los
cohetes manuales. Puedes usar ``frameCount`` como viste en la
`Entrega y reto extra de la práctica 1 <entrega>`_ de la práctica 1:

.. code-block:: javascript

   // En draw(), antes del bucle de cohetes:
   if (frameCount % 90 === 0) {
     cohetes.push({
       x:         random(width),
       y:         height,
       vx:        random(-2, 2),
       vy:        random(-10, -6),
       tono:      random(360),
       explotado: false,
       chispas:   []
     });
   }


Ampliación
-----------

Añade una propiedad ``tipo`` a cada cohete (``"estrella"`` o
``"cascada"``) y cambia la distribución de velocidades de las chispas
según el tipo. En ``"cascada"`` las chispas tienen ``vy`` siempre
positiva, de modo que caen hacia abajo desde el punto de explosión:

.. code-block:: javascript

   // En explotar(), según el tipo:
   vy: c.tipo === "cascada" ? random(1, 5) : random(-4, 4)


Entrega
--------

Cuando tu composición esté terminada:

- Guarda el proyecto en el editor de p5.js (necesitas cuenta para guardarlo
  online).
- Copia el enlace del proyecto (botón Share en el editor).
- Entrega el enlace respondiendo a las preguntas de la ficha:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - Título de tu composición
     -
   * - ¿Qué diferencia notaste al usar un objeto en lugar de variables sueltas?
     -
   * - ¿Qué variación añadiste en "Hazlo tuyo"?
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
   * - ``{ }``
     - Agrupa propiedades relacionadas en un objeto literal.
   * - ``objeto.propiedad``
     - Accede o modifica una propiedad con notación de punto.
   * - ``array.push({ })``
     - Añade un objeto nuevo al final del array.
   * - ``array.splice(i, 1)``
     - Elimina el elemento en la posición ``i`` del array.
   * - ``vida`` / alfa
     - Hace las chispas más transparentes conforme se apagan.
   * - ``explotado``
     - Booleano que actúa como interruptor de un solo uso en ``draw()``.
   * - ``mousePressed()``
     - Se ejecuta cada vez que se hace clic; aquí lanza un cohete nuevo.
   * - Bucle al revés
     - Recorrer el array de ``length-1`` a ``0`` permite borrar elementos
       sin saltarse ninguno.
   * - Función auxiliar
     - Extraer lógica repetida a una función hace ``draw()`` más corto
       y el código más fácil de ampliar.
