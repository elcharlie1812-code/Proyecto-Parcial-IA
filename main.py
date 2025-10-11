import pygame
from scrips.Config import *
from scrips.Jugador import Jugador
from scrips.Enemigo import Enemigo
from scrips.Albordecomportamiento import Albordecomportamiento


def main():
    # Inicializar pygame
    pygame.init()
    
    # Crear ventana
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    
    # Reloj para controlar los FPS
    clock = pygame.time.Clock()
    
    # Variable de control del loop
    running = True
    
    # Loop principal del juego
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica del juego (de momento vacía)
        
        # Dibujar fondo
        screen.fill(BLACK)
        
        # Actualizar pantalla
        pygame.display.flip()
        
        # Controlar FPS
        clock.tick(FPS)
    
    pygame.quit()


# Esto asegura que solo se ejecute si corres main.py directamente
if __name__ == "__main__":
    main()



