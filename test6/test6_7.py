import random
my_list=[random.randint(1,100) for i in range(50)]
print(my_list)
for item in my_list[::-1]:
    if item%2!=0:
        my_list.remove(item)
print(my_list)