class ManageStudent:
    def __init__(self):
        self.students = []  # Danh sách sinh viên

    def add_student(self, student):
        self.students.append(student)

    def edit_student(self, student_id, new_info):
        for student in self.students:
            if student.id == student_id:
                # Cập nhật thông tin mới
                student.__dict__.update(new_info)
                break

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

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