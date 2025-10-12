import pygame 

class Personaje:
    def __init__(self, x, y):
        self .forma = pygame.Rect(0,0,20,20)
        self .forma.center = (x,y)# Verde

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color: (2255,255,0) , (self.x, self.y, 50, 50))