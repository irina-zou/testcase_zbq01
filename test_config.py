# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/29 22:15
from unittest import TestCase
from config import config


# @Function :
class TestConfig(TestCase):
    def test_get_http_config(self):
        emailConfig = config.get_email_config()
        print(emailConfig.mail_pass)
