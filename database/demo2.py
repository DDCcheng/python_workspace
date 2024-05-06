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
conn.select_db("db_shop")

#执行sql
cursor.execute("insert into test_pymysql values(100)")

#提交事务或者设置自动提交
# conn.commit()

#关闭连接
conn.close()


