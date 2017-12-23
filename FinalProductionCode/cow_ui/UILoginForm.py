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
        Form.resize(269, 136)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnLogin = QtWidgets.QPushButton(Form)
        self.btnLogin.setGeometry(QtCore.QRect(60, 100, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLoginExit = QtWidgets.QPushButton(Form)
        self.btnLoginExit.setGeometry(QtCore.QRect(140, 100, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnLoginExit.setFont(font)
        self.btnLoginExit.setObjectName("btnLoginExit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 211, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter username..."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter password..."))
        self.btnLogin.setText(_translate("Form", "Login"))
        self.btnLoginExit.setText(_translate("Form", "Exit"))
        self.label_3.setText(_translate("Form", "ESTRUS DETECTION AND MONITORING"))

