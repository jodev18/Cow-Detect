import serial
import time

class SMSSender:

    def __init__(self):
        #The com port where the arduino belongs here...
        #self.serialconn = serial.Serial('COM5')
        self.serialconn = serial.Serial()
        self.serialconn.baudrate = 115200
        self.serialconn.port = 'COM5' # Change this to the current port where arduino is connected
        self.serialconn.open()


    def sendSMS(self,phonenumber,text):
        time.sleep(3)
        self.serialconn.write(phonenumber + ';' + text)
        self.serialconn.flush()
        self.serialconn.close()
