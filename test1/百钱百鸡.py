Cock=0
Hen=0
Chicken=0
for Cock in range(0,20):
    for Hen in range(0,33):
        Chicken=100-Cock-Hen
        if Chicken/3+Cock*5+Hen*3==100:
            print(f'Cock={Cock},Hen={Hen},Chicken={Chicken}')
