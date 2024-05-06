#登录页面
def sign_in():
    number = 3
    while number != 0:
        print("请输入您的姓名")
        name = input()
        print("请输入您的密码")
        password = int(input())
        if password == 123 and name == "henu":
            print(f'欢迎{name}')
            return 1
        else:
            number -= 1
            print(f'登录失败，还有{number}次机会')
    else:
        print("登录超限，请明天再来")
        return 0
