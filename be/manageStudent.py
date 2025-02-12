import random
from student import Student
from createData import createStudent
class ManageStudent:
    def __init__(self):
        self.students = []  # Danh sách sinh viên

    def add_student(self, student):
        self.students.append(student)
        return True

    def edit_student(self, student_id, new_info):
        for student in self.students:
            if student.id == student_id:
                # Cập nhật thông tin mới
                student.__dict__.update(new_info)
                break

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return True
    def search_student(self, search_term):
        # Tìm kiếm theo ID hoặc số điện thoại
        return [s for s in self.students if s.id == search_term or s.phone == search_term]

    def list_students_by_language(self, language):
        return [s for s in self.students if s.language == language]

    def calculate_success_rate(self):
        # Tính phần trăm sinh viên đạt mục tiêu
        pass
    def list_failed_students(self):
        # Danh sách sinh viên chưa đạt mục tiêu
        pass
    def sort_students(self, criteria, order):
        # Sắp xếp sinh viên theo tiêu chí
        pass

    def top_students(self, language):
        # Top 5 sinh viên xuất sắc nhất
        pass
    def getListStudents(self):
        return self.students
    def showStudent(self,student):
        print(student.__dict__)
    def exam(self):
        for student in self.students:
            if student.language['language'] == 'Japanese':
                listLevelJa = ['N1', 'N2', 'N3', 'N4','N5']
                student.language['level']=random.choice(listLevelJa)
            elif student.language['language'] == 'Korean':
                listLevelKo = ['Sơ cấp', 'Trung cấp','Cao cấp']
                student.language['level']=random.choice(listLevelKo)
            else:
                if student.language['level_type'] == 'IELTS':
                    student.language['level'] = random.choice([i/2 for i in range(0, 19)])  
                else: #TOEFL
                    student.language['level'] = random.randint(0, 120) 