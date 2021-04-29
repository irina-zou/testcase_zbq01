# _*_ coding :utf-8
#@Author : 'zoubq'
# @Time : 2021/4/29 22:22
# @Function :

class TestCase(object):

    def __init__(self, model):
        self.caseName = model["CaseName"]
        self.automatic = model["automatic"]
        self.uri = model["uri"]
        self.request_mode = model["request_mode"]
        self.headers = model["headers"]
        self.params = model["params"]