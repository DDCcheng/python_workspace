list2=list(eval(input('输入第一组向量列表:\n')))
list3=list(eval(input('输入第二组向量列表(与第一个等长):\n')))
print('内积之和为:',sum(map(lambda x,y:x*y,list2,list3)))