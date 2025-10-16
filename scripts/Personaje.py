import pygame
from scripts.Constantes import *

class Personaje:
    def __init__(self, x, y, image):

        self.image = image
        self.rect = pygame.Rect(x, y, ALTO_PERSONAJE, ANCHO_PERSONAJE) 

    def movimiento(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
        #pygame.draw.rect(pantalla, (COLOR_PERSONAJE), self.rect)
