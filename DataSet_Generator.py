import numpy as np
import cv2
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.createLBPHFaceRecognizer()
cam = cv2.VideoCapture(0);

id = raw_input("Enter the id of the user: ")

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




