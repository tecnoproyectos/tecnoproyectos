:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Ámbitos de variables
====================
Las variables pueden ser de ámbito global o local:

* **Variables globales**: su ámbito es todo el programa.
* **Variables locales**: su ámbito es solamente la función donde se
  encuentran.
  
Ejemplo:

.. code-block:: arduino
   :linenos:

   int a = 2; // Variable global, funciona en todo el programa

   void setup() {
   }

   void loop() {
     int b = 5;  // Variable local, na más afecta a la función loop()
   }

Las variables locales funcionan en un ámbito más pequeño pero van a
consumir menos de memoria, por lo que el programa será algo más eficiente.
