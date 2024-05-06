
def test_Student(name,gender,age,dormitoryNumber,institute,major,phone):
    print(f'{name}您好,您的性别是{gender},'
          f'\n目前{age}岁,'
          f'\n宿舍号为{dormitoryNumber},'
          f'\n学院是{institute},'
          f'\n专业是{major},'
          f'\n电话号为{phone}')

print("请输入您的姓名，性别，年龄，宿舍号，学院，专业，电话号")
name=input()
gender=input()
age=input()
dormitoryNumber=int(input())
institute=input()
major=input()
phone=int(input())
test_Student(name,gender,age,dormitoryNumber,institute,major,phone)
