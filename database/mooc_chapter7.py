from pymysql import Connection

conn=Connection(
    host='localhost',
    port=3306,
    user='root',
    password='20030418ldc',
    autocommit=True
)

# print(conn.get_server_info())

#获取游标对象
cursor=conn.cursor()

#选择数据库
conn.select_db("student")

#执行sql
cursor.execute("select * from score")

results:tuple= cursor.fetchall()

for i in results:
    print(i)

cursor.execute("DELETE  FROM score WHERE score < 70;")

#关闭连接
conn.close()