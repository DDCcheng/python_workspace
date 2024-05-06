

def addmy(*args):
    num=[]
    for i in range(len(args)):
        for j in range(len(args[i])):
            if isinstance(args[i], set):
                num.append(list(args[i])[j])
            else:
                num.append(args[i][j])
    args=tuple(num)
    return args

my_list=[1,2,3]
my_tuple=(10,20)
my_str="www"
my_set={5,6,7}
print(addmy(my_list,my_tuple,my_str,my_set))
