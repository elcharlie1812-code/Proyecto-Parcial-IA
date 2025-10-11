import pygame
from scripts.Config import *

def main():
    pygame.init()
    
    # Crear ventana
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Proyecto Gauntlet")
    
    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Fondo negro
        pantalla.fill((0, 0, 0))
        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
