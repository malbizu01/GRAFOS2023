import pygame #Requiere la instalacion de libreria
import random
import math
import matplotlib.pyplot as plt #Requiere la instalacion de libreria matplotlib 

# la instalaciones de libreria se pueden  realizar a travez del cmd del sistema
# por ejemplo : pip install pygame para luego dirigirse a 
# python 3.11 (Version utilizada para este proyecto)
# y asi colocar por ejemplo: import pygame
# para asi utlizarlo en Visual Studio Code

width = 500
height = width
radio = width

red = pygame.Color('red')
green = pygame.Color('green')
blue = pygame.Color('blue')
white = pygame.Color('white')
gray = pygame.Color('gray')
light_gray = pygame.Color('lightgray')
black = pygame.Color('black')

pygame.init()

nPuntos = 0
nDentroCirculo = 0
radio2 = radio*radio 
iteracion = 0
epsilon = 0.000005

pi_values = []
iterations = []

while True:
    iteracion += 1
    x = random.randint(0,width)
    y = random.randint(0,height)
    nPuntos += 1

    if x*x + y*y <= radio2:
        nDentroCirculo += 1
        pi_aprox = nDentroCirculo * 4 / nPuntos
        pi_values.append(pi_aprox)
        iterations.append(iteracion)
        print(f'Simulacion N° {iteracion} -- Tiros dentro del círculo: {nDentroCirculo} -- Tiros dentro del cuadrado: {nPuntos - nDentroCirculo} -- Aproximación de pi: {pi_aprox:.6f}')

    else:
        pi_aprox = nDentroCirculo * 4 / nPuntos

        if abs(pi_aprox - math.pi) <= epsilon:
            print(f'Se alcanzo la aproximacion deseada despues de {iteracion} simulaciones')
            break

# Como recomendacion si son demasiadas simulaciones esperar un poco
# o cerrar el programa si ejecutarlo denuevo para que genere el grafico

plt.plot(iterations, pi_values)
plt.axhline(y=math.pi, color='r', linestyle='-')
plt.xlabel('Simulaciones')
plt.ylabel('Aproximación de pi')
plt.title('Grafico de convergencia en PI')
plt.show()

pygame.quit()
