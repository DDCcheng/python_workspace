
def number_factorial_add(number1,number2,number3):
    number1_new=number1*number1*number1
    number2_new=number2*number2*number2
    number3_new=number3*number3*number3
    number_new=number1_new+number2_new+number3_new
    return number_new

for i in range(100,199):
    i_unit=int(i%10)
    i_decade=int(i%100/10)
    i_hundreds=int(i/100)
    if i==number_factorial_add(i_unit,i_decade,i_hundreds):
        print(i)

