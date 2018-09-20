import MySQLdb
from com.hot.config.definer import *
from DBUtils.PooledDB import PooledDB


# 数据库连接管理类
class DbManager:
    def __init__(self):
        print("Init DB pool ...")
        conn_kwargs = {'host': options.DB_HOST, 'user': options.DB_USER, 'passwd': options.DB_PASS,
                       'db': options.DB_NAME, 'charset': "utf8"}
        self._pool = PooledDB(MySQLdb, mincached=0, maxcached=10, maxshared=10, maxusage=10000, **conn_kwargs)
        print("Finished init DB pool !!!")

    def get_conn(self):
        return self._pool.connection()


_dbManager = DbManager()


# 数据库操作类
class DBHelper:
    @staticmethod
    def execute_and_get_id(sql, param=None):
        """ 执行插入语句并获取自增id """
        conn = _dbManager.get_conn()
        cursor = conn.cursor()
        if param is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, param)
        table_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return table_id

    @staticmethod
    def execute(sql, param=None):
        """ 执行sql语句 """
        conn = _dbManager.get_conn()
        cursor = conn.cursor()
        if param is None:
            rowcount = cursor.execute(sql)
        else:
            rowcount = cursor.execute(sql, param)
        cursor.close()
        conn.close()

        return rowcount

    @staticmethod
    def query_one(sql, param=None):
        """ 获取一条信息 """
        conn = _dbManager.get_conn()
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        if param is None:
            rowcount = cursor.execute(sql)
        else:
            rowcount = cursor.execute(sql, param)
        if rowcount > 0:
            res = cursor.fetchone()
        else:
            res = None
        cursor.close()
        conn.close()

        return res

    @staticmethod
    def query_all(sql, param=None):
        """ 获取所有信息 """
        conn = _dbManager.get_conn()
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        if param is None:
            rowcount = cursor.execute(sql)
        else:
            rowcount = cursor.execute(sql, param)
        if rowcount > 0:
            res = cursor.fetchall()
        else:
            res = None
        cursor.close()
        conn.close()

        return res


# if __name__ == '__main__':
    # res = DBHelper.execute('select count(*) from users ')
    # print(str(res))
    #
    # res = DBHelper.query_one("select * from users limit 1")
    # print(str(res))
    #
    # res = DBHelper.query_all('select * from users limit 10')
    # print(str(res))

    # ok 防sql 注入
    # res = DBHelper.query_one("select * from users where phone = %s and email = %s",
    #                          ("18520523706", "kawai566@yeah.net"))
    # res = DBHelper.query_one("select * from users where money = %s", (11.2,))
    # res = DBHelper.query_all("select * from users where phone = %s and email = %s",
    #                          ("18520523706", "kawai566@yeah.net"))
    #
    # print(str(res))

