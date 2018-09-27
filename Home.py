import sys
from Tkinter import *
import os



class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Attendance Monitoring System")

        self.pack(fill=BOTH, expand=1)

        buttondef = Button(self, text="Generate Defaulter List",command = self.generate_Defaulter,height = 0,width=30)
        buttonIns = Button(self, text="Insert New Records",command = self.insert_Data,height = 0,width=30)
        buttonCap = Button(self, text="Capture Image",command = self.capture_Image,height = 0,width=30)
        buttonTrain = Button(self, text="Train Model",command = self.train_data,height = 0,width=30)
       
        
        
       
        buttonIns.pack(side = TOP)
        buttonCap.pack(side = TOP)
        buttonTrain.pack(side = TOP)
        buttondef.pack(side = TOP)

    def generate_Defaulter(self):
        os.system('Defaulter_List.py')

    def insert_Data(self):
        self.master.destroy()
        os.system('InsertData.py')
        
        
    def capture_Image(self):
        os.system('DataSet_Generator.py')

    def train_data(self):
        os.system('Trainer.py')
    
    

root = Tk()

app = Window(root)
root.geometry("400x300")

root.mainloop()
