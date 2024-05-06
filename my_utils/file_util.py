




def print_file_info(file_name):
    """
    功能：是打印内容
    :param file_name:
    :return:
    """
    f=None
    try:
        f=open(file_name,"r",encoding="UTF-8")
        content=f.read()
        print("文件的全部内容如下")
        print(content)
    except Exception as e:
        print(f"程序出错了，原因是{e}")
    finally:
        if f:
            f.close()





def append_to_file(file_name,data):
    f=open(file_name,"w",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    append_to_file("E:/测试2.txt","他是谁")
    # print_file_info("E:/测试1.txt")















