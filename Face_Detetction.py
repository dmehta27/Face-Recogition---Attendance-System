import numpy as np
import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0);

id = raw_input("Enter the name of the user")
imgcount=0

while(True):
    ret, img = cam.read()
    
    
    faces = faceDetect.detectMultiScale(img,1.3,5);

    for(x,y,w,h) in faces:
        imgcount=imgcount+1
        cv2.imwrite("DataSet/User."+str(id)+"."+str(imgcount)+".jpg",img[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)

    cv2.imshow('frame',img)
    cv2.waitKey(1)
    
    if(imgcount>20):
        break

    
cam.release()
cv2.destroyAllWindows()




