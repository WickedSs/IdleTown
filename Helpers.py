import pygame
from PIL import Image
from Settings import *

def updateObjectPosition(objectsList, oldScreen, newScreen):
    x, y = (0, 0)
    for index in range(len(objectsList)):
        currentPosition = objectsList[index]['position']
        if newScreen[0] > oldScreen[0]:
            x = currentPosition[0] + (newScreen[0] - oldScreen[0]) / 2
            y = currentPosition[1] + (newScreen[1] - oldScreen[1]) / 4
        else:
            x = currentPosition[0] - (oldScreen[0] - newScreen[0]) / 2
            y = currentPosition[1] - (oldScreen[1] - newScreen[1]) / 4
        objectsList[index]['position'] = (x, y)

    return objectsList


def addPlacedObject(array, objectName, position):
    currentID = len(array)
    array[currentID] = {'name': objectName, 'position': position}


def newComponentSize(size, oldScreen, newScreen):
    scale_x, scale_y = newScreen[0] / oldScreen[0], newScreen[1] / oldScreen[1]
    newWidth, newHeight = size[0] * scale_x, size[1] * scale_y
    return (newWidth, newHeight)


def deactivateButton(hoverList, start, end):
    for index in range(start, start + end, 1):
        hoverList.append(index)

    return hoverList


def getImageSize(image):
    image = Image.open('./Resources/' + image + '.png')
    return image.size


def incrementPositionSlot(i, width):
    range = width * 0.75 - width * 0.25
    toAdd = range / 10 - TILESIZE
    i += TILESIZE + toAdd
    return i


def incrementPositionSprite(i, j, posType, row):
    if posType == 'continue':
        i -= TILESIZE / 2
        j += TILESIZE / 4
    else:
        i = (WIDTH / 2.2) + ((TILESIZE / 2) * row)
        j = (HEIGHT / 12) + ((TILESIZE / 4) * row)
    return (i, j)


def fill_woutline(surface, border):
    surface.fill(WHITE)
    surface.fill((0, 0, 0, 210), surface.get_rect().inflate(-border, -border))


def getFontSize(width, height):
    titleSize = width / 12
    buttonSize = height / 14
    return (
     titleSize, buttonSize)


def resizeimageForSlot(image=None):
    if image != None:
        img = Image.open('./Resources/Buildings/' + image)
        img.thumbnail((48, 48))
        img.save('./Resources/Buildings/Resized/' + image)
        return pygame.image.load('./Resources/Buildings/Resized/' + image)
    else:
        return
