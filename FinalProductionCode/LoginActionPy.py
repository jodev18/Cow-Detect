
from PyQt5 import QtWidgets,QtCore,QtGui
from FinalProductionCode.cow_ui import UILoginForm
from FinalProductionCode.database.db_manager import MySQLHelper
### THIS WILL CONTAIN THE CODE FOR HANDLING LOGIN ACTION.

class LoginForm(QtWidgets.QWidget, UILoginForm.Ui_Form):

    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)

    def init_buttons(self):
        self.btnLogin.clicked.connect(self.login)
        self.btnLoginExit.clicked.connect(self.exit_login)

    def login(self):

        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()

        if len(self.username) > 0:

            if len(self.password) > 0:
                #.showdialog("Ok","OK")

                sqlhelper = MySQLHelper()
                sqlhelper.login(self.username,self.password)

            else:
                self.showdialog("Password","Please enter your password.")

        else:
            self.showdialog("Username","Please enter your username.")


        print("Entered username: " + self.username)
        print("Entered password: " + self.password)

        #print "Login"

    def showdialog(self,title,message):
        msg = QtWidgets.QMessageBox()
        msg.about(self, title, message)

        #retval = msg.exec_()
        #print "value of pressed message box button:", retval

    def exit_login(self):
        exit(0)
        print "Exit"