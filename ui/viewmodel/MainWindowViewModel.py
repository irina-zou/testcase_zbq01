import json
import os

from PySide2.QtWidgets import QFileDialog

import ui.model.MainWindowModel as MainWindowModel
from Constant import PROJECT_DIR_PATH
from ExcelExporter import ExcelExporter
from model.ExcelResult import ExcelResult


class MainWindowViewModel(object):

    def __init__(self, window):
        self.view = window
        self.model = MainWindowModel.MainWindowModel(self)

    def handle_select_button_click(self):
        print("select button click")
        file_path, file_type = QFileDialog.getOpenFileName(self.view.ui, "选择文件路径")
        self.view.set_path_text_content(file_path)

    def handle_action_button_click(self):
        file_path = self.view.get_path_text_content()
        print("action button click: " + file_path)
        if file_path is not None and len(file_path) > 0:
            self.view.set_all_button_disable()
            self.view.progress_dialog_close()
            self.view.progress_dialog_show()
            self.model.action_test_case()


    def handle_export_button_click(self):
        print("export button click: ")
        action_result_list = self.model.result_list
        print(action_result_list)
        export = ExcelExporter()
        excel_result_list = []
        for i in range(len(action_result_list)):
            action_result = action_result_list[i]
            print(action_result)
            export_result = ExcelResult()
            export_result.transform(action_result)
            excel_result_list.append(export_result)
        export.write_to_excel(PROJECT_DIR_PATH + os.sep + 'test_result' + os.sep + 'test_result.xlsx', excel_result_list)




    def progress_dialog_closed(self):
        self.view.set_all_button_enable()

    def get_file_path(self):
        return self.view.get_path_text_content()

    def set_progress_callback(self, progress_rate):
        self.view.set_progress_value(progress_rate*100)

    def set_success_num(self, num):
        self.view.set_success_num(str(num))

    def set_fail_num(self, num):
        self.view.set_fail_num(str(num))

    def set_sum_num(self, num):
        self.view.set_sum_num(str(num))
