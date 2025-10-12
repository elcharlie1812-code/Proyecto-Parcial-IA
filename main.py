import pygame
from scripts.Constantes import *
from scripts.Personaje import Personaje

Jugador = Personaje(50,50)


pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(Gauntlet)


run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pantalla.fill() 

