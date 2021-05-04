# _*_ coding :utf-8
# @Author : 'zoubq'
# @Time : 2021/4/28 21:11
# @Function :
from PySide2 import QtGui, QtWidgets, QtCore
import random


class MainWindowByCode(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        # 定义按钮
        self.button = QtWidgets.QPushButton("Click me!")

        self.hello = ["Hallo Welt", "你好世界！", "Hola Mundo", "Привет мир", "Hello world"]

        # 定义标签
        self.text = QtWidgets.QLabel("Hello World")
        # 文字居中对齐
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        # 定义布局，垂直分布
        self.layout = QtWidgets.QVBoxLayout()

        # 在布局上添加文字
        self.layout.addWidget(self.text)
        # 在布局上添加按钮
        self.layout.addWidget(self.button)
        # 在主窗口上布置布局
        self.setLayout(self.layout)

        # 添加槽链接
        self.button.clicked.connect(self.magic)

    # 定义槽函数
    def magic(self):
        self.text.setText(random.choice(self.hello))
