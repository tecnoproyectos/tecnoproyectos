:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Leer variables
==============
Para leer variables desde el monitor serie, dependiendo del tipo, usaremos:

.. code-block:: arduino
   :linenos:

   // Para enteros --> Serial.parseInt();
   int numEntero;
   numEntero = Serial.parseInt();

   // Para decimales --> Serial.parseFloat();
   float numDecimal;
   numDecimal = Serial.parseFloat();

   // Para texto --> Serial.readString();
   String mensaje;
   mensaje = Serial.readString();

