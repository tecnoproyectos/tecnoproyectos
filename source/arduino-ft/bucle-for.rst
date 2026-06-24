:date: 2026-06-21
:modified: 2026-06-24
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Bucle for()
===========
|icono-video| VÍDEO: `Bucles for() en Arduino
<https://www.youtube.com/watch?v=BBouhq2HR10>`__

Ejemplo de **repetir 5 veces** con el bucle ``for()``,
que podríamos interpretarlo como: 

* Comenzando con i igual a 1
* Repetir mientras i sea menor o igual a 5
* Aumentando i de uno en uno (i++)

.. code-block:: arduino
   :linenos:

   int i;
   for (i = 1; i <= 5; i++) {
     digitalWrite(13, HIGH);
     delay(200);
     digitalWrite(13, LOW);
     delay(200);
   }

Si queremos que el contador disminuya de 1 en 1:

.. code-block:: arduino
   :linenos:

   for (i = 5; i >= 5; i--) {


Si queremos que el contador vaya aumentando de 5 en 5:

.. code-block:: arduino
   :linenos:

   for (i = 0; i <= 25; i = i + 5) {


Tarea Bucle for()
-----------------
Monta el circuito de la figura:

.. figure:: _images/arduino-ft-03.png
   :align: center


Realiza el siguiente programa con el código equivalente a:

.. figure:: _images/arduino-ft-07.png
   :width: 420px
   :align: center




.. |icono-video| image:: _images/arduino-ft-video.png
   :alt: Icono de vídeo de YouTube
   :height: 32px