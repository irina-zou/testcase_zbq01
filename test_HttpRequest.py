# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/5/6 22:43
from unittest import TestCase


# @Function :
from Config import Config
from HttpRequest import HttpRequest


class TestHttpRequest(TestCase):

    def test_login(self):
        config = Config()
        http_request = HttpRequest()
        token = http_request.login('admin', 'admin')
        print(token)

