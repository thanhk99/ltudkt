from be.manageStudent import ManageStudent
from be.student import Student
from be.createData import createCC, createStudent , createName , createPhone
import json
import os
class MainBackend():
    def __init__(self):
        self.manager = ManageStudent()

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Thêm mới người học")
            print("2. Sửa thông tin người học")
            print("3. Xóa người học")
            print("4. Tìm kiếm người học")
            print("5. Xem danh sách người học")
            print("6. Hiển thị danh sách người học theo ngôn ngữ đăng kí")
            print("7. Tỉ lệ người học đạt mục tiêu")
            print("8. Danh sách người học chưa đạt mục tiêu")
            print("9. Danh sách người học xuất sắc nhất")
            print("10. Thoát")
            choice = input("Chọn chức năng: ")
            match choice:
                case "1":
                    student = createStudent()
                    if self.manager.add_student(student):
                        print("Thêm người học thành công")
                        print(student.__dict__)
                    else:
                        print("Thêm người học thất bại")

                case "2":
                    s1 = createStudent()
                    while True:
                        print("1.Sửa từng thông tin")
                        print("2.Sửa toàn bộ thông tin")
                        print("3.Thoát")
                        choice = input("Chọn cách sửa: ")
                        match choice:
                            case "1":
                                print("sửa thông tin name / address , id / phone ")
                                choice1 = input("Chọn thông tin cần sửa (name/address/phone): ")

                                match choice1:
                                    case "name":
                                        new_name = createName()
                                        a = ManageStudent.edit_student(self.manager, s1.id , new_name)
                                        print(self.manager.getListStudents())
                                        if a in self.manager.getListStudents():
                                            print("Sửa thông tin người học thành công")
                                        else:
                                            print("Sửa thông tin người học thất bại")
                                    case "address":
                                        tinh , cancuoc = createCC()
                                        new_address = tinh
                                        new_cc = cancuoc
                                        a = ManageStudent.edit_student(self.manager, s1.id , new_address)
                                        if a in self.manager.students:
                                            print("Sửa thông tin người học thành công")
                                        else:
                                            print("Sửa thông tin người học thất bại")
                                        a = ManageStudent.edit_student(self.manager, s1.id , new_cc)
                                        if a in self.manager.students:
                                            print("Sửa thông tin người học thành công")
                                        else:
                                            print("Sửa thông tin người học thất bại")
                                    case "phone":
                                        new_phone = createPhone()
                                        a = ManageStudent.edit_student(self.manager, s1.id , new_phone)
                                        if a in self.manager.students:
                                            print("Sửa thông tin người học thành công")
                                        else:
                                            print("Sửa thông tin người học thất bại")
                                
                                    case _:
                                        print("Thông tin không hợp lệ")
                                        return
                            case "2":
                                new_name = createName()
                                tinh , cancuoc = createCC()
                                new_address = tinh
                                new_cc = cancuoc
                                new_phone = createPhone()
                                new_info = {'name': new_name, 'address': new_address, 'phone': new_phone}
                                a = ManageStudent.edit_student(self.manager, s1.id , new_info)
                                if a in self.manager.students:
                                    print("Sửa thông tin người học thành công")
                                else:
                                    print("Sửa thông tin người học thất bại")
                            case "3":
                                break

                            case _:
                                print("Chức năng không hợp lệ")
                                return
                case "3":
                    cccd=input("Nhập cccd muốn xóa : ")
                    if self.manager.delete_student(cccd):
                        print("Xóa người học thành công")
                    else:
                        print("Xóa người học thất bại")
                case "4":
                    id=input("Nhập cccd hoặc tên của người học : ")
                    students=self.manager.getListStudents()
                    if id.isdigit():
                        for s in students:
                            if id in s.id :
                                print(s.__dict__)
                    else:
                        for s in students:
                            if id in s.name :
                                print(s.__dict__)
                    print("Tìm kiếm hoàn tất")
                case "5":
                    self.showList()
                case "6":
                    students=self.manager.getListStudents()
                    language=input("Nhập ngôn ngữ muốn tìm (Enghlish / Japanese / korean) : ")
                    for s in students:
                        if s.language['language']== language:
                            self.manager.showStudent(s)
                    print("Tìm kiếm hoàn tất")
                case "7":
                    self.manager.exam()
                    self.manager.calculate_success_rate()
                    print("Tỉ lệ người học đạt mục tiêu :" , self.manager.calculate_success_rate() ,"%")
                    # self.manager.calculate_success_rate()
                    # print("Tỉ lệ người học đạt mục tiêu :" , self.manager.calculate_success_rate() ,"%")
                case "8":
                    self.manager.exam()
                    self.manager.list_failed_students()
                case "9":
                    self.manager.exam()
                    self.manager.top_students(self.manager)
                case "10":
                    break
                case _:
                    print("Chức năng không hợp lệ")
                    return
    def createStudent(self):
        student = createStudent()
        self.manager.add_student(student)
        file_path = 'data.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                try:
                    existing_data = json.load(json_file)  # Đọc dữ liệu
                    # Kiểm tra xem dữ liệu có phải là danh sách không
                    if not isinstance(existing_data, list):
                        existing_data = []  # Nếu không phải, khởi tạo danh sách rỗng
                except json.JSONDecodeError:
                    existing_data = []  # Nếu file rỗng hoặc không hợp lệ, khởi tạo danh sách rỗng
        else:
            existing_data = []  # Nếu file không tồn tại, khởi tạo danh sách rỗng

        existing_data.append(student.__dict__)
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
        return True
    def showSearchRs(self,id):
        file_path = 'data.json'
        with open(file_path, 'r', encoding='utf-8') as json_file:
            students=json.load(json_file)
        listRs=[]
        if id.isdigit():
            for s in students:
                if id in s['id'] :
                    listRs.append(s)
        else:   
            for s in students:
                if id in s['name'] :
                    listRs.append(s)
        return listRs
    def deleteStudent(self ,cccd):
        file_path = 'data.json'
        with open(file_path,'r', encoding='utf-8') as json_file:
            students=json.load(json_file)
        for i , s in enumerate(students):
            if cccd in s['id']:
                del students[i]
        with open(file_path,'w', encoding='utf-8') as json_file:
            json.dump(students, json_file, ensure_ascii=False, indent=4)
    def showList(self):
        students=self.manager.getListStudents()
        if len(students)==0:
            print("khong co sinh vien nao")
        else:
            for student in students:
                print(student.language['language'])
                self.manager.showStudent(student)