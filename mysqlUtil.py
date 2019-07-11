import pymysql
import MySQLdb as mdb


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton()


# @singleton()
class MySQLUtil():
    def __init__(self, host, user, psd, dbName):
        self.host = host
        self.user = user
        self.passwd = psd
        self.dbName = dbName

    def connect(self):
        # self.db = MySQLdb.connect(self.host, self.user, self.passwd, self.dbName, charset='utf8')
        # self.cursor = self.db.cursor()

        self.conn = mdb.connect(self.host, self.user, self.passwd, self.dbName)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        # try:
        self.connet()
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.close()
        # except:
        #     print("查询失败")
        return res

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            # self.close()
        except:
            print("查询失败")
        return res

    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldList = []

        if (len(args) > 0) :
            for item in args:
                fieldList.append(item)
        else:
            pass
        return resList

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("事务提交失败")
            self.db.rollback()

        return count