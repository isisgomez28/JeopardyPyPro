from PyQt4 import QtCore, QtGui
import sys
from MainWindow import *
from GamePL import *
from Models import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow();
    game = GamePL()
    categorias = game.getCategorias()
    preguntas = game.getPreguntas()
    respuestas = game.getRespuestas()

    # Obtener data de BD de Prolog
    gameModel = GameModel()
    for categoria in categorias:
        gameModel.addCategoria(CategoryModel(categoria["Categoria"], 100, 100))

    for pregunta in preguntas:
        i = int((pregunta["Numero"]-1) / 5)
        gameModel.categorias[i].setPregunta(pregunta["Puntos"] , pregunta["Pregunta"])

    for respuesta in respuestas:
        i = int((respuesta["Numero"]-1) / 5)
        j = respuesta["Numero"] % 5
        j = j if j else 5
        j *= 100
        gameModel.categorias[i].setRespuesta(j, respuesta["Respuesta"])

    ex.setModel(gameModel)

    ex.show();
    sys.exit(app.exec_());
