:date: 2026-06-23
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Entrega y reto extra
====================
.. parsed-literal::
  
  Paso 8/8 de práctica 1 "Lienzo interactivo"
  
Con todo lo que has aprendido, es el momento de tomar tus propias
decisiones. Aquí tienes la estructura mínima que debe tener tu versión:

.. code-block:: javascript

   function setup() {
     createCanvas(600, 400);
     // Opcional: colorMode(HSB, 360, 100, 100);
   }

   function draw() {
     background( /* tu color de fondo */ );

     // Al menos una variable calculada con map()
     let ??? = map(mouseX, 0, width, ???, ???);

     // Al menos dos formas distintas
     // Forma principal:
     fill( /* tu color */ );
     ellipse( /* o rect() */ );

     // Forma secundaria:
     fill( /* tu color */ );
     ellipse( /* o rect() */ );
   }


Lista de decisiones que debes tomar
-------------------------------------

1. ¿Qué modo de color usas: RGB o HSB?
2. ¿Cuál es el color de tu fondo? ¿Oscuro o claro?
3. ¿Qué formas usas: círculos, cuadrados, rectángulos, mezcla?
4. ¿Qué controla mouseX: el color, el tamaño, la posición de una forma?
5. ¿Qué controla mouseY: el mismo concepto o algo diferente?
6. ¿Cuántas formas tienes en pantalla al mismo tiempo?
7. ¿Tu fondo borra el fotograma anterior o deja rastro (alpha)?


Entrega
-------
Cuando tu composición esté terminada:

* Guarda el proyecto en el editor (necesitas cuenta si quieres guardarlo
  online).
* Copia el enlace del proyecto (botón Compartir / Share en el editor).
* Entrega el enlace respondiendo a las siguientes preguntas:

.. list-table::
   :widths: 40 60
   :header-rows: 0

   * - Título de tu composición
     -
   * - ¿Qué hace mouseX en tu programa?
     -
   * - ¿Qué hace mouseY en tu programa?
     -
   * - ¿Qué modo de color usaste y por qué?
     -
   * - ¿Qué fue lo más difícil de esta práctica?
     -
   * - ¿Qué cambiarías si tuvieras más tiempo?
     -


Reto extra (opcional)
---------------------
¿Quieres ir más allá? Aquí van unas cuantas ideas:

- **frameCount con sin() / cos():** añade ``frameCount`` a tu código para
  crear movimiento autónomo sin necesidad del ratón:

  .. code-block:: javascript

     // sin() devuelve un valor que oscila entre -1 y 1
     // map() lo convierte al rango que necesites
     let oscilacion = map(sin(frameCount * 0.05), -1, 1, 20, 150);
     ellipse(width / 2, height / 2, oscilacion, oscilacion);

- **mouseIsPressed:** haz que tu composición reaccione también al botón
  del ratón. Usa ``mouseIsPressed`` (true/false) para cambiar algo cuando
  se pulsa el botón.

- **Lienzo más grande:** cambia el tamaño del lienzo a 800x600 y añade
  una tercera forma que use tanto ``mouseX`` como ``mouseY`` de una forma
  que no hayas usado antes.


Resumen de lo aprendido en esta práctica
----------------------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Elemento
     - Para qué sirve
   * - ``setup()``
     - Se ejecuta una vez. Aquí se crea el lienzo con ``createCanvas()``.
   * - ``draw()``
     - Se ejecuta en bucle continuo. Aquí se dibuja cada fotograma.
   * - ``background()``
     - Borra el lienzo (o lo oscurece si se añade transparencia).
   * - ``ellipse()`` / ``rect()``
     - Dibujan formas en las coordenadas indicadas.
   * - ``fill()`` / ``stroke()``
     - Establecen el color de relleno y borde antes de dibujar.
   * - ``mouseX`` / ``mouseY``
     - Variables que guardan la posición actual del ratón.
   * - ``map()``
     - Convierte un valor de un rango a otro proporcionalmente.
   * - ``colorMode(HSB,...)``
     - Cambia el modelo de color a Tono / Saturación / Brillo.
