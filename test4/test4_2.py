#登录页面
from sign_in import sign_in
#装饰器
def deco1(fun):
    def inner(*args,**kwargs):
        result=sign_in()
        if result==1:
            fun(*args,**kwargs)
    return inner

@deco1
def fun():
    print()
    print("who you are")
    print("your father")
    print("fuck you bitch")
fun()



