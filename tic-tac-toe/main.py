import pygame
from pygame.locals import *
from models import Cell


def main():
    pygame.init()
    display = createDisplay((600, 600), "tic tac toe")
    cellStructure = createCellStructure()
    turn = "X"
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mousePos = event.pos
                turn = choice(cellStructure, mousePos,  turn)
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    pygame.quit()
                    main()
        pygame.display.update()


def createCellStructure() -> list:
    """
    return: A list thats contains the cells of game.
    """
    display = pygame.display.get_surface()
    width = display.get_width()
    height = display.get_height()
    cellStructure = []
    posX = posY = 0
    for cell in range(9):
        newCell = Cell(posX, posY)
        posX += Cell.size
        if posX == width:
            posX = 0
            posY += Cell.size
        cellStructure.append(newCell)
    lines = [[[int(width/3), 0], [int(width/3), height]],
             [[int(width/3)*2, 0], [int(width/3)*2, height]],
             [[0, int(height/3)], [width, int(height/3)]],
             [[0, int(height/3)*2], [width, int(height/3)*2]]]
    for line in lines:
        pygame.draw.line(display, (255, 255, 255), line[0], line[1], 1)
    return cellStructure


def choice(cellStructure: list, mousePos: tuple, turn: str) -> str:
    """
    cellStructure: A list thats contains the cells of the game.
    mousePos: A tuple thats contains where the play clickled.
    """

    for cell in cellStructure:
        if mousePos[0] > cell.x and mousePos[1] > cell.y and mousePos[0] < cell.x+Cell.size and mousePos[1] < cell.y+Cell.size and not cell.reveal:
            if turn == "X":
                cell.value = turn
                color = (0, 255, 0)
                turn = "O"
            else:
                color = (255, 0, 0)
                cell.value = turn
                turn = "X"
            cell.mark(color)
            break

    return turn


def createDisplay(sizes: tuple, caption: str) -> pygame.Surface:
    """
    sizes: A tuple thats contains the width and the height of display.
    caption: A string with the label of display.
    return: An instance of Surface.
    """
    pygame.display.init()
    display = pygame.display.set_mode(sizes)
    pygame.display.set_caption(caption)
    return display


if __name__ == "__main__":
    main()
