#时间包
import time

def deco1(log):
    def inner(*args,**kwargs):
        #输出函数名和运行时的时间节点
        print(log.__name__)
        print(time.strftime("%Y-%M-%d %H:%M %S", time.localtime(time.time())))
        log(*args,**kwargs)
    return inner

@deco1
def log():
    print("fuck you")

log()