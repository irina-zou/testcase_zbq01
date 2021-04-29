# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/29 22:48
from unittest import TestCase

from constant import TEST_EXCEL_DIR_PATH
from excelLoader import ExcelLoader
import os

# @Function :
class TestExcelLoader(TestCase):
    def test_read_sheet(self):
        loader = ExcelLoader()
        filePath = TEST_EXCEL_DIR_PATH + os.sep + 'abcd.xlsx'
        print(filePath)
        loader.load(TEST_EXCEL_DIR_PATH + os.sep + 'abcd.xlsx')

    def test_batch_load(self):
        loader = ExcelLoader()
        test_case_list = loader.batchLoad(TEST_EXCEL_DIR_PATH)
        print(len(test_case_list))
