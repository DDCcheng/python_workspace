import math


def func(a,b,c):
    num=b*b-4*a*c
    if b*b-4*a*c<0:
        return
    else:
        num1=math.sqrt(b * b - 4 * a * c)
        x1=(-b-num1)/2*a
        x2=(-b+num1)/2*a
        print(f"x1={'%.0f'%x1}\nx2={'%.0f'%x2}")


func(1,1,-6)
