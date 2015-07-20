from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from TimerWidget import *

class ResponseDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(ResponseDialog, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.addButton(QPushButton("Responder", self.buttonBox), QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(QPushButton("Desertar", self.buttonBox), QDialogButtonBox.RejectRole)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)
        self.respuesta = QtGui.QLineEdit(self)

        self.respuestaTimer = TimerWidget(10, self)
        self.respuestaTimer.timeout.connect(self.respuestaTimerTimedOut)
        self.respuestaTimer.show()

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.respuesta)
        self.verticalLayout.addWidget(self.respuestaTimer)
        self.verticalLayout.addWidget(self.buttonBox)
        self.setWindowTitle('Respuesta')

    def respuestaTimerTimedOut(self):
        self.reject()

    def accepted(self):
        self.accept()

    def rejected(self):
        self.reject()


