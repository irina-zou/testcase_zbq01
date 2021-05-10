# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/5/10 23:00
# @Function :

RESULT_KEY_LIST = ['case_name', 'automatic', 'uri', 'request_mode', 'headers', 'params',
                   'expect_response_status_code',
                   'expect_response_payload', 'result', 'response_status_code', 'response_payload']


class ExcelResult(object):

    def __init__(self):
        self.result = None
        self.response_status_code = None
        self.response_payload = None
        self.case_name = None
        self.automatic = None
        self.uri = None
        self.request_mode = None
        self.headers = None
        self.params = None
        self.expect_response_status_code = None
        self.expect_response_payload = None

    def transform(self, action_result):
        # 执行结果
        self.result = action_result.result
        # 响应状态码
        self.response_status_code = action_result.response_status_code
        # 响应体
        self.response_payload = action_result.response_payload

        test_case = action_result.test_case
        self.case_name = test_case.case_name
        self.automatic = test_case.automatic
        self.uri = test_case.uri
        self.request_mode = test_case.request_mode
        self.headers = test_case.headers
        self.params = test_case.params

        self.expect_response_status_code = test_case.expect_response_status_code
        self.expect_response_payload = test_case.expect_response_payload

    def parse_to_dict(self):
        ret_dict = {'case_name': self.case_name,
                    'automatic': self.automatic,
                    'uri': self.uri,
                    'request_mode': self.request_mode,
                    'headers': self.headers,
                    'params': self.params,
                    'expect_response_status_code': self.expect_response_status_code,
                    'expect_response_payload': self.expect_response_payload,
                    'result': self.result,
                    'response_status_code': self.response_status_code,
                    'response_payload': self.response_payload}
        return ret_dict
