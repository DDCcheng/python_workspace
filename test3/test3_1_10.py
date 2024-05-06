

def addmy(**kwargs):
    print(kwargs)

my_dic1={'one':1}
my_dic2={'two':2}

addmy(**my_dic1,**my_dic2)