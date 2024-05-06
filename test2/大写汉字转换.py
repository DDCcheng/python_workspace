

list1=["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
list2=["圆","拾","佰","仟","萬"]
money=input("请输入五位数以内的金额：\n")
n=len(money)
new_money=[]
for i in money:
    n-=1
    new_money.append(list1[int(i)])
    new_money.append(list2[n])
new_money.append("整")
for i in new_money:
    print(i,end="")



