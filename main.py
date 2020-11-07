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
        timer = QTimer(self)
        timer.timeout.connect(method)
        timer.start(timeout)

    def _change_label_time(self):
        self.ui.label.setText(self._get_time())

    def _get_time(self):
        current_time = QTime.currentTime()
        return current_time.toString('hh:mm:ss')

    def _make_background_transparent(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


app = QtWidgets.QApplication([])
win = uic.loadUi(os.path.join(MAIN_DIRECTORY, 'ui/main.ui'))

application = MyWindow()
application.show()

sys.exit(app.exec())
