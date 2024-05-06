# import time
#
# t = open("E:/测试.txt", "r", encoding="UTF-8")
# print(type(t))
#
#
# # print(f"读取10字节的结果{t.read(10)}")
# # print(f"读取全部内容: {t.read()}")
#
#
# print(t.readlines())  #一次读取所有内容，并存放到列表中
# print(t.readline())  #一次读取一行
#
#
#
# for line in t:
#     print(f"每一行数据: {line}")
#
#
# t.close()
#
# with open("E:/测试.txt", "r", encoding="UTF-8") as  f:
#     for line in f:
#         print(f"每一行数据是:{line}")
#
#
# time.sleep(10)
#
#


#单词计数

#方法1
#r是读取
# t = open("E:/测试.txt", "r", encoding="UTF-8")
# sum=0
# for line in t:
#     splits = line.strip()
#     words = splits.split(" ")
#     for s in words:
#         if s=="itheima":
#             sum+=1
#
# t.close()
# print(sum)


#方法2
# content=t.read()
# count=content.count("itheima")
# print(count)

#w是写文件,如果文件存在并且有内容，会全部清空再写入



f=open("E:/测试1.txt","w",encoding="UTF-8")

f.write("我是谁")


f.flush()

f.close()


#a是写文件，会在文件原有的基础上继续写，不会清空





#   清华的镜像网站下载第三方包
#   -i https://pypi.tuna.tsinghua.edu.cn/simple









