from PyQt5 import QtWidgets,QtCore,QtGui
from FinalProductionCode.cow_ui import UILoginForm
from FinalProductionCode.cow_ui import  UICowStreamForm

from CowOverlapDetection import Cam
from requests.exceptions import ConnectionError
from requests.exceptions import InvalidURL

class StreamForm(QtWidgets.QWidget, UICowStreamForm.Ui_Form):

    def __init__(self, parent=None):
        super(StreamForm, self).__init__(parent)
        self.setupUi(self)


    def init_buttons(self):

        self.pushButton.clicked.connect(self.init_stream)


    def init_stream(self):

        s_link = self.lineEdit.text()
        s_window = self.lineEdit_2.text()

        if len(s_link) > 0:

            if "rstp://" not in s_link:
                if "http://" not in s_link:
                    print "Stream error"
                    self.showdialog("Link Error","Stream link error.")
                else:
                    print "Window title ok"
                    self.start_scan(s_link, s_window)
            else:
                if len(s_window) > 0:
                    print "Window title ok"
                    self.start_scan(s_link,s_window)

                else:
                    self.showdialog("No Window Title","Please enter a window title.")
                    print "Valid stream link"

        else:
            self.showdialog("No Stream Link","Please enter a stream link.")


    def showdialog(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.about(self, title, message)

    def start_scan(self,s_link,s_window):
        try:

            #self.listView.addItem("Abcd")

            self.camscan = Cam(s_link, s_window)
            self.camscan.start_scan(s_link, s_window)
        except ConnectionError as connE:
            print "Connection error: "
            print connE
        except InvalidURL as iurl:
            print "Invalid URL"
            print iurl