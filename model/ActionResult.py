# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/28 21:30
# @Function : 测试结果与测试用例的预期结果对比

class ActionResult(object):

    def __init__(self):
        # 执行结果
        self.result = False
        # 响应状态码
        self.response_status_code = ''
        # 响应体
        self.response_payload = ''
        # 对应的测试用例
        self.test_case = None
