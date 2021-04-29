# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/28 21:11
# @Function : 读取 config.json中的内容

from constant import CONFIG_PATH
import json

from model.DatabaseConfig import DatabaseConfig
from model.EmailConfig import EmailConfig
from model.HttpConfig import HttpCinfig


class Config(object):
    def __init__(self):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_database_config(self):
        databaseJson = self.data["database"]
        return DatabaseConfig(databaseJson["host"],
                              databaseJson["port"],
                              databaseJson["user"],
                              databaseJson["password"],
                              databaseJson["db"])

    def get_http_config(self):
        httpJson = self.data["http"]
        return HttpCinfig(httpJson["baseurl"], httpJson["port"], httpJson["timeout"])

    def get_email_config(self):
        emailJson = self.data["email"]
        return EmailConfig(emailJson["on_off"],emailJson["mail_host"],
                           emailJson["mail_user"],emailJson["mail_pass"],
                           emailJson["mail_port"],emailJson["sender"],
                           emailJson["receiver"],emailJson["subject"],
                           emailJson["content"])


config = Config()
emailConfig = config.get_email_config()
print(emailConfig.mail_pass)
