# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/5/10 22:51
import os
from unittest import TestCase

# @Function :
from Constant import PROJECT_DIR_PATH
from ExcelExporter import ExcelExporter
from model.ExcelResult import ExcelResult


class TestExcelExporter(TestCase):
    def test_write_to_excel(self):
        export = ExcelExporter()
        excel_result_list = []
        excel_result = ExcelResult()
        excel_result.case_name = '测试'
        excel_result.response_payload = "{ 'success': 'ok' }"

        excel_result_list.append(excel_result)
        export.write_to_excel(PROJECT_DIR_PATH + os.sep + 'test_result' + os.sep + 'test.xlsx', excel_result_list)
