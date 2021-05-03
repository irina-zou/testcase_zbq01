import ui.view.MainWindow as MainWindow


class MainWindowViewModel(object):

    def __init__(self, view: MainWindow.MainWindow):
        self.view = view

    def handle_select_button_click(self):
        print("select button click")

    def handle_action_button_click(self):
        print("action button click")

    def handle_export_button_click(self):
        print("export button click")
