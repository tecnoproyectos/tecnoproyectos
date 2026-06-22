:date: 2026-06-22
:modified: 2026-06-22
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Entradas digitales
==================

VÍDEO: `Pulsadores, entradas digitales en Arduino
<https://www.youtube.com/watch?v=0Ple_lD5zLo>`__

La conexión más sencilla usando el modo PULLUP INTERNO sería
(se podría usar cualquier pin digital, no tiene por qué ser el 8):

.. figure:: _images/arduino-ft-03.png
   :width: 290px
   :align: center

Las instrucciones básicas para los pulsadores en modo PULLUP INTERNO
serían:

.. code-block:: arduino
   :linenos:

   int pinPulsador = 8;
   int valorPulsador;
   
   void setup() {
     // Configura el pin como entrada "PULLUP"
     pinMode(pinPulsador, INPUT_PULLUP);
   }
   
   void loop() {
     // En PULLUP invertimos el valor con ! (NOT)
     valorPulsador = !digitalRead(pinPulsador);
   }

.. note:: 
   El signo ! antes de digitalRead se usa para invertir el valor digital:
   de 0 se transforma en 1 y el 1 se transforma en 0.


Tarea Pulsador_monitor
----------------------
Monta el circuito de la figura anterior.

Crea el programa que se explica en el vídeo anterior que has visualizado
(Pulsadores, entradas digitales en Arduino) para que se muestre en el
monitor serie:

* 1 mientras pulsamos el pulsador
* 0 si no lo pulsamos


Tarea Pulsadores AND
--------------------

VÍDEO: `if, else, AND y OR, variables booleanas y constantes
<https://www.youtube.com/watch?v=mHiiZT8c-t8>`__

.. figure:: _images/arduino-ft-15.png
   :width: 480px
   :align: center

Imagina que tienes que diseñar una máquina para una fábrica.
La máquina es peligrosa si el operario introduce una mano en ella.
Debes diseñarla de tal manera que para que el operario la pueda poner en
marcha, deba pulsar dos pulsadores a la vez, uno con cada mano, de tal
manera de que no le quede ninguna mano libre que pueda introducir por
error en la máquina. El funcionamiento de la máquina lo vamos a simbolizar
con un LED.

Monta el circuito de la figura con dos pulsadores, un LED y una
resistencia de 220Ω.

.. hint::
   Para sacar un 10. Si en vez de con 1 LED lo haces con 3 LEDs que se
   enciendan secuencialmente, tendrás un 10 en la práctica.

El programa sería similar al siguiente:

.. figure:: _images/arduino-ft-16.png
   :width: 641px
   :align: center


Tarea Pulsadores OR
-------------------
Con lo que has aprendido en el vídeo de la tarea anterior, imagina que
tienes que diseñar una máquina y quieres que se pueda poner en marcha
desde un pulsador ubicado en una zona o desde otro pulsador ubicado en
otro lugar.

Monta el mismo circuito de la práctica anterior con dos pulsadores,
un LED y una resistencia de 220Ω.

El programa sería similar al siguiente:

.. figure:: _images/arduino-ft-17.png
   :width: 641px
   :align: center
