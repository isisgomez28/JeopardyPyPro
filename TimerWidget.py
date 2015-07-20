from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class TimerWidget(QtGui.QLCDNumber):
    timeout = pyqtSignal()

    def __init__(self, duration, parent=None):
        super(TimerWidget, self).__init__(parent)
        self.timeLeft = duration
        self.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.setStyleSheet('color: black')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTimeLeft)
        self.timer.start(1000)

        self.resize(300, 60)
        self.showTimeLeft()

    @pyqtSlot()
    def showTimeLeft(self):
        self.display(self.timeLeft)

        if self.timeLeft == 0:
            self.timeout.emit()
        else:
            self.timeLeft -= 1

