from manageStudent import ManageStudent
from student import Student
from createData import createStudent

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
                    ManageStudent.add_student(self=self.manager, createStudent())
                case "2":
                    self.edit_student()
                case "3":
                    self.delete_student()
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