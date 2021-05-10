# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/29 22:22
# @Function :
import json


class TestCase(object):

    def __init__(self, model):
        self.case_name = model["case_name"]
        self.automatic = model["automatic"]
        self.uri = model["uri"]
        self.request_mode = model["request_mode"]
        self.headers = json.loads(model["headers"])
        self.params = json.loads(model["params"])

        self.expect_response_status_code = model["expect_response_status_code"]
        self.expect_response_payload = json.loads(model["expect_response_payload"])
