import pygame
from Elements import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1360, 768))
    pygame.display.set_caption("Idle Town")
    startGame = MainMenu(screen)
    startGame.draw(WIDTH//16, HEIGHT//16)
