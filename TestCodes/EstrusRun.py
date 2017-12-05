from ComputerVision import SeeCows

scows = SeeCows()
#sender = SMSSender()
#sender.sendSMS('In heat cow detected!')
#ser = serial.Serial()
#ser.baudrate = 115200
#ser.port = 'COM5'
#ser.open()
#sleep for 2 seconds, according to stackoverflow lol
#time.sleep(2)
#ser.write(b'helloasdsadsadsa\n')
#ser.readline()

#print ('Writing')
#ser.write(b'In-heat Cow is detected\n')
#ser.flush()

#time.sleep(2)
#while ser.read() is not None:
 #   print(ser.readline())
#ser.close()
#sender.sendSMS(b'Cow heat detected')
scows.init_scan()
