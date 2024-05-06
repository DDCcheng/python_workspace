import numpy as np

my_list=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(my_list)
print()
my_list_part1=my_list[0:2,1:3]
print(my_list_part1)
print()

my_list_part2=my_list[1:2,0:2]
print(my_list_part2)
print()

my_list_part3=my_list[2:3,0:1]
print(my_list_part3)
print()

my_list_part4=my_list[:,0:1]
print(my_list_part4)
print()

my_new_list=my_list*2
print(my_new_list)
print()

row_max=my_new_list.max(0)
print(row_max)
print()

column_max=my_new_list.max(1)
print(column_max)