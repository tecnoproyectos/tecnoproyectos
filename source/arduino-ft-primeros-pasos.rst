:date: 2026-06-20
:modified: 2026-06-20
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/
:tocdepth: 2


Primeros pasos con Arduino
==========================
.. figure:: arduino-ft/arduino-01.png
   :width: 480px
   :align: right

Comienza visualizando el vídeo del enlace mientras practicas con el kit
de Arduino o el simulador de circuitos online TinkerCAD.
De momento no tienes que entregar ninguna tarea.


VÍDEO: `Primer programa con Arduino IDE y simulador de TinkerCAD
<https://www.youtube.com/watch?v=QmZUwqoM6y8>`__


Ejemplo de programa básico. Encender y apagar el LED integrado:


.. code-block:: arduino
   :linenos:

   void setup() {
     pinMode(13, OUTPUT);  // Configuramos pin13 como salida
   }
   
   void loop() {
     digitalWrite(13, HIGH); // Activamos la salida en el pin13
     delay(300);             // Retardo de 300 milisegundos
     digitalWrite(13, LOW);  // Desactivamos la salida en el pin13
     delay(300);             // Retardo de 300 milisegundos
   }

