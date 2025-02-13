
from PyQt5 import QtCore, QtGui, QtWidgets

import AddHv , Home , Search , HomeTk , Edit
import sys
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def Homeui():
    global ui
    ui = Home.Ui_Home()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    MainWindow.show()

def AddHvUi():
    global ui
    ui = AddHv.Ui_MainWindow()
    ui = ui.setupUi(MainWindow)
    MainWindow.show()

def SearchHv():
    global ui  
    ui = Search.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    ui.pushButton_4.clicked.connect(EditHV)
    MainWindow.show()

def EditHV():
    global ui
    ui = Edit.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    MainWindow.show()

def HomeTkHv():
    global ui
    ui = HomeTk.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    MainWindow.show()

Homeui()
sys.exit(app.exec())