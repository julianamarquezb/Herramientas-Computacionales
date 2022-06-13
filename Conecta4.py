""" Código para crear el juego Conecta 4"""

import numpy as np
import math
import pygame
import sys
import random

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
filas = 6
columnas = 7
tamaño = (columnas*100, filas*100 + 200)
pantalla = pygame.display.set_mode(tamaño)
fuente = pygame.font.Font(pygame.font.get_default_font(), 100)
texto = fuente.render('Conecta 4', True, blanco)
""" Matriz que representa el tablero de juego """

def tablero():

    tablero = np.zeros((columnas, filas))
    return tablero
    
""" Función que dibuja las fichas de acuerdo a los valores
en la matriz del tablero """
 
def dibujar_tablero(tablero):

    for i in range(columnas):
        for j in range(filas):
            if tablero[i][j] == 1:
                pygame.draw.circle(pantalla, rojo, (int(100*(i+0.5)), tamaño[1]-int(100*(j+0.5))), 45)
            elif tablero[i][j] == 2:
                pygame.draw.circle(pantalla, amarillo, (int(100*(i+0.5)), tamaño[1]-int(100*(j+0.5))), 45)
            else:
                pygame.draw.circle(pantalla, negro, (int(100*(i+0.5)), tamaño[1]-int(100*(j+0.5))), 45)

    pygame.display.update()

""" Función que identifica 4 fichas en línea """

def ganar(tablero, jugador):

    for i in range(columnas-3): """ Línea horizontal """
        for j in range(filas):
            if tablero[i][j] == jugador and tablero[i+1][j] == jugador and tablero[i+2][j] == jugador and tablero[i+3][j] == jugador:
                return True

    for i in range(columnas):   """ Línea vertical """
        for j in range(filas-3):
            if tablero[i][j] == jugador and tablero[i][j+1] == jugador and tablero[i][j+2] == jugador and tablero[i][j+3] == jugador:
                return True

    for i in range(columnas-3): """ Línea en diagonal / """
        for j in range(filas-3):
            if tablero[i][j] == jugador and tablero[i+1][j+1] == jugador and tablero[i+2][j+2] == jugador and tablero[i+3][j+3] == jugador:
                return True

    for i in range(3,columnas): """ Línea en diagonal \ """
        for j in range(filas-3):
            if tablero[i][j] == jugador and tablero[i-1][j+1] == jugador and tablero[i-2][j+2] == jugador and tablero[i-3][j+3] == jugador:
                return True

""" Función que ubica la ficha en la posición indicada """

def poner_ficha(tablero, jugador, fila, columna):
    tablero[columna][fila] = jugador

""" Función que actualiza las gráficas """

def mostrar():

    pantalla.fill(negro)
    pantalla.blit(texto, dest = (120, 50))
    pygame.draw.rect(pantalla, azul_oscuro, (0, 200, tamaño[0], tamaño[1]))
    dibujar_tablero(tablero)
    pygame.display.flip()
    
pygame.init()
tablero = tablero()
game_over = False

""" Loop que permite el funcionamiento del juego """

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    mostrar()

pygame.quit()
