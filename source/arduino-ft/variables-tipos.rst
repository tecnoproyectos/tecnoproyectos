:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Tipos de variables
==================

|icono-video| VÍDEO: `Variables en Arduino II. Tipos, advertencias, ámbitos...
<https://www.youtube.com/watch?v=bfXBH6XgZ3E>`__

Existen más tipos de variables, en nuestros proyectos los que más
necesitaremos serán:

.. list-table:: Tabla de tipos de variables en Arduino
   :header-rows: 1
   :widths: auto
   :align: center

   * - Tipo
     - Tamaño
     - Rango
   * - bool
     - 1 byte
     - 0, 1 (false, true)
   * - byte
     - 1 byte
     - 0 a 255
   * - int
     - 2 bytes
     - -32768 a 32767
   * - unsigned int
     - 2 bytes
     - 0 a 65535
   * - long
     - 4 bytes
     - -2147483648 a 2147483647
   * - unsigned long
     - 4 bytes
     - 0 a 4294967295
   * - float
     - 4 bytes
     - 3,4028235E-38 a 3,4028235E+38

       Con 7 decimales de precisión

Desbordamiento
--------------
Si sobrepasamos el rango de una variable se produce un **desbordamiento**,
reiniciándose a los primeros valores del rango.

Por ejemplo, damos a la variable ``a = 255``, el máximo para el tipo
``byte`` (255), si después le sumamos 1 se produce desbordamiento y vemos
en el monitor serie que el resultado no será 256, sino se reinicia al
mínimo valor del rango (0):

.. code-block:: arduino
   :linenos:

   byte a = 255; // Asigno a la variable a el máximo valor posible

   void setup() {
     Serial.begin(9600);
   }

   void loop() {
     a = a + 1;
     Serial.println(a);
     delay(1000);
   }

   Salida por el monitor serie:

   0
   1
   2


Limitaciones del tipo float
---------------------------
* El tipo de datos float tiene sólo entre 6 y 7 dígitos decimales de
  precisión. Eso significa el número total de dígitos,
  no el número a la derecha del punto decimal.
* Si hacemos cálculos con float, debemos agregar un punto decimal;
  de lo contrario, se tratará como un int:

  .. code-block:: arduino

     int a = 9;

     void setup() {
       Serial.begin(9600);

       Serial.println(a/2);

       Serial.println(a/2.0);
     }

     Salida por el monitor serie:

     4      <-- Numero entero

     4.50   <-- Número en coma flotante

* Los números de coma flotante no son exactos y pueden producir resultados
  extraños al compararlos. Por ejemplo, es posible que 9,0/0,3 no sea
  igual a 30,0 al compararlos.


* Para que realice un redondeo correcto al pasar a int, hay que usar la
  función ``round()``:

  .. code-block:: arduino

     float x = 2.9;    // Variable de tipo float
     int y = x;        // Nos da como resultado y = 2
     int y = round(x); // Nos da como resultado y = 3

* Las matemáticas de punto flotante son mucho más lentas que las
  matemáticas de enteros al realizar cálculos, por lo que deben evitarse
  si, por ejemplo, un bucle tiene que ejecutarse a máxima velocidad.

* Para obtener un número de decimales concreto en el monitor serie, 
  se indica de la siguiente manera (ejemplo para que se muestren
  4 decimales):

  .. code-block:: arduino

     void setup() {
       Serial.begin(9600);

       Serial.println(3.14159265359, 4);
     }

     Salida por el monitor serie:

     3.1416


.. |icono-video| image:: _images/arduino-ft-video.png
   :alt: Icono de vídeo de YouTube
   :height: 32px
