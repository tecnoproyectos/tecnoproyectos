:date: 2026-06-22
:modified: 2026-06-22
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Comunicación serie II
=====================

VÍDEO: `Comunicación serial: enviando información a Arduino
<https://www.youtube.com/watch?v=FmVy-vH9oqY>`__

Para esperar hasta que Arduino reciba nuestro mensaje:

.. code-block:: arduino
   :linenos:

   while (Serial.available() == 0) {
      // Mientras no haya respuesta ( == 0)
      // No hacer nada
   }

Para guardar en la variable "brillo" el número entero que hemos escrito
como respuesta:

.. code-block:: arduino
   :linenos:

   int brillo;

   brillo = Serial.parseInt();  // Guarda la respuesta en brillo


Tarea pedir nivel de brillo
---------------------------
Monta el circuito de la figura:

.. figure:: arduino-ft/arduino-03.png
   :align: center

realiza un programa en Arduino IDE que haga el algoritmo de los bloques
siguientes:

.. figure:: arduino-ft/arduino-12.png
   :width: 765px


Tarea pedir numero de parpadeos
-------------------------------
Con el mismo circuito que la práctica anterior, realiza un programa que
te pida el número de parpadeos de LED que quieras, una vez que introduzcas
el número, el LED parpadeará ese número de veces.

Si necesitas ayuda, puedes guiarte con el siguiente programa de bloques:

.. figure:: arduino-ft/arduino-13.png
   :width: 964px
