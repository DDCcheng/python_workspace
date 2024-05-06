import random

my_list=[random.randint(1,100) for i in range(20)]
print("翻转前")
print(my_list)

print("翻转后")
my_list[::2]=sorted(my_list[::2],reverse=True)
print(my_list)