def func():
    x=input("请输入若干整数，用空格隔开\n")
    x_list=x.split()
    my_list=[int(x_list[i]) for i in range(len(x_list))]
    new_list=list(map(str,my_list))
    print(new_list)


func()
