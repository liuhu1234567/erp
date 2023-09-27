import pymysql


class MyMysql(object):
    def __init__(self, host, user, password, port, database):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.cursor = self.db.cursor()

    def insert(self, sql):
        """
        向数据库插入数据
        @param sql: sql语句
        @return: 受影响的行数
        """
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.rowcount

    def select(self, sql):
        """
        查询数据库
        @param sql: sql语句
        @return: 查到的结果
        """
        self.cursor.execute(sql)
        self.db.commit()
        r = self.cursor.fetchall()
        return r

    def close(self):
        """关闭游标，关闭数据库链接"""
        self.cursor.close()
        self.db.close()
