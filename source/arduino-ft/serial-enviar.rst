:date: 2026-06-22
:modified: 2026-06-24
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Comunicación serie II
=====================

|icono-video| VÍDEO: `Comunicación serial: enviando información a Arduino
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

.. figure:: _images/arduino-ft-03.png
   :align: center

realiza un programa en Arduino IDE que haga el algoritmo de los bloques
siguientes:

.. figure:: _images/arduino-ft-12.png
   :align: center
   :width: 765px


Tarea pedir numero de parpadeos
-------------------------------
Con el mismo circuito que la práctica anterior, realiza un programa que
te pida el número de parpadeos de LED que quieras, una vez que introduzcas
el número, el LED parpadeará ese número de veces.

Si necesitas ayuda, puedes guiarte con el siguiente programa de bloques:

.. figure:: _images/arduino-ft-13.png
   :align: center
   :width: 964px



.. |icono-video| image:: _images/arduino-ft-video.png
   :alt: Icono de vídeo de YouTube
   :height: 32px