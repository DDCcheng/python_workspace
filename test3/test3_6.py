import random
num = 5
x = random.randint(1, 20)
while 1:
    if num <=0:
        print("您没有机会了")
        break
    my_num = int(input("请输入你的猜测数字\n"))
    if my_num==x:
        print("猜对了！")
        break
    elif my_num>x:
        print("猜大了")
        num-=1
        continue
    elif my_num<x:
        print("猜小了")
        num-=1
        continue



