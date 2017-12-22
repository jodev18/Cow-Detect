# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DetectionWindow(object):
    def setupUi(self, DetectionWindow):
        DetectionWindow.setObjectName("DetectionWindow")
        DetectionWindow.resize(520, 408)
        self.centralwidget = QtWidgets.QWidget(DetectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 461, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.lblSec6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSec6.setObjectName("lblSec6")
        self.gridLayout.addWidget(self.lblSec6, 5, 2, 1, 1)
        self.lblSec1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSec1.setObjectName("lblSec1")
        self.gridLayout.addWidget(self.lblSec1, 3, 0, 1, 1)
        self.lblSec2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSec2.setObjectName("lblSec2")
        self.gridLayout.addWidget(self.lblSec2, 3, 1, 1, 1)
        self.lblSec3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSec3.setObjectName("lblSec3")
        self.gridLayout.addWidget(self.lblSec3, 3, 2, 1, 1)
        self.lblSec5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSec5.setObjectName("lblSec5")
        self.gridLayout.addWidget(self.lblSec5, 5, 1, 1, 1)
        self.lblSec4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSec4.setObjectName("lblSec4")
        self.gridLayout.addWidget(self.lblSec4, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 2, 1, 1)
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(30, 10, 411, 16))
        self.lblTitle.setObjectName("lblTitle")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(420, 350, 75, 23))
        self.btnExit.setObjectName("btnExit")
        DetectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DetectionWindow)
        self.statusbar.setObjectName("statusbar")
        DetectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DetectionWindow)
        QtCore.QMetaObject.connectSlotsByName(DetectionWindow)

    def retranslateUi(self, DetectionWindow):
        _translate = QtCore.QCoreApplication.translate
        DetectionWindow.setWindowTitle(_translate("DetectionWindow", "Detection Window"))
        self.label_8.setText(_translate("DetectionWindow", "SECTOR 2"))
        self.label_7.setText(_translate("DetectionWindow", "SECTOR 3"))
        self.lblSec6.setText(_translate("DetectionWindow", "COW"))
        self.lblSec1.setText(_translate("DetectionWindow", "COW"))
        self.lblSec2.setText(_translate("DetectionWindow", "COW"))
        self.lblSec3.setText(_translate("DetectionWindow", "COW"))
        self.lblSec5.setText(_translate("DetectionWindow", "COW"))
        self.lblSec4.setText(_translate("DetectionWindow", "COW"))
        self.label_9.setText(_translate("DetectionWindow", "SECTOR 1"))
        self.label_10.setText(_translate("DetectionWindow", "SECTOR 4"))
        self.label_11.setText(_translate("DetectionWindow", "SECTOR 5"))
        self.label_12.setText(_translate("DetectionWindow", "SECTOR 6"))
        self.lblTitle.setText(_translate("DetectionWindow", "ESTRUS LOCATION AND OVERLAP DETECTION"))
        self.btnExit.setText(_translate("DetectionWindow", "Exit"))


    def get_instance(self):
        return self