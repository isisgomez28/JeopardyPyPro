from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from TimerWidget import *
from ResponseDialog import *
from PLSolver import *

class QuestionDialog(QtGui.QDialog):
    def __init__(self, parent, prolog, pregunta, respuesta, preguntaNum):
        super(QuestionDialog, self).__init__(parent)
        self.respuesta = respuesta.lower()
        self.prolog = prolog
        self.preguntaNum = preguntaNum
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

        #self.plSolver = PLSolver(prolog, preguntaNum, 5)
        #self.plSolver.finished.connect(self.maquinaResponded)
        #self.plSolver.start()

        self.ganador = None
        self.malaRespuesta = []
        self.respondiendo = False
        self.respuestaTimedOut = False

        QTimer.singleShot(5000, self.performPLQuery)

    def respuestaTimerTimedOut(self):
        self.respuestaTimedOut = True
        if not self.respondiendo:
            self.accept()

    def performPLQuery(self):
        while (self.respondiendo):
            QTimer.singleShot(500, self.performPLQuery)
            return

        if not self.respuestaTimedOut and self.ganador is None:
            self.btnRespuesta.setEnabled(False)
            self.prolog.consult('pl/IA_Analysis.pl')
            print 'preguntaNum: ' + repr(self.preguntaNum)
            solucion = [s["X"] for s in self.prolog.query('pregunta_' + repr(self.preguntaNum) + '(X)', maxresult=1)]
            respuesta = solucion[0]

            print 'plSolver respuesta: ' + respuesta

            if self.respuesta == respuesta.lower():
                self.ganador = 'maquina'
                QMessageBox.warning(self, 'Respuesta Acertada por Maquina', 'Respuesta Acertada por Maquina:\n' + respuesta, QMessageBox.Ok)
                self.accept()
            else:
                self.malaRespuesta.append('maquina')
                QMessageBox.warning(self, 'Respuesta NO Acertada por Maquina', 'Respuesta NO Acertada por Maquina:\n' + respuesta, QMessageBox.Ok)
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
