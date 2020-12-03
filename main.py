import os
import shutil
import time
import sys
import importlib.util

from PyQt5.QtCore import Qt

from widget import settings

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFileDialog, QPushButton, QSystemTrayIcon, QDialog, QMenu

from widget.compile_ui import UiCompiler
from widget.db_worker import DBWorker
from widget.ui.main_design import Ui_MainWindow
from widget.ui.error_message_design import Ui_Dialog
from widget.base_widget import BaseWidget


class NewWidget(BaseWidget):
    """
    This class is for creating new widget from compiled py-file
    command:
        $ pyuic5 design.ui -o design.py
    """

    def __init__(self, design_ui, name: str) -> None:
        super().__init__(name)

        self.ui = design_ui()
        self.ui.setupUi(self)
        self.ui.label.mouseMoveEvent = self.move_window


class WidgetAdder:
    """
    This class add button for displaying widget to main window
    and adding functions for their processing
    """

    def __init__(self, main_window_obj: QtWidgets.QMainWindow) -> None:
        self.main_window_obj = main_window_obj
        self.db_worker = DBWorker()
        self.widgets = []

    def visualise_widgets(self) -> None:
        """
        This function visualize widgets and add button to the scrollbar
        :return: None
        """
        rows = self.get_db_rows()
        for row in rows:
            if row['visible'] and not row['del']:  # if visible == True and del == False
                widget = self.add_widget(filename=row['filename'], path=row['path'], x=row['x'], y=row['y'])
                self.main_window_obj.display_widget(widget=widget)
            elif not row['del']:
                self.add_widget(filename=row['filename'], path=row['path'], x=row['x'], y=row['y'])

    def add_widget(self, filename=None, path=None, x=None, y=None):
        """
        This function adding pushButton to ScrollBar and
        create function for activating this button
        :return: widget class with design UI_Form
        """
        filename, path = self.__prepare_widget_data(filename, path)

        if not self.__is_input_data_valid(filename):
            return

        widget = self.create_widget(filename[0], path)
        if widget is not None:
            if x is not None and y is not None:
                widget.move(x, y)
            self.widgets.append(widget)
            self.add_widget_to_db(filename[0], path)

            button = self.__create_widget_button(filename, widget)
            self.main_window_obj.ui.widgets_layout.addWidget(button)

            return widget

    def get_db_rows(self) -> list:
        """
        This function get data from database
        :return: tuple of rows in database table
        """
        return self.db_worker.get_rows()

    def add_widget_to_db(self, filename: str, path: str) -> None:
        """
        This function add data to the database
        :param filename: name of py-file
        :param path: path to this file
        :return: None
        """
        self.db_worker.add_row(filename, path)

    def create_widget(self, filename: str, path: str) -> NewWidget:
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

        if hasattr(module, 'main'):
            return module.main()
        elif hasattr(module, 'Ui_Form'):
            return NewWidget(module.Ui_Form, filename)
        else:
            self.main_window_obj.show_error_dialog('Must be Ui_Form in py-file')

    def __create_widget_button(self, filename: list, widget: BaseWidget) -> QPushButton:
        """
        This function create button for widget displaying
        :param filename: py-file name
        :param widget: widget object
        :return: button
        """
        button = QPushButton(filename[0])
        button.clicked.connect(lambda: self.main_window_obj.double_click_event(widget, button))
        button.setFont(QFont('MS Shell Dlg 2', 14))
        return button

    def __is_input_data_valid(self, filename: list) -> bool:
        """
        This function return True or False
        check if data is valid
        :param filename: name of py-file
        :return: True or False
        """
        for widget in self.widgets:
            print(widget.name, filename[0])
            if widget.name == filename[0]:
                self.main_window_obj.show_error_dialog('Widget already exist')
                return False
            if filename is None:
                self.main_window_obj.show_error_dialog('Cant add that widget')
                return False
        return True

    def __prepare_widget_data(self, filename=None, path=None) -> tuple:
        """
        This function prepare data for adding widget and
        check existing of widget
        :param filename: name of file
        :param path: path to the file
        :return: filename and path ro this file
        """
        if filename is None or path is None:
            filename, path = self.__get_file()
            path = self.__copy_file(filename, path)
            if filename[1] == 'ui':
                ui_compiler = UiCompiler(filename=filename[0], path=path)
                path = ui_compiler.out_file_path

        else:
            filename = [filename]
        return filename, path

    @staticmethod
    def __copy_file(filename, path) -> str:
        """
        This function copy file select by user to directory: 'ui/user_ui/'
        :param filename: py-file name
        :param path: path to this file
        :return:
        """
        new_path = f'{settings.MAIN_DIRECTORY}\\ui\\user_ui\\{filename[0]}.{filename[1]}'
        shutil.copyfile(path, new_path)
        return new_path

    @staticmethod
    def __get_file() -> tuple:
        """
        This function return data of the file
        :return: filename and path to file
        """
        path = QFileDialog.getOpenFileName()
        filename = path[0].split('/')
        filename = filename[-1].split('.')
        return filename, path[0]


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.click_time = time.time()
        self.widget_adder = WidgetAdder(main_window_obj=self)
        self.db_worker = DBWorker()
        self.selected_widget = ()
        self.tray_menu_actions = [
            ['close', self.close]
        ]

        self.__normalize_window()
        self.__set_tray_icon()

        self.widget_adder.visualise_widgets()

        self.ui.add_widget_button.clicked.connect(self.widget_adder.add_widget)
        self.ui.del_widget_button.clicked.connect(lambda: self.delete_button())

    def __set_tray_icon(self) -> None:
        """
        This function add tray icon and sets icon img
        :return: None
        """
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(self.main_icon)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.tray_icon_click)
        self.tray_context_menu = QMenu()
        self.add_tray_actions()
        self.tray_icon.setContextMenu(self.tray_context_menu)
        self.tray_context_menu.triggered.connect(self.tray_menu_activation)

    def add_tray_actions(self):
        for action_data in self.tray_menu_actions:
            action = self.tray_context_menu.addAction(action_data[0])
            action_data.append(action)

    def tray_menu_activation(self, action):
        for action_data in self.tray_menu_actions:
            if action is action_data[2]:
                action_data[1]()

    def tray_icon_click(self, reason):
        if reason == 2:  # double click
            self.show()

    def __normalize_window(self) -> None:
        """
        This function normalize window
        :return: None
        """
        self.main_icon = QIcon(os.path.normpath(f'{settings.MAIN_DIRECTORY}/ui/res/logo.png'))
        self.error_dialog_ui = Ui_Dialog()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Widget Manager')
        self.setWindowIcon(self.main_icon)

        flags = QtCore.Qt.Tool
        self.setWindowFlags(flags)

    def delete_button(self) -> None:
        """
        This function hide widget and button of this widget
        :return: None
        """
        widget = self.selected_widget[1]
        filename = widget.name
        self.db_worker.delete_row(filename)
        self.selected_widget[0].hide()
        self.selected_widget[1].hide()
        self.widget_adder.widgets.remove(widget)

    def double_click_event(self, widget: QtWidgets, button: QPushButton) -> None:
        """
        This function check: is click double or not
        :param button: selected button
        :param widget: widget, that will be displayed
        :return:
        """
        if (time.time() - self.click_time) < .5:
            self.display_widget(widget=widget, button=button)
            self.toggle_visibility_db(button)
        else:
            self.click_time = time.time()
        self.selected_widget = (button, widget)

    def toggle_visibility_db(self, button: QPushButton) -> None:
        """
        This function toggle visibility of widget in database
        :param button: button that was pressed
        :return: None
        """
        self.db_worker.toggle_visibility(button.text())

    def close(self) -> None:
        """
        This is override function that calls when window is closing
        :return: None
        """
        self.tray_icon.hide()
        sys.exit(app.exec())

    def show_error_dialog(self, message: str) -> None:
        """
        This function shows error dialog message
        :param message: Your message
        :return: None
        """
        dialog = QDialog()
        self.error_dialog_ui.setupUi(dialog)
        self.error_dialog_ui.error_message_label.setText(message)
        dialog.setWindowTitle('Dialog')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    @staticmethod
    def display_widget(widget: BaseWidget, button=None) -> None:
        """
        display the widget on users screen
        :param button: pressed button
        :param widget: widget, that will be displayed
        :return: None
        """
        if not widget.isVisible():
            widget.show()
        elif button is not None:
            widget.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    application = MainWindow()
    application.show()

    sys.exit(app.exec())
