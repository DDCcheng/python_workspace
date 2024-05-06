
from file_define import TextFileReader,JsonFileReader
from data_define import Record
from database_define import db_define




textFileReader = TextFileReader("E:/Desktop/python/2011年1月销售数据.txt")
jsonFileReader = JsonFileReader("E:/Desktop/python/2011年2月销售数据JSON.txt")

jan_data=textFileReader.read_data()

feb_data=jsonFileReader.read_data()

all_data:list[Record]=jan_data+feb_data


#获取数据库链接以及游标
my_conn=db_define("root","20030418ldc","py_sql")
cursor=my_conn.connection_db()[0]
conn=my_conn.connection_db()[1]
#执行sql
for record in all_data:
    sql=f"insert into orders(order_data,order_id,money,province) " \
        f"values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    cursor.execute(sql)


#关闭链接
conn.close()
