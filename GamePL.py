from pyswip import Prolog

class GamePL(object):
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult('pl/GameDatabase.pl')
        self.prolog.consult('pl/GameLogic.pl')

    def nuevoJugador(self, name):
        None

    def actualizaPuntuacion(self, jugador, puntos):
        None

    def borrarMemoria(self):
        None

    def getPuntuacion(self, jugador):
        None

    def getCategorias(self):
        return self.prolog.query('categoria(Categoria, Descripcion)')

    def getPreguntas(self):
        return self.prolog.query('pregunta(Numero, Pregunta, Categoria, Puntos)')

    def getRespuestas(self):
        return self.prolog.query('respuesta(Numero, Respuesta)')
