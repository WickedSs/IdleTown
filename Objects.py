import pygame


class Sprite:
    def __init__(self, x, y, screen, type, filename):
        self.screen = screen
        self.type = type
        self.x = x
        self.y = y
        self.sprite_normal = pygame.image.load("./Resources/Sprites/"+filename+".png")
        self.sprite_hovered = pygame.image.load("./Resources/Sprites/"+filename+"-hovered.png").convert_alpha()
        self.rect = self.sprite_normal.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.occupied = False

    # def draw(self):
    #     self.screen.blit(self.sprite_normal, (self.x, self.y))

    def onHover(self):
        pass


class Chunk:
    def __init__(self, number, sprites, x, y, screen):
        self.x = x
        self.y = y
        self.number = number
        self.sprites = sprites
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        for i in range(len(self.sprites)):
            current = self.sprites[i]
            self.screen.blit(current.sprite_normal, (current.x, current.y))

    def updateSprites(self, lst):
        self.sprites = lst
