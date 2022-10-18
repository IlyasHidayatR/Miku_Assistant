import cv2, time
import os
from PIL import Image
import urllib.request
import numpy as np


faceDetections = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('dataset/trainer.yml')

#camera face
def camera_face(cam):
    if cam == 1:
        camera = 0
    elif cam == 2:
        camera = "http://192.168.43.95/800x600.jpg"
    return camera

#face recognition with camera cable
def face_recognition(camera):
    global id
    video = cv2.VideoCapture(camera_face(camera), cv2.CAP_DSHOW)
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
            else:
                id = "Unknown"
            cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Recognition", frame)
        key = cv2.waitKey(1)
        if id == "Ilyas Hidayat Rusdy":
            time.sleep(1)
            print("Face recognized")
            id = "open"
            break
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


#face recognition with camera wifi
def face_recognition1(camera):
    global id
    url = camera_face(camera)
    cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
    while True:
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetections.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if id == 1:
                id = "Ilyas Hidayat Rusdy"
            else:
                id = "Unknown"
            cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Recognition',img)
        key = cv2.waitKey(1)
        if id == "Ilyas Hidayat Rusdy":
            time.sleep(1)
            print("Face recognized")
            id = "open"
            break
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition(1)
    print(id)
    # face_recognition1(2)