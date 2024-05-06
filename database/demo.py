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
conn.select_db("db_shop")

#执行sql
# cursor.execute("create table test_pymysql(id int);")
cursor.execute("select * from t_member")

results:tuple= cursor.fetchall()

for i in results:
    print(i)

cursor.execute("delete")