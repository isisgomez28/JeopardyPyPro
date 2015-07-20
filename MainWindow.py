# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Models import *
from QuestionDialog import *
from functools import partial

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    questionSelected = pyqtSignal(object, object)

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.categoryWidgets = []

        self.setupUi(self)
        self.questionSelected.connect(self.onQuestionSelected)
        self.remainingQuestions = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1375, 827)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.setupButtons()
        self.setupScoreBoard()

        self.categoryWidgets[0]["verticalLayoutWidget"].raise_()
        self.categoryWidgets[1]["verticalLayoutWidget"].raise_()
        self.categoryWidgets[2]["verticalLayoutWidget"].raise_()
        self.categoryWidgets[3]["verticalLayoutWidget"].raise_()
        self.categoryWidgets[4]["verticalLayoutWidget"].raise_()
        self.categoryWidgets[1]["label"].raise_()
        self.formLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor('black'))
        self.setPalette(palette)



    def setupButtons(self):
        # Initialize Widgets
        for i in range(0, 5):
            self.categoryWidgets.append({})
            self.categoryWidgets[i]["verticalLayoutWidget"] = QtGui.QWidget(self.centralwidget)
            self.categoryWidgets[i]["verticalLayoutWidget"].setGeometry(QtCore.QRect(10+(270*i), 30, 261, 641))
            self.categoryWidgets[i]["verticalLayoutWidget"].setObjectName(_fromUtf8("verticalLayoutWidget"))
            self.categoryWidgets[i]["verticalLayout"] = QtGui.QVBoxLayout(self.categoryWidgets[i]["verticalLayoutWidget"])
            self.categoryWidgets[i]["verticalLayout"].setObjectName(_fromUtf8("verticalLayout"))
            self.categoryWidgets[i]["label"] = QtGui.QLabel(self.categoryWidgets[i]["verticalLayoutWidget"])
            self.categoryWidgets[i]["label"].setObjectName(_fromUtf8("label_"+repr(i)))
            self.categoryWidgets[i]["label"].setStyleSheet("color: yellow; background-color: blue;")
            self.categoryWidgets[i]["label"].setAlignment(Qt.AlignCenter)
            self.categoryWidgets[i]["verticalLayout"].addWidget(self.categoryWidgets[i]["label"])

            self.categoryWidgets[i]["spacer"] = QtGui.QSpacerItem(240, 3, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
            self.categoryWidgets[i]["verticalLayout"].addItem(self.categoryWidgets[0]["spacer"])

            self.categoryWidgets[i]["buttons"] = []
            for j in range(0, 5):
                self.categoryWidgets[i]["buttons"].append(QtGui.QPushButton(self.categoryWidgets[i]["verticalLayoutWidget"]))
                self.categoryWidgets[i]["buttons"][j].setMaximumSize(QtCore.QSize(16777215, 100))
                self.categoryWidgets[i]["buttons"][j].setText(_fromUtf8(""))
                self.categoryWidgets[i]["buttons"][j].setObjectName(_fromUtf8("pushButton_" + repr(i+j)))
                self.categoryWidgets[i]["verticalLayout"].addWidget(self.categoryWidgets[i]["buttons"][j])

                palette = self.categoryWidgets[i]["buttons"][j].setStyleSheet("color: yellow; background-color: blue")
                self.categoryWidgets[i]["buttons"][j].clicked.connect(partial(self.onQuestionSelected, i, j))


    def setupScoreBoard(self):
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(460, 690, 431, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet("color: yellow")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)
        self.lcdNumber_Jugador = QtGui.QLCDNumber(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumber_Jugador.setFont(font)
        self.lcdNumber_Jugador.setProperty("value", 400.0)
        self.lcdNumber_Jugador.setObjectName(_fromUtf8("lcdNumber_Jugador"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lcdNumber_Jugador)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.setStyleSheet("color: yellow")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lcdNumber_Computador = QtGui.QLCDNumber(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumber_Computador.setFont(font)
        self.lcdNumber_Computador.setProperty("value", 300.0)
        self.lcdNumber_Computador.setObjectName(_fromUtf8("lcdNumber_Computador"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lcdNumber_Computador)

        # Set lcd color to red
        self.lcdNumber_Jugador.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_Computador.setSegmentStyle(QtGui.QLCDNumber.Flat)

        palette = self.lcdNumber_Jugador.palette()
        palette.setColor(self.lcdNumber_Jugador.foregroundRole(), QColor('yellow'))
        self.lcdNumber_Jugador.setPalette(palette)

        palette = self.lcdNumber_Computador.palette()
        palette.setColor(self.lcdNumber_Computador.foregroundRole(), QColor('yellow'))
        self.lcdNumber_Computador.setPalette(palette)


    def displayScore(self):
        self.lcdNumber_Jugador.display(self.model.puntos['jugador'])
        self.lcdNumber_Computador.display(self.model.puntos['maquina'])


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Jeoperdy", None))
        self.label.setText(_translate("MainWindow", "Computador", None))
        self.label_6.setText(_translate("MainWindow", "Jugador", None))

    def setModel(self, gameModel):
        self.model = gameModel
        self.setCategories()
        self.displayScore()

    def setCategories(self):
        i = 0
        for category in self.model.categorias:
            self.categoryWidgets[i]["label"].setText(category.nombre)
            self.setQuestions(i)
            i += 1

    def setQuestions(self, categoryNum):
        for k in self.model.categorias[categoryNum].preguntas:
            self.categoryWidgets[categoryNum]["buttons"][(k-1)/100].setText('$' + repr(k))

    def onQuestionSelected(self, categoryNum, questionNum):
        # Disable Question
        self.categoryWidgets[categoryNum]["buttons"][questionNum].setEnabled(False)
        self.categoryWidgets[categoryNum]["buttons"][questionNum].setStyleSheet('background-color: gray')

        print 'categoryNum: ' + repr(categoryNum) + ', questionNum: ' + repr(questionNum)
        precio = (questionNum+1)*100
        pregunta = self.model.categorias[categoryNum].preguntas[precio]
        respuesta = self.model.categorias[categoryNum].respuestas[precio]

        questionDialog = QuestionDialog(self, self.model.prolog, pregunta, respuesta, (categoryNum*5)+questionNum+1)
        questionDialog.exec_()


        # Update scoreboard
        for i in questionDialog.malaRespuesta:
            self.model.puntos[i] -= precio

        if questionDialog.ganador:
            self.model.puntos[questionDialog.ganador] += precio

        self.displayScore()

        self.remainingQuestions -= 1
        ganador = ''
        if not self.remainingQuestions:
            ganador = 'La maquina' if model.puntos['maquina'] > model.puntos['jugador'] else 'Usted'
            QMessageBox.information(self, 'Se ha terminado el juego', + 'Se ha terminado el juego!\n' + ganador + ' es el ganador', QMessageBox.Ok)
            return

        if questionDialog.ganador == 'maquina':
            # strategy: Attempt to finish cateogyr, if not, loop categories
            j = 0
            for btn in self.categoryWidgets[categoryNum]["buttons"]:
                if btn.isEnabled():
                    self.questionSelected.emit(categoryNum,j)
                    return
                j += 1

            print 'no encontro en esta categoria...buscando en otra'

            for i in range(0, 5):
                print 'categoria ' + repr(i)
                if i == categoryNum:
                    continue
                for j in range(0, 5):
                    print 'pregunta ' + repr(j)
                    if self.categoryWidgets[i]["buttons"][j]:
                        self.questionSelected.emit(i,j)
                        return
                    j += 1
                i += 1




