



def filtration_sentivewords(str):

    str_new=str.replace("中国","**").replace("共产党","***")
    print(str_new)
print("请输入您想说的话")

str=input()
filtration_sentivewords(str)