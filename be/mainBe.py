from manageStudent import ManageStudent
from student import Student
from createData import createCC, createStudent , createName , createPhone

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
            print("7. Thống kê tỉ lệ người học đạt mục tiêu")
            print("8. Danh sách người học chưa đạt mục tiêu")
            print("9. Thoát")
            choice = input("Chọn chức năng: ")
            match choice:
                case "1":
                    student = createStudent()
                    a = ManageStudent.add_student(self.manager, student)
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
                                        if a in self.manager.students:
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
                    s1 = createStudent()
                    if self.manager.delete_student(s1.id):
                        print("Xóa người học thành công")
                    else:
                        print("Xóa người học thất bại")
                case "4":
                    self.search_student()
                case "5":
                    self.list_students()
                case "6":
                    self.list_students_by_language()
                case "7":
                    self.calculate_success_rate()
                case "8":
                    self.list_failed_students()
                case "9":
                    break
                case _:
                    print("Chức năng không hợp lệ")
                    return
                
MainBackend.run(self=MainBackend())
