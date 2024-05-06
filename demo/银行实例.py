




money=50000
name=None

name=input("请输入您的姓名")

# 查询函数

def query(show_header):
    if show_header:
        print("------------查询余额---------------")

    print(f"{name}您好，您的余额为{money}")


# 存款
def add(num):
    global  money
    money+=num
    print("-------------存款----------------")
    print(f"{name}，您好，您存款{num}成功")
    query(False)


# 取款
def get_money(num):
    global  money
    money-=num
    print("-------------取款----------------")
    print(f"{name}，您好，您取款{num}成功")

    query(False)
def main():
    print("------------主菜单----------------")
    print(f"{name}您好，欢迎来到黑马银行，请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入你的选择")


while True:
    keboard_input=main()
    if keboard_input=="1":
        query(True)
        continue
    elif keboard_input=="2":
        num=int(input("您要存多少钱"))
        add(num)
        continue
    elif keboard_input=="3":
        num=int(input("您要取多少钱"))
        get_money(num)
        continue
    else:
        print("程序退出了")
        break















