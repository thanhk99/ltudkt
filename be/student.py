
class Student:
    def __init__(self, id, name, address, phone, language):
        self.id = id  # Căn cước công dân
        self.name = name
        self.address = address
        self.phone = phone
        self.language = language
    
class EnglishStudent(Student):
    def __init__(self, id, name, address, phone, initial_level, exam_score, target_score):
        super().__init__(id, name, address, phone, "English")
        self.initial_level = initial_level  # Trình độ ban đầu (IELTS/TOEFL)
        self.exam_score = exam_score  
        self.target_score = target_score 

class JapaneseStudent(Student):
    def __init__(self, id, name, address, phone, initial_level, exam_result, target_level):
        super().__init__(id, name, address, phone, "Japanese")
        self.initial_level = initial_level  # Trình độ ban đầu (N5, N4, ...)
        self.exam_result = exam_result  
        self.target_level = target_level  

class KoreanStudent(Student):
    def __init__(self, id, name, address, phone, initial_level, exam_result, target_level):
        super().__init__(id, name, address, phone, "Korean")
        self.initial_level = initial_level  # Trình độ ban đầu (Sơ cấp, Trung cấp, ...)
        self.exam_result = exam_result  
        self.target_level = target_level  