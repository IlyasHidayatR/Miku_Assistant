import cv2, time
import os
from PIL import Image
import urllib.request
import numpy as np
import tkinter as tk

faceDetections = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('dataset/trainer.yml')

#dictionary ID and name of the person for face recognition with camera wifi
recognize_ID = {1: "Ilyas Hidayat Rusdy",
                2: "Dika Priyatna",
                3: "Diksa Dinata",
                4: "Agung Wicaksana",
                5: "Sindu",
                6: "Resika Arthana",
                7: "Acep Taufik Hidayat",
                8: "Meirli",
                9: "Zahra",
                10: "Anisza"}

#camera face
def camera_face(cam):
    if cam == 1:
        camera = 0
    elif cam == 2:
        camera = "http://192.168.43.95/1024x768.jpg"
    return camera

#face recognition with camera cable
valid1 = False
def face_recognition(camera):
    global id, conf, valid1
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
                valid1 = True
                #print confidance dalam persen
                conf = "{0}%".format(round(100-conf))
                print(id + " " + "("+conf+")")
            else:
                id = "Unknown"
                valid1 = False
            cv2.putText(frame, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Recognition", frame)
        key = cv2.waitKey(1)
        if valid1 == True:
            time.sleep(1)
            print("Face recognized")
            # valid1 = False
            break
        # elif valid1 == False:
        #     time.sleep(1)
        #     print("Face not recognized")
        #     # valid1 = False
        #     break
        elif key == ord('q'):
            #input password with GUI tkinter
            root = tk.Tk()
            root.title("Password")
            root.geometry("300x200")
            root.resizable(False, False)
            label = tk.Label(root, text="Enter password: ")
            label.pack()
            entry = tk.Entry(root, show="*")
            entry.pack()
            def check():
                global valid1
                if entry.get() == "123":
                    print("Password correct")
                    valid1 = True
                    root.destroy()
                else:
                    print("Password incorrect. Please verify with correctly face or restart the program")
                    exit()
            button = tk.Button(root, text="Enter", command=check)
            button.pack()
            root.mainloop()
            break
        elif key == ord('n'):
            valid1 = False
            break
    video.release()
    cv2.destroyAllWindows()

#function validasi face recognition to other file and back valid1 to False (Camera cable)
def validasi():
    global valid1
    if valid1 == True:
        valid1 = False
        return True
    else:
        return False
    
#face recognition with camera wifi
valid2 = False
def face_recognition1(camera):
    global id, conf, valid2
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
            #if id is already in the database and the confidence is greater than 0 then print the face recognized
            if id in recognize_ID and conf < 100:
                id = recognize_ID[id]
                valid2 = True
                #print confidance dalam persen
                conf = "{0}%".format(round(100-conf))
                print(id + " " + "("+conf+")")
            else:
                id = "Unknown"
                valid2 = False
            cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Recognition',img)
        key = cv2.waitKey(1)
        if valid2 == True:
            time.sleep(1)
            print("Face recognized")
            # valid = False
            break
        # elif valid2 == False:
        #     time.sleep(1)
        #     print("Face not recognized")
        #     # valid = False
        #     break
        elif key == ord('q'):
            #input password with GUI tkinter
            root = tk.Tk()
            root.title("Password")
            root.geometry("300x200")
            root.resizable(False, False)
            label = tk.Label(root, text="Enter password: ")
            label.pack()
            entry = tk.Entry(root, show="*")
            entry.pack()
            def check():
                global valid2
                if entry.get() == "123":
                    print("Password correct")
                    valid2 = True
                    root.destroy()
                else:
                    print("Password incorrect. Please verify with correctly face or restart the program")
                    exit()
            button = tk.Button(root, text="Enter", command=check)
            button.pack()
            root.mainloop()
            break
        elif key == ord('n'):
            valid2 = False
            break
    cv2.destroyAllWindows()

#function validasi face recognition to other file and back valid1 to False (Camera wifi)
def validasi1():
    global valid2
    if valid2 == True:
        valid2 = False
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        print("1. Face Recognition with Camera Cable")
        print("2. Face Recognition with Camera Wifi")
        print("3. Exit")
        pilihan = int(input("Choose the camera: "))
        if pilihan == 1:
            #start time
            start = time.time()
            face_recognition(1)
            validasi()
            #end time
            end = time.time()
            print("Time: ", end - start)
        elif pilihan == 2:
            #start time
            start = time.time()
            face_recognition1(2)
            validasi1()
            #end time
            end = time.time()
            #print time
            print("Time: ", end - start)
        elif pilihan == 3:
            break
        else:
            print("Please choose the correct camera")