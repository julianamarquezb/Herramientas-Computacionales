""" Código para crear el juego Conecta 4"""

import numpy as np
import math
import pygame
import sys
import random

pygame.init()
fps = pygame.time.Clock()
num_fps = 30

""" Lista de los colores que se usarán en el juego """

rojo = (255, 0, 0)
azul_oscuro = (0, 0, 255)
azul_claro = (0, 150, 255)
verde_oscuro = (0, 100, 0)
verde_claro = (0, 200, 0)
amarillo = (255, 255, 0)
naranja_oscuro = (255, 100, 0)
naranja_claro = (255, 180, 130)
morado_oscuro = (90, 0, 180)
morado_claro = (100, 100, 255)
rosado_oscuro = (255, 50, 200)
rosado_claro = (255, 200, 255)
gris_oscuro = (75, 75, 75)
gris_claro = (150, 150, 150)
negro = (0, 0, 0)
blanco = (255, 255, 255)

""" Inicio de las gráficas del juego """

tamaño = (1000, 1000)
pantalla = pygame.display.set_mode(tamaño)
filas = 6
columnas = 7

def tablero()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pantalla.fill(negro)
    pygame.display.flip()

pygame.quit()
