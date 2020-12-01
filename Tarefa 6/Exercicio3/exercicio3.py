import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
def comparar(imagem1, imagem2):
    color = ('b','g', 'r')

    for i, col in enumerate(color):
        histograma1 = cv2.calcHist([imagem1],[i],None,[256],[0,256])
        plt.plot(histograma1, color = col)
        plt.xlim([0,256])
    

    for i, col in enumerate(color):
        histograma2 = cv2.calcHist([imagem2],[i],None,[256],[0,256])
        plt.plot(histograma2, color = col)
        plt.xlim([0,256])


    Correlacao = cv2.compareHist(histograma1, histograma2, cv2.HISTCMP_CORREL)
    Chi_Square = cv2.compareHist(histograma1, histograma2, cv2.HISTCMP_CHISQR)
    Bhattacharrya = cv2.compareHist(histograma1, histograma2, cv2.HISTCMP_BHATTACHARYYA)

    resultado = math.sqrt(math.pow(Correlacao,2) + math.pow(Chi_Square,2) + math.pow(Bhattacharrya,2))
    print("o resultado de cada comparacao: %.1f" %resultado)
    return resultado

def main():
    s1 = cv2.imread("messi2.jpg")
    s2 = cv2.imread("messi1.jpg")
    d1 = cv2.imread("iphone.jpg")
    d2 = cv2.imread("carrancas.jpg")
    d3 = cv2.imread("mario.jpg")


    Resultado_0 = comparar(s1, d1)
    Resultado_1 = comparar(s1, d2)
    Resultado_2 = comparar(s1, d3)
    Resultado_3 = comparar(s1, s2)

    Lista_Resultados = [Resultado_0, Resultado_1, Resultado_2, Resultado_3]

    menor=Resultado_0
    id=0
    

    for i in range (0, len(Lista_Resultados)):
        if(menor > Lista_Resultados[i]):
            menor = Lista_Resultados[i]
            id = i
    if(id == 0):
        cv2.imshow("img", d1)
        plt.show()
        cv2.imshow("imagem principal", s1)
        plt.show()
    if(id == 1):
        cv2.imshow("img", d2)
        cv2.imshow("imagem principal", s1)
        plt.show()
    if(id == 2):
        cv2.imshow("img", d3)
        cv2.imshow("imagem principal", s1)
        plt.show()
    if(id == 3):
        cv2.imshow("img", s2)
        cv2.imshow("imagem principal", s1)
        plt.show()    
        
cv2.destroyAllWindows()
main()
