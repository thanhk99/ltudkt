import random
import pandas as pd
import os
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

def get_file_path(filename):
    base_dir = r'd:\HK2_2024-2025\LT_KTHT\ltudkt\be'
    return os.path.join(base_dir, filename)

def createCC():
    file_path = get_file_path('new2.csv')
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
    listLeagues=['English','Japanese','Korean']
    listLevelEn=['A1','A2','B1','B2','C1','C2']
    listLevelJa=['N5','N4','N3','N2','N1']
    listLevelKo=['Sơ cấp','Trung cấp','Cao cấp']
    course={}
    course['leangue']=random.choice(listLeagues)
    if course['leangue']=='English':
        course['level']=random.choice(listLevelEn)
        course['goal']='Improve English skills'
    elif course['leangue']=='Japanese':
        course['level']=random.choice(listLevelJa)
        course['goal']='Pass JLPT exam'
    elif course['leangue']=='Korean':
        course['level']=random.choice(listLevelKo)
        course['goal']='Pass TOPIK exam'

def createStudent():
    student = {}
    student['name'] = createName()
    student['phone'] = createPhone()
    tinh , cancuoc = createCC()
    student['local'] = tinh
    student['can cuoc'] = cancuoc
    student['Gioi tinh'] = createSexual()
    student['Khoa hoc']=createCourse()
    return student

createStudent()
print(createStudent())

    

        
    