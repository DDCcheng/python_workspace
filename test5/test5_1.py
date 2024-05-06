
class Animal:
    sum=0
    def __init__(self,sex):
        self.sex=sex
        Animal.sum+=1
    def func(*args):
        print("类对象的个数为",Animal.sum)

cat=Animal("female")
dog=Animal("male")

Animal.func()

