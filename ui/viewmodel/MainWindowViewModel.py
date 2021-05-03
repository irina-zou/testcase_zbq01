from PySide2.QtWidgets import QFileDialog

import ui.view.MainWindow as MainWindow


class MainWindowViewModel(object):

    def __init__(self, view: MainWindow.MainWindow):
        self.view = view
        self.ui = view.ui
        self.view.ui.selectButton.clicked.connect(self.handle_select_button_click)
        self.view.ui.actionButton.clicked.connect(self.handle_action_button_click)
        self.view.ui.exportButton.clicked.connect(self.handle_export_button_click)

    def handle_select_button_click(self):
        print("select button click")
        file_path, file_type = QFileDialog.getOpenFileName(self.view.ui, "选择文件路径")
        self.ui.pathText.setText(file_path)

    def handle_action_button_click(self):
        print("action button click")

    def handle_export_button_click(self):
        print("export button click")
