from time import sleep

from PySide2.QtCore import QObject, Signal

from threading import Thread

from ExcelLoader import ExcelLoader
from HttpRequest import httpRequest
from model.ActionResult import ActionResult


class TestCaseSignals(QObject):
    progress_signal = Signal(float)
    result_list_signal = Signal(list)


test_case_signals = TestCaseSignals()


class MainWindowModel(object):

    def __init__(self, view_model):
        self.progress_rate = 0
        self.result_list = []
        self.success_num = 0
        self.fail_num = 0
        self.sum_num = 0

        self.viewModel = view_model
        test_case_signals.progress_signal.connect(self.set_progress_rate)
        test_case_signals.result_list_signal.connect(self.set_result_list)

    def set_progress_rate(self, rate: float):
        self.progress_rate = rate
        self.viewModel.set_progress_callback(self.progress_rate)

    def set_success_num(self, num):
        self.success_num = num
        self.viewModel.set_success_num(self.success_num)

    def set_fail_num(self, num):
        self.fail_num = num
        self.viewModel.set_fail_num(self.fail_num)

    def set_sum_num(self, num):
        self.sum_num = num
        self.viewModel.set_sum_num(self.sum_num)

    def set_result_list(self, result_list):
        self.result_list = result_list
        self.set_sum_num(len(self.result_list))
        self.set_success_num(len(list(filter(lambda model: model.result, self.result_list))))
        self.set_fail_num(len(list(filter(lambda model: not model.result, self.result_list))))

    def action_test_case(self):
        self.clear_cache()
        thread = Thread(target=self.action_task)
        thread.start()

    def clear_cache(self):
        self.set_progress_rate(0)
        self.set_success_num(0)
        self.set_fail_num(0)
        self.set_sum_num(0)
        self.set_result_list([])

    def action_task(self):
        # 1. 读取出excel内容
        excel_loader = ExcelLoader()
        test_case_list = excel_loader.load(self.viewModel.get_file_path())
        test_case_signals.progress_signal.emit(0.5)
        # 2. 一条条执行testcase
        result_list = []
        for test_case in test_case_list:
            action_result = httpRequest.assert_request(test_case)
            result_list.append(action_result)
        # 3. 完成
        test_case_signals.result_list_signal.emit(result_list)
        test_case_signals.progress_signal.emit(1.0)

