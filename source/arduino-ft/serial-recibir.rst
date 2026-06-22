:date: 2026-06-22
:modified: 2026-06-22
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Comunicación serie I
====================

VÍDEO: `Arduino nos envía mensajes (comunicación serial)
<https://www.youtube.com/watch?v=x2IdOeIPhRY>`__

Vamos a comunicarnos con Arduino. Primero vamos a ver cómo Arduino nos va
a transmitir información. Dentro de void setup(), debemos iniciar la
comunicación serie, indicando la velocidad de transmisión, por defecto
9600 bauds:

.. code-block:: arduino
   :linenos:

   void setup() {
     Serial.begin(9600);

Dentro de void loop(), el comando para que se imprima en pantalla una
línea sería:

.. code-block:: arduino
   :linenos:

   Serial.println(i);

Si queremos que no haya salto de línea, simplemente Serial.print:

.. code-block:: arduino
   :linenos:

   Serial.print("El valor de la intensidad es ");
   Serial.println(i);

El código anterior nos daría como mensajes en el monitor serie::

  El valor de la intensidad es 124
  El valor de la intensidad es 119


Tarea visualiza el nivel de brillo
----------------------------------
Monta el circuito de la figura:

.. figure:: _images/arduino-03.png
   :align: center

Realiza el programa Brillo_sube_baja, pero visualizando la intensidad de
brillo en el monitor serie:

.. figure:: _images/arduino-11.png
   :width: 480px