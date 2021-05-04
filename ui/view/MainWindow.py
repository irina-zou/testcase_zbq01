
from PySide2.QtUiTools import QUiLoader

from Constant import UI_XML_DIR
from ui.view.ProgressBarDialog import ProgressBarDialog
from ui.viewmodel.MainWindowViewModel import MainWindowViewModel


class MainWindow(object):

    def __init__(self):
        self.ui = QUiLoader().load(UI_XML_DIR + 'MainWindow.ui')
        self.viewModel = MainWindowViewModel(self)
        self.ui.selectButton.clicked.connect(self.viewModel.handle_select_button_click)
        self.ui.actionButton.clicked.connect(self.viewModel.handle_action_button_click)
        self.ui.exportButton.clicked.connect(self.viewModel.handle_export_button_click)

        self.progressDialog = ProgressBarDialog()
        self.progressDialog.set_close_callback(self.viewModel.progress_dialog_closed)

    def set_path_text_content(self, file_path):
        self.ui.pathText.setText(file_path)

    def get_path_text_content(self):
        return self.ui.pathText.toPlainText()

    def set_all_button_disable(self):
        self.ui.selectButton.setEnabled(False)
        self.ui.actionButton.setEnabled(False)
        self.ui.exportButton.setEnabled(False)

    def set_all_button_enable(self):
        self.ui.selectButton.setEnabled(True)
        self.ui.actionButton.setEnabled(True)
        self.ui.exportButton.setEnabled(True)

    def progress_dialog_close(self):
        self.progressDialog.close()

    def progress_dialog_show(self):
        self.progressDialog.show()

    def set_progress_value(self, value):
        self.progressDialog.progressBar.setValue(value)
        if value >= 100:
            self.progress_dialog_close()
            self.set_all_button_enable()

    def set_success_num(self, num):
        self.ui.succNumLabel.setText(num)

    def set_fail_num(self, num):
        self.ui.failNumLabel.setText(num)

    def set_sum_num(self, num):
        self.ui.sumNumLabel.setText(num)


