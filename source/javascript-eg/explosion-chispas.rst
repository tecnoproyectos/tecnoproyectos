:date: 2026-06-28
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Explosión con chispas: push() y splice()
========================================

.. parsed-literal::

   Paso 3/5 de práctica 3 "Fuegos artificiales"

El destello del paso anterior es sencillo pero poco realista. Ahora vamos
a crear una **lluvia de chispas**: cuando el cohete explote, que se generen
60 puntos que salgan disparados en todas direcciones, que caigan por la gravedad
y se desvanezcan poco a poco hasta desaparecer.

Para ello necesitamos dos herramientas nuevas: ``push()`` para añadir
elementos a un array, y ``splice()`` para eliminarlos.

Un array de chispas dentro del objeto cohete
---------------------------------------------

Añadimos una propiedad nueva al objeto: ``cohete.chispas``, que es un
array vacío. Cada chispa será a su vez un objeto con posición, velocidad
y vida:

.. code-block:: javascript

   function setup() {
     createCanvas(windowWidth, windowHeight);
     cohete.x         = width / 2;
     cohete.y         = height;
     cohete.vx        = random(-2, 2);
     cohete.vy        = random(-10, -5);
     cohete.explotado = false;
     cohete.tono      = random(360);
     cohete.chispas   = []; // array vacío: se llenará al explotar
   }


Crear las chispas con push()
-----------------------------

Cuando el cohete alcanza su punto más alto, llenamos el array de chispas
con ``push()``. Cada llamada a ``push()`` añade un elemento al final del
array. Las 60 chispas se crean de golpe en un bucle ``for``:

.. figure::
   _images/javascript-eg-306.png
   :width: 400px
   :align: center

.. note::
    Compara el *for* del bloque de código anterior con este:

    .. figure::
       _images/javascript-eg-307.png
       :width: 300px
       :align: center

  ¿Son iguales? ¿Qué diferencias ves? ¿Cuál te parece más claro y fácil de entender?


Mover y borrar chispas con splice()
-------------------------------------

En cada fotograma movemos todas las chispas, reducimos su ``vida`` y
las dibujamos. Cuando ``vida`` llega a 0 las eliminamos del array con
``splice()``.

El bucle recorre el array **al revés** (de ``length - 1`` hasta ``0``)
para que al eliminar una chispa no se salten las siguientes:

.. figure::
    _images/javascript-eg-308.png
   :width: 400px
   :align: center


.. admonition:: ¿Por qué al revés?

   Si recorriéramos el *array* de 0 hacia adelante y elimináramos el
   elemento ``i``, el siguiente elemento pasaría a ocupar la posición
   ``i`` y el bucle lo saltaría. Recorriendo al revés, los índices que
   aún no hemos visitado no cambian al eliminar uno.

.. note:: 
  *splice()* recibe dos parámetros: el índice del elemento a 
  eliminar y el número de elementos a eliminar. 
  En nuestro caso, siempre eliminamos un solo elemento, 
  así que el segundo parámetro es ``1``.

  La función *pop()* también elimina elementos de un array, 
  pero solo el último. 
  

El programa completo con un cohete y chispas
---------------------------------------------

.. figure::
   _images/javascript-eg-309.png
   :width: 600px
   :align: center


.. admonition:: Experimenta

   Cambia el número de chispas de ``60`` a ``120``. ¿Qué efecto tiene?
   Prueba también a cambiar ``ch.vida -= 4`` a ``ch.vida -= 8``:
   ¿las chispas duran más o menos?

   Prueba a cambiar el modo de color de RGB a HSB, necesitarías 
   una nueva variable para variar el tono de las chispas. 
   ¿Podrías hacer que cada chispa tenga un color distinto?
