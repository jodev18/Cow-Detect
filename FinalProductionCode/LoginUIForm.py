# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 171)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnLogin = QtWidgets.QPushButton(Form)
        self.btnLogin.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLoginExit = QtWidgets.QPushButton(Form)
        self.btnLoginExit.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.btnLoginExit.setObjectName("btnLoginExit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 191, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.btnLogin.setText(_translate("Form", "Login"))
        self.btnLoginExit.setText(_translate("Form", "Exit"))
        self.label_3.setText(_translate("Form", "ESTRUS DETECTION AND MONITORING"))

