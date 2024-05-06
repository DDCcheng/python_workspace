
def func(list):
    return sorted(list,key=lambda x:x,reverse=True)


x=input()
my_x=x.split()
my_list=[int(my_x[i]) for i in range(len(my_x))]
print(func(my_list))