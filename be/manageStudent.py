import random
from .student import Student
from .createData import createStudent
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
    def search_student(self, search_term):
        # Tìm kiếm theo ID hoặc số điện thoại
        return [s for s in self.students if s.id == search_term or s.phone == search_term]

    def list_students_by_language(self, language):
        return [s for s in self.students if s.language == language]

    def calculate_success_rate(self):
        # Tính phần trăm sinh viên đạt mục tiêu
        total = len(self.students)
        successful_students=0
        if total == 0:
            return 0
        for student in self.students:
            if student.language['language'] == 'Japanese' and student.language['level'] in ['N1', 'N2']:
                successful_students += 1
            elif student.language['language'] == 'Korean' and student.language['level'] in ['Trung cấp', 'Cao cấp']:
                successful_students += 1
            elif student.language['level_type'] == 'IELTS' and student.language['level'] >= 6.0:
                successful_students += 1
            elif student.language['level_type'] == 'TOEFL' and student.language['level'] >= 80:
                successful_students += 1

        success_rate = (successful_students / total) * 100
        return success_rate
    
        pass
    def list_failed_students(self):
        # Danh sách sinh viên chưa đạt mục tiêu
        failed_students = []
        for student in self.students:
            if student.language['language'] == 'Japanese' and student.language['level'] not in ['N1', 'N2']:
                failed_students.append(student)
            elif student.language['language'] == 'Korean' and student.language['level'] not in ['Trung cấp', 'Cao cấp']:
                failed_students.append(student)
            elif student.language['level_type'] == 'IELTS' and student.language['level'] < 6.0:
                failed_students.append(student)
            elif student.language['level_type'] == 'TOEFL' and student.language['level'] < 80:
                failed_students.append(student)
        
        if failed_students:
            print("Danh sách sinh viên chưa đạt mục tiêu:")
        for student in failed_students:
            if student.language['language'] == 'Japanese':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Trình độ: {student.language['level']}")
            elif student.language['language'] == 'korean':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Trình độ: {student.language['level']}")
            elif student.language['level_type'] == 'IELTS':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Chứng chỉ : {student.language['level_type']} , Trình độ : {student.language['level']}")
            elif student.language['level_type'] == 'TOEFL':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Chứng chỉ : {student.language['level_type']} , Trình độ : {student.language['level']}")
        else:
            print("Không có sinh viên nào chưa đạt mục tiêu.")
        return failed_students


        pass
    def sort_students(self, criteria, order):
        # Sắp xếp sinh viên theo tiêu chí
        pass

    def top_students(self, language):
    # Top 5 sinh viên xuất sắc nhất
        excellent_students = []

        for student in self.students:
            if student.language['language'] == language:
                if language == 'Japanese' and student.language['level'] in ['N1', 'N2']:
                    excellent_students.append(student)
            elif language == 'Korean' and student.language['level'] in ['Cao cấp', 'Trung cấp']:
                excellent_students.append(student)
            elif language == 'English' and (
                (student.language['level_type'] == 'IELTS' and student.language['level'] >= 6.5) or
                (student.language['level_type'] == 'TOEFL' and student.language['level'] >= 80)):
                excellent_students.append(student)

    # Sắp xếp danh sách sinh viên xuất sắc
        if language == 'Japanese':
            excellent_students.sort(key=lambda x: ['N1', 'N2', 'N3', 'N4', 'N5'].index(x.language['level']))
        elif language == 'Korean':
            excellent_students.sort(key=lambda x: ['Cao cấp', 'Trung cấp', 'Sơ cấp'].index(x.language['level']))
        elif language == 'English':
            excellent_students.sort(key=lambda x: x.language['level'], reverse=True)

    # In ra danh sách sinh viên xuất sắc
        if excellent_students:
            print(f"Danh sách sinh viên xuất sắc ngôn ngữ {language}:")
        for student in excellent_students:
            if student.language['language'] == 'Japanese':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Trình độ: {student.language['level']}")
            elif student.language['language'] == 'korean':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Trình độ: {student.language['level']}")
            elif student.language['level_type'] == 'IELTS':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Chứng chỉ : {student.language['level_type']} , Trình độ : {student.language['level']}")
            elif student.language['level_type'] == 'TOEFL':
                print(f"- Tên: {student.name} , Ngôn ngữ: {student.language['language']} , Chứng chỉ : {student.language['level_type']} , Trình độ : {student.language['level']}")
            else:
                print("Không có sinh viên nào chưa đạt mục tiêu.")
        else:
            print(f"Không có sinh viên nào xuất sắc ngôn ngữ {language}.")

        return excellent_students


        
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