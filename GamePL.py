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

    def getPreguntas(self):
        for result in self.prolog.query('pregunta(Numero, Pregunta, Categoria, Puntos)'):
            print 'Pregunta ' + repr(result['Numero']) + ': ' + result['Pregunta']

    def getRespuestas(self):
        None
