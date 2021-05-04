import sys
from unittest import TestCase

from PySide2 import QtWidgets

from ui.MainWindowByCode import MainWindowByCode


class TestMainWindow(TestCase):

    def test_main_window(self):
        app = QtWidgets.QApplication([])
        window = MainWindowByCode()
        window.show()
        sys.exit(app.exec_())
