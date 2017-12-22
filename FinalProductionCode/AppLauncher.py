from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from LoginActionPy import LoginForm


def main_func():

    app = QtWidgets.QApplication(sys.argv)

    #LOGIN FORM INITIALIZATION
    login_form = LoginForm()
    login_form.init_buttons()
    login_form.show()

    app.exec_()

if __name__ == '__main__':
    main_func()


