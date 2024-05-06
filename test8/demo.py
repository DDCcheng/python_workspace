# import numpy as np
#
# a=np.arange(10)
# print(a)
#
# name="snow storm"
# name[5]='x'
# print(name)

s1 = 'Hello \
World!'
# s2 = 'It's a desk.'
s3 = 'It\'s a desk.'
s4 = "It's a desk."
s5 = '''He said:
"It's a desk." '''
print(s1)
# print(s2)
print(s3)
print(s4)
print(s5)
print('Hello \nWorld!')
print('Hello \tWorld!')
x,y=4,5
print(x|y)

def func2(**kwargs):
    print(kwargs)
d = {'name':'Alex'}
func2(name='alex')
func2(**d)
