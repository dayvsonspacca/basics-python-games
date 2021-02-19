import pygame
from pygame.locals import *
from drop import Drop
from random import randint


def main(): 

    pygame.init()
    display = createDisplay()
    clock = pygame.time.Clock()
    rain = createRain()

    while True:
        rain = updateRain(rain)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
        clock.tick(30)
        pygame.display.update()


def createDisplay() -> pygame.Surface:

    width:int = 600
    height:int = 300
    pygame.display.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('rainsimulatorv2')

    return display 


def createDrop() -> Drop:

    display = pygame.display.get_surface()
    speed:int = randint(5, 8)
    lenght:int = randint(10, 20)
    positionX:int = randint(0, display.get_width())
    positionY:int = randint(0, display.get_height())
    drop = Drop(speed, positionX, positionY, lenght)

    return drop


def createRain() -> list:
    
    rain:list = []
    numberOfDrops:int = 400
    for drop in range(numberOfDrops):
        newDrop = createDrop()
        rain.append(newDrop)

    return rain


def drawRain(rain:list) -> None:
    
    display = pygame.display.get_surface()
    display.fill((230, 230, 150))
    dropColor:tuple = (138, 43, 226)
    for drop in rain:
        pygame.draw.line(display, dropColor, (drop.positionX, drop.positionY),
         (drop.positionX, drop.positionY + drop.lenght))


def updateRain(rain:list) -> list:

    display = pygame.display.get_surface()
    height = display.get_height()

    for drop in rain:
        drop.isOutOfWindow(height)
        drop.fall()

    drawRain(rain)

    return rain


if __name__ == '__main__':
    main()
