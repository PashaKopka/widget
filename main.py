import time
import sys
import importlib.util

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QPushButton

from widget.compile_ui import UiCompiler
from widget.db_worker import DBWorker
from widget.ui.main_design import Ui_MainWindow
from widget.clockwidget import ClockWidget
from widget.widged import BaseWidget


class NewWidget(BaseWidget):
    """
    This class is for creating new widget from compiled py-file
    command:
        $ pyuic5 design.ui -o design.py
    """

    def __init__(self, design_ui):
        super().__init__()

        self.ui = design_ui()
        self.ui.setupUi(self)
        self.ui.label.mouseMoveEvent = self.move_window


class WidgetAdder:
    """
    This class add button for displaying widget to main window
    and adding functions for their processing
    """

    def __init__(self, main_window_obj):
        self.main_window_obj = main_window_obj
        self.db_worker = DBWorker()
        self.widgets_names = []

    def add_widget(self, filename=None, path=None):
        """
        This function adding pushButton to ScrollBar and
        create function for activating this button
        :return: None
        """
        filename, path = self.__prepare_widget_data(filename, path)

        if filename is None or filename[0] in self.widgets_names:
            return

        widget = self.create_widget(filename[0], path)
        self.widgets_names.append(filename[0])

        button = QPushButton(filename[0])
        button.clicked.connect(lambda: self.main_window_obj.double_click_event(widget, button))
        button.setFont(QFont('MS Shell Dlg 2', 14))

        self.main_window_obj.ui.widgets_layout.addWidget(button)

    def __prepare_widget_data(self, filename=None, path=None):
        """
        This function prepare data for adding widget and
        check existing of widget
        :param filename: name of file
        :param path: path to the file
        :return: filename and path ro this file
        """
        if filename is None or path is None:
            filename, path = self.get_file_name()
            if filename[1] == 'ui':
                ui_compiler = UiCompiler(filename=filename[0], path=path)
                path = ui_compiler.out_file_path
            self.add_widget_to_db(filename[0], path)

        else:
            filename = [filename]
        return filename, path

    def add_widgets_from_db(self):
        """
        This function call add_widget function and give data from database
        :return: None
        """
        rows = self.get_db_rows()
        for row in rows:
            if not row[3]:
                self.add_widget(row[1], row[2])

    def get_db_rows(self) -> tuple:
        """
        This function get data from database
        :return: tuple of rows in database table
        """
        return self.db_worker.get_rows()

    def add_widget_to_db(self, filename, path):
        """
        This function add data to the database
        :param filename: name of py-file
        :param path: path to this file
        :return: None
        """
        self.db_worker.add_row(filename, path)

    @staticmethod
    def get_file_name():
        """
        This function return data of the file
        :return: filename and path to file
        """
        path = QFileDialog.getOpenFileName()
        filename = path[0].split('/')
        filename = filename[-1].split('.')
        return filename, path[0]

    @staticmethod
    def create_widget(filename, path):
        """
        This function import widget py-file, generated by command:
            $ pyuic5 design.ui -o design.py
        and create specimen of this widget class
        :param filename: name of file for naming module
        :param path: path to file
        :return: widget class with design UI_Form
        """
        module_importer = importlib.util.spec_from_file_location(filename, path)
        module = importlib.util.module_from_spec(module_importer)
        module_importer.loader.exec_module(module)

        if not hasattr(module, 'Ui_Form'):
            raise Exception('File have not class Ui_Form')
        else:
            return NewWidget(module.Ui_Form)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.click_time = time.time()
        self.widget_adder = WidgetAdder(main_window_obj=self)
        self.db_worker = DBWorker()
        self.selected_widget = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Widget Manager')

        self.widget_adder.add_widgets_from_db()

        self.ui.add_widget_button.clicked.connect(self.widget_adder.add_widget)
        self.ui.del_widget_button.clicked.connect(lambda: self.delete_button(self.selected_widget))

        self.clock_widget = ClockWidget()
        self.ui.clock_widget_button.clicked.connect(
            lambda: self.double_click_event(self.clock_widget, self.ui.clock_widget_button))

    def delete_button(self, button: QPushButton):
        filename = button.text()
        self.db_worker.delete_row(filename)
        self.selected_widget.hide()
        self.widget_adder.widgets_names.remove(filename)

    def double_click_event(self, widget: QtWidgets, button: QPushButton):
        """
        This function check: is click double or not
        :param button: selected button
        :param widget: widget, that will be displayed
        :return:
        """
        if (time.time() - self.click_time) < .5:
            self.display_widget(widget)
        else:
            self.click_time = time.time()
        self.selected_widget = button

    @staticmethod
    def display_widget(widget: BaseWidget):
        """
        display the widget on users screen
        :param widget: widget, that will be displayed
        :return: None
        """
        if not widget.isVisible():
            widget.show()
        else:
            widget.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    application = MainWindow()
    application.show()

    sys.exit(app.exec())
