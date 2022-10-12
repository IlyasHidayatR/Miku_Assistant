from msilib.schema import Condition
import cv2, time
import os
from PIL import Image
import urllib.request
import numpy as np

def camera_face(cam):
    if cam == 1:
        camera = 0
    elif cam == 2:
        camera = urllib.request.urlopen("http://192.168.43.95/cam-lo.jpg")
    return camera

#main program
def face_recognition(camera):
    global Condition
    video = cv2.VideoCapture(camera_face(camera), cv2.CAP_DSHOW)
    faceDetections = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('dataset/trainer.yml')
    a = 0
    while True:  
        a = a + 1
        check, frame = video.read()
        tampil = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetections.detectMultiScale(tampil, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            id, conf = recognizer.predict(tampil[y:y+h, x:x+w])
            if id == 1:
                id = "Ilyas Hidayat Rusdy"
                Condition = 1
            else:
                id = "Unknown"
                Condition = 0
            cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Recognition", frame)
        key = cv2.waitKey(1)
        if Condition == 1:
            print("Face recognized")
            break
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition(1)