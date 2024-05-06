my_str=input()
n=int(my_str.split(" ")[0])
m=int(my_str.split(" ")[1])
k=100
num=[]
for i in range(n):
    num[i]=[]
for i in range(n):
    str1=input()
    for j in range(m):
        num[i][j]=str1[j]

print(num)
