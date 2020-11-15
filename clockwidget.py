import sys

from PyQt5.QtCore import QTime

from widget.ui.clock_design import Ui_Form
from PyQt5 import QtWidgets

from widget.widged import BaseWidget


class ClockWidget(BaseWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.mouseMoveEvent = self.move_window
        self.ui.label.setText(self._get_time())
        self.set_timer(method=self._change_label_time, timeout=1000)

    def _change_label_time(self):
        """
        Function change label with time
        :return: None
        """
        self.ui.label.setText(self._get_time())

    @staticmethod
    def _get_time():
        """
        :return: current time
        """
        current_time = QTime.currentTime()
        return current_time.toString('hh:mm:ss')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    application = ClockWidget()
    application.show()

    sys.exit(app.exec())
