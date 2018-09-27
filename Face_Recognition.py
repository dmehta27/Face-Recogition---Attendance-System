import numpy as np
import cv2
import sqlite3
import smtplib
import datetime
import tkMessageBox
import Tkinter

def getRecognizedName(final_id):
    conn = sqlite3.connect("Attendance.db")
    cmd = "SELECT name,email FROM Student_info WHERE id ="+str(final_id)
    cursor = conn.execute(cmd)
    rec_name = None

    for row in cursor:
        rec_name = row
        print rec_name[0] 
    conn.close()
    return rec_name


def sendMail(recv_email,recv_name ):
    content = "Dear "+str(recv_name)+", your attendance for the day has been marked successfully."

    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()
    mail.starttls()

    mail.login('bhavya.kothari19@gmail.com','beautifulmystery')
    mail.sendmail('bhavya.kothari19@gmail.com',recv_email,content)

    mail.close()
  

def updateAttendance(final_id):
    mydate = datetime.datetime.now()

    cur_day = mydate.strftime("%d")
    cur_month = mydate.strftime("%m")
    curr_month = mydate.strftime("%B")
    curr_year = mydate.strftime("%Y")
    
    cur_date = mydate.strftime ("%d-%m-%Y")
    print cur_date
    
    conn = sqlite3.connect("Attendance.db")
    c=conn.cursor()
    c.execute("UPDATE Attendance_"+str(curr_month)+" SET "+str(curr_month)+"_"+str(cur_day)+" = ? WHERE id = ?",('P',final_id))
    conn.commit()
    print "Attendance marked successfully"



def Recognition():

    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    rec = cv2.createLBPHFaceRecognizer()
    cam = cv2.VideoCapture(0);

    rec.load("Training Data\\trainingData.yml")

    imgcount=0
    id=0
    x=0
    y=0
    global final_name
    final_name = None
    final_email = None
    
    
    IDs = []

        
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,2)

    while(True):
        ret, img = cam.read()
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        gray = cv2.bilateralFilter(gray,9,75,75)
        faces = faceDetect.detectMultiScale(gray,1.3,5);

        for(x,y,w,h) in faces:
            imgcount=imgcount+1
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf = rec.predict(gray[y:y+h,x:x+w])


            IDs.append(id)

            
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y),font,255)
        cv2.imshow('frame',img)    
        cv2.waitKey(1)


        
        if(imgcount>20):
            break

    cam.release()

    final_id = max(set(IDs), key=IDs.count)
    resultSet = getRecognizedName(final_id)

    final_name = str(resultSet[0])
    final_email = str(resultSet[1])
    
    cv2.destroyAllWindows()

    tkMessageBox.showinfo('Successful Recognition','Recognized As : '+str(final_name)+' successfully.')

    updateAttendance(final_id)
    sendMail(final_email,final_name)
    
    tkMessageBox.showinfo('E-Mail Delivery','Mail sent to Email : '+str(final_email)+' successfully.')
    






