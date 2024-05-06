
class student:
    name=None,
    def sayhi1(self):
        print(f'大家好我是{self.name}')
    def sayhi2(self, msg):
        print(f'大家好,我是{self.name}，{msg}')
    def __init__(self):
        print("大家好，我是你们的大爹")


stu = student()
stu.name="周杰伦"
stu.sayhi1()
stu.sayhi2("m3")
stu.__init__()