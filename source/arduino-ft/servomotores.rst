:date: 2026-06-22
:modified: 2026-06-22
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Servomotores
============

VÍDEO: `Servomotores en Arduino. Guía básica
<https://www.youtube.com/watch?v=kE_ou58E7Hw>`__

.. figure:: _images/arduino-ft-24.png
   :width: 300px
   :align: center

Son motores en los que podemos controlar el ángulo de giro mediante la
programación del Arduino.

El modelo SG90 (el de la figura anterior) es muy utilizado porque es el
más económico, pero no puede transmitir mucha potencia.
Puede girar de 0º a 180º.

La conexión básica sería como en la imagen, teniendo que conectar
**el cable naranja a cualquier salida PWM**.

.. figure:: _images/arduino-ft-25.png
   :width: 360px
   :align: center

Instrucciones básicas para Arduino IDE:

.. code-block:: arduino
   :linenos:

   #include <Servo.h>  // Incluimos la librería Servo.h
   
   Servo miServo;  // asignamos al servomotor el nombre "miServo"
   
   int pinServo = 9; // Pin PWM donde está conectado el servomotor
   int angulo = 90;  // Declaramos la variable con el ángulo de giro
   
   void setup() {
     // Iniciamos miServo en el pin pinServo
     miServo.attach(pinServo);
   }
   
   void loop() {
     // Movemos el servomotor al ángulo "anguloServo"
     miServo.write(angulo);
   }


Tarea limpiaparabrisas
----------------------
Con el montaje básico de la figura anterior, programa el servo usando el
bucle ``for( )`` para que haga un movimiento de vaivén como el de un
limpiaparabrisas de un coche:

* Que vaya aumentando el ángulo de uno en uno desde 5º hasta 175º,
  con una espera de 8 ms entre una posición y la siguiente.
* Que vaya disminuyendo el ángulo de uno en uno desde 174º hasta 6º
  con una espera de 8 ms entre una posición y la siguiente.

Aquí tienes el programa con bloques que puedes usar como guía:

.. figure:: _images/arduino-ft-26.png
   :width: 480px
   :align: center

