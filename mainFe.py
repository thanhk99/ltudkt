from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import Qt
import tkinter as tk
from tkinter import messagebox
from mainBe import MainBackend
from be.student import Student
import fe.AddHv as AddHv , fe.Home , fe.Search , fe.HomeTk , fe.Edit 
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

def AddHvUi(): #thêm học viên : Thêm nhanh với dự liệu được tạo ngẫu nhiên hoặc với dữ liệu nhập từ bàn phím
    global ui
    ui = AddHv.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_them.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_5.clicked.connect(HomeTkHv)
    ui.pushButton_6.clicked.connect(lambda:addStudent())
    ui.pushButton_7.clicked.connect(lambda:quickAddStudent()) #thêm nhanh
    MainWindow.show()
def quickAddStudent():
    be=MainBackend()
    if MainBackend.createStudent(be):  
        messagebox.showinfo( "Thông báo", "Thêm học viên thành công")
    else:
        messagebox.showwarning( "Thông báo", "Thêm học viên không thành công")
def addStudent():
    be=MainBackend()
    lang=ui.comboBox.currentText()
    id=ui.lineEdit.text()
    name=ui.lineEdit_2.text()
    address=ui.lineEdit_3.text()
    phone=ui.lineEdit_4.text()
    course = {}
    course['language']=lang
    if lang== 'English':
        course['level_type']=ui.comboBox_4.currentText()
        course['level']=ui.lineEdit_5.text()
        course['goal']=ui.lineEdit_6.text()
    else: 
        course['level_type']=lang
        course['level']=ui.comboBox_2.currentText()
        course['goal']=ui.comboBox_3.currentText()
    s=Student(id,name,address,phone,course)
    if MainBackend.regexAddress(address):
        if MainBackend.regexPhone(phone):
            if MainBackend.regexName(name):
                if MainBackend.regexId(id):
    # if MainBackend.regexName(name):
    #     messagebox.showinfo( "Thông báo", "Tên không hợp lệ")
    # if MainBackend.addStudent(be,s):
    #     messagebox.showinfo( "Thông báo", "Thêm học viên thành công")
    # else:
    #     messagebox.showwarning( "Thông báo", "Thêm học viên không thành công")
def SearchHv():
    global ui  
    ui = fe.Search.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_2.clicked.connect(lambda:search())    #tìm kiếm học viên
    ui.pushButton_5.clicked.connect(HomeTkHv)
    ui.pushButton_4.clicked.connect(lambda : edit())             #Edit       
    ui.pushButton_6.clicked.connect(lambda :delete())
    MainWindow.show()
def search():
    be = MainBackend()
    temp=ui.lineEdit.text()
    data = MainBackend.showSearchRs(be,temp)
    ui.tableWidget.setRowCount(0)
    for index, student_info in enumerate(data):
        if isinstance(student_info,dict):
            row=ui.tableWidget.rowCount()
            ui.tableWidget.insertRow(row)
            item_id = QtWidgets.QTableWidgetItem(student_info['id'])
            item_id.setFlags(item_id.flags() & ~Qt.ItemIsEditable)
            ui.tableWidget.setItem(row, 0, item_id)
            ui.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(student_info['name']))
            ui.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(student_info['language']['language']))
            ui.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(student_info['phone']))
        else:
            print(student_info)
def delete() :
    be=MainBackend()
    ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
    ui.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
    current_row = ui.tableWidget.currentRow()
    current_item =ui.tableWidget.item(current_row, 0)
    if current_item and current_item.column() == 0:
        # Lấy dữ liệu từ ô
        data = current_item.text()  
        MainBackend.deleteStudent(be,data)
        ui.tableWidget.removeRow(current_row)
    else:
        print("No item selected.")
def edit():
    be=MainBackend()
    print('ok')
def HomeTkHv():
    global ui
    ui = fe.HomeTk.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    MainWindow.show()
Homeui()
sys.exit(app.exec())