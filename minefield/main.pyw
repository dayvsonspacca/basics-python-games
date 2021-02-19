import pygame
from pygame.locals import *
from models import Cell
import random


def main():
    pygame.init()
    display = createDisplay((1000, 1000))
    cellStructure = createCellStructure()
    updateCellsValues(cellStructure)
    showCells(cellStructure)
    playing = True
    win = False
    while playing:
        if win:
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousePos = event.pos
                cellClickled = cellClickledIndex(mousePos, cellStructure)
                if cellClickled != None:
                    playing = cellStructure[cellClickled].showValue()
        pygame.display.update()
    if not playing:
        main()


def createCellStructure() -> list:
    """
    return: A linear array that contains the cells informations.
    """

    display = pygame.display.get_surface()
    width = display.get_width()
    height = display.get_height()
    numberOfCells = int((width/Cell.size) * (height/Cell.size))
    posX = posY = 0
    cellStructure = []
    options = [i for i in range(numberOfCells)]
    numberOfBombs = 20
    for cell in range(numberOfCells):
        hasBomb = False
        newCell = Cell(posX, posY, hasBomb)
        posX += Cell.size
        if posX == width:
            posX = 0
            posY += Cell.size
        cellStructure.append(newCell)

    for bomb in range(numberOfBombs):
        index = random.choice(options)
        cellStructure[index].hasBomb = True
        options.remove(index)

    return cellStructure


def showCells(cellStructure: list):
    for cell in cellStructure:
        cell.showCell()


def cellClickledIndex(mousePos: tuple, cellStructure: list) -> int:
    """
    mousePos: A tuple thats represents the mouse pos in screen.
    createCellStructure: A linear array thats represents the cells informations.
    return: The clickled cell index in cellStructure
    """
    for cell in cellStructure:
        if mousePos[0] > cell.posX and mousePos[0] < cell.posX+Cell.size and mousePos[1] > cell.posY and mousePos[1] < cell.posY+Cell.size:
            return cellStructure.index(cell)


def updateCellsValues(cellStructure: list):
    """
    Finish the cells informations.
    cellStructure: A linear array to be updated.
    """
    for cell in cellStructure:
        cell.calcCellFriends(cellStructure)
        cell.updateValue(cellStructure)


def createDisplay(sizes: tuple) -> pygame.Surface:
    """
    return? An instace of Surface object.
    sizes: A tuple with the sizes of window,
    """
    pygame.display.init()
    display = pygame.display.set_mode(sizes)
    pygame.display.set_caption("Minefield")
    return display


if __name__ == "__main__":
    main()
