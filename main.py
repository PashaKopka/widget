import os
import time

import pyvda
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTime, QTimer, Qt
from ui.mydesign import Ui_Form
from PyQt5 import QtWidgets, uic
import sys
import win32gui

MAIN_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.mouseMoveEvent = self._move_window
        self._normalize_window()
        self.ui.label.setText(self._get_time())
        self._set_timer(method=self._change_label_time, timeout=1000)

        self._stay_at_all_virtual_descktops()

    def _move_window(self, e):
        """
        Function for moving window
        :param e: -
        :return: None
        """
        if not self.isMaximized() and e.buttons() == Qt.LeftButton:
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

    def _set_timer(self, method, timeout):
        """
        Function make QTimer for other method

        :param method: method you want to call
        :param timeout: timeout in ms
        :return: None
        """
        timer = QTimer(self)
        timer.timeout.connect(method)
        timer.start(timeout)

    def _change_label_time(self):
        """
        Function change label with time
        :return: None
        """
        self.ui.label.setText(self._get_time())

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

    @staticmethod
    def _get_time():
        """
        :return: current time
        """
        current_time = QTime.currentTime()
        return current_time.toString('hh:mm:ss')


app = QtWidgets.QApplication([])
win = uic.loadUi(os.path.join(MAIN_DIRECTORY, 'ui/main.ui'))

application = MyWindow()
application.show()

sys.exit(app.exec())
