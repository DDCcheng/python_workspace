import csv
my_list=[]
with open('StudentInfo.csv',mode='r',encoding='GBK') as f:
    re=csv.DictReader(f)
    for line in list(re):
        my_list.append(line)
print(my_list)
f.close()