from funtions import funs
#装饰器
def deco1(fun):
    def inner(*args,**kwargs):
        print("hello")
        fun(*args,**kwargs)
        print("good bye")
    return inner
@deco1
def my_funs():
    funs()

my_funs()