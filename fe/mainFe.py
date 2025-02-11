
from PyQt5 import QtCore, QtGui, QtWidgets

import AddHv , Home
import sys
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def Homeui():
    global ui
    ui = Home.Ui_Home()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    MainWindow.show()

def AddHvUi():
    global ui
    ui = AddHv.Ui_MainWindow()
    ui = ui.setupUi(MainWindow)
    MainWindow.show()

Homeui()
sys.exit(app.exec())