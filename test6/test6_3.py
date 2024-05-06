class Student:
    def __init__(self,grade):
        self.grade=grade
stu_list=[]
stu1=Student(80)
stu2=Student(100)
stu3=Student(70)
stu4=Student(90)
stu5=Student(60)
stu_list.append(stu1)
stu_list.append(stu2)
stu_list.append(stu3)
stu_list.append(stu4)
stu_list.append(stu5)
#排序
stu_list.sort(key=lambda x:x.grade,reverse=True)
for item in stu_list:
    print(item.grade)
#max and min

max=stu_list[0].grade
min=stu_list[len(stu_list)-1].grade
print(f"最大值为{max}")
print(f"最小值为{min}")
print("----------------")
#移除最大，最小值
stu_list.remove(stu_list[0])
stu_list.remove(stu_list[len(stu_list)-1])
print("移除后的列表为")
for item in stu_list:
    print(item.grade)
print("-----------------")
#拷贝加反转
stu_list1=stu_list.copy()
stu_list1=stu_list1[::-1]
for item in stu_list1:
    print(item.grade)
