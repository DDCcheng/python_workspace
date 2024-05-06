class Circle:
    def __init__(self,radius=0,area=0):
        self.__radius=radius
        self.area=area
    def SetRadius(self,radius):
        self.__radius=radius
    def Area(self):
        self.area=3.14*self.__radius*self.__radius
        return self.area
    def __str__(self):
        print(f"圆的面积是{self.area}")
    def __gt__(self, other):
        return self.area>other.area

if __name__ == '__main__':
    #first
    circle1=Circle()
    circle1.SetRadius(eval(input("第一个圆的半径为\n")))
    a=circle1.Area()
    print(f"第一个圆的面积为{a}")
    #second
    circle2=Circle()
    circle2.SetRadius(eval(input("第二个圆的半径为\n")))
    b = circle2.Area()
    print(f"第二个圆的面积为{b}")
    #compare
    # print(circle1)
    print(f"第一个圆的面积比第二个大  {circle1>circle2}")