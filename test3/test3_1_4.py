def examine(my):
    num = 0
    word=0
    whitespace=0
    others=0
    for i in range(len(my)):
        if str.isalpha(my[i]):
            word+=1
        elif my[i]==" ":
            whitespace+=1
        elif str.isdigit(my[i]):
            num += 1
        else:
            others+=1
    print(f"num={num}")
    print(f"word={word}")
    print(f"whitespace={whitespace}")
    print(f"others={others}")

my_str="abc   123==="
examine(my_str)