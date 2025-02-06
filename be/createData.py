import random
import pandas as pd
import os
from student import Student
def createName():
    firstName=['Phạm','Nguyễn','Trần','Lê','Huỳnh','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Đào','Đinh','Kim','Phan','Vũ','Tạ','Trịnh','Chu','La','Lâm','Lưu','Mai','Quách','Thái','Tô','Hoa','Tăng','Đoàn','Trương','Nghiêm','Đinh','Đặng']
    middleName=['Thị','Văn','Đình','Ngọc','Hữu','Thế','Quốc','Văn','Thành','Hồng','Đức','Minh']
    lastName=['An','Bình','Châu','Dũng','Hải','Hào','Hiền','Hùng','Hưng','Khánh','Linh','Long','Mạnh','Minh','Nghĩa','Phú','Quân','Quang','Sơn','Thắng','Thành','Thu','Tiến','Trung','Tuấn','Tùng','Vinh','Xuân','Yến']
    name=random.choice(firstName)+' '+random.choice(middleName)+' '+random.choice(lastName)
    return name

def createPhone():
    phone='0'
    nhamang=['32','33','34','35','36','37','38','39','70','79','77','76','78','89','88','86','96','97','98','86','91','94','83','84','85','92','56','58','99']
    phone+=random.choice(nhamang)
    for i in range(7):
        phone+=str(random.randint(0,9))
    return phone

def createCC():
    file_path = __file__  # Lấy đường dẫn của file hiện tại
    directory_path = os.path.dirname(file_path)
    file_path=os.path.join(directory_path, 'new2.csv')
    try:
        df = pd.read_csv(file_path, dtype={'ma': str})  # Đọc cột 'ma' dưới dạng chuỗi


        # Đảm bảo tất cả mã tỉnh có đúng 3 số
        df['ma'] = df['ma'].str.zfill(3)  # Thêm số 0 nếu thiếu

        # Tạo dictionary ánh xạ tỉnh -> mã tỉnh
        local_dict = dict(zip(df['tinh'], df['ma']))

        # Chọn ngẫu nhiên một tỉnh
        selected_tinh = random.choice(list(local_dict.keys()))
        ma_tinh = local_dict[selected_tinh]  # Lấy mã tỉnh tương ứng

        # Sinh số ngẫu nhiên cho 9 số còn lại
        cc_number = ma_tinh
        for _ in range(9):
            cc_number += str(random.randint(0, 9))  # Thêm 9 số ngẫu nhiên

        return selected_tinh, cc_number
    except Exception as e:
        print(f"An error occurred in createCC(): {e}")
        return None
    
def createSexual():
    sexual=['Nam','Nữ']
    return random.choice(sexual)

def createCourse():
    listLeagues = ['English', 'Japanese', 'Korean']
    listLevelEn = ['IELTS', 'TOEFL']  # Nên dùng số cho IELTS, TOEFL
    listLevelJa = ['N5', 'N4', 'N3', 'N2', 'N1']
    listLevelKo = ['Sơ cấp', 'Trung cấp', 'Cao cấp']
    course = {}
    course['language'] = random.choice(listLeagues)  # Sửa lỗi chính tả "leangue"

    if course['language'] == 'English':
        course['level_type'] = random.choice(listLevelEn) # Loại level (IELTS hay TOEFL)
        if course['level_type'] == 'IELTS':
            course['level'] = random.choice([i/2 for i in range(0, 19)])  # IELTS từ 0.0 - 9.0, bước 0.5
            course['goal'] = random.choice([i/2 for i in range(int(course['level']*2), 19)]) # Goal >= level, max 9
        else: #TOEFL
            course['level'] = random.randint(0, 120)  # TOEFL từ 0 - 120
            course['goal'] = random.randint(course['level'], 120) # Goal >= level, max 120
    elif course['language'] == 'Japanese':
        course['level'] = random.choice(listLevelJa)
        # Đặt mục tiêu phù hợp với level tiếng Nhật. Ví dụ:
        levels = {'N5': 1, 'N4': 2, 'N3': 3, 'N2': 4, 'N1': 5}
        current_level_num = levels[course['level']]
        possible_goals = [level for level, num in levels.items() if num >= current_level_num]
        course['goal'] = random.choice(possible_goals)

    elif course['language'] == 'Korean':
        course['level'] = random.choice(listLevelKo)
        # Tương tự tiếng Nhật, đặt mục tiêu phù hợp
        levels = {'Sơ cấp': 1, 'Trung cấp': 2, 'Cao cấp': 3}
        current_level_num = levels[course['level']]
        possible_goals = [level for level, num in levels.items() if num >= current_level_num]
        course['goal'] = random.choice(possible_goals)

    return course

def createStudent():
    tinh , cancuoc = createCC()
    student= Student(cancuoc,createName(),tinh,createPhone(),createCourse())
    return student
# def resultStudent():

s=createStudent()
print(s.id)
print(s.name)
print(s.address)
print(s.phone)
print(s.language)



    

        
    