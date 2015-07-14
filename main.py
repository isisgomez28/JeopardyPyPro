from PyQt4 import QtCore, QtGui
import sys
from MainWindow import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow();
    ex.setPrices()
    cats = ['Categoria1', 'Categoria2', 'Categoria3', 'Categoria4', 'Categoria5']
    ex.setCategories(cats)
    ex.show();
    sys.exit(app.exec_());
