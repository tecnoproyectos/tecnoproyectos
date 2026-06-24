:date: 2026-06-23
:modified: 2026-06-23
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Componer más de una forma
=========================
Hasta ahora tenemos una forma que reacciona al ratón. Vamos a añadir formas
secundarias para crear una composición. Aquí es donde entra en juego tu
decisión estética personal.

Algunas ideas para formas secundarias:

- Una forma que sigue al ratón pero con la mitad de tamaño
- Una forma en la posición simétrica al ratón
  (``width - mouseX``, ``height - mouseY``)
- Una forma fija en el centro que cambia solo de color
- Varias formas pequeñas repartidas por el lienzo con colores derivados del
  tono principal

Es el momento de tomar tus propias decisiones. A continuación te mostramos
dos propuestas completas distintas para que veas cómo la misma estructura
puede producir resultados muy diferentes. **No copies ninguna: úsalas como
inspiración para crear la tuya.**


Propuesta A - colores complementarios
-------------------------------------
Usa el modo HSB para crear tres círculos con colores separados 120 grados
en el arco iris. El ratón controla el tono principal y el tamaño general:

.. code-block:: javascript

   function setup() {
     createCanvas(600, 400);
     colorMode(HSB, 360, 100, 100);
   }

   function draw() {
     background(240, 20, 10); // fondo casi negro azulado

     let tono   = map(mouseX, 0, width,  0, 360);
     let tamaño = map(mouseY, 0, height, 30, 180);

     noStroke();

     // Luna central: color principal
     fill(tono, 80, 90);
     ellipse(width / 2, height / 2, tamaño, tamaño);

     // Luna izquierda: 120 grados de diferencia
     fill((tono + 120) % 360, 70, 80);
     ellipse(width / 2 - 160, height / 2, tamaño * 0.6, tamaño * 0.6);

     // Luna derecha: 240 grados de diferencia
     fill((tono + 240) % 360, 70, 80);
     ellipse(width / 2 + 160, height / 2, tamaño * 0.6, tamaño * 0.6);

     // Reflejo: simetría vertical del ratón
     fill(tono, 50, 60, 0.4);
     ellipse(mouseX, mouseY, tamaño * 0.3, tamaño * 0.3);
   }

.. note::

   El operador ``% 360`` hace que el tono vuelva a 0 si supera 360,
   recorriendo el arco iris de forma cíclica sin salirse del rango.


Propuesta B - Cuadrados con rastro
----------------------------------

Usa el modo RGB con un fondo semitransparente que crea un efecto de rastro:

.. code-block:: javascript

   function setup() {
     createCanvas(600, 400);
     // Modo RGB por defecto, no hace falta colorMode()
   }

   function draw() {
     // background con transparencia: crea un rastro que se desvanece
     background(15, 15, 30, 40);

     let rojo   = map(mouseX, 0, width,  50, 255);
     let verde  = map(mouseY, 0, height, 50, 200);
     let tamaño = map(mouseX, 0, width,  20, 120);

     noFill();
     strokeWeight(2); // grosor de 2 píxeles para el borde

     // Cuadrado principal en la posición del ratón
     stroke(rojo, verde, 100);
     rect(mouseX - tamaño / 2, mouseY - tamaño / 2, tamaño, tamaño);

     // Cuadrado secundario, posición simétrica
     stroke(255 - rojo, 255 - verde, 200);
     let tam2 = tamaño * 0.6;
     rect(width - mouseX - tam2 / 2, height - mouseY - tam2 / 2, tam2, tam2);

     // Cuadrado central fijo
     stroke(rojo, 150, verde);
     rect(width / 2 - 30, height / 2 - 30, 60, 60);
   }


.. note::

   ``background(15, 15, 30, 40)`` usa un cuarto valor
   (alfa = transparencia).
   En lugar de borrar el lienzo completamente, lo oscurece ligeramente,
   creando un rastro de las posiciones anteriores del ratón. Prueba a
   cambiar este valor para comparar los resultados.
