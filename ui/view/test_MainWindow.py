from unittest import TestCase

from PySide2 import QtWidgets
from MainWindow import MainWindow
import sys


class TestMainWindows(TestCase):

    def test_test(self):
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.ui.show()
        sys.exit(app.exec_())
