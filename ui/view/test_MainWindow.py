from unittest import TestCase

from PySide2 import QtWidgets
import MainWindow as MainWindow
import sys


class TestMainWindows(TestCase):

    def test_test(self):
        app = QtWidgets.QApplication([])
        window = MainWindow.MainWindow()
        window.ui.show()
        sys.exit(app.exec_())
