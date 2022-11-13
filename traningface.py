import cv2, os
import numpy as np
from PIL import Image

# Training model dengan metode LBPH (Local Binary Pattern Histogram)
def TrainingFace():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    def getImagesWithLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            pillImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pillImage, 'uint8') 
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(imageNp)
            for (x, y, w, h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples, ids
    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    if os.path.exists('dataset/trainer.yml'):
        os.remove('dataset/trainer.yml')
    faces, ids = getImagesWithLabels('dataset')
    recognizer.train(faces, np.array(ids))
    recognizer.write('dataset/trainer.yml')
    print("{0} faces trained. Exiting Program".format(len(np.unique(ids))))


#main
# TrainingFace()