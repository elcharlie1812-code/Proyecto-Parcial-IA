# scripts/Menu.py
# Autor: [Charlie Baez, 21-SISN-2-028]
# Menú principal 

import pygame 

from scripts.Constantes import *

class menu: 

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente_titulo = pygame.font.Sysfont("Aria", 70)
        self.fuente_opciones = pygame.font.SysFont("Arial, 40")
        self.fuente_opciones =["iniciar Juego", "Reiniciar", "Salir"]
        self.opcion_seleccionada = 0 


        

