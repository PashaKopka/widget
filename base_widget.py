from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenu

import PyQt5
import pyvda
import win32gui

from widget.db_worker import DBWorker


class BaseWidget(QtWidgets.QMainWindow):

    def __init__(self, name: str):
        super(BaseWidget, self).__init__()
        self.name = name
        self.draggable = True
        self.click_position = None

        self.menu = QMenu(self)
        self.menu.setStyleSheet('QMenu{color : white;}')
        self.actions = {
            'move center': self.move_window_center,
            'pin': self.toggle_pinned_value
        }
        self._create_context_menu()

        self._normalize_window()
        self._stay_at_all_virtual_desktops()
        self.db_worker = DBWorker()

    def move_window(self, e) -> None:
        """
        This is override function that add coordinates of widget in database and move widget

        :param e: -
        :return: None
        """
        if not self.isMaximized() and e.buttons() == Qt.LeftButton and self.draggable:
            self.move(self.pos() + e.globalPos() - self.click_position)
            self.click_position = e.globalPos()
            e.accept()
            x = self.x()
            y = self.y()
            self.db_worker.add_coordinate(self.name, x, y)

    def toggle_pinned_value(self) -> None:
        """
        This function toggle pinned value of widget and call function
        that toggle pinned value in database

        :return: None
        """
        if self.draggable:
            self.draggable = False
        else:
            self.draggable = True
        self._toggle_db_pinned_value()

    def move_window_center(self) -> None:
        """
        This function move widget on the center of active screen

        :return: None
        """
        frame_gm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(
            PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        center_point = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())

        self.db_worker.add_coordinate(self.name, self.x(), self.y())

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        Function for handling mouse click event

        :param a0:
        :return: None
        """
        self.click_position = a0.globalPos()

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        """
        Function toggle draggable of window

        :param event: choice button of context menu
        :return:
        """
        action = self.menu.exec_(self.mapToGlobal(event.pos()))
        if action:
            self.actions[action.text()]()

    def set_timer(self, method, timeout) -> None:
        """
        Function make QTimer for other method

        :param method: method you want to call
        :param timeout: timeout in ms
        :return: None
        """
        timer = QTimer(self)
        timer.timeout.connect(method)
        timer.start(timeout)

    def _normalize_window(self) -> None:
        """
        Function make background of program transparent
        and set window always on bottom

        :return: None
        """
        flags = QtCore.Qt.FramelessWindowHint
        flags |= QtCore.Qt.Tool
        flags |= QtCore.Qt.WindowStaysOnBottomHint
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def _toggle_db_pinned_value(self) -> None:
        """
        This function toggle pinned value in database

        :return: None
        """
        self.db_worker.toggle_pinned_value(self.name)

    def _create_context_menu(self) -> None:
        """
        This function create actions for context menu

        :return:
        """
        for action in self.actions:
            self.menu.addAction(action)

    @staticmethod
    def _stay_at_all_virtual_desktops() -> None:
        """
        Function make window visible at all virtual desktops
        (tested only on windows 10)

        :return:
        """
        current_desktop = pyvda.GetCurrentDesktopNumber()
        current_window_handle = win32gui.GetForegroundWindow()
        pyvda.MoveWindowToDesktopNumber(current_window_handle, current_desktop)
