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

%% Ganador
ganador(Jug1, Jug2, Ganador):- puntuacion(Jug1, X), puntuacion(Jug2, Y), auxiliarGanador(X, Y, Ganador, Jug1, Jug2).
auxiliarGanador(X, Y, Ganador, Jug1, Jug2) :-  X > Y, Ganador = Jug1 ; X < Y, Ganador = Jug2; X==Y, Ganador = 'Empate'.

%% Regla de Limpieza de Memoria.
borra_memoria():- retractall(puntuacion(_, _)), retractall(jugador(_)).