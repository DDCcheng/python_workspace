class Student:
    grades=[]
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def add_grade(self,*args):
        for item in args:
            if isinstance(item,Grade):
                self.grades.append(item.score)
            else:
                pass

    def get_average(self):
        sum=0
        for item in self.grades:
            sum+=item
        sum=sum/len(self.grades)
        return sum
class Grade:
    passing=60
    def __init__(self,score):
        self.score=score
    def is_passing(self):
        if self.score>self.passing:
            return True
        else:
            return False
grade1=Grade(100)
grade2=Grade(90)
grade3=Grade(85)
grade4=Grade(88)
grade5=Grade(70)
stu1=Student("Jerry","five grade")
stu1.add_grade(grade1,grade2,grade3,grade4,grade5)
#输出平均分
print(stu1.get_average())
#判断是否有不及格成绩
if grade1.is_passing() and grade2.is_passing() and grade3.is_passing() and grade4.is_passing()and grade5.is_passing():
    print("没有不及格成绩")
else:
    print("有不及格成绩")




