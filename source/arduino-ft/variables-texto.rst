:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Variables de texto
==================

.. list-table:: Tabla de tipos de variables en Arduino
   :header-rows: 1
   :widths: auto
   :align: center

   * - Tipo
     - Almacena
     - Ejemplo
   * - char
     - Caracteres
     - ``char letra = 'a';``
   * - String
     - Caracteres
     - ``String mensaje = "Hola, mundo!";``

Ejemplo para declarar una variable de tipo ``char`` con nombre ``letra``
y cuyo valor queremos que sea la letra ``'a'``:

.. code-block:: arduino
   :linenos:

   char letra = 'a';

   void setup() {
     Serial.begin(9600);
   }

   void loop() {
     Serial.println(letra);
     delay(1000);
   }

   Salida por el monitor serie:

   a
   a
   
Ejemplo para crear un objeto de la clase String:

.. code-block:: arduino
   :linenos:

   String miFrase = "Hola, mundo!";

   void setup() {
     Serial.begin(9600);
   }

   void loop() {
     Serial.println(miFrase);
     delay(1000);
   }

   Salida por el monitor serie:

   Hola, mundo!
   Hola, mundo!


