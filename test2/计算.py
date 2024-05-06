import math

for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+100+168))
    if(x*x==i+100 and y*y==i+100+168):
        print(i)

