:date: 2026-06-20
:modified: 2026-06-20
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Variables
=========

Para declarar una variable global de tipo entero (“integer” en inglés)
llamada pinLED, usamos el comando:

.. code-block:: arduino
   :linenos:

   int pinLED = 13;

VÍDEO: `Variables con Arduino IDE
<https://www.youtube.com/watch?v=safEHD4d2Q4>`__


Tarea Variables
---------------
Monta el circuito de la figura:

.. figure:: _images/arduino-03.png
   :align: center

Realiza el mismo circuito y mismo programa de la tarea anterior,
pero usa las siguientes variables:

* **pinLed**: número de pin donde está conectado el LED.
* **delayOn**: tiempo que está encendido del LED
* **delayOff**: tiempo que está apagado del LED
* **finalDelay**: tiempo final

Prueba después a ir cambiando el tiempo de encendido y apagado del LED,
verás cómo es más rápido ahora usando las variables.

Sería el código equivalente al siguiente programa:

.. figure:: _images/arduino-06.png
   :width: 320px