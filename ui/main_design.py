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
        MainWindow.resize(542, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgets_area = QtWidgets.QScrollArea(self.centralwidget)
        self.widgets_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.widgets_area.setWidgetResizable(True)
        self.widgets_area.setObjectName("widgets_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 497, 346))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgets_layout = QtWidgets.QVBoxLayout()
        self.widgets_layout.setObjectName("widgets_layout")
        self.clock_widget_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.clock_widget_button.setFont(font)
        self.clock_widget_button.setMouseTracking(False)
        self.clock_widget_button.setTabletTracking(False)
        self.clock_widget_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.clock_widget_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.clock_widget_button.setAcceptDrops(False)
        self.clock_widget_button.setToolTip("")
        self.clock_widget_button.setStatusTip("")
        self.clock_widget_button.setWhatsThis("")
        self.clock_widget_button.setAccessibleName("")
        self.clock_widget_button.setAccessibleDescription("")
        self.clock_widget_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clock_widget_button.setAutoFillBackground(True)
        self.clock_widget_button.setCheckable(True)
        self.clock_widget_button.setAutoRepeat(False)
        self.clock_widget_button.setAutoExclusive(False)
        self.clock_widget_button.setAutoDefault(True)
        self.clock_widget_button.setDefault(True)
        self.clock_widget_button.setFlat(False)
        self.clock_widget_button.setObjectName("clock_widget_button")
        self.widgets_layout.addWidget(self.clock_widget_button)
        self.verticalLayout.addLayout(self.widgets_layout)
        self.widgets_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.widgets_area)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_widget_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_widget_button.setFont(font)
        self.add_widget_button.setObjectName("add_widget_button")
        self.horizontalLayout.addWidget(self.add_widget_button)
        self.del_widget_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_widget_button.setFont(font)
        self.del_widget_button.setObjectName("del_widget_button")
        self.horizontalLayout.addWidget(self.del_widget_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clock_widget_button.setText(_translate("MainWindow", "clock widget"))
        self.add_widget_button.setText(_translate("MainWindow", "Add widget"))
        self.del_widget_button.setText(_translate("MainWindow", "Delete widget"))
