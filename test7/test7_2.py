import csv
my_list=[]
#读操作
with open('user.csv',mode='r',encoding='UTF-8') as f1:
    re1=csv.DictReader(f1)
    for line in re1:
        my_list.append(line)
        print(line['name'],line['email'])

#写操作
with open('usercopy.csv',mode='w',encoding='UTF-8',newline="") as f2:
    fieldname=['name','username','email']
    wr=csv.DictWriter(f2,fieldnames=fieldname)
    wr.writeheader()
    wr.writerows(my_list)
