# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgets_area = QtWidgets.QScrollArea(self.centralwidget)
        self.widgets_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.widgets_area.setWidgetResizable(True)
        self.widgets_area.setObjectName("widgets_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgets_layout = QtWidgets.QVBoxLayout()
        self.widgets_layout.setObjectName("widgets_layout")
        self.clock_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.clock_checkbox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clock_checkbox.setFont(font)
        self.clock_checkbox.setObjectName("clock_checkbox")
        self.widgets_layout.addWidget(self.clock_checkbox)
        self.verticalLayout.addLayout(self.widgets_layout)
        self.widgets_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.widgets_area)
        self.add_widget_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_widget_button.setMinimumSize(QtCore.QSize(0, 40))
        self.add_widget_button.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.add_widget_button.setObjectName("add_widget_button")
        self.verticalLayout_2.addWidget(self.add_widget_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clock_checkbox.setText(_translate("MainWindow", "clock widget"))
        self.add_widget_button.setText(_translate("MainWindow", "Add widget"))
