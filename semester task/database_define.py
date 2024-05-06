from pymysql import Connection
'''
前提条件：
需在用户对应的数据库中建立一个order表
order_data,order_id,money,province
'''
class db_define:
    def __init__(self,user,password,db_name):
        self.user=user
        self.password=password
        self.db_name=db_name
    def connection_db(self):
        conn=Connection(
            host='localhost',
            port=3306,
            user=self.user,
            password=self.password,
            autocommit=True
        )
        cursor = conn.cursor()
        conn.select_db(self.db_name)
        return cursor,conn




