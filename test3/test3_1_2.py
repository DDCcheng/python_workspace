def examine(my):
    if len(my)>6:
        print("该对象长度大于6")
    else:
        print("NO")


my_str="fuckyou"
my_list=[1,2,3,4]
my_tuple=(1,2,3,4,5,6)
examine(my_str)
examine(my_list)
examine(my_tuple)