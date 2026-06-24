:date: 2026-06-24
:modified: 2026-06-24
:author: Carlos Félix Pardo Martín
:license: Creative Commons Attribution-ShareAlike 4.0 International
:license_url: https://creativecommons.org/licenses/by-sa/4.0/


Herramientas del proyecto
=========================
Esta es la lista de herramientas que se necesita para compilar la página
web y obtener los archivos html.

No es necesario instalar todas estas herramientas para aportar contenidos,
pero si es recomendable para que puedas compilar el proyecto en tu propio
ordenador y comprobar que todo lo escrito funciona correctamente antes de
enviarlo al repositorio principal, ahorrando trabajo a los administradores.

Herramientas en Linux
---------------------
A continuación aparece la lista de herramientas necesarias para la
distribución Debian y sus distribuciones derivadas (Ubuntu, MAX, etc).

* **Python**: lenguaje de programación que utiliza el proyecto.
  
  ``sudo apt install python3``

* **Sphinx**: generador de documentación que compila los ficheros fuente
  para convertirlos en html estático, epub o pdf.

  ``sudo apt install python3-sphinx``

* **Furo**:
  
  ``apt install python3-furo``

* **TeX Live**: paquete del lenguaje LaTeX para generación de fórmulas
  con Sphinx.

  ``sudo apt install texlive-full``

* **Git**: gestor de versiones. Es la herramienta de control de revisiones
  de Linux y la que trabaja por debajo del servicio GitHub.

  ``sudo apt install git –y``

* **ImageMagick**: paquete de manejo de imágenes por línea de comandos.
  No es necesario para compilar la web, solo para modificar las imágenes
  del proyecto a mano cuando sea necesario.

  ``sudo apt install imagemagick``


Compilando el proyecto
----------------------
Para compilar el proyecto y obtener los archivos html estáticos que 
forman la página web es necesario ir al directorio del proyecto y escribir:

``make html``

