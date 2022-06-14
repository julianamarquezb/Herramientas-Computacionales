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

pygame.init()
filas = 6
columnas = 7
tamaño = (columnas*100, filas*100 + 200)
pantalla = pygame.display.set_mode(tamaño)
fuente = pygame.font.Font(pygame.font.get_default_font(), 100)
titulo = fuente.render('Conecta 4', True, blanco)

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

    for i in range(columnas-3): # Línea horizontal
        for j in range(filas):
            if tablero[i][j] == jugador and tablero[i+1][j] == jugador and tablero[i+2][j] == jugador and tablero[i+3][j] == jugador:
                return True

    for i in range(columnas):   # Línea vertical
        for j in range(filas-3):
            if tablero[i][j] == jugador and tablero[i][j+1] == jugador and tablero[i][j+2] == jugador and tablero[i][j+3] == jugador:
                return True

    for i in range(columnas-3): # Línea en diagonal /
        for j in range(filas-3):
            if tablero[i][j] == jugador and tablero[i+1][j+1] == jugador and tablero[i+2][j+2] == jugador and tablero[i+3][j+3] == jugador:
                return True

    for i in range(3,columnas): # Línea en diagonal \
        for j in range(filas-3):
            if tablero[i][j] == jugador and tablero[i-1][j+1] == jugador and tablero[i-2][j+2] == jugador and tablero[i-3][j+3] == jugador:
                return True


""" Función que decide si la posición de la ficha es válida """

def valido(tablero, columna):
    if tablero[columna][-1] == 0:
        return True
    else:
        return False

""" Función que retorna la fila en la que debe caer la ficha """

def cual_fila(tablero, columna):
    for i in range(filas):
        if tablero[columna][i] == 0:
            return i

""" Función que ubica la ficha en la posición indicada """

def poner_ficha(tablero, jugador, fila, columna):
    tablero[columna][fila] = jugador
    return tablero

""" Función que actualiza las gráficas """

def mostrar():
    pantalla.fill(negro)
    pantalla.blit(titulo, dest = (120, 50))
    pygame.draw.rect(pantalla, azul_oscuro, (0, 200, tamaño[0], tamaño[1]))
    dibujar_tablero(tablero)
    pygame.display.flip()

""" Loop que permite el funcionamiento del juego """

tablero = tablero()
game_over = False
turno = 0

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        if turno == 0:
            pygame.draw.rect(pantalla, negro, (50, 500, 600, 20))
            texto = pygame.font.Font(pygame.font.get_default_font(), 15)
            instrucciones = texto.render('Para jugar, desliza la ficha hasta la columna y déjala caer presionando el mouse', True, blanco)
            pantalla.blit(instrucciones, dest=(50,500))

        if event.type == pygame.MOUSEMOTION:
            posicion = pygame.mouse.get_pos()[0]
            if turno % 2 == 0:
                pygame.draw.circle(pantalla, rojo, (posicion, 150), 45)
            else:
                pygame.draw.circle(pantalla, amarillo, (posicion, 150), 45)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion = pygame.mouse.get_pos()[0]
            columna = int(posicion//100)

            if turno % 2 == 0:
                if valido(tablero, columna) == True:
                    fila = cual_fila(tablero, columna)
                    poner_ficha(tablero, 1, fila, columna)
                if ganar(tablero, 1) == True:
                    ganador = texto.render('El jugador 1 ha ganado', True, blanco)
                    game_over = True

            elif turno % 2 == 1:
                if valido(tablero, columna) == True:
                    fila = cual_fila(tablero, columna)
                    poner_ficha(tablero, 2, fila, columna)
                if ganar(tablero, 2) == True:
                    ganador = texto.render('El jugador 2 ha ganado', True, blanco)
                    game_over = True
            turno += 1

        mostrar()

pantalla.blit(ganador, dest = (50,500))
pygame.quit()
