import sys
import importlib.util

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QCheckBox

from widget.ui.main_design import Ui_MainWindow
from widget.clockwidget import ClockWidget
from widget.widged import BaseWidget


class NewWidget(BaseWidget):

    def __init__(self, design_ui):
        super().__init__()

        self.ui = design_ui()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Widget Manager')

        self.ui.add_widget_button.clicked.connect(self.add_widget)

        self.clock_widget = ClockWidget()
        self.ui.clock_checkbox.clicked.connect(lambda: self.display_widget(self.ui.clock_checkbox, self.clock_widget))

    def add_widget(self):
        filename, path = self.get_file_name()
        widget = self.create_widget(filename, path)

        checkbox = QCheckBox(filename)
        checkbox.clicked.connect(lambda: self.display_widget(checkbox, widget))
        checkbox.setFont(QFont('MS Shell Dlg 2', 14))

        self.ui.widgets_layout.addWidget(checkbox)

    @staticmethod
    def create_widget(filename, path):
        module_importer = importlib.util.spec_from_file_location(filename, path)
        module = importlib.util.module_from_spec(module_importer)
        module_importer.loader.exec_module(module)

        return NewWidget(module.Ui_Form)

    @staticmethod
    def display_widget(checkbox: QCheckBox, widget: BaseWidget):
        if checkbox.isChecked():
            widget.show()
        else:
            widget.hide()

    @staticmethod
    def get_file_name():
        path = QFileDialog.getOpenFileName()
        filename = path[0].split('/')
        filename = filename[-1].split('.')
        filename = filename[0]
        return filename, path[0]


app = QtWidgets.QApplication([])

application = MainWindow()
application.show()

sys.exit(app.exec())
