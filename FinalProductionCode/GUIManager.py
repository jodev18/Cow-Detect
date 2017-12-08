from Tkinter import *
from CowOverlapDetection import Cam
from requests.exceptions import ConnectionError
from requests.exceptions import InvalidURL

class MainForm:

    def __init__(self):
        self.notify_incomplete_field = None
        self.window = Tk()
        self.window.wm_title("Estrus monitoring and detection")

        self.title = Label(self.window, text="Estrus Detection")
        self.title.grid(row=0, column=0, columnspan=2)

        # labels
        self.stream_l = Label(self.window, text="Stream Link: ")
        self.stream_l.grid(row=1, column=0)

        self.window_l = Label(self.window, text="Window Name: ")
        self.window_l.grid(row=2, column=0)

        # Text Field
        self.stream_f = Entry(self.window)
        self.stream_f.grid(row=1, column=1)
        self.stream_f.insert(0,"http://")

        self.window_f = Entry(self.window)
        self.window_f.grid(row=2, column=1)

        # Button initialization
        self.bOk = Button(self.window, text="Start Monitoring",command=self.begin_check)
        self.bOk.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()

    def begin_check(self):
        wintitle= self.window_f.get()
        streamlink= self.stream_f.get()

        if len(wintitle) > 0 and len(streamlink) > 0:
            print "Fields complete"

            if self.notify_incomplete_field is not None:
                self.notify_incomplete_field.grid_forget()

            try:
                camscan = Cam(streamlink, wintitle)
                camscan.start_scan(streamlink, wintitle)
            except ConnectionError as connE:
                self.notify_incomplete_field = Label(self.window,
                                                     text="Unable to stream from the link provided.")
                self.notify_incomplete_field.grid(row=4, column=0, columnspan=2)
                print "Connection Error: "
                print connE
            except InvalidURL as iurl:
                print "Invalid URL"
                print iurl
                self.notify_incomplete_field = Label(self.window,
                                                     text="Invalid URL. Please enter a valid URL.")
                self.notify_incomplete_field.grid(row=4, column=0, columnspan=2)
        else:
            print "Fields aren't complete"

            self.notify_incomplete_field = Label(self.window,
                                                 text="Fields are incomplete! Please enter appropriate "
                                                      "input for the fields set.")
            self.notify_incomplete_field.grid(row=4, column=0, columnspan=2)

if __name__ == '__main__':
    mainf = MainForm()
