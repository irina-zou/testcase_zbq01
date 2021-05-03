from PySide2.QtWidgets import QFileDialog

import ui.view.MainWindow as MainWindow


class MainWindowViewModel(object):

    def __init__(self, view: MainWindow.MainWindow):
        self.view = view

    def handle_select_button_click(self):
        print("select button click")
        file_path, file_type = QFileDialog.getOpenFileName(self.view.ui, "选择文件路径")
        self.view.set_path_text_content(file_path)

    def handle_action_button_click(self):
        file_path = self.view.get_path_text_content()
        print("action button click: " + file_path)
        if file_path is not None and len(file_path) > 0:
            self.view.set_all_button_disable()
            self.view.progress_dialog_close()
            self.view.progress_dialog_show()


    def handle_export_button_click(self):
        print("export button click")

    def progress_dialog_closed(self):
        self.view.set_all_button_enable()
