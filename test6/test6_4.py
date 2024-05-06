


good_lists=[568,239,368,425,121,219,834,1263,26]
x=eval(input("请输入左区间值\n"))
y=eval(input("请输入右区间值\n"))
required_lists=[]
for item in good_lists:
    if item>=x and item<=y:
        required_lists.append(item)
print("正排序")
required_lists_right=sorted(required_lists,reverse=False)
print(required_lists_right)
print("反排序")
required_lists_oppsite=sorted(required_lists,reverse=False)
print(required_lists_oppsite)
print("平均价格")
sum=0
for item in required_lists_oppsite:
    sum+=item
sum=sum/len(required_lists_oppsite)
print(sum)
