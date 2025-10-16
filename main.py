import pygame
from scripts.Constantes import *
from scripts.Personaje import Personaje

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Gauntlet")

Jugador_imagenes = pygame.image.load("assets//image//jugador//Jugador_1.png")
Jugador_imagenes = pygame.transform.scale(
    Jugador_imagenes,
    (Jugador_imagenes.get_width() * ESCALA_IMAGEN,
     Jugador_imagenes.get_height() * ESCALA_IMAGEN))

Jugador = Personaje(ALTO_PERSONAJE,ANCHO_PERSONAJE,Jugador_imagenes)


# Movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#control de frame rate
reloj = pygame.time.Clock()

run = True
while run == True:
     
    reloj.tick(FPS)

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
        delta_x = Velocidad
    if mover_izquierda:
        delta_x = -Velocidad
    if mover_arriba:
        delta_y = -Velocidad
    if mover_abajo:
        delta_y = Velocidad

    Jugador.movimiento(delta_x, delta_y)


    pantalla.fill(COLOR_FONDO)  # Fondo negro
    Jugador.dibujar(pantalla)
    pygame.display.update()

pygame.quit()