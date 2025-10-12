import pygame 
from scripts.Constantes import *

class Personaje:
    def __init__(self, x, y):
       self.forma = pygame.Rect(0 , 0, ALTO_PERSONAJE, ANCHO_PERSONAJE) 
       self.forma.center = (x,y) 
       
       
    def dibujar(self, interfaz):   # Un cuadrado de 50x50
        pygame.draw.rect(interfaz, COLOR_PERSONAJE , self.forma)