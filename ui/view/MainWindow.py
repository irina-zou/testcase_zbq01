
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtUiTools import QUiLoader
import os

from Constant import PROJECT_DIR_PATH


class MainWindow(object):

    def __init__(self):
        self.ui = QUiLoader().load(PROJECT_DIR_PATH + os.sep + 'resource/ui/MainWindow.ui')

    def test(self):
        pass
