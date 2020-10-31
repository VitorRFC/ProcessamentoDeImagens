import numpy as np
import cv2
import time

def onChange(value):
    pass

img = cv2.imread("imagem.png")
copia = img.copy() 
windowTitle = "Limiarizacao" 
cv2.namedWindow(windowTitle) 

cv2.createTrackbar("Limiar", windowTitle, 100,255, onChange)

valorInicial = 100 #valor inicial do trackbar
novoLimiar = False
tempo = 0 

while True:
    limiarBar = cv2.getTrackbarPos("Limiar", windowTitle)

    if(valorInicial != limiarBar):
        novoLimiar = True 
        tempo = time.time() #tempo de movimentacao no trackbar
        valorInicial = limiarBar #altera o valor inicial atual do trackbar

    if(novoLimiar == True and (time.time() - tempo > 0.5)): #se trocou limiar e passou 1s q o usuario clico no track bar
        #pegamos o valor do limiar da posição do trackbar e passamos p método de limiarizar a img
        limiarBar, copia =  cv2.threshold(img, limiarBar, 255, cv2.THRESH_BINARY)
        #img atualizada entao atualizar limiar recebe falso
        novoLimiar = False

    cv2.imshow(windowTitle, copia)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 




