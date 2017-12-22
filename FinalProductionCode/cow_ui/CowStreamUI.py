# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cowstreaminterface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 292)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 161, 381, 131))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 140, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 171, 20))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(224, 120, 101, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cow Stream Initializer"))
        self.label.setText(_translate("Form", "Streams Created"))
        self.label_2.setText(_translate("Form", "Stream Link:"))
        self.label_3.setText(_translate("Form", "Stream Title:"))
        self.lineEdit.setPlaceholderText(_translate("Form", "rstp://,http://"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Stream window title..."))
        self.pushButton.setText(_translate("Form", "Initialize Stream"))

