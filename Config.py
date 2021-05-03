# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/28 21:11
# @Function : 读取 config.json中的内容

from Constant import CONFIG_PATH
import json

from model.DatabaseConfig import DatabaseConfig
from model.EmailConfig import EmailConfig
from model.HttpConfig import HttpConfig


class Config(object):
    def __init__(self):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_database_config(self):
        database_json = self.data["database"]
        return DatabaseConfig(database_json["host"],
                              database_json["port"],
                              database_json["user"],
                              database_json["password"],
                              database_json["db"])

    def get_http_config(self):
        http_json = self.data["http"]
        return HttpConfig(http_json["baseurl"], http_json["port"], http_json["timeout"])

    def get_email_config(self):
        email_json = self.data["email"]
        return EmailConfig(email_json["on_off"], email_json["mail_host"],
                           email_json["mail_user"], email_json["mail_pass"],
                           email_json["mail_port"], email_json["sender"],
                           email_json["receiver"], email_json["subject"],
                           email_json["content"])


config = Config()

