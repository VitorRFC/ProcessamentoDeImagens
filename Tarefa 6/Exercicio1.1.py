import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread ("ranger.jpg")
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    print (i,col)
    histograma = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histograma, color = col)
    plt.xlim([0,256])

cv2.imshow("imagem",img)
plt.show()
