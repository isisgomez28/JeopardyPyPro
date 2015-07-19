class CategoryModel(object):
    def __init__(self, nombre, startAmount, increment, preguntas=[None, None, None, None, None], respuestas=[None, None, None, None, None]):
        self.nombre = nombre
        self.preguntas = {}
        self.respuestas = {}
        for i in range(0, 5):
            currentAmount = startAmount+(i*increment)
            self.preguntas[currentAmount] = preguntas[i]
            self.preguntas[currentAmount] = respuestas[i]

    def setPregunta(self, cantidad, pregunta):
        self.preguntas[cantidad] = pregunta

    def setRespuesta(self, cantidad, respuesta):
        self.respuestas[cantidad] = respuesta

class GameModel(object):
    def __init__(self):
        self.categorias = []

    def addCategoria(self, categoria):
        self.categorias.append(categoria)
