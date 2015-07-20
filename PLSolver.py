from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import time
import sys

from pyswip import Prolog

class PLSolver(QThread):
    def __init__(self, prolog, num, sleepSecs):
        super(PLSolver, self).__init__()
        self.sleepSecs = sleepSecs
        self.respuesta = None
        self.num = num
        print 'num: ' + repr(self.num)
        self.prolog = prolog

    def run(self):
        time.sleep(self.sleepSecs)
        print '1'
        self.prolog.consult('pl/IA_Analysis.pl')
        print '2'
        num = self.num

        print 'about to query'

        solucion = [s["X"] for s in self.prolog.query('pregunta_' + repr(num) + '(X)', maxresult=1)]
        self.respuesta = solucion[0]

