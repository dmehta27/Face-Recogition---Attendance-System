import Tkinter
import ttk
import sqlite3
import sys
from Tkinter import *
import tkMessageBox
import os

fields = 'ID','First Name','Last Name','Gender','Age','Designation','Email'

def fetch(entries):

     tkMessageBox.showinfo('Insert Data','Record inserted successfully')
     print('%s'% (text))

def getRecognizedName(final_id):
    conn = sqlite3.connect("Attendance.db")
    cmd = "INSERT INTO Personal_Information Values()"
    cursor = conn.execute(cmd)
    rec_name = None

    for row in cursor:
        rec_name = row
    conn.close()
    return rec_name      

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
      
   return entries



def demo():
    #root = tk.Tk()
    schedGraphics = Tkinter
    root = schedGraphics.Tk()

    root.title("Admin Panel")
    universal_height = 503

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 600,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 600,height = universal_height)
    page3 = ttk.Frame(nb,width = 600,height = universal_height)


    nb.add(page1, text='Insert Data')
    nb.add(page2, text='Manage Academic Calendar')
    nb.add(page3, text='Manage and Control')
    
    nb.grid(column=0)

    ename = StringVar()

    day_label = schedGraphics.Label(page1, text="Name")
    e = Entry(root,textvariable = ename)
    day_label.pack()
    e.pack()
    day_label.place(x=0, y=30)
    e.place(x=50, y=50)
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
      
    b0 = Button(root, text='Back',
          command=(lambda e=ents: fetch(e)))   

    b1 = Button(root, text='Insert',
          command=(lambda e=ents: fetch(e)))

    b0.pack(side=LEFT)
    b1.pack(side=LEFT, padx=5, pady=5)
   
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)

    day_label = schedGraphics.Label(page2, text="Day2:")
    day_label.pack()
    day_label.place(x=0, y=30)

    canvas = schedGraphics.Canvas(root, width=0, height=universal_height)
    canvas.create_rectangle(50, 500, 300, 600, fill="red")
    canvas.grid(column=1, row=0)

    root.mainloop()

if __name__ == "__main__":
   demo()


