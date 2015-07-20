# JeopardyPyPro
Proyecto final para la asignatura de Programación Lógica, basado en el famoso juego Jeopardy.

Lenguajes:
  Python - FrontEnd
  Prolog - BackEnd

Herramientas
  QT empleando el plugin PyQT.


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
La idea de definir los hechos viene de poder quitarle ventaja a la maquina sobre el hombre, y ser justos con los turnos e interacciones de los jugadores.
GameLogic en esta parte decidimos colocar las reglas que contribuyen con el manejo de las interacciones de los jugadores, el manejo de la puntuacion, etc.
IA_Analysis aqui detallamos las acciones en cuanto a consultas que debe la maquina procesar para hacer frente al humano y poder ser un rival intimidante.
