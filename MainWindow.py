# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

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
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1370, 749)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 261, 641))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout.addWidget(self.label_1)
        spacerItem = QtGui.QSpacerItem(240, 3, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_1 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_1.setText(_fromUtf8(""))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.verticalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_4.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 30, 261, 641))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(240, 3, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_6 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_7.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_8.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_9.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_9.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(550, 30, 261, 641))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(240, 3, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton_11 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_12.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_12.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_12.setText(_fromUtf8(""))
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_13 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_13.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_13.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_13.setText(_fromUtf8(""))
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setDefault(False)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.verticalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_14.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_14.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_14.setText(_fromUtf8(""))
        self.pushButton_14.setAutoDefault(False)
        self.pushButton_14.setDefault(False)
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.verticalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_15 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_15.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_15.setText(_fromUtf8(""))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.verticalLayout_3.addWidget(self.pushButton_15)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(820, 30, 261, 641))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(240, 3, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.pushButton_16 = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_16.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_16.setText(_fromUtf8(""))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.verticalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_17.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_17.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_17.setText(_fromUtf8(""))
        self.pushButton_17.setAutoDefault(False)
        self.pushButton_17.setDefault(False)
        self.pushButton_17.setFlat(False)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.verticalLayout_4.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_18.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_18.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_18.setText(_fromUtf8(""))
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(False)
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.verticalLayout_4.addWidget(self.pushButton_18)
        self.pushButton_19 = QtGui.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_19.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_19.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_19.setText(_fromUtf8(""))
        self.pushButton_19.setAutoDefault(False)
        self.pushButton_19.setDefault(False)
        self.pushButton_19.setFlat(False)
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.verticalLayout_4.addWidget(self.pushButton_19)
        self.pushButton_20 = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_20.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_20.setText(_fromUtf8(""))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.verticalLayout_4.addWidget(self.pushButton_20)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(1090, 30, 261, 641))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtGui.QSpacerItem(240, 3, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.pushButton_21 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_21.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_21.setText(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.verticalLayout_5.addWidget(self.pushButton_21)
        self.pushButton_22 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_22.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_22.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_22.setText(_fromUtf8(""))
        self.pushButton_22.setAutoDefault(False)
        self.pushButton_22.setDefault(False)
        self.pushButton_22.setFlat(False)
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.verticalLayout_5.addWidget(self.pushButton_22)
        self.pushButton_23 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_23.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_23.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_23.setText(_fromUtf8(""))
        self.pushButton_23.setAutoDefault(False)
        self.pushButton_23.setDefault(False)
        self.pushButton_23.setFlat(False)
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.verticalLayout_5.addWidget(self.pushButton_23)
        self.pushButton_24 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 3))
        self.pushButton_24.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_24.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_24.setText(_fromUtf8(""))
        self.pushButton_24.setAutoDefault(False)
        self.pushButton_24.setDefault(False)
        self.pushButton_24.setFlat(False)
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.verticalLayout_5.addWidget(self.pushButton_24)
        self.pushButton_25 = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_25.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pushButton_25.setText(_fromUtf8(""))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.verticalLayout_5.addWidget(self.pushButton_25)
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label_2.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1370, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Jeoperdy", None))

    def setPrices(self):
        for i in range(1, 26):
            m = i % 5
            exec('self.pushButton_' + repr(i) + '.setText("$' + repr(m if m else 5) + '00")')

    def setCategories(self, categories):
        if len(categories) != 5:
            return False

        for i in range(1, 6):
            exec('self.label_' + repr(i) + '.setText("' + categories[i-1] + '")')



