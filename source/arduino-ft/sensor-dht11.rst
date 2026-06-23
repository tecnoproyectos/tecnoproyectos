:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Sensor DTH11
============
El sensor DTH11 es un sensor de temperatura y de humedad relativa del
aire ambiente.

.. figure:: _images/arduino-ft-39.jpg
   :width: 234px
   :align: center
   
   Sensor DHT11 de temperatura y humedad relativa.

El sensor tiene 3 cables de conexión:

* Vcc (5V)
* GND
* Data: cualquier pin digital.


Instalación de la biblioteca
----------------------------
Si no lo hemos hecho antes, en Arduino IDE ir al menú Herramientas --> 
Gestionar bibliotecas e instalar la siguiente librería: 
**DHT sensor library de Adafruit**.

Programación básica
-------------------
Programación básica mostrando los datos en el monitor serie:

.. code-block:: arduino
   :linenos:
   
   #include <DHT.h> // Incluimos la biblioteca necesaria
   
   // Definimos el sensor con un nombre (dht11 en este caso)
   // Pin donde conectamos Data (8) y tipo de DHT (DHT11):
   DHT dht11(8, DHT11); 
   
   void setup() {
     Serial.begin(9600);
     dht11.begin();      // Iniciamos el sensor DHT11
   }
   
   void loop() {
     
     delay(2000);
   
     // Leemos humedad y la guardamos en una variable
     int humedad = dht.readHumidity(); 
   
     // Leemos temperatura y la guardamos en una variable
     // de tipo float (con decimales) 
     float temp = dht.readTemperature();
   
     // Mostramos los valores por el monitor serie
     Serial.print("Humedad: ");
     Serial.print(humedad);
     Serial.print("%");
   
     Serial.print(" Temperatura: ");
     Serial.print(temp, 1); // Muestra un decimal
     Serial.println("ᵒC");
   }

.. nota::
   Recordatorio: para mostrar en una pantalla LCD1602 el símbolo º de
   grados, escribimos la siguiente línea:

   .. code-block:: arduino

      lcd.print((char)223);


.. |icono-video| image:: _images/arduino-ft-video.png
   :alt: Icono de vídeo de YouTube
   :height: 32px