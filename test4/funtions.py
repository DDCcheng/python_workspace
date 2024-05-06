#登录页面
from sign_in import sign_in
#五大功能
def show():
    print("welcome")

def add():
    print("add")

def updata():
    print("updata")

def delete():
    print("delete")

def out():
    print("exit")


#集合
def funs():
    print("请选择菜单：1 查看   2 添加    3 修改   4 删除   0 退出")
    add_result = 0
    delete_result = 0
    updata_result = 0
    while(1):
        num = int(input())
        if num == 1:
            show()
        elif num == 2:
            if add_result==0:
                add_result=sign_in()
            add()
        elif num == 3:
            if updata_result==0:
                updata_result=sign_in()
            updata()
        elif num == 0:
            out()
            return
        elif num == 4:
            if delete_result==0:
                delete_result=sign_in()
            delete()






