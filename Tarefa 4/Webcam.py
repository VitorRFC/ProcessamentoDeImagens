import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read() #ler a webcam

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    roxoMin = np.array([130, 50, 0])
    roxoMax = np.array([150, 255, 255])
    
    mascara = cv2.inRange(hsvImage, roxoMin, roxoMax)
    contorno, hierarquia = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contorno:
        maxArea = cv2.contourArea(contorno[0])
        contourId = 0; i = 0
        for cnt in contorno:
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourId = i
            i += 1

        x,y,w,h = cv2.boundingRect(contorno[contourId])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow('Procurando Roxo', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()