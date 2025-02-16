import json
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
    be=MainBackend
    if ui.lineEdit_5.text() =='' and ui.lineEdit_6.text() == '':
        messagebox.showwarning( "Thông báo", "Hãy nhập thông tin học viên")
        return
    lang=ui.comboBox.currentText()
    id=ui.lineEdit.text()
    name=ui.lineEdit_2.text()
    address=ui.lineEdit_3.text()
    phone=ui.lineEdit_4.text()
    course = {}
    course['language']=lang
    if lang== 'English':
        course['level_type']=ui.comboBox_4.currentText()
        if course['level_type'] == 'IELTS' and  0< int(ui.lineEdit_5.text()) <10 and 0< int(ui.lineEdit_6.text()) <10:
            course['level']=ui.lineEdit_5.text()
            course['goal']=ui.lineEdit_6.text()
        elif course['level_type'] == 'TOEFL' and  0< int(ui.lineEdit_5.text()) <120 and 0< int(ui.lineEdit_6.text()) <120:
            course['level']=ui.lineEdit_5.text()
            course['goal']=ui.lineEdit_6.text()
        else: 
            messagebox.showerror( "Thông báo", "Giá trị điểm không phù hợp")
            return
    else: 
        course['level_type']=lang
        course['level']=ui.comboBox_2.currentText()
        course['goal']=ui.comboBox_3.currentText()
        if ui.comboBox_2.currentIndex() >ui.comboBox_3.currentIndex():
            messagebox.showwarning( "Thông báo", "Mức độ và mục tiêu không hợp lệ")
            return
    s=Student(id,name,address,phone,course)
    if MainBackend.regexAddress(address):
        if MainBackend.regexPhone(phone):
            if MainBackend.regexName(name):
                if MainBackend.regexId(id):
                    if MainBackend.addStudent(be,s):
                        messagebox.showinfo( "Thông báo", "Thêm học viên thành công")
                    else:
                        messagebox.showwarning( "Thông báo", "Thêm học viên không thành công")
                else:
                    messagebox.showwarning( "Thông báo", "CCCD không hợp lệ hoặc đã tồn tại")
            else:
                messagebox.showwarning( "Thông báo", "Tên không hợp lệ")
        else:
            messagebox.showwarning( "Thông báo", "Số điện thoại không hợp lệ")
    else:
        messagebox.showwarning("Thông báo", "Địa chỉ không hợp lệ")
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
            ui.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(student_info["phone"]))
            level = student_info['language'].get('level', 'N/A')  
            ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(level)))
            level = student_info['language'].get('goal', 'N/A')  
            ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(level)))
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
    with open('data.json','r', encoding='utf-8') as file:
        data = json.load(file)
    for row in range(ui.tableWidget.rowCount()):
        for student in data:
            if student['id'] == ui.tableWidget.item(row, 0).text():
                student['name']=str(ui.tableWidget.item(row,1).text())
                student['phone']=ui.tableWidget.item(row,2).text()
                student['language']['level']=ui.tableWidget.item(row,3).text()
                student['language']['goal']=ui.tableWidget.item(row,4).text()
    with open('data.json','w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    messagebox.showinfo('Thông báo','Lưu thành công')
def HomeTkHv():
    global ui
    ui = fe.HomeTk.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(AddHvUi)
    ui.pushButton_3.clicked.connect(SearchHv)
    ui.pushButton_2.clicked.connect(lambda:thongke())
    MainWindow.show()
def thongke():
    lang=ui.comboBox_2.currentText()
    option=ui.comboBox.currentIndex()
    ui.tableWidget.setRowCount(0)
    listKo=['Sơ cấp','Trung cấp','Cao cấp']
    listJa=['N1','N2','N3','N4','N5']
    with open('data.json','r', encoding='utf-8') as file:
            data = json.load(file)
    match option:
        case 0:
            if lang =='Tất cả':
                for i ,students in enumerate(data):
                    if isinstance(students,dict):
                        addSvTk(students)
            else:
                for i ,students in enumerate(data):
                    if students['language']['language'] == lang :
                        addSvTk(students)
        case 1:

            if lang =='Japanese' or lang == 'Tất cả':
                for i ,students in enumerate(data):
                    if students['language']['language'] =='Japanese' :
                        indexLevel= listJa.index(students['language']['level'])
                        indexGoal= listJa.index(students['language']['goal'])
                        if indexLevel >= indexGoal:
                            addSvTk(students)
            if lang =='Korean' or lang == 'Tất cả':
                for i ,students in enumerate(data):
                    if students['language']['language'] == 'Korean':
                        indexLevel= listKo.index(students['language']['level'])
                        indexGoal= listKo.index(students['language']['goal'])
                        if indexLevel >= indexGoal:
                            addSvTk(students)
            if lang =='English' or lang == 'Tất cả':
                for i ,students in enumerate(data):
                    if students['language']['language'] == 'English':
                        if students['language']['level'] >= students['language']['goal']:
                            addSvTk(students)
        case 2 :

            if lang =='Japanese' or lang == 'Tất cả':
                for i ,students in enumerate(data):
                    if students['language']['language'] =='Japanese' :
                        indexLevel= listJa.index(students['language']['level'])
                        indexGoal= listJa.index(students['language']['goal'])
                        if indexLevel < indexGoal:
                            addSvTk(students)
            if lang =='Korean' or lang == 'Tất cả':
                for i ,students in enumerate(data):
                    if students['language']['language'] == 'Korean':
                        indexLevel= listKo.index(students['language']['level'])
                        indexGoal= listKo.index(students['language']['goal'])
                        if indexLevel < indexGoal:
                            addSvTk(students)
            if lang =='English' or lang == 'Tất cả':
                for i ,students in enumerate(data):
                    if students['language']['language'] == 'English':
                        if students['language']['level'] < students['language']['goal']:
                            addSvTk(students)
        case 3:
            ui.tableWidget.setRowCount(0)
            listTemp=[]
            temp=-1
            listIe=[]
            listTof=[]
            tempIe=-1 
            tempTof=-1
            for i ,students in enumerate(data):
                if lang== 'Japanese':
                    if students['language']['language'] == 'Japanese':
                        indexLevel= listJa.index(students['language']['level'])
                        if indexLevel > temp:
                            temp=indexLevel
                            listTemp =[]
                            listTemp.append(students)
                        elif indexLevel == temp:
                            listTemp.append(students)
                elif lang== 'Korean':
                    if students['language']['language'] == 'Korean':
                        indexLevel= listKo.index(students['language']['level'])
                        if indexLevel > temp:
                            temp=indexLevel
                            listTemp =[]
                            listTemp.append(students)
                        elif indexLevel == temp:
                            listTemp.append(students)
                elif lang== 'English':
                    if students['language']['level_type'] == 'IELTS' :
                        if float(students['language']['level']) >tempIe:
                            tempIe=float(students['language']['level'])
                            listIe=[]
                            listIe.append(students)
                        elif float(students['language']['level']) == tempIe:
                            listIe.append(students)
                    elif students['language']['level_type'] == 'TOEFL' :
                        if int(students['language']['level']) >tempTof:
                            tempTof=int(students['language']['level'])
                            listTof=[]
                            listTof.append(students)
                        elif int(students['language']['level']) == tempTof:
                            listTof.append(students)
            listTemp.extend(listIe)
            listTemp.extend(listTof)
            for i in listTemp:
                addSvTk(i)
                

def addSvTk(students):
    row=ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(row)
    ui.tableWidget.setItem(row,0, QtWidgets.QTableWidgetItem(str(students['id'])))
    ui.tableWidget.setItem(row,1, QtWidgets.QTableWidgetItem(str(students['name'])))
    ui.tableWidget.setItem(row,2, QtWidgets.QTableWidgetItem(str(students['phone'])))
    ui.tableWidget.setItem(row,3, QtWidgets.QTableWidgetItem(str(students['language']['level_type'])))
    level = students['language'].get('level', 'N/A')  
    ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(level)))
    level = students['language'].get('goal', 'N/A')  
    ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(level)))
Homeui()
sys.exit(app.exec())