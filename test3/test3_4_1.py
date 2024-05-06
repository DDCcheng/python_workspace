from functools import reduce


# def func():
#     x=input("输入一个字符串\n")
#     my_str=x[::-1]
#     print(my_str)
#
# func()
from operator import add
from functools import reduce
# 注意，input()本身就返回字符串，在输入时不需要在内容两侧加引号
text = input('请输入一个字符串：\n')
print(reduce(add,reversed(text)))
