import pygame

# Initialize Pygame
pygame.init()   
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mijuego")

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False


screen  .fill((0, 0, 0))  # Fill the screen with black
pygame.display.update()  # Update the display

pygame.quit()