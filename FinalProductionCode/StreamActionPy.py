from PyQt5 import QtWidgets,QtCore,QtGui
from FinalProductionCode.cow_ui import UILoginForm
from FinalProductionCode.cow_ui import  UICowStreamForm

class StreamForm(QtWidgets.QWidget, UICowStreamForm.Ui_Form):

    def __init__(self, parent=None):
        super(StreamForm, self).__init__(parent)
        self.setupUi(self)