from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import windetect
import logindetect

class ExampleApp(QtWidgets.QMainWindow, windetect.Ui_DetectionWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnExit.clicked.connect(self.exit_py)

    def exit_py(self):
        print "Exit"

class LoginForm(QtWidgets.QWidget,logindetect.Ui_Form):

    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    loginform = LoginForm()
    form.show()
    loginform.show()
    app.exec_()

if __name__ == '__main__':
    main()

