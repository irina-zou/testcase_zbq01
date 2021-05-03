# _*_ coding :utf-8
#@Author : 'zoubq'
# @Time : 2021/4/28 21:12
# @Function : 常量
import os

PROJECT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

"""
config.json path
"""
CONFIG_PATH = PROJECT_DIR_PATH + os.sep + 'resource' + os.sep + 'config' + os.sep + 'config.json'

"""
*.ui 文件所在目录 
"""
UI_XML_DIR = PROJECT_DIR_PATH + os.sep + 'resource' + os.sep + 'ui' + os.sep

TEST_EXCEL_DIR_PATH = PROJECT_DIR_PATH + os.sep + 'test_excel'



