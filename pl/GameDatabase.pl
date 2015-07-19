%	Categorias
categoria("Bandas Sonoras", "Musica en las peliculas.").
categoria("Actores y Hechos Curiosos", "Actores fuera de las peliculas.").
categoria("","").
categoria("", "").
categoria("", "").

% Preguntas.
%% Preguntas relacionadas a la categoría de Bandas Sonoras.
pregunta(1, "Es un compositor famoso de las peliculas Star Wars, Harry Potter y Jaws", "Bandas Sonoras", 100).
pregunta(2, "Cancion utilizada por Rocky Balboa en sus entrenamientos en la saga completa", "Bandas Sonoras", 200).
pregunta(3, "Es el compositor que gano mejor cancion en los Oscar en el 2015", "Bandas Sonoras", 300).
pregunta(4, "Canción utilizada en Inception para despertar a los personajes", "Bandas Sonoras", 400).
pregunta(5, "Efecto de sonido de stock usado por primera vez en 1951 en la pelicula Distant Drums", "Bandas Sonoras", 500).

% Preguntas relacionadas a la categoría de Actores y Hechos Curiosos.
pregunta(6, "Enfermedad que arruino su carrera de actor a Charlie Sheen", "Actores y Hechos Curiosos", 100).
pregunta(7, "Es el actor que rechazo interpretar el papel de Neo en la trilogia de Matrix", "Actores y Hechos Curiosos", 200).
pregunta(8, "Fue el superheroe por el cual Riggan Thomson (Michael Keaton) tuvo delirios durante su vida personal y profesional.", "Actores y Hechos Curiosos" ,300).
pregunta(9, "", "", 400).
pregunta(10, "", "", 500).

pregunta(11, "", "", 100).
pregunta(12, "", "", 200).
pregunta(13, "", "", 300).
pregunta(14, "", "", 400).
pregunta(15, "", "", 500).

pregunta(16, "", "", 100).
pregunta(17, "", "", 200).
pregunta(18, "", "", 300).
pregunta(19, "", "", 400).
pregunta(20, "", "", 500).

pregunta(21, "", "", 100).
pregunta(22, "", "", 200).
pregunta(23, "", "", 300).
pregunta(24, "", "", 400).
pregunta(25, "", "", 500).

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
respuesta(11, "").
respuesta(12, "").
respuesta(13, "").
respuesta(14, "").
respuesta(15, "").
respuesta(16, "").
respuesta(17, "").
respuesta(18, "").
respuesta(19, "").
respuesta(20, "").
respuesta(21, "").
respuesta(22, "").
respuesta(23, "").
respuesta(24, "").
respuesta(25, "").

%% Hechos de Analisis.

% Persona y su Ocupación
persona_ocupacion("John Williams", "Compositor").
persona_ocupacion("Patrick Doyle", "Compositor").
persona_ocupacion("Nicolas Hooper", "Compositor").
persona_ocupacion("Alexandre Desplat", "Compositor").
persona_ocupacion("John Legend", "Compositor").
persona_ocupacion("Rita Ora", "Compositor").
persona_ocupacion("Tegan Quin", "Compositor").
persona_ocupacion("Charlie Sheen", "Actor").
persona_ocupacion("Will Smith", "Actor").
persona_ocupacion("Michael Keaton", "Actor").

% Enfermedad
enfermedad("Alcoholismo").

% Padece de
padece_de("Charlie Sheen", "Alcoholismo").

% Pelicula
pelicula("Star Wars Episode I: The Phantom Menace").
pelicula("Star Wars Episode II: Attack of the Clones").
pelicula("Star Wars Episode III: Revenge of the Sith").
pelicula("Star Wars Episode IV: A New Hope").
pelicula("Star Wars Episode V: The Empire Strikes Back").
pelicula("Star Wars Episode VI: Return of the Jedi").
pelicula("Star Wars Episode VII: The Force Awakens").
pelicula("Harry Potter y la Piedra Filosofal").
pelicula("Harry Potter y la Camara Secreta").
pelicula("Harry Potter y el Prisionero de Azkaban").
pelicula("Harry Potter y el Caliz de Fuego").
pelicula("Harry Potter y la Orden del Fenix").
pelicula("Harry Potter y el Misterio del Príncipe").
pelicula("Harry Potter y las Reliquias de la Muerte - Parte 1").
pelicula("Harry Potter y las Reliquias de la Muerte - Parte 2").
pelicula("Jaws").

cancion("Everything is Awesome").
cancion("Grateful").
cancion("Everything is Awesome").
cancion("Glory").
cancion("I'm not gonna miss you").
cancion("Lost Stars").

efecto_sonido("Castle Thunder", 1931).
efecto_sonido("Howie Scream", 1980).
efecto_sonido("El grito de Wilhem", 1951).
efecto_sonido("Deep Note", 1983).
efecto_sonido("Los rayos blaster", 1977).
efecto_sonido("El Goofy Holler", 1941).
efecto_sonido("El timbre de teléfono Universal", 1974).

% Pelicula y Cancion
cancion_pelicula_accion("Gonna Fly Now", "Rocky", "Entrenar").
cancion_pelicula_accion("Gonna Fly Now", "Rocky II", "Entrenar").
cancion_pelicula_accion("Gonna Fly Now", "Rocky III", "Entrenar").
cancion_pelicula_accion("Gonna Fly Now", "Rocky IV", "Entrenar").
cancion_pelicula_accion("Gonna Fly Now", "Rocky V", "Entrenar").
cancion_pelicula_accion("Gonna Fly Now", "Rocky VI", "Entrenar").
cancion_pelicula_accion("Gonna Fly Now", "Rocky - Creed", "Entrenar").
cancion_pelicula_accion("Rocky`s reward", "Rocky", "Creditos Finales").
cancion_pelicula_accion("Take you back", "Rocky III", "Caminar cerca de Casa").
cancion_pelicula_accion("Eye of the Tiguer", "Rocky III", "Preparacion Pelear").
cancion_pelicula_accion("Burning heart", "Rocky IV", "Conflictos de Peleas").
cancion_pelicula_accion("Heart on fire", "Rocky IV", "Preparacion Boxeadores").
cancion_pelicula_accion("No easy way out", "Rocky IV", "Conducir").
cancion_pelicula_accion("Non Je Ne Regrette Rien", "Inception", "Despertar").

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
compositor_de("John Legend", "Glory").
compositor_de("Tegan Quin", "Everything is Awesome").
compositor_de("Rita Ora", "Grateful").
compositor_de("Glen Campbell", "I'm not gonna miss you").
compositor_de("Adam Levin", "Lost Stars").

interpretar_en("Will Smith", "Will", "El Principe de Bel Air").
interpretar_en("Will Smith", "Detective Mike Lowrey", "Bad Boys").
interpretar_en("Will Smith", "Agente J", "Hombres de negro").
interpretar_en("Will Smith", "Chris Gardner", "En busca de la felicidad").
interpretar_en("Michael Keaton", "Riggan Thomson", "Birdman").
interpretar_en("Michael Keaton", "Bruce Wayne", "Batman").
interpretar_en("Michael Keaton", "Bruce Wayne", "Batman Returns").

superheroe("Birdman").
superheroe("Batman").

% Ganadore(s) de Oscar
ganador_oscar("Glory", 2015).