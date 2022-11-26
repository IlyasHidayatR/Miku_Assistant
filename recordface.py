import cv2, os, time
import tkinter as tk

#record face
valid = 0
def record_face():
    global valid
    camera = 0
    video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
    faceDetections = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #input ID with tkinter GUI and convert to string
    screen_form = tk.Tk()
    screen_form.title("Form")
    screen_form.geometry("300x200")
    screen_form.configure(background="white")
    label = tk.Label(screen_form, text="Enter ID", bg="white", fg="black", font=("Arial", 15))
    label.pack()
    entry = tk.Entry(screen_form, width=30)
    entry.pack()
    def save():
        global valid
        valid = entry.get()
        screen_form.destroy()
    button = tk.Button(screen_form, text="Save", command=save)
    button.pack()
    screen_form.mainloop()
    id = str(valid)
    try:
        #if id not exist in dataset
        if not os.path.exists('dataset/User.' + str(id) + '.1.jpg') and id != "":
            valid = 1
            a = 0
            while True:
                a = a + 1
                check, frame = video.read()
                tampil = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceDetections.detectMultiScale(tampil, scaleFactor=1.3, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.imwrite("dataset/User." + str(id) + '.' + str(a) + ".jpg", tampil[y:y+h, x:x+w])
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow("Face Recognition", frame)
                if a > 30:
                    break
            video.release()
            cv2.destroyAllWindows()
        elif os.path.exists('dataset/User.' + str(id) + '.1.jpg'):
            valid = 0
            print("ID already exist")
            exit()
    except:
        valid = 0
        print("Error")
        video.release()
        cv2.destroyAllWindows()
        
def validasi3():
    global valid
    if valid == 1:
        valid = 0
        return 1
    else:
        return 0

#main
# if __name__ == "__main__":
#     record_face()
#     print(valid)