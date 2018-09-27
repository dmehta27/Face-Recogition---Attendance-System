import sys
from Tkinter import *
import os
from PIL import *
import Tkinter
from Face_Recognition import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        global message
        message = Tkinter.StringVar()
    
        message.set('Click to Recognize yourself:-')
        self.master = master
        w = Label(master, textvariable=message,  font='size, 20')
        w1 = Label(master)
        w.pack(side = TOP)
        w1.pack(side = TOP)

        self.init_window()
       
    def init_window(self):

        self.master.title("Attendance Monitoring System")

        self.pack(fill=BOTH, expand=1)
       
        buttonRecog = Button(self, text="Recognize Me",command = self.recognize_me,height = 0,width=30)
      
        buttonRecog.pack(side = TOP)

    def recognize_me(self):
        Recognition()

    def printName(final_name):    
        print("HEy")

root = Tk()

app = Window(root)
root.geometry("400x300")

root.mainloop()
