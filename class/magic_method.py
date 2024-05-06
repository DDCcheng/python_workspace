class student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"大家好,我是{name}，我{age}岁了")
    def __eq__(self, other):
        return self.age==other.age

stu1=student("zhou",20)
stu2=student("cheng",20)
print(stu1==stu2)