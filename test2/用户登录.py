number=3
while number!=0:
    print("请输入您的姓名,和密码")
    name=input()
    password=int(input())
    if password==123:
        print(f'欢迎{name}')
        break
    else:
        number-=1
        print(f'登录失败，还有{number}次机会')
else:
    print("登录超限，请明天再来")