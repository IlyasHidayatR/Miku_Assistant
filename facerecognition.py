import cv2, time
import os
from PIL import Image

camera = 0
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
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
        cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Face Recognition", frame)
    key = cv2.waitKey(1)
    if id == 1:
        #jalankan miku.py dan stop facerecognition.py
        os.system('python miku.py')
        break
video.release()
cv2.destroyAllWindows()