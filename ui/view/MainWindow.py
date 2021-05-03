
from PySide2.QtUiTools import QUiLoader

from Constant import UI_XML_DIR
import ui.viewmodel.MainWindowViewModel as MainWindowViewModel


class MainWindow(object):

    def __init__(self):
        self.ui = QUiLoader().load(UI_XML_DIR + 'MainWindow.ui')
        self.viewModel = MainWindowViewModel.MainWindowViewModel(self)
