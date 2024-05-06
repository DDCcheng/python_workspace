from functools import reduce

def func():
    my_list=list(eval(input("请输入一个整数列表\n")))
    print(reduce(lambda x,y:x*y,my_list))

func()