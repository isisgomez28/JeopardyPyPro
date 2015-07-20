:- consult('GameDatabase').
%% Preguntas pendientes 16 y 17.

% P - Pelicula.
% X - Respuesta Compositor.
% Z - Compositor.
pregunta_1(X, P):- persona_ocupacion(Z, "Compositor"), pelicula(P), compositor_de(Z, P), X = Z, !.

% A - Accion.
% I - Personaje Interpretado.
% X - Respuesta Cancion.
pregunta_2(X, I, A):- interpretar_en(_, I, P), cancion_pelicula_accion(Y, P, A), X = Y, !.

% A - Año
% X - Respuesta.
pregunta_3(X, A):- ganador_oscar(Z, A), cancion(Z), compositor_de(W, Z), X = W, !. 

% A - Accion.
% P - Pelicula
% X - Respuesta Cancion.
pregunta_4(X, P, A):- cancion_pelicula_accion(Y, P, A), X = Y, !.

% A - Año
% P - Pelicula
% X - Respuesta Efecto de Sonido.
pregunta_5(X, A, P):- efecto_sonido(Q, A), utilizado_en(Q, P), X = Q, !.

% A - Nombre del Actor.
% X - Respuesta Enfermedad.
pregunta_6(X, A):- persona_ocupacion(A, "Actor"), padece_de(A, E), X = E, !.

% I - Personaje Interpretado.
% P - Pelicula
% X - Respuesta.
pregunta_7(X, P, I):- pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), X = Persona.
pregunta_7(X, P, I):- interpretar_en(Persona, _, _), persona_ocupacion(Persona, "Actor"), X = Persona, !.

% A - Actor.
% I - Interpreta Personaje
% X - Respuesta.
pregunta_8(X, A, I):- interpretar_en(A, I, Pel), pelicula(Pel), superheroe_pelicula(H, Pel), X = H, !.

% P - Pelicula
% I - Interpreta Personaje
% X - Respuesta.
pregunta_9(X, P, I):- pelicula(P), interpretar_en(Persona, I, P), persona_ocupacion(Persona, "Actor"), X = Persona, !.

% A - Actor.
% X - Respuesta.
pregunta_10(X, A):- pregunta_6(X, A).

% P - Pelicula.
% X - Respuesta.
pregunta_11(X, P):- pelicula(P), director_de(Dir, P), X = Dir, !.

% P - Pelicula.
% X - Respuesta.
pregunta_12(X, P):- pelicula_tematica(P, T), X = T, !.

% P - Pelicula.
% X - Respuesta.
pregunta_13(X, P):- pelicula(P), villano_pelicula(V, P), X = V, !.

% T - Tematica.
% X - Respuesta.
pregunta_14(X, T):- pelicula_tematica(P, T), X = P, !.

% A - Actor.
% I - Interpreta Personaje
% X - Respuesta.
pregunta_15(X, P, I):- pregunta_9(X, P, I), !.

% P - Pelicula.
% I - Interpreta Personaje
% X - Respuesta.
pregunta_18(X, P, I):- pregunta_9(X, P, I), !.

% T - Tematica
% D - Director.
% X - Respuesta.
pregunta_19(X, T, D):- pelicula_tematica(P, T), director_de(D, P), P = X, !.

% P - Pelicula.
% I - Personaje Interpretado.
% X - Respuesta.
pregunta_20(X, P, I):- pelicula(P), personaje_historico(H, I), X = H, !. 

% P - Pelicula.
% X - Respuesta.
pregunta_21(X, P):- interpretar_en(A, _, P), persona_ocupacion(A, "Actriz"), ganador_oscar(A, 2015), X = A, !.

% A - Año
% X - Respuesta.
pregunta_22(X, A):- pelicula_animada(X), ganador_oscar(X, A), !.

% P - Pelicula.
% X - Respuesta.
pregunta_23(X, P):- pelicula(P), persona_ocupacion(Y, "Ambientador de Decoracion"), ganador_oscar(Y, 2015), X = Y , !.

% D - Director.
% X - Respuesta.
pregunta_24(X, D):- director_de(D, P), pelicula_extranjera(P), ganador_oscar(P, 2015), X = P, !.

% P - Pelicula.
% X - Respuesta.
pregunta_25(X, P):- pelicula(P), pregunta_11(X, P), !.