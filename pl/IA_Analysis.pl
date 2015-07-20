:- consult('GameDatabase').

pregunta_1(X, P, O):- persona_ocupacion(Z, O), pelicula(P), compositor_de(Z, P), X = Z.

pregunta_2(X, P, A):- cancion(Y), cancion_pelicula_accion(Y, P, A), X = Y, !.

pregunta_3(X):- cancion(Z), compositor_de(W, Z), ganador_oscar(Z, 2015), X = W, !. 

pregunta_4(X, P, A):- pregunta_2(X, P, A).

pregunta_5(X, A, P):- efecto_sonido(Q, A), utilizado_en(Q, P), X = Q, !.

pregunta_6(X, A, O):- persona_ocupacion(A, O), padece_de(A, E), X = E, !.

pregunta_7(X, P, I):- pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), X = Persona.
pregunta_7(X, P, I):- interpretar_en(Persona, _, _), persona_ocupacion(Persona, "Actor"), X = Persona, !.

pregunta_8(X, Actor, Int):- interpretar_en(Actor, Int, Pel), pelicula(Pel), superheroe(Pel), X = Pel, !.

pregunta_9(X, P, I):- pregunta_7(X, P, I), !.