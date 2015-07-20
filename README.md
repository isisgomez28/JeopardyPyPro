# JeopardyPyPro
Proyecto final para la asignatura de Programación Lógica, basado en el famoso juego Jeopardy.

Lenguajes:
  Python
  Prolog

Herramientas
  QT empleando el plugin PyQT.
  PyWIP libreria de integracion entre Python y SWIP.


PySWIP es un puente entre Python y SWI-Prolog permite consultar SWI-Prolog en sus programas en Python. Cuenta con una (incompleta) SWI-Prolog interfaz de idioma extranjero, una clase de utilidad que facilita la consulta con Prolog y también una interfaz Pythonic.

Desde PySWIP utiliza SWI-Prolog como una biblioteca compartida y ctypes para acceder a ella, que no requiere compilación para ser instalado.


Requerimientos
Python 2.3 y superior.
ctypes 1.0 y superior.
SWI-Prolog 5.6.x y superior (no la rama de desarrollo).
libpl como una biblioteca compartida.
Funciona en Linux y Win32, deben trabajar en todo POSIX.

PyQt es un conjunto de Python bindings V2 y V3 para framework de aplicaciones Qt Qt de la Compañía y se ejecuta en todas las plataformas soportadas por Qt incluyendo Windows, MacOS / X y Linux. Los enlaces se implementan como un conjunto de módulos de Python y contienen más de 1.000 clases.
PyQt es un conjunto de Python bindings V2 y V3 para framework de aplicaciones Qt Qt de la Compañía y se ejecuta en todas las plataformas soportadas por Qt incluyendo Windows, MacOS / X y Linux. Los enlaces se implementan como un conjunto de módulos de Python y contienen más de 1.000 clases.


Diseño

Nuestro proyecto esta dividido en las siguientes partes:.
	- Models
	- Main
	- GameDatabase
	- GameLogic
	- IA_Analysis

Cada una de ellas tiene una funcion bajo proof of concept.
En Models manejamos las objetos que conforman el juego tenemos las Categorias, Preguntas, Respuestas y Jugadores.
En el Main hacemos la coordinación de las partes del juego.
En GameDatabase tenemos listas cada una de las Preguntas con sus Respuestas, a su vez definimos los hechos que serán empleados para fundamentar las respuestas que seran proporcionadas por la maquina y sus analisis.
La idea de definir los hechos viene de poder quitarle ventaja a la maquina sobre el humano, y ser justos con los turnos e interacciones de los jugadores.
GameLogic en esta parte decidimos colocar las reglas que contribuyen con el manejo de las interacciones de los jugadores, el manejo de la puntuacion, etc.
IA_Analysis aqui detallamos las acciones en cuanto a consultas que debe la maquina procesar para hacer frente al humano y poder ser un rival intimidante.
