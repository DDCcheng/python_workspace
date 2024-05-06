
# *args 所有参数会被整合为一个元组
# **args 所有参数会被整合为一个字典


def user_info(*args):
    print(args)


user_info('tom')

user_info('tttt',11,22222,'sb')


def user_info1(**kwargs):
    print(kwargs)




user_info1(ww=22,ll=11)
