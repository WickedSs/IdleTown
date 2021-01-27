from __future__ import division

import pygame
from pygame.locals import *
import sys, os, random
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from PIL import Image
from Objects import *
from Helpers import *
from Player import *
from Elements import *

pygame.font.init()
pygame.init()


### Building logic
Buildings = [file for file in os.listdir('./Resources/Buildings') if os.path.isfile("./Resources/Buildings/"+file)]
isBuilding = False
currentBuildingObject = None
currentBuildingPosition = None
placedObjects = {}
###

### UI logic
pause = False
playing = True
option = False
newGame = False
video = False
keyBinding = False
clickedBtns = [[9],[]]
noHover = []
MenuItems = []
###

### Game logic
resolutionChanged = []
all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
###





### Components


# def Sprite(sprite, spriteType, id, x, y):
#     image = pygame.image.load("./Resources/Sprites/"+sprite+".png")
#     hover = pygame.image.load("./Resources/Sprites/Hover.png")
#     points = None
#     size = getImageSize("Sprites/"+sprite)
#     rect = pygame.Rect(x, y, size[0], size[1])
#     mouseX, mouseY = pygame.mouse.get_pos()
#     mousePos = Point(mouseX, mouseY)
#     points = (x+32, y), (x-(TILESIZE/2)+32, y+(TILESIZE/4)), (x+32, y+TILESIZE/2), (x+(TILESIZE/2)+32, y+(TILESIZE/4))
#     poly = Polygon(points)
#     screen.blit(image, (x, y))
#
#     if not pause and not isBuilding:
#         if (poly.contains(mousePos)):
#             screen.blit(hover, (x, y))
#
#     return points

# def Slot(bid, x, y, buildingResized, building):
#     global placed, isBuilding, currentBuildingObject
#     animate = 0
#     slot = pygame.image.load("./Resources/UI/Slot/slot.png")
#     hovered = pygame.image.load("./Resources/UI/Slot/select-Slot.png")
#     size = getImageSize("UI/Slot/slot")
#     if (len(resolutionChanged) and resolutionChanged[0]):
#         size = newComponentSize(size, resolutionChanged[1], resolutionChanged[2])
#     rect = pygame.Rect(x, y, size[0], size[1])
#     mousePos = pygame.mouse.get_pos()
#     if not pause:
#         if (rect.collidepoint(mousePos)):
#             screen.blit(hovered, (x, y))
#             if buildingResized: screen.blit(buildingResized, (x+8, y+8))
#             for event in pygame.event.get():
#                 if event.type == MOUSEBUTTONDOWN and event.button == 1:
#                     isBuilding = True
#                     currentBuildingObject = building
#         else:
#             screen.blit(slot, (x, y))
#             if buildingResized: screen.blit(buildingResized, (x+8, y+8))
#
#     return spriteWidth, spriteHeight
#
# def Building(building, place, time=0.1):
#     global currentBuildingPosition
#     if building != None and not pause:
#         image = pygame.image.load('./Resources/Buildings/Building01.png')
#         size = getImageSize("Buildings/Building01")
#         mosx = 0
#         mosy = 0
#         x, y = pygame.mouse.get_pos()
#         dx, dy = (x - x), (y - y)
#         x, y = x + dx * time, y + dy * time
#         w, h = image.get_size()
#         x = ((round(x/32))*32)
#         y = ((round(y/16))*16)
#         if (screen.get_width() == 1920):
#             y = y - 2
#         currentBuildingPosition = (x - w/2, y - h/2 - h/4)
#         # print screen.get_width(), screen.get_height(), currentBuildingPosition
#         screen.blit(image, (x - w/2, y - h/2 - h/4))
# ### end of Components


### Game intializeing
# def drawEmptyChunks():
#     for i in range(len(self.chunks)):
#         current = self.chunks[i]
#         pts = current["points"]
#         right = pts[0] + (10 * 32), pts[1] + (5 * 16)
#         left = pts[0] - (10 * 32), pts[1] + (5 * 16)
#         up = pts[0], pts[1] - (5 * 16)
#         bottom = pts[0], pts[1] + (15 * 16)
#         pygame.draw.circle(self.screen, RED, (right), 5)
#         pygame.draw.circle(self.screen, RED, (left), 5)
#         pygame.draw.circle(self.screen, RED, (up), 5)
#         pygame.draw.circle(self.screen, RED, (bottom), 5)
#
# def addSpriteToList(key, id, points, spriteType):
#     spritesPositions[key] = {
#         "id" : key,
#         "points" : points,
#         "spriteType" : spriteType,
#     }
#
# def HugeIsometricSquare(screen):
#     global placedObjects, resolutionChanged, all_sprites, tiles, isBuilding, pause
#     count, i, j = 1, screen.get_width()/2, screen.get_height()/4
#     rows = 1
#     key = 0
#     for row in range(10):
#         i, j = incrementPositionSprite(i, j, "break", row, screen.get_width(), screen.get_height())
#         for count in range(10):
#             sprite = Sprite(i, j, isBuilding)
#             tiles.add(sprite)
#             all_sprites.add(sprite)
#             i, j = incrementPositionSprite(i, j, "continue", count, screen.get_width(), screen.get_height())
#
#     if (len(resolutionChanged) and resolutionChanged[0]):
#         updateObjectPosition(resolutionChanged[1], resolutionChanged[2])
#
#     for index in range(len(placedObjects)):
#         current = placedObjects[index]
#         gameObject = pygame.image.load("./Resources/Buildings/"+current["name"])
#         screen.blit(gameObject, (current["position"][0], current["position"][1]))
#
#     resolutionChanged = []
#
# def handleEvents():
#     global all_sprites, MenuItems, pause, option, newGame, Playing, OptionItems, keyBinding, video, currentBuildingObject, isPlaced, isBuilding, currentBuildingPosition, noHover, clickedBtns
#     clicked = False
#     all_sprites.update()
#     # all_sprites.draw(screen)
#     mousePos = pygame.mouse.get_pos()
#     clock.tick()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == KEYUP:
#             if event.key == K_ESCAPE:
#                 pause = not pause
#                 if (not pause):
#                     noHover = []
#                     option = False
#                     video = False
#                     clickedBtns[1] = []
#             if event.key == K_e:
#                 pass
#             if event.key == K_p:
#                 pass
#         elif event.type == MOUSEBUTTONDOWN and event.button == 1:
#             clicked = True
#     if isBuilding:
#         Building(currentBuildingObject, False)
#         if (clicked):
#             addPlacedObject(currentBuildingObject, currentBuildingPosition)
#             isBuilding = False
#             currentBuildingObject = None
#             currentBuildingPosition = None
#             clicked = False
#     pygame.display.update()
#
# def MainMenu(x, y):
#     global pause, Playing, spritesPositions, MenuItems
#     count, offsetx, offsety = 0, 0, 0
#     x += 25
#     ButtonText(100, screen.get_width()//16, screen.get_height()//16, "MAIN MENU", getFontSize()[0])
#     while (count < len(initWords)):
#         x, y = x - 5, y + offsety
#         nextRect = ButtonText(count, x, y, initWords[count], getFontSize()[1])
#         offsety = nextRect[3] + 10
#         offsetx = nextRect[2] / 24
#         count += 1
#
# def OptionMenu(x, y):
#     global pause, Playing, spritesPositions, MenuItems
#     count, offsetx, offsety = len(MenuItems), 0, 0
#     x += 25
#     y -= 5
#     maxLength = len(OptionsWords) + len(initWords)
#     while (count < maxLength):
#         x, y = x - 5, y + offsety
#         newRect = ButtonText(count, x, y, OptionsWords[count - len(initWords)], getFontSize()[1])
#         offsety = newRect[3] + 10
#         offsetx = newRect[2] / 24
#         count += 1
#
# def videoMenu(x, y):
#     global pause, Playing, MenuItems
#     count, offsetx, offsety = len(MenuItems), 0, 0
#     constant = count
#     x += 25
#     y += 3
#     maxLength = len(OptionsWords) + len(initWords) + len(VideoWords)
#     while (count < maxLength):
#         x, y = x - 5, y + offsety
#         newRect = ButtonText(count, x, y, VideoWords[count - constant], getFontSize()[1])
#         offsety = newRect[3] + 10
#         offsetx = newRect[2] / 24
#         count += 1
#
# def Inventory():
#     count, i, j = 0, screen.get_width() * 0.25, screen.get_height() * 0.9
#     buildingNormal, buildingResized = None, None
#     while (count < 10):
#         try:
#             buildingNormal = Buildings[count]
#             buildingResized = resizeimageForSlot(buildingNormal)
#         except:
#             building = None
#         slWidth, slHeigth = Slot(count, i, j, buildingResized, buildingNormal)
#         i = incrementPositionSlot(i)
#         count += 1
#
# def draw():
#     global pause, Playing, spritesPositions, MenuItems, size
#     screen.fill(BGCOLOR)
#     HugeIsometricSquare()
#     Inventory()
#     MenuItems = []
#     if (pause):
#         for i in range(len(initWords)): MenuItems.append([i, False])
#         size = pygame.display.get_surface().get_size()
#         uiPanel = pygame.Surface([size[0],size[1]], pygame.SRCALPHA, 32)
#         uiPanel = uiPanel.convert_alpha()
#         uiPanel.fill((0, 0, 0, 180))
#         screen.blit(uiPanel, (0, 0))
#         MainMenu(size[0]/24, size[1]/4)
#         if (option):
#             OptionMenu(size[0]/6, size[1]/3)
#             length = len(OptionsWords) + len(initWords)
#             for i in range(len(MenuItems), length, 1): MenuItems.append([i, False])
#             if (video):
#                 videoMenu(size[0]/3.2, size[1]/2.5)
#                 length = len(OptionsWords) + len(initWords) + len(VideoWords)
#                 for i in range(len(MenuItems), length, 1): MenuItems.append([i, False])

class Game:
    def __init__(self):
        self.player = Player()
        self.availableSaves = self.player.load_data()
        self.width = 1360
        self.height = 768
        self.screen = pygame.display.set_mode((1360, 768))
        pygame.display.set_caption("Idle Town")
        self.enemys = []
        self.build_inMap = []
        self.cameraScroll = [0, 0]
        self.selected_object = None
        self.landObjects = []
        self.buildingObjects = []
        self.resourcesObjects = []
        self.chunkLands = []
        self.menuButtons = []
        self.startMenu = True
        self.playing = False
        self.pause = False
        self.howToPlay = False
        self.conGame = False
        self.newGame = False

    def menuEvents(self):
        mousePos = pygame.mouse.get_pos()
        ## check for pressed keys && mouse buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pause = not pause
                    if (not pause):
                        noHover = []
                        option = False
                        video = False
                        clickedBtns[1] = []
                if event.key == K_p:
                    pass
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicked = True

    def gameEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.cameraScroll[0] += 32
        if keys[pygame.K_a]:
            self.cameraScroll[0] -= 32

    # def mainMenu(self, x, y):
    #     self.menuButtons = []
    #     x += 25
    #     menuTitle = ButtonText(100, x, y, "MAIN MENU", self.screen, 100)
    #     menuTitle.draw()
    #     y += 100
    #     count = 0
    #     for word in self.initWords:
    #         x, y = x - 5, y + 60
    #         button = ButtonText(count, x, y, word, self.screen, 60, self.menuFunctions[count])
    #         self.menuButtons.append(button)
    #         count += 1

    def mapGen(self):
        self.landObjects = []
        self.chunkLands = []
        i, j = WIDTH/2, HEIGHT/8
        chunk = Chunk(len(self.chunkLands), [], i, j, self.screen)
        for row in range(1, 20, 1):
            i, j = incrementPositionSprite(i, j, "break", row)
            for count in range(1, 20, 1):
                sprite = Sprite(i+self.cameraScroll[0], j+self.cameraScroll[1], self.screen, "Grass", "grass")
                self.landObjects.append(sprite)
                i, j = incrementPositionSprite(i, j, "continue", count)

        chunk.updateSprites(self.landObjects)
        self.chunkLands.append(chunk)

    def Continue(self):
        self.pause = False
        self.startMenu = False
        for chunk in self.chunkLands:
            chunk.draw()

    def NewGame(self):
        self.pause = False
        self.startMenu = False
        self.landObjects = []
        self.chunkLands = []
        i, j = WIDTH/2, HEIGHT/8
        chunk = Chunk(len(self.chunkLands), [], i, j, self.screen)
        for row in range(1, 20, 1):
            i, j = incrementPositionSprite(i, j, "break", row)
            for count in range(1, 20, 1):
                sprite = Sprite(i+self.cameraScroll[0], j+self.cameraScroll[1], self.screen, "Grass", "grass")
                self.landObjects.append(sprite)
                i, j = incrementPositionSprite(i, j, "continue", count)

        chunk.updateSprites(self.landObjects)
        self.chunkLands.append(chunk)
        chunk.draw()

    def KeyBinding(self): self.keyBindings = True

    def HowToPlay(self): self.howToPlay = True

    def Exit(self):
        # pygame.quit()
        # sys.exit()
        pass

    def run(self):
        # btn = self.mainMenu(WIDTH//16, HEIGHT//16)
        clock.tick(60)
        while True:
            self.screen.fill((126,200,80))
            if not self.pause and not self.startMenu:
                self.gameEvents()
            self.menuEvents()
            if (self.startMenu):
                self.mapGen()
                for chunk in self.chunkLands: chunk.draw()
                main = MainMenu(self.screen)
                main.draw()

            pygame.display.update()






if __name__ == "__main__":
    game = Game()
    game.run()
