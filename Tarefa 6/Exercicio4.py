import numpy as np
import cv2
import time
from tqdm import tqdm

src = cv2.imread("j.png")

def onChange(value):
    pass

def VideoErosao():
    title_window_erosion = 'Erosao'
    cv2.namedWindow(title_window_erosion)
    cv2.createTrackbar('Valor', title_window_erosion , 0, 50, onChange)

    Erosao_Inicial = 0
    Atualizar_Erosao = False
    Erosao_Destino = src.copy()
    Tempo_Espera = 0

    while True:
        QuantidadeErosao = cv2.getTrackbarPos('Valor', title_window_erosion)

        if(Erosao_Inicial != QuantidadeErosao):
            Atualizar_Erosao = True
            Tempo_Espera = time.time()
            Erosao_Inicial = QuantidadeErosao

        if(Atualizar_Erosao == True and (time.time() - Tempo_Espera > 0.5)):
            erosaoPrincipal = 0
            element = cv2.getStructuringElement(erosaoPrincipal, (2*QuantidadeErosao + 1,2*QuantidadeErosao+1), (QuantidadeErosao, QuantidadeErosao))
            Erosao_Destino = cv2.erode(src, element)
            Atualizar_Erosao = False


        cv2.imshow(title_window_erosion, Erosao_Destino)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cv2.destroyAllWindows()

def VideoDilatacao():
    title_window_dilatation = 'Dilatacao'
    cv2.namedWindow(title_window_dilatation)
    cv2.createTrackbar('Valor', title_window_dilatation , 0, 100, onChange)

    Dilatacao_Inicial = 0
    Atualizar_Dilatacao = False
    Dilatacao_Destino = src.copy()
    Tempo_Espera = 0

    while True:
        QuantidadeDilatacao = cv2.getTrackbarPos('Valor', title_window_dilatation)
        if(Dilatacao_Inicial != QuantidadeDilatacao):
            Atualizar_Dilatacao = True
            Tempo_Espera = time.time()
            Dilatacao_Inicial = QuantidadeDilatacao

        if(Atualizar_Dilatacao == True and (time.time() - Tempo_Espera > 0.5)):
            dilatacaoPrincipal = 0
            element = cv2.getStructuringElement(dilatacaoPrincipal, (2*QuantidadeDilatacao + 1,2*QuantidadeDilatacao+1), (QuantidadeDilatacao, QuantidadeDilatacao))
            Dilatacao_Destino = cv2.dilate(src, element)
            Atualizar_Dilatacao = False


        cv2.imshow(title_window_dilatation, Dilatacao_Destino)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def main():
    VideoErosao()
    VideoDilatacao()

main()