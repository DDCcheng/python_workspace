
fib=0

print("请输入范围")

n=int(input())

first_number=0

second_number=1
#如果小于3，就直接输出前两个数
if(n<=2):
    print(1)
    print(1)
#如果大于3，就先输出第一个数，再依次按规律输出后面的数
else:
    print(1)
    for i in range(1,n):
        fib=first_number+second_number
        first_number=second_number
        second_number=fib
        print(fib)
