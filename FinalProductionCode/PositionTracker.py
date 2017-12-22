from Tkinter import *
import Tkinter as tk

class PositionMarker:


    def __init__(self):

        self.window = tk.Tk()

        w2 = tk.Label(self.window,
                      row = 0,
                      column = 0,
                      justify=tk.LEFT,
                      padx=10,
                      text="Sector 1",
                      font="Helvetica").pack(side="left")


        self.window.mainloop()


if __name__ == '__main__':
    pos = PositionMarker()