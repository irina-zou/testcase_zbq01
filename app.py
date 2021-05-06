# _*_ coding :utf-8
#@Author : 'zoubq'
# @Time : 2021/5/6 22:51
# @Function :
import sys

from PySide2 import QtWidgets

from ui.view.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec_())

