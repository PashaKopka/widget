from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtWidgets

import os
import pyvda
import win32gui
from PyQt5.QtWidgets import QMenu

import settings


class BaseWidget(QtWidgets.QMainWindow):

    def __init__(self):
        super(BaseWidget, self).__init__()
        self.draggable = True

        self._normalize_window()
        self._stay_at_all_virtual_descktops()

    def move_window(self, e):
        """
        Function for moving window
        :param e: -
        :return: None
        """
        if not self.isMaximized() and e.buttons() == Qt.LeftButton and self.draggable:
            self.move(self.pos() + e.globalPos() - self.click_position)
            self.click_position = e.globalPos()
            e.accept()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        Function for handling mouse click event
        :param a0:
        :return: None
        """
        self.click_position = a0.globalPos()

    def set_timer(self, method, timeout):
        """
        Function make QTimer for other method

        :param method: method you want to call
        :param timeout: timeout in ms
        :return: None
        """
        timer = QTimer(self)
        timer.timeout.connect(method)
        timer.start(timeout)

    def _normalize_window(self):
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

    @staticmethod
    def _stay_at_all_virtual_descktops():
        """
        Function make window visible at all virtual desktops
        (tested only on windows 10)
        :return:
        """
        current_desktop = pyvda.GetCurrentDesktopNumber()
        current_window_handle = win32gui.GetForegroundWindow()
        pyvda.MoveWindowToDesktopNumber(current_window_handle, current_desktop)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        """
        Function toggle draggable of window
        :param event: choice button of context menu
        :return:
        """
        menu = QMenu(self)
        if self.draggable:
            pin_action = menu.addAction("pin")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == pin_action:
                self.draggable = False
        else:
            pin_action = menu.addAction("unpin")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == pin_action:
                self.draggable = True
