from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import time
import sys

from pyswip import Prolog

class PLSolver(QThread):
    def __init__(self, num, sleepSecs):
        super(PLSolver, self).__init__()
        self.sleepSecs = sleepSecs
        self.respuesta = None

    def run(self):
        time.sleep(self.sleepSecs)
        self.respuesta = 'gonna fly now'
