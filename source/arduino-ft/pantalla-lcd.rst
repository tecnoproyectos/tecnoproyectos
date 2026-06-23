:date: 2026-06-23
:modified: 2026-06-23
:author: Francisco Trigueros
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Pantalla LCD1602
================

|icono-video| VÍDEO: `Pantalla LCD1602 con Arduino
<https://www.youtube.com/watch?v=YWU2VdI-G4Q>`__

La pantalla LCD1602 (16 columnas x 02 filas) para microcontrolador Arduino
permite mostrar visualmente los datos de los sensores.

.. figure:: _images/arduino-ft-35.jpg
   :width: 225px
   :align: center
   
   Pantalla LCD1602 con conexión I2C.

Nosotros vamos a usar la que tiene un módulo I2C que reduce las conexiones
a 4 cables:

* GND
* Vcc (5V)
* SDA: serial data, siempre conectado al pin A4 en Arduino UNO.
* SCL: serial clock, siempre conectado al pin A5 en Arduino UNO.

.. figure:: _images/arduino-ft-36.png
   :width: 920px
   :align: center


Instalación de la biblioteca
----------------------------
Nos vamos al menú Herramientas --> Gestionar bibliotecas e instalamos
la siguiente:

* En Arduino IDE 1: LiquidCrystal I2C de Marco Schwartz
  (ponemos Schwartz en el buscador):
 
  .. figure:: _images/arduino-ft-37.png
     :width: 800px
     :align: center

* En Arduino IDE 2: LiquidCrystal I2C de Frank de Brabander
  (ponemos Brabander en el buscador):
  
  .. figure:: _images/arduino-ft-38.png
     :width: 800px
     :align: center
  

Programación básica
-------------------

.. code-block:: arduino
   :linenos:

   // Incluímos las dos bibliotecas siguientes:
   #include "Wire.h"
   #include "LiquidCrystal_I2C.h"
   
   //definimos el display con el nombre lcd,
   //la LCD está en la dirección I2C 0x27, tiene 16 columnas y 2 filas:
   LiquidCrystal_I2C lcd(0x27, 16, 2); 
   
   void setup() {
     lcd.init();      // Iniciamos el LCD
     lcd.backlight(); // Encendemos la retroiluminación
   
     // Colocamos el cursor donde queremos que inicie el texto
     // Comenzamos a contar desde cero para la posición del cursor: 0, 1, 2...
     lcd.setCursor(2, 0);     // Tercera columna de la primera fila
     lcd.print("APRENDEMOS"); // Mostramos en pantalla el texto
     lcd.setCursor(3, 1);     // Cuarta columna de la segunda fila 
     lcd.print("TECNOLOGIA"); // NO ES COMPATIBLE CON TILDES
   }
   
   void loop() {
   }

.. note::
   Si no se ven o se ven mal los caracteres, podemos ajustar el contraste
   de la pantalla usando el potenciómetro azul de la parte de atrás.


Decimales de float
------------------
Para elegir el número de decimales mostrado de una variable float ponemos
una coma y el número de decimales deseado.
Ejemplo para mostrar el valor de la variable temp con un decimal:

.. code-block:: arduino

   lcd.print(temp, 1); 

Caracteres especiales
---------------------
* Tenemos en cuenta que el LCD no es compatible con tildes.
* Para poner el símbolo º de grados, escribimos la siguiente línea:
  
  .. code-block:: arduino

     lcd.print((char)223);
      
La programación básica de un corazón sería así, fíjate que los 0 y 1
forman el dibujo del corazón:

.. code-block:: arduino
   :linenos:

   #include <Wire.h>
   #include <LiquidCrystal_I2C.h>

   LiquidCrystal_I2C lcd(0x27, 16, 2);

   // Define el carácter personalizado del corazón
   byte heart[8] = {
     B00000,
     B01010,
     B11111,
     B11111,
     B11111,
     B01110,
     B00100,
     B00000
   };

   void setup() {
     lcd.init();
     lcd.backlight();

     // Cargar el carácter personalizado en la memoria del LCD:
     lcd.createChar(0, heart);
     
     // Limpiar la pantalla:
     lcd.clear();

     // Coloca el cursor en la posición (0, 0)
     lcd.setCursor(0, 0);

     // Muestra el carácter personalizado del corazón (caracter 0)
     lcd.write(0);
   }

   void loop() {
   }

Para dibujar caracteres personalizados de forma más visual, hay editores
online como el `editor de Arduinoblocks
<https://www.steamakersblocks.com/web/help/chareditor>`__
que nos generan el código directamente.


.. |icono-video| image:: _images/arduino-ft-video.png
   :alt: Icono de vídeo de YouTube
   :height: 32px