import numpy as  np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'   # 使图形中的中文正常编码显示
plt.rcParams['axes.unicode_minus'] = False
list=np.loadtxt("goods.csv",dtype=str,delimiter=",")
header=list[0]
my_list=list[1:4]
print(my_list)
print()
my_list_price=my_list[:,2:3]
my_list_price=my_list_price.astype(int)


#排序
print("排序后")
# index=np.argsort(-my_list_price,axis=0)
# print(my_list[index[:,-1]])
my_list=sorted(my_list,key=lambda x:x[2],reverse=False)
print(header)
for item in my_list:
    print(item)


#max and min and avg
column_max=my_list_price.max()
column_min=my_list_price.min()
column_avg=my_list_price.mean()
print(f"商品的最高价格：{column_max},最低价格：{column_min}，平均价格：{column_avg:.2f}")

#show
price_list=[]
for item in my_list_price:
    price_list.append(item[0])
print(price_list)
hist,bins=np.histogram(my_list_price,bins=[10,20,30,40],range=(10,40))
x=bins[0:-1]
y=price_list
plt.bar(x,y,width=5,color='steelblue',align='center')
plt.xticks(x,['香皂','洗发水','毛巾'])
plt.title("商品价格情况分布图")
plt.xlabel("商品")
plt.ylabel("价格")
for x,y in zip(x,y):
    plt.text(x,y,str(y),ha='center',va='bottom')
# plt.grid(True)
plt.show()