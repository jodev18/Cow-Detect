from Tkinter import *

window = Tk()

title = Label(window,text="Estrus Detection")
title.grid(row=0,column=0,columnspan=2)

#labels
stream_l = Label(window,text="Stream Link: ")
stream_l.grid(row=1,column=0)

window_l = Label(window,text="Window Name: ")
window_l.grid(row=2,column=0)

#Text Field
stream_f = Entry(window)
stream_f.grid(row=1,column=1)

window_f = Entry(window)
window_f.grid(row=2,column=1)

#Button initialization
bOk = Button(window,text="Start Monitoring")
bOk.grid(row=3,column=0,columnspan=2)

window.mainloop()