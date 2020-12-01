import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("girafa.png")

imagem = cv2.cvtColor (imagem, cv2.COLOR_BGR2GRAY)
equalizada = cv2.equalizeHist (imagem)

cv2.imshow ( 'Imagem original' , imagem)
cv2.imshow ( 'Imagem equalizada' , equalizada)

cv2.imwrite("GirafaEqualizada.png", equalizada)

cv2.waitKey ()