%	Categorias
categoria("Bandas Sonoras", "Musica en las peliculas.").
categoria("Actores y Hechos Curiosos", "Actores fuera de las peliculas.").
%% categoria("","").
%% categoria("", "").
%% categoria("", "").

% Preguntas.
%% Preguntas relacionadas a la categoría de Bandas Sonoras.
pregunta(1, "Es un compositor famoso de las peliculas Star Wars, Harry Potter y Jaws", "Bandas Sonoras", 100).
pregunta(2, "Cancion utilizada por Rocky Balboa en sus Entrenamientos en la saga completa", "Bandas Sonoras", 200).
pregunta(3, "Es el compositor que gano mejor cancion en los Oscar en el 2015", "Bandas Sonoras", 300).
pregunta(4, "Canción utilizada en Inception para despertar a los personajes", "Bandas Sonoras", 400).
pregunta(5, "Efecto de sonido de stock usado por primera vez en 1951 en la pelicula Distant Drums", "Bandas Sonoras", 500).

% Preguntas relacionadas a la categoría de Actores y Hechos Curiosos.
pregunta(6, "Enfermedad que arruino su carrera de actor a Charlie Sheen", "Actores y Hechos Curiosos", 100).
pregunta(7, "Es el actor que rechazo interpretar el papel de Neo en la trilogia de Matrix", "Actores y Hechos Curiosos", 200).
pregunta(8, "Fue el superheroe por el cual Riggan Thomson (Michael Keaton) tuvo delirios durante su vida profesional.", "Actores y Hechos Curiosos" ,300).
pregunta(9, "", "", 400).
pregunta(10, "", "", 500).

% Preguntas
respuesta(1, "Quien es John Williams").
respuesta(2, "Gonna Fly Now").
respuesta(3, "Quien es John Legend").
respuesta(4, "Non Je Ne Regrette Rien").
respuesta(5, "Que es el El grito de Wilhem").
respuesta(6, "Alcoholismo").
respuesta(7, "Quien es Will Smith").
respuesta(8, "Quien es Birdman").
respuesta(9, "").
respuesta(10, "").

%% Hechos de Analisis.

% Persona y su Ocupación
persona_ocupacion("John Williams", "Compositor").
persona_ocupacion("Patrick Doyle", "Compositor").
persona_ocupacion("Nicolas Hooper", "Compositor").
persona_ocupacion("Alexandre Desplat", "Compositor").
persona_ocupacion("John Legend", "Compositor").

% Trabajos realizados.
compositor_de("John Williams", "Star Wars Episode I: the Phantom Menace").
compositor_de("John Williams", "Star Wars Episode II: Attack of the Clones").
compositor_de("John Williams", "Star Wars Episode III: Revenge of the Sith").
compositor_de("John Williams", "Star Wars Episode IV: A New Hope").
compositor_de("John Williams", "Star Wars Episode V: The Empire Strikes Back").
compositor_de("John Williams", "Star Wars Episode VI - Return of the Jedi").
compositor_de("John Williams", "Star Wars: Episode VII - The Force Awakens").
compositor_de("John Williams", "Harry Potter y la Piedra Filosofal").
compositor_de("John Williams", "Harry Potter y la Camara Secreta").
compositor_de("John Williams", "Harry Potter y el Prisionero de Azkaban").
compositor_de("Patrick Doyle", "Harry Potter y el Caliz de Fuego").
compositor_de("Nicolas Hooper", "Harry Potter y la Orden del Fenix").
compositor_de("Nicolas Hooper", "Harry Potter y el Misterio del Príncipe").
compositor_de("Alexandre Desplat", "Harry Potter y las Reliquias de la Muerte - Parte 1").
compositor_de("Alexandre Desplat", "Harry Potter y las Reliquias de la Muerte - Parte 2").
compositor_de("John Williams", "Jaws").


