%% Hecho del Jugador.
:- dynamic jugador/1.
jugador(maquina).

%% Hecho Puntuación del Jugador.
:- dynamic puntuacion/2.
puntuacion(maquina, 0).

%% Regla para agregar Nombre Jugador Humano y Puntuacion Inicial.
nuevo_jugador(Nombre):- assertz(jugador(Nombre)), assertz(puntuacion(Nombre, 0)).

%% Regla para la Actualizacion de la Puntacion del Jugador.
actualiza_puntuacion(Jug, PtosNuevos):- number(PtosNuevos), retract(puntuacion(Jug, X)), Y is (X + PtosNuevos), assertz(puntuacion(Jug, Y)).

%% Regla de Limpieza de Memoria.
borra_memoria():- retractall(puntuacion(_, _)), retractall(jugador(_)).
