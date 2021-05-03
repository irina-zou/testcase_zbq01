
from PySide2.QtUiTools import QUiLoader

from Constant import UI_XML_DIR
import ui.viewmodel.MainWindowViewModel as MainWindowViewModel
import ui.view.ProgressBarDialog as ProgressBarDialog


class MainWindow(object):

    def __init__(self):
        self.ui = QUiLoader().load(UI_XML_DIR + 'MainWindow.ui')
        self.viewModel = MainWindowViewModel.MainWindowViewModel(self)
        self.ui.selectButton.clicked.connect(self.viewModel.handle_select_button_click)
        self.ui.actionButton.clicked.connect(self.viewModel.handle_action_button_click)
        self.ui.exportButton.clicked.connect(self.viewModel.handle_export_button_click)

        self.progressDialog = ProgressBarDialog.ProgressBarDialog()
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


