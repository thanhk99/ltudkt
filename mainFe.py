from PyQt5 import QtCore, QtGui, QtWidgets
from mainBe import MainBackend
import fe.AddHv as AddHv , fe.Home , fe.Search , fe.HomeTk , fe.Edit , fe.Edit_fail , fe.Edit_success , fe.Message_Add_fail , fe.Message_Add_success,fe.Message_Delete,fe.Message_Delete_fail,fe.Message_Delete_success
import sys
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def Homeui():
    global ui
    ui = fe.Home.Ui_Home()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    MainWindow.show()

def AddHvUi():
    global ui
    ui = AddHv.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_them.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    ui.pushButton_6.clicked.connect(Message_Add_successUi)

    MainWindow.show()

def SearchHv():
    global ui  
    ui = fe.Search.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    ui.pushButton_4.clicked.connect(EditHV)
    ui.pushButton_6.clicked.connect(Message_DeleteUi)
    MainWindow.show()

def EditHV():
    global ui
    ui = fe.Edit.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    ui.pushButton_6.clicked.connect(Edit_successUi)
    MainWindow.show()

def HomeTkHv():
    global ui
    ui = fe.HomeTk.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    MainWindow.show()

def Edit_failUi():
    global ui
    ui = fe.Edit_fail.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

def Edit_successUi():
    global ui
    ui = fe.Edit_success.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_6.clicked.connect(EditHV)
    MainWindow.show()

def Message_Add_failUi():
    global ui
    ui = fe.Message_Add_fail.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_6.clicked.connect(AddHvUi)
    MainWindow.show()
    pass

def Message_Add_successUi():
    global ui
    ui = fe.Message_Add_success.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_6.clicked.connect(AddHvUi)
    MainWindow.show()
    pass

def Message_DeleteUi():
    global ui
    ui = fe.Message_Delete.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_6.clicked.connect(Message_Delete_successUi)
    ui.pushButton_7.clicked.connect(SearchHv)
    MainWindow.show()
    pass

def Message_Delete_failUi():
    global ui
    ui = fe.Message_Delete_fail.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    pass
def Message_Delete_successUi():
    global ui
    ui = fe.Message_Delete_success.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_6.clicked.connect(SearchHv)
    MainWindow.show()
    pass
Homeui()
sys.exit(app.exec())