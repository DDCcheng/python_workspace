def examine(my):
    if len(my)>6:
        return my[0],my[1]
    else:
        return None

my_list=[1,2,3,4,5,6,7]
my_list2=[1,2,3,4,5]

list1=examine(my_list)
list2=examine(my_list2)
print(list1)
print(list2)