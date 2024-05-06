
numberIncrease=1
numberDecrease=1
for i in range(1,365):
    numberIncrease=1.01*numberIncrease
    numberDecrease=0.99*numberDecrease
print('天天向上='+str(numberIncrease))
print('天天后退='+str(numberDecrease))
I3D2=1.01*1.01*1.01*0.99*0.99
numberI3D2=1
for i in range(1,int(365/5)):
    numberI3D2*=I3D2
print("3打2晒="+str(round(numberI3D2,3)))