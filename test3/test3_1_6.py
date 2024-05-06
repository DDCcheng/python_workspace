

def addnum(*num1):
    num=0
    for i in range(len(num1)):
        num+=num1[i]
    print(num)
addnum(1,2,3,4)