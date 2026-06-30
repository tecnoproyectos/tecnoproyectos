:date: 2026-06-28
:modified: 2026-06-28
:author: Esther Gordo
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/

Explosión en destello: variable booleana
========================================

.. parsed-literal::

   Paso 2/5 de práctica 3 "Fuegos artificiales"

Cuando el cohete alcanza su punto más alto (``vy > 0``, es decir, empieza
a caer), queremos que explote. La primera versión es un destello simple:
un círculo que crece rápidamente en el punto de explosión.

Dos propiedades nuevas en el objeto
-------------------------------------

Añadimos al objeto ``cohete`` dos propiedades nuevas:

- ``explotado`` — booleano que indica si el cohete ya ha llegado al
  punto más alto. Empieza en ``false`` (es decir, no ha explotado)
  y se pone a ``true`` cuando ``vy > 0``.
- ``radioDest`` — radio del círculo de destello. Empieza en ``0`` y
  crece cada fotograma tras la explosión.

.. figure::
   _images/javascript-eg-303.png
   :width: 600px
   :align: center


.. admonition:: ¿Por qué necesitamos un booleano?

   ``draw()`` se ejecuta decenas de veces por segundo. Sin
   ``cohete.explotado``, el programa detectaría ``vy > 0`` en cada
   fotograma y intentaría explotar continuamente. El booleano actúa
   como interruptor: una vez puesto a ``true``, la explosión solo
   ocurre una vez.


La lógica de explosión en draw()
----------------------------------

En ``draw()``, después de mover el cohete, comprobamos si ha llegado al
punto más alto. Si es así, marcamos ``explotado = true``. Luego
dibujamos el cohete o el destello según el estado:

Mover el cohete solo si no ha explotado:

.. figure::
   _images/javascript-eg-304.png
   :width: 600px
   :align: center


Dibujar cohete o destello según el estado:

.. figure::
   _images/javascript-eg-305.png
   :width: 600px
   :align: center

.. admonition:: Experimenta

   Cambia el incremento de ``radioDest`` (ahora ``4``) a ``8`` o a
   ``2``. ¿Cómo afecta a la velocidad de expansión?

   Añade una condición para que el destello desaparezca cuando
   ``radioDest`` supere 80 y el cohete se reinicie:

   .. code-block:: javascript

      if (cohete.radioDest > 80) {
        cohete.radioDest = 0;
        cohete.explotado = false;
        cohete.y  = height;
        cohete.vy = random(-10, -5);
      }
