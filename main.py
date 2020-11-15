import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QCheckBox

from widget.ui.main_design import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Widget Manager')

        self.ui.add_widget_button.clicked.connect(self.get_widget_ui)

    def get_widget_ui(self):
        filename = self.get_file_name()

        label = QCheckBox(filename)
        label.setFont(QFont('MS Shell Dlg 2', 14))

        self.ui.widgets_layout.addWidget(label)

    @staticmethod
    def get_file_name():
        filename = QFileDialog.getOpenFileName()
        filename = filename[0].split('/')
        filename = filename[-1].split('.')
        filename = filename[0]
        return filename


app = QtWidgets.QApplication([])

application = MainWindow()
application.show()

sys.exit(app.exec())
