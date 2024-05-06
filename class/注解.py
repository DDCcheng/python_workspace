from typing import Union


def add(x: int,y: int):
    return x+y

def func(data:list)->list:
    return data



mylist:list[Union[str,int]]=[1,2,3,"cheng"]

my_dic:dict[str,Union[str,int]]={"name":"cheng","age":20}

def funcw(data:Union[str,int])->Union[str,int]:
    return data

