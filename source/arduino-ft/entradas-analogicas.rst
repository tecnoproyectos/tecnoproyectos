:date: 2026-06-22
:modified: 2026-06-22
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Entradas analógicas
===================
.. figure:: _images/arduino-ft-18.png
   :width: 153px
   :align: right

:index:`LDR` (Fotorresistencia o Light Dependent Resistor)
   Es una resistencia que varía con la luz.
   Cuanta más luz recibe, más corriente deja pasar.
   Por lo tanto, cuanta más luz recibe tiene menos resistencia.

La conexión eléctrica forma un divisor de tensión:

.. figure:: _images/arduino-ft-19.png
   :width: 600px
   :align: center

.. figure:: _images/arduino-ft-20.png
   :width: 320px
   :align: center


Instrucciones básicas para una LDR (fotorresistencia):

.. code-block:: arduino
   :linenos:

   int pinLDR = A0;
   int valorLuz;
   
   void setup() {
     // Configuramos el pin como entrada
     pinMode(pinLDR, INPUT);
   }
   
   void loop() {
     // Guardamos el valor de entrada en valorLuz
     valorLuz = analogRead(pinLdr);
   }

Módulos LDR
-----------
Existen módulos LDR de 3 pines con potenciómetro en los que no hace falta
conectar la resistencia porque ya la lleva incorporada, además de un
potenciómetro para calibrarla.

.. figure:: _images/arduino-ft-21.png
   :width: 320px
   :align: center

Pines y su conexión a la placa Arduino:

* **Vcc**: a 5V de Arduino
* **GND**: a GND de Arduino
* **DO**: (data output) a entrada analógica de Arduino


Tarea LDR monitor
-----------------

VÍDEO: `Entradas digitales en Arduino. LDR y monitor serie
<https://www.youtube.com/watch?v=Vd1G-iW1Jx8>`__

Monta el siguiente circuito con Arduino y siguiendo las instrucciones
del vídeo realiza un programa para visualizar en el monitor serie cómo
detecta la LDR el nivel de luz.

.. figure:: _images/arduino-ft-22.png
   :width: 320px
   :align: center


Tarea Sensor de luz LEDs
------------------------

VÍDEO: `Arduino: Sensor de luz con LEDs
<https://www.youtube.com/watch?v=_TE2JDuPRSs>`__

Monta el circuito de la imagen y realiza el programa de un sensor de luz
que muestre con una luz verde un nivel normal de luz y se encienda una
luz roja de alarma en el caso de una luz muy brillante como sería la luz
directa sobre la LDR de la linterna del móvil.

.. hint::
   Para sacar un 10: el LED rojo deberá parpadear para lograr el 10
   en la práctica.

Necesitarás dos resitencias de 220Ω para los LEDs y otra de 10kΩ que va
junto a la LDR.

.. figure:: _images/arduino-ft-23.png
   :width: 320px
   :align: center
