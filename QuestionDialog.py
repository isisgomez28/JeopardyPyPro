from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

class QuestionDialog(QtGui.QDialog):
    def __init__(self, parent, pregunta, respuesta):
        super(QuestionDialog, self).__init__(parent)
        self.respuesta = respuesta.lower()
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #self.buttonBox = QtGui.QDialogButtonBox(self)
        #self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.btnRespuesta = QtGui.QPushButton(self)
        self.btnRespuesta.setText('Responder')
        self.btnRespuesta.clicked.connect(self.btnRespuestaClicked)

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setStyleSheet('background-color: blue; color: white')
        self.textBrowser.setText(pregunta)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        #self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.btnRespuesta)
        self.ganador = None

    @pyqtSlot()
    def btnRespuestaClicked(self):
            text, ok = QtGui.QInputDialog.getText(self, 'Respuesta',
                'Entre su respuesta:')

            if ok:
                if self.respuesta == str(text).lower():
                    self.ganador = 'jugador'
                    self.accept()
                else:
                    self.btnRespuesta.setEnabled(False)

