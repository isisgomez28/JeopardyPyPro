:- consult('GameDatabase').

concatena_str(X, Y, R):- string_concat(X, Y, FinalString), R = FinalString.

pregunta_1(X):- persona_ocupacion(Z, "Compositor"), pelicula(P), compositor_de(Z, P), concatena_str("Quien es ", Z, X), !.

pregunta_2(X):- interpretar_en(_, "Rocky Balboa", P), cancion_pelicula_accion(Y, P, "Entrenar"), X = Y, !.

pregunta_3(X):- ganador_oscar(Z, 2015), cancion(Z), compositor_de(W, Z), X = W, !. 

pregunta_4(X):- cancion_pelicula_accion(Y, "Inception", "Despertar"), X = Y, !.

pregunta_5(X):- efecto_sonido(Q, 1951), utilizado_en(Q, "Distant Drums"), X = Q, !.

pregunta_6(X):- A = "Charlie Sheen", persona_ocupacion(A, "Actor"), padece_de(A, E), X = E, !.

pregunta_7(X):- P ="Matrix", I ="Neo", pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), X = Persona.
pregunta_7(X):- interpretar_en(Persona, _, _), persona_ocupacion(Persona, "Actor"), X = Persona, !.

pregunta_8(X):- A = "Michael Keaton", I="Riggan Thomson", interpretar_en(A, I, Pel), pelicula(Pel), superheroe_pelicula(H, Pel), X = H, !.

pregunta_9(X):- P ="Batman: El Caballero de la Noche", I= "Alfred", pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), X = Persona, !.

pregunta_10(X):- A = "Jim Carrey", persona_ocupacion(A, "Actor"), padece_de(A, E), X = E, !.

pregunta_11(X):- P ="Interestellar", pelicula(P), director_de(Dir, P), X = Dir, !.

pregunta_12(X):- P= "Mad Max", pelicula_tematica(P, T), concatena_str("Que es ", T, X), !.

pregunta_13(X):- P="Terminator",pelicula(P), villano_pelicula(V, P), concatena_str("Quien es ", V, X), !.

pregunta_14(X):- T="Olvido", pelicula_tematica(P, T), X = P, !.

pregunta_15(X):- P ="Matrix", I= "Merovingio", pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), X = Persona, !.

pregunta_16(X):- P="JFK", interpretar_en(_, I, P), personaje_nombre_popular(N, I), X = N.

pregunta_17(X):- I="Dr. Jack Kevorkian", personaje_nombre_popular(I, X), !.

pregunta_18(X):- P ="Schindler's List", I= "Oscar Schindler", pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), concatena_str("Quien es ", Persona, X), !.

pregunta_19(X):- T="Septiembre Negro", D="Steven Spielberg", pelicula_tematica(P, T), director_de(D, P), P = X, !.

pregunta_20(X):- P="Los Miserables", I="Jean ValJean", pelicula(P), personaje_historico(H, I), X = H, !. 

pregunta_21(X):- P="Siempre Alice", interpretar_en(A, _, P), persona_ocupacion(A, "Actriz"), ganador_oscar(A, 2015), X = A, !.

pregunta_22(X):- A=2015, ganador_oscar(X, A),pelicula_animada(X), !.

pregunta_23(X):- P="El Gran Hotel Budapest", pelicula(P), persona_ocupacion(Y, "Ambientador de Decoracion"), ganador_oscar(Y, 2015), X = Y , !.

pregunta_24(X):- D="Pawel Pawlikowski", director_de(D, P), pelicula_extranjera(P), ganador_oscar(P, 2015), X = P, !.

pregunta_25(X):- P="Birdman", pelicula(P), director_de(Dir, P), X = Dir, !.