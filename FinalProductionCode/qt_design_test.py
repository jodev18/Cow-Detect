from PyQt5 import QtWidgets
import sys
from FinalProductionCode.cow_ui import UIDetectionForm, UILoginForm


class ExampleApp(QtWidgets.QMainWindow, UIDetectionForm.Ui_DetectionWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnExit.clicked.connect(self.exit_py)

    def exit_py(self):
        print "Exit"

class LoginForm(QtWidgets.QWidget, UILoginForm.Ui_Form):

    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    #loginform = LoginForm()
    form.show()

    #formcurrinst = form.get_instance()
    #form.btnExit.setText("hello")

    #loginform.show()
    app.exec_()

if __name__ == '__main__':
    main()

