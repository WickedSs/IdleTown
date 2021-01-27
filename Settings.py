import random
import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (112, 111, 111)
HIGHLIGHTED = (202, 240, 248)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKYBLUE = (137, 196, 244)
DARKSKYBLUE = (79, 196, 244)
MATTE_BLACK = 20, 20, 20
DIRT = (155, 118, 83)
MAP_DATA = [[random.randint(0, 1) for x in range(15)] for x in range(15)]


# game settings
WIDTH = 1360   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Idle Town"
BGCOLOR = DIRT
EDGEREMOVAL = 0

CHUNK_WIDTH = [256, 768]
CHUNK_HEIGHT = [192, 576]

TILESIZE = 64
SLOTSIZE = 64
TILESIZE_HALF = TILESIZE / 2
GRIDWIDTH = WIDTH / 2
GRIDHEIGHT = HEIGHT / 2
GRIDWIDTH_HALF = GRIDWIDTH / 2
GRIDHEIGHT_HALF = GRIDHEIGHT / 2

## Game Parametters
pygame.init()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pg.key.set_repeat(500, 100)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
initWords = ["Continue", "New Game", "Options", "Exit"]
OptionsWords = ["Video", "Key Bindings", "BACK"]
VideoWords = ["1024 x 512", "1280 x 768", "1536 x 768", "Full Screen", "Back"]

## loaded Assetes
tree = pygame.image.load("./Resources/Sprites/tree.png")
tree_hovered = pygame.image.load("./Resources/Sprites/tree-hovered.png")
background = pygame.image.load("./Resources/Images/bgCopy.png")
