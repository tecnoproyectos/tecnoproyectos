:date: 2026-06-22
:modified: 2026-06-22
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Potenciómetro
=============
Los potenciómetros son resistencias variables. Las ajustamos al hacer
girar su mando, aunque también las hay deslizables.

.. figure:: _images/arduino-ft-27.png
   :width: 165px
   :align: center
   
   Potenciómetro.

.. figure:: _images/arduino-ft-28.png
   :width: 165px
   :align: center
   
   Resistencia ajustable.
   
.. figure:: _images/arduino-ft-29.png
   :width: 330px
   :align: center
   
   Símbolos del potenciómetro.
   

VÍDEO: `Potenciómetro. Conexión y programación en Arduino
<https://www.youtube.com/watch?v=bA1hnIIX6Iw>`__

Conexión básica a Arduino:

.. figure:: _images/arduino-ft-30.png
   :width: 430px
   :align: center


La instrucción para leer la entrada analógica será la estándar:

.. code-block:: arduino
   :linenos:

   int valorPotenciometro;
   int pinPotenciometro = A0;

   void setup() {
     Serial.begin(9600);
   }

   void loop() {
     valorPotenciometro = analogRead(pinPotenciometro);
     Serial.println(valorPotenciometro);
     delay(1000);
   }


Función :index:`map()`
----------------------
La **función ``map( )``** en Arduino permite remapear un número desde
un rango a otro. Es útil para hacer equivalencias entre diferentes
rangos. Por ejemplo para remapear una lectura analógica que está en un
rango de 0-1023 a un nivel de salida PWM que está en un rango 0-255.

Ejemplo:
.. code-block:: arduino

   brillo = map(valorPotenciometro, 0, 1023, 0, 255);

la variable brillo será proporcional a la entrada analógica del
potenciómetro y se usará para establecer el nivel de brillo de un LED.


Tarea regulador de luz
----------------------
Realiza un circuito que permita ajustar el nivel de luz de un LED
mediante un potenciómetro:

.. figure:: _images/arduino-ft-31.png
   :width: 458px
   :align: center

El programa debe ser equivalente al siguiente en bloques:

.. figure:: _images/arduino-ft-32.png
   :width: 683px
   :align: center


Tarea potenciómetro servo
-------------------------
Realiza la práctica que se visualiza `al final del vídeo
<https://www.youtube.com/watch?v=Z_TcgRC4zvk&t=332s>`__
en la que un potenciómetro se usa para mover un servomotor.