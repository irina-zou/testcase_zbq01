# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/29 22:33
# @Function :
import json

import requests
from requests import Response

from Config import config
from model.ActionResult import ActionResult
from model.TestCase import TestCase


class HttpRequest(object):

    def __init__(self):
        self.base_url = config.get_http_config().baseurl + ':' + config.get_http_config().port
        self.token = ''

    def login(self, account: str, password: str) -> str:
        payload = {
            'account': account,
            'password': password
        }
        headers = {
            'content-type': 'application/json'
        }
        result = requests.post(self.base_url + '/login', data=json.dump(payload), headers=headers)
        ret_json = result.json()
        self.token = ret_json['data']["token"]
        return self.token

    def assert_request(self, test_case: TestCase) -> ActionResult:
        request_mode = test_case.request_mode.upper()
        if request_mode is 'POST':
            return self.assert_post(test_case)
        else:
            return self.assert_get(test_case)

    def assert_post(self, test_case: TestCase) -> ActionResult:
        if self.token is None or len(self.token) <= 0:
            raise Exception('token is none or empty')

        url = self.base_url + test_case.uri
        payload = test_case.params
        headers = test_case.headers
        headers['token'] = self.token
        result = requests.post(url, data=json.dump(payload, headers=headers))
        return self.generate_action_result(result, test_case)

    def assert_get(self, test_case: TestCase) -> ActionResult:
        if self.token is None or len(self.token) <= 0:
            raise Exception('token is none or empty')

        url = self.base_url + test_case.uri
        payload = test_case.params
        headers = test_case.headers
        headers['token'] = self.token
        result = requests.get(url, data=json.dump(payload, headers=headers))
        return self.generate_action_result(result, test_case)

    def generate_action_result(self, result: Response, test_case: TestCase) -> ActionResult:
        action_result = ActionResult()
        action_result.result = result.status_code == test_case.expect_response_status_code and result.json() == test_case.expect_response_payload
        action_result.test_case = test_case
        action_result.response_payload = result.json()
        action_result.response_status_code = result.status_code
        return action_result


httpRequest = HttpRequest()
