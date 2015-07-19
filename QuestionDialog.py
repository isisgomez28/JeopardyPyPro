from PyQt4 import QtCore, QtGui

class QuestionDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QuestionDialog, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.textBrowser = QtGui.QTextBrowser(self)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.buttonBox)

    def setPregunta(self, pregunta):
        self.textBrowser.setText(pregunta)
