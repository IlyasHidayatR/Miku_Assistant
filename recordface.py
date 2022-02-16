import cv2, time
camera = 0
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
faceDetections = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id = input('Masukkan ID: ')
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