from pymysql import Connection

conn=Connection(
    host='localhost',
    port=3306,
    user='root',
    password='20030418ldc'
)

# print(conn.get_server_info())

#获取游标对象
cursor=conn.cursor()

#选择数据库
conn.select_db("py_sql")

#执行sql
# cursor.execute("create table test_pymysql(id int);")
cursor.execute("select * from orders order by order_data DESC")
# 获取查询的内容
results:tuple=(cursor.fetchall())
#打开文件，进行读取模式
f=open("E:/Desktop/test.txt","w",encoding="UTF-8")
#利用for语句循环读入
for i in results:
    f.write(str(i))
    f.write("\n")

# results:tuple= cursor.fetchall()
#
# for i in results:
#     print(i)

#关闭链接，并刷新
conn.close()
f.flush()
f.close()

