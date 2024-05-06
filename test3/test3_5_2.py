def is_even(x):
    return x%2==0

my_list=list(eval(input("请输入一个整数的列表\n")))
new_list=list(filter(is_even,my_list))
print(new_list)