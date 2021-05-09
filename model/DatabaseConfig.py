# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/28 21:30
# @Function : 数据库配置文件的参数化


class DatabaseConfig(object):

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
