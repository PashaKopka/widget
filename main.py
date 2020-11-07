import os
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTime, QTimer
from ui.mydesign import Ui_Form
from PyQt5 import QtWidgets, uic
import sys

MAIN_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._make_background_transparent()

        self.ui.label.setText(self._get_time())

        self._set_timer(method=self._change_label_time, timeout=1000)

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

    def _make_background_transparent(self):
        """
        Function make background of program transparent
        :return: None
        """
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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
