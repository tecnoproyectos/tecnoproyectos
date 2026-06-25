:date: 2026-06-25
:modified: 2026-06-25
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Varias partículas rebotando: arrays y for
==========================================
.. parsed-literal::

  Paso 2/4 de práctica 2 "Partículas conectadas"

Ahora queremos 50 partículas en lugar de una. Podríamos crear 50 variables
(``x1``, ``x2``, ``x3``...), pero eso es inviable. Necesitamos dos
herramientas nuevas: el **array** y el **bucle for**.


El array: una lista de valores
-------------------------------

Un array es una lista numerada que agrupa muchos valores bajo un mismo
nombre:

.. code-block:: javascript

   let nombres = ['Ana', 'Luis', 'María']; // array de textos
   let edades  = [17, 16, 18];             // array de números

   // Acceder a un elemento: nombre_del_array[índice]
   // El índice empieza en 0, no en 1
   console.log(nombres[0]); // 'Ana'
   console.log(edades[2]);  // 18

Para guardar la posición y velocidad de 50 partículas usaremos
**cuatro arrays paralelos**: uno para cada dato. El índice ``i``
identifica a la misma partícula en todos ellos:

.. code-block:: javascript

   let nb  = 50; // número de partículas
   let px  = []; // posición x de cada partícula
   let py  = []; // posición y
   let pvx = []; // velocidad horizontal
   let pvy = []; // velocidad vertical


El bucle for: inicializar todas las partículas
-----------------------------------------------

El bucle ``for`` recorre los índices de 0 a ``nb - 1`` y ejecuta el
código interior una vez por partícula. Lo usamos en ``setup()`` para
dar valores iniciales a los cuatro arrays:

.. code-block:: javascript

   function setup() {
     createCanvas(windowWidth, windowHeight);
     for (let i = 0; i < nb; i = i + 1) {
       px[i]  = width / 2;
       py[i]  = height / 2;
       pvx[i] = random(-3, 3);
       pvy[i] = random(-3, 3);
     }
   }


El bucle for en draw(): mover y dibujar
----------------------------------------

El mismo patrón se repite en ``draw()``: recorremos todas las partículas
para moverlas, hacerlas rebotar y dibujarlas:

.. code-block:: javascript

   function draw() {
     background(255);
     noStroke();
     fill(0);
     for (let i = 0; i < nb; i = i + 1) {
       px[i] = px[i] + pvx[i];
       py[i] = py[i] + pvy[i];
       if (px[i] < 0 || px[i] > width)  { pvx[i] = -pvx[i]; }
       if (py[i] < 0 || py[i] > height) { pvy[i] = -pvy[i]; }
       circle(px[i], py[i], 6);
     }
   }

.. admonition:: El bucle for aparece dos veces, con el mismo patrón

   Una vez en ``setup()`` para crear todas las partículas, y otra en
   ``draw()`` para moverlas y dibujarlas. En los dos casos el recorrido
   es idéntico: de ``i = 0`` hasta ``i < nb``.

.. admonition:: Experimenta

   Cambia ``nb`` a 200. El programa funciona igual, solo con cambiar
   un número. Esa es la ventaja del array combinado con el bucle.
