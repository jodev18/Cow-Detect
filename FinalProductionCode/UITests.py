# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 119)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineUsername = QtWidgets.QLineEdit(Dialog)
        self.lineUsername.setMaxLength(40)
        self.lineUsername.setObjectName("lineUsername")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineUsername)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.linePassword = QtWidgets.QLineEdit(Dialog)
        self.linePassword.setInputMask("")
        self.linePassword.setMaxLength(30)
        self.linePassword.setObjectName("linePassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.linePassword)
        self.loginBox = QtWidgets.QDialogButtonBox(Dialog)
        self.loginBox.setOrientation(QtCore.Qt.Horizontal)
        self.loginBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.loginBox.setObjectName("loginBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.loginBox)

        self.retranslateUi(Dialog)
        self.loginBox.accepted.connect(Dialog.accept)
        self.loginBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "LOGIN TO ESTRUS LOCATION MAPPER"))
        self.label_2.setText(_translate("Dialog", "Username:"))
        self.lineUsername.setPlaceholderText(_translate("Dialog", "Enter username..."))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.linePassword.setPlaceholderText(_translate("Dialog", "Enter password..."))

if __name__ == '__main__':
    dg = Ui_Dialog()
    #dg.setupUi(QDialog())