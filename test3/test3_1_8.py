def add_instance(*num1):
    num=0
    for i in range(len(num1)):
        if isinstance(num1[i],int):
            num+=num1[i]
    print(num)
add_instance(1,2,3,4,5.1,5.55)
