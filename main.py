import pygame
from scripts.Constantes import *
from scripts.Personaje import Personaje

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Gauntlet")


Jugador = Personaje(50,50)


# Movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

run = True
while run == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Detectar cuando se presionan las teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        # Detectar cuando se sueltan las teclas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    # movimiento
    delta_x = 0
    delta_y = 0

    if mover_derecha:
        delta_x = 5
    if mover_izquierda:
        delta_x = -5
    if mover_arriba:
        delta_y = -5
    if mover_abajo:
        delta_y = 5

    Jugador.movimiento(delta_x, delta_y)


    pantalla.fill((0, 0, 0))  # Fondo negro
    Jugador.dibujar(pantalla)
    pygame.display.update()

pygame.quit()