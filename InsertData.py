import sqlite3
import sys
from Tkinter import *
import tkMessageBox
import os
import numpy as np
import cv2


fields = 'First Name','Last Name','Gender','Age','Designation','Email'

def fetch(entries):


      ids = -1
    
      fname  = entries[0][1].get()
      lname  = entries[1][1].get()
      gen  = entries[2][1].get()
      age  = entries[3][1].get()
      desg  = entries[4][1].get()
      email  = entries[5][1].get()

      if fname == '' or lname == '' or gen == '' or age == '' or desg == '' or email == '' : 
             tkMessageBox.showwarning('Insert Record','Please fill all the Personal - Details.')
      else:
        
        conn = sqlite3.connect("Attendance.db")
        cursor = conn.execute("SELECT max(id) FROM Student_info")

        for row in cursor:
          temp_id = row[0]

        conn.commit()
        conn.close()  

        ids = int(temp_id)+1

        conn = sqlite3.connect("Attendance.db")
        conn.execute("INSERT INTO Student_info (id,name,email,Designation,Gender,Age,last_Name) VALUES(?,?,?,?,?,?,?)",(ids,fname,email,gen,desg,age,lname))
        conn.commit()
        conn.close()    

        conn = sqlite3.connect("Attendance.db")
        conn.execute("INSERT INTO Attendance_April (id,name,lname) VALUES(?,?,?)",(ids,fname,lname))
        conn.commit()
        conn.close()

        captureStart()
        tkMessageBox.showinfo('Insert Record','Record Insert Successfully')
        entries[0][1].delete(0,'end')
        entries[1][1].delete(0,'end')
        entries[2][1].delete(0,'end')
        entries[3][1].delete(0,'end')
        entries[4][1].delete(0,'end')
        entries[5][1].delete(0,'end')
        

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

def navigate():
      root.destroy()
      os.system('Home.py')


def captureStart():

     conn = sqlite3.connect("Attendance.db")
     cursor = conn.execute("SELECT max(id) FROM Student_info")

     for row in cursor:
          temp_id = row[0]

     
     conn.commit()
     conn.close()
          
     faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
     recognizer = cv2.createLBPHFaceRecognizer()
     cam = cv2.VideoCapture(0);

     id = int(temp_id)
     x=0
     y=0

     imgcount=0
     while(True):
         ret, img = cam.read()
         
         gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         gray = cv2.equalizeHist(gray)
         gray = cv2.bilateralFilter(gray,9,75,75)

         resized_image = cv2.resize(gray, (100, 50)) 
         
         faces = faceDetect.detectMultiScale(gray,1.3,5);
         
         

         for(x,y,w,h) in faces:
             imgcount=imgcount+1
             cv2.imwrite("DataSet/User."+str(id)+"."+str(imgcount)+".jpg",gray[y:y+h,x:x+w])
             cv2.waitKey(100)
             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

         cv2.imshow('frame',img)    
         cv2.waitKey(1)
         
         if(imgcount>20):
             break

     cam.release()
     cv2.destroyAllWindows()



if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
      
   b0 = Button(root, text='Back',
          command=navigate)   

   b1 = Button(root, text='Capture and Register',
          command=(lambda e=ents: fetch(e)))
   b0.pack(side=LEFT)
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   
   root.mainloop()
