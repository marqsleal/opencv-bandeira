import numpy as np
import cv2 as cv

altura = 400
largura = 600
centro = (largura//2, altura//2)

# Cores
verde = (34, 139, 34) # Verde em BGR
amarelo = (0, 255, 255) # Amarelo em BGR
azul = (255, 0, 0) # Azul em BGR
branco = (255, 255, 255) # Branco em BGR

# Bandeira verde
bandeira = np.zeros((altura, largura, 3), np.uint8)
bandeira[:] = verde

# Losanglo amarelo
pts = np.array([[largura//2, 50],
                [largura-50, altura//2],
                [largura//2, altura-50],
                [50, altura//2]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(bandeira, [pts], amarelo)

# Circulo azul
cv.circle(bandeira, centro, 100, azul, -1)

# Faixa Branca
eixo = (100, 20)
cv.ellipse(bandeira, centro, eixo, angle=180, startAngle=0, endAngle=360, color=branco, thickness=-1)

cv.imshow('Bandeira do Brasil (Precione ESC para sair)', bandeira)

# Apertar ESC para fechar
if cv.waitKey(0) & 0xFF == 27:  # ASCII para ESC
    cv.destroyAllWindows()