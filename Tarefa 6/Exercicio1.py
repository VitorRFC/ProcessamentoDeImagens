import numpy as np
from matplotlib import pyplot as plt
import cv2

imagem = cv2.imread ("ranger.jpg", 0)

plt.hist(imagem.ravel(), 256, [0,256])
cv2.imshow("Imagem",imagem)
plt.show()

