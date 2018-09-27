import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer();

path = "DataSet"

def getImageWithId(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    faces = []
    IDs = []
    
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L');
       
        faceNP = np.array(faceImg,'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNP)
        print(ID)
        IDs.append(ID)
        cv2.imshow('training',faceNP)
        cv2.waitKey(10)
    return np.array(IDs),faces

IDs, faces = getImageWithId(path)

recognizer.train(faces,IDs)
recognizer.save("Training Data/trainingData.yml")
cv2.destroyAllWindows()
