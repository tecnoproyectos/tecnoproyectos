:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Sensor ultrasónico
==================

|icono-video| VÍDEO: `Dos maneras de programar el sensor de distancia
<https://www.youtube.com/watch?v=T7k-bUrIvc8>`__

Los sensores de distancia HC-SR04 utilizan ondas ultrasónicas para
determinar la distancia entre el sensor y un objeto.
El sensor mide con una precisión aceptable entre 2 cm y 400 cm.

.. figure:: _images/arduino-ft-33.jpg
   :width: 256px
   :align: center
   
   Sensor de distancia ultrasónico HC-SR04.

Las patillas TRIG (trigguer o disparador) y ECHO (eco) pueden ir a
cualquier pin digital de Arduino, configurando el TRIG como salida
digital y ECHO como entrada.

El montaje básico sería:

.. figure:: _images/arduino-ft-34.png
   :width: 480px
   :align: center


Programación del sensor
-----------------------
Hay dos posibles formas de programar el sensor. Sin biblioteca o con 
biblioteca.

Sin biblioteca, con más líneas de código, quedaría así:

.. code-block:: arduino
   :linenos:

   const int TRIG = 9;     // Definimos un pin digital para TRIG
   const int ECHO = 8;     // Definimos un pin digital para ECHO
   long tiempo, distancia; // Variables de tipo long por ser cantidades
                           // grandes en microsegundos
   
   void setup() {
     pinMode(TRIG, OUTPUT); // El pin TRIG es de salida
     pinMode(ECHO, INPUT);  // El pin ECHO de entrada
     Serial.begin(9600);
   }
   
   void loop() {
     //Emitimos un pulso de 10µs
     digitalWrite(TRIG, LOW);  // Nos aseguramos de que el trigger está desactivado
     delayMicroseconds(2);     // Esperamos 2µs
     digitalWrite(TRIG, HIGH); // Mandamos un pulso de 10µs al TRIG
     delayMicroseconds(10);
     digitalWrite(TRIG, LOW);
   
     tiempo = pulseIn(ECHO, HIGH); // Mide en µs el tiempo en detectar el eco
     distancia = tiempo * 0.017;   // Convertimos µs -> cm
   
     Serial.print(distancia);  // Mostramos la distancia en el monitor serial
     Serial.println(" cm");

     delay(1000); // Tiempo entre mediciones
   }


Con biblioteca, con menos líneas de código, quedaría así:

.. code-block:: arduino
   :linenos:

   #include <Ultrasonic.h>  // Librería Ultrasonic de Erick Simões
   
   Ultrasonic sensorDistancia(9, 8); // Pines de TRIG y de ECHO
   int distancia;
   
   void setup() {
     Serial.begin(9600);
   }
   
   void loop() {
     distancia = sensorDistancia.read();  // Lee la distancia en cm
   
     Serial.print(distancia);
     Serial.println(" cm");

     delay(1000); // Tiempo entre mediciones
   }


.. |icono-video| image:: _images/arduino-ft-video.png
   :alt: Icono de vídeo de YouTube
   :height: 32px
