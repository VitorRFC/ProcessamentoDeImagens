import numpy as np
import cv2
from matplotlib import pyplot as plt

def SeisImagens():
    imgSemFiltro = cv2.imread("iphone.jpg") #le a img

    media = cv2.blur(imgSemFiltro,( 20,20))
    
    gaussiana = cv2.GaussianBlur(imgSemFiltro , ( 7 , 7 ), 0 ) #gera menos borrão na img, traz um efeito mais natural e reduz ruido
    mediana = cv2.medianBlur(imgSemFiltro,9)
    
    sobelX = cv2.Sobel(imgSemFiltro, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(imgSemFiltro, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobel = cv2.bitwise_or(sobelX, sobelY)

    Laplaciano = cv2.Laplacian(imgSemFiltro, cv2.CV_64F)
    Laplaciano = np.uint8(np.absolute(Laplaciano))

    Imagens = [imgSemFiltro, media, gaussiana, mediana, sobel, Laplaciano] #array com as imagens
    Titulos = ['Original','Média', 'Gaussiana', 'Mediana', 'Sobel', 'Laplaciano']
    GridImagens(Imagens, Titulos, 2, 3) #2 colunas e 3 linhas

def GridImagens(Imagens, Titulos, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return

   
    fig, axis = plt.subplots(y, x)
    ContX, ContY, ContTitulo = 0, 0, 0 #contadores da img  e titulo
    
    for img in Imagens: 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        axis[ContY, ContX].set_title(Titulos[ContTitulo]) 
        axis[ContY, ContX].imshow(img) #pedir p img atual ser exibida

        if(len(Titulos[ContTitulo]) == 0):
            axis[ContY,ContX].axis('off') #se o titulo nao tem caracter não aparece 

        #percorrido a primeira imagem, passo p seguinte
        ContTitulo += 1
        ContX += 1 

        
        if ContX == x:
            ContX = 0 
            ContY += 1

    fig.tight_layout(pad=0.8) #diminui a distancia das img
    plt.show() #para imprimir as imagens

SeisImagens()