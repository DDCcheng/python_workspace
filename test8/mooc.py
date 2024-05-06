import numpy as  np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'   # 使图形中的中文正常编码显示
plt.rcParams['axes.unicode_minus'] = False
#左边
plt.subplot(1,2,1)
x=np.arange(-10,10.4,0.4)
y=x*x

plt.plot(x,y,'ro-.')

plt.xlabel("tick")
plt.ylabel("voltage")
plt.title("抛物线示意图")

#右边
plt.subplot(1,2,2)
my_list=np.loadtxt("sales.csv",dtype=str,delimiter=",")
my_list_sales=my_list[1:5,1:2]
my_list_sales=my_list_sales.astype(int)
price_list=[]
for item in my_list_sales:
    price_list.append(item[0])
print(price_list)
hist,bins=np.histogram(my_list_sales,bins=[100,200,300,400,500],range=(100,500))
x=bins[0:-1]
y=price_list
plt.bar(x,y,width=5,color='steelblue',align='center')
plt.xticks(x,['第1季度','第2季度','第3季度','第4季度'])
plt.title("销量分布图")
plt.xlabel("season")
plt.ylabel("sales")
# plt.grid(True)
for x,y in zip(x,y):
    plt.text(x,y,str(y),ha='center',va='bottom')
#显示
plt.show()