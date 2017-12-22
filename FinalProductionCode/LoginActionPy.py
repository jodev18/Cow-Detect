
from PyQt5 import QtWidgets
from FinalProductionCode.cow_ui import LoginUIForm


### THIS WILL CONTAIN THE CODE FOR HANDLING LOGIN ACTION.

class LoginForm(QtWidgets.QWidget, LoginUIForm.Ui_Form):

    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)

    def init_buttons(self):
        self.btnLogin.clicked.connect(self.login)
        self.btnLoginExit.clicked.connect(self.exit_login)

    def login(self):

        print "Login"


    def exit_login(self):

        print "Exit"