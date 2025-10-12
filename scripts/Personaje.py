import pygame
from scripts.Constantes import *

class Personaje:
    def __init__(self, x, y):
        
        self.rect = pygame.Rect(x, y, ALTO_PERSONAJE, ANCHO_PERSONAJE) 

    def movimiento(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 255, 255), self.rect)
