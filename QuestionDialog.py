from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from TimerWidget import *
from ResponseDialog import *
from PLSolver import *

class QuestionDialog(QtGui.QDialog):
    def __init__(self, parent, pregunta, respuesta, preguntaNum):
        super(QuestionDialog, self).__init__(parent)
        self.respuesta = respuesta.lower()
        print self.respuesta
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

        self.respuestaTimer = TimerWidget(30, self)
        self.respuestaTimer.timeout.connect(self.respuestaTimerTimedOut)
        self.respuestaTimer.show()

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.respuestaTimer)
        self.verticalLayout.addWidget(self.btnRespuesta)

        self.plSolver = PLSolver(preguntaNum, 5)
        self.plSolver.finished.connect(self.maquinaResponded)
        self.plSolver.start()

        self.ganador = None
        self.malaRespuesta = []
        self.respondiendo = False
        self.respuestaTimedOut = False

    def respuestaTimerTimedOut(self):
        self.respuestaTimedOut = True
        if not self.respondiendo:
            self.accept()

    def maquinaResponded(self):
        print 'plSolver respuesta: ' + self.plSolver.respuesta

        self.btnRespuesta.setEnabled(False)
        if self.respuesta == self.plSolver.respuesta.lower():
            self.ganador = 'maquina'
            QMessageBox.warning(self, 'Respuesta Acertada por Maquina', 'Respuesta Acertada por Maquina:\n' + self.respuesta, QMessageBox.Ok)
            self.accept()
        else:
            self.malaRespuesta.append('maquina')
            QMessageBox.warning(self, 'Respuesta NO Acertada por Maquina', 'Respuesta NO Acertada por Maquina:\n' + self.respuesta, QMessageBox.Ok)
            self.btnRespuesta.setEnabled(True)


    @pyqtSlot()
    def btnRespuestaClicked(self):
        self.respondiendo = True
        responseDialog = ResponseDialog(self)
        self.btnRespuesta.setEnabled(False)
        status = responseDialog.exec_()

        if status == QDialog.Accepted:
            print 'accepted'
            print responseDialog.respuesta.text()
            if self.respuesta == str(responseDialog.respuesta.text()).lower():
                print 'gana jugador'
                self.ganador = 'jugador'
                self.accept()
        else:
            print 'rejected'
            self.malaRespuesta.append('jugador')

        self.respondiendo = False
        if self.respuestaTimedOut:
            self.accept()
