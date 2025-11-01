# scripts/Menu.py
# Autor: [Charlie Baez, 21-SISN-2-028]
# Menú principal 

import pygame 
from scripts.Constantes import *

class menu: 

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente_titulo = pygame.font.SysFont("Aria", 70)
        self.fuente = pygame.font.SysFont("Arial", 40)
        self.fuente_opciones =["iniciar Juego", "Reiniciar", "Salir"]
        self.opcion_seleccionada = 0 
    
    def manejarevento (self, evento):
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        

    def dibujar(self):
        self.pantalla.fill((0, 0, 0))

    # Título del menú
        titulo = self.fuente_titulo.render("GAUNTLET", True, (255, 255, 0))
        self.pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 120))

    # Opciones del menú
        for i, texto in enumerate(self.fuente_opciones):
          color = (0, 255, 0) if i == self.opcion_seleccionada else (255, 255, 255)
          render = self.fuente.render(texto, True, color)
          self.pantalla.blit(render, (ANCHO // 2 - render.get_width() // 2, 300 + i * 70))


        pygame.display.flip()

