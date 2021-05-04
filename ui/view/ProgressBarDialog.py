from PySide2.QtWidgets import QDialog, QProgressBar, QPushButton, QVBoxLayout


class ProgressBarDialog(QDialog):

    def __init__(self, parent=None):
        super(ProgressBarDialog, self).__init__(parent)

        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 100)
        self.cancelButton = QPushButton("取消")
        self.resize(600, 200)

        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        layout.addWidget(self.cancelButton)
        self.setLayout(layout)

        self.cancelButton.clicked.connect(self.cancel_task)
        # 先暂时disable掉取消，后面实现
        self.cancelButton.setEnabled(False)

    def cancel_task(self):
        self.close()
        self.close_callback()

    def set_close_callback(self, callback):
        self.close_callback = callback

