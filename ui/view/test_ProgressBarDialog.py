import sys
from unittest import TestCase

from PySide2 import QtWidgets

from ui.view.ProgressBarDialog import ProgressBarDialog


class TestProgressBarDialog(TestCase):

    def test_cancel_task(self):
        app = QtWidgets.QApplication([])
        dialog = ProgressBarDialog()
        dialog.show()
        sys.exit(app.exec_())
