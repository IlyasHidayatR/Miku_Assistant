import cv2, time
import os
from PIL import Image
import urllib.request
import numpy as np

faceDetections = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('dataset/trainer.yml')

#dictionary ID and name of the person for face recognition with camera wifi
recognize_ID = {1: "Ilyas Hidayat Rusdy", 
                4: "Agung Wicaksana", 
                8: "Meirli",
                9: "Zahra",
                7: "Acep Taufik Hidayat",
                10: "Anisza"}

#camera face
def camera_face(cam):
    if cam == 1:
        camera = 0
    elif cam == 2:
        camera = "http://192.168.43.95/1024x768.jpg"
    return camera

#face recognition with camera cable
def face_recognition(camera):
    global id, conf
    valid = False
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
            #face recognition of owners
            if id == 1 and conf < 100:
                id = "Ilyas Hidayat Rusdy"
                valid = True
                #print confidance dalam persen
                conf = "{0}%".format(round(100-conf))
                print(id + " " + "("+conf+")")
            else:
                id = "Unknown"
            cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Recognition", frame)
        key = cv2.waitKey(1)
        if valid == True:
            time.sleep(1)
            print("Face recognized")
            valid = False
            break
        if key == ord('q'):
            #input password
            password = input("Enter password: ")
            if password == "123":
                print("Password correct")
                break
            else:
                print("Password incorrect. Please verify with correctly face or restart the program")
    video.release()
    cv2.destroyAllWindows()


#face recognition with camera wifi
def face_recognition1(camera):
    global id, conf
    valid = False
    url = camera_face(camera)
    cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
    while True:
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetections.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            #if id is already in the database and the confidence is greater than 50 then print the face recognized
            if id in recognize_ID and conf < 100:
                id = recognize_ID[id]
                valid = True
                #print confidance dalam persen
                conf = "{0}%".format(round(100-conf))
                print(id + " " + "("+conf+")")
            else:
                id = "Unknown"
            cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Recognition',img)
        key = cv2.waitKey(1)
        if valid == True:
            time.sleep(1)
            print("Face recognized")
            valid = False
            break
        if key == ord('q'):
            #input password
            password = input("Enter password: ")
            if password == "123":
                print("Password correct")
                break
            else:
                print("Password incorrect. Please verify with correctly face or restart the program")
    cv2.destroyAllWindows()


# if __name__ == "__main__":
#     while True:
#         print("1. Face Recognition with Camera Cable")
#         print("2. Face Recognition with Camera Wifi")
#         print("3. Exit")
#         pilihan = int(input("Choose the camera: "))
#         if pilihan == 1:
#             #start time
#             start = time.time()
#             face_recognition(1)
#             #end time
#             end = time.time()
#             print("Time: ", end - start)
#         elif pilihan == 2:
#             #start time
#             start = time.time()
#             face_recognition1(2)
#             #end time
#             end = time.time()
#             #print time
#             print("Time: ", end - start)
#         elif pilihan == 3:
#             break
#         else:
#             print("Please choose the correct camera")