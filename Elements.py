import pygame
import os, sys, json
from Settings import *
from pygame.locals import *

"""
    <rect(0, 0, 284, 91)> <rect(110, 48, 284, 284)>
    <rect(0, 0, 143, 55)> <rect(105, 208, 143, 143)>
    <rect(0, 0, 161, 55)> <rect(100, 268, 161, 161)>
    <rect(0, 0, 205, 55)> <rect(95, 328, 205, 205)>
    <rect(0, 0, 200, 55)> <rect(90, 388, 200, 200)>
    <rect(0, 0, 64, 55)>  <rect(85, 448, 64, 64)>

"""
continueBtn_low = pygame.image.load('./Resources/UI/Menu/Continue-LOW.png').convert_alpha()
NewGameBtn_low = pygame.image.load('./Resources/UI/Menu/NewGame-LOW.png').convert_alpha()
KeysBtn_low = pygame.image.load('./Resources/UI/Menu/Keys-LOW.png').convert_alpha()
HowToPlayBtn_low = pygame.image.load('./Resources/UI/Menu/HowToPlay-LOW.png').convert_alpha()
ExitBtn_low = pygame.image.load('./Resources/UI/Menu/Exit-LOW.png').convert_alpha()
continueBtn_high = pygame.image.load('./Resources/UI/Menu/Continue-HIGH.png').convert_alpha()
NewGameBtn_high = pygame.image.load('./Resources/UI/Menu/NewGame-HIGH.png').convert_alpha()
KeysBtn_high = pygame.image.load('./Resources/UI/Menu/Keys-HIGH.png').convert_alpha()
HowToPlayBtn_high = pygame.image.load('./Resources/UI/Menu/HowToPlay-HIGH.png').convert_alpha()
ExitBtn_high = pygame.image.load('./Resources/UI/Menu/Exit-HIGH.png').convert_alpha()
menuBG = pygame.image.load('./Resources/UI/Menu/MenuBG.png').convert_alpha()

class ButtonText:
    def __init__(self, screen):
        self.low = None
        self.high = None
        self.image = None
        self.x = 0
        self.y = 0
        self.action = None
        self.screen = screen
        self.rect = None

    def draw(self):
        self.rect[0], self.rect[1] = self.x, self.y
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos): self.image = self.high
        else: self.image = self.low
        self.screen.blit(self.image, (self.x-25, self.y+10))


class ContinueBtn(ButtonText):
    def __init__(self, screen):
        super().__init__(screen)
        self.low = continueBtn_low
        self.high = continueBtn_high
        self.x = WIDTH//16
        self.y = HEIGHT//16 + 100
        self.image = self.low
        self.rect = self.image.get_rect()

class NewGameBtn(ButtonText):
    def __init__(self, screen):
        super().__init__(screen)
        self.low = NewGameBtn_low
        self.high = NewGameBtn_high
        self.x = WIDTH//16
        self.y = HEIGHT//16 + 150
        self.image = self.low
        self.rect = self.image.get_rect()

class KeysBtn(ButtonText):
    def __init__(self, screen):
        super().__init__(screen)
        self.low = KeysBtn_low
        self.high = KeysBtn_high
        self.x = WIDTH//16
        self.y = HEIGHT//16 + 200
        self.image = self.low
        self.rect = self.image.get_rect()

class HowToPlayBtn(ButtonText):
    def __init__(self, screen):
        super().__init__(screen)
        self.low = HowToPlayBtn_low
        self.high = HowToPlayBtn_high
        self.x = WIDTH//16
        self.y = HEIGHT//16 + 250
        self.image = self.low
        self.rect = self.image.get_rect()

class ExitBtn(ButtonText):
    def __init__(self, screen):
        super().__init__(screen)
        self.low = ExitBtn_low
        self.high = ExitBtn_high
        self.x = WIDTH//16
        self.y = HEIGHT//16 + 300
        self.image = self.low
        self.rect = self.image.get_rect()

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.dimScreen = pygame.Surface(screen.get_size()).convert_alpha()
        self.dimScreen.fill((0, 0, 0, 90))
        self.buttons = [ContinueBtn(self.screen), NewGameBtn(self.screen), KeysBtn(self.screen), HowToPlayBtn(self.screen), ExitBtn(self.screen)]
        # self.menuFunctions = [self.Continue(), self.NewGame(), self.KeyBinding(), self.HowToPlay(), self.Exit()]

    def draw(self):
        self.screen.blit(self.dimScreen, (0, 0))
        self.screen.blit(menuBG, (WIDTH//16 - 50, HEIGHT//16+80))
        # menuTitle = ButtonText(100, self.x, self.y, "MAIN MENU", self.screen, 100)
        # menuTitle.draw()
        for btn in self.buttons: btn.draw()
