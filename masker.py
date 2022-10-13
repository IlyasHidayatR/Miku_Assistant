import cv2


def masker():
    facecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    nosecade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")

    video_capture = cv2.VideoCapture(0)
    mask_on = False

    while True:
        #ambil frame by frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        wajah = facecade.detectMultiScale(gray, 1.1, 5)

        #gambar kotak di wajah
        for(x, y, w, h) in wajah:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            if mask_on:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, 'Mask on', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(frame, 'Mask off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

            hidung = nosecade.detectMultiScale(roi_gray, 1.18, 35)
            for (sx, sy, sw, sh) in hidung:
                cv2.rectangle(roi_color, (sh, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
                cv2.putText(frame, 'hidung', (x + sx,y + sy), 1, 1, (0, 255, 0), 1)
                
                if len(hidung) == 0:
                    mask_on = True
                elif len(hidung) > 0:
                    mask_on = False

        cv2.putText(frame, 'jumlah wajah: ' + str(len(wajah)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()