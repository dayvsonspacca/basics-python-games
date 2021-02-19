from classes import Wall, Player
import pygame
from pygame.locals import *
from  os import getcwd

def main():
    
    display = createDisplay()
    wallStructure:list = createWallStructure()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                saveMap(wallStructure)
                exit()
        wallStructure:list = updateWalls(wallStructure)
        pygame.display.update()

def createDisplay() -> pygame.Surface:
    
    pygame.init()
    pygame.display.init()
    display = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('create map mode')
    return display

def createWall(posX:int, posY:int, walkable:bool=True, color:tuple=(255 ,255 ,255), constant=False)-> Wall:
    wall = Wall(posX, posY, walkable, color, constant, False)
    return wall

def createWallStructure()-> list:
    
    wallStructure = []
    posX = posY = 0
    display = pygame.display.get_surface()
    displayWidth:int = display.get_width()
    displayHeight:int = display.get_height()
    numberOfWalls:int = int(displayWidth/Wall.wallSize * displayHeight/Wall.wallSize)
    for wall in range(numberOfWalls):
        if posX == 0 or posY == 0 or posX == displayWidth-Wall.wallSize or posY == displayHeight-Wall.wallSize:
            newWall = createWall(posX, posY, False, (0, 0, 0), True)
        elif posX == Wall.wallSize and posY == displayHeight-Wall.wallSize*2:
            newWall = createWall(posX, posY, True, Player.color, True)
        else:
            newWall = createWall(posX, posY)
        posX += Wall.wallSize
        if posX == displayWidth:
            posX = 0 
            posY += Wall.wallSize
        wallStructure.append(newWall)
    return wallStructure

def updateWalls(wallStructure:list) -> list:
    
    mousePos:tuple = pygame.mouse.get_pos()
    mousePressed:tuple = pygame.mouse.get_pressed()
    for wall in wallStructure:
        wall.checkCollision(mousePos, mousePressed)
        drawWall(wall)
    return wallStructure

def drawWall(wall:Wall):
    
    display = pygame.display.get_surface()
    pygame.draw.rect(display, wall.color, ((wall.posX, wall.posY), (Wall.wallSize, Wall.wallSize)))

def saveMap(wallStructure:list):
    currentFolder = getcwd()
    _map = open(f'{currentFolder}\map1.txt', 'w')
    for wall in wallStructure:
        _map.writelines(f'{wall.posX}-{wall.posY}-{wall.walkable}-{wall.color}-{wall.constant}-{wall.win}\n')
        
    
    _map.close()
if __name__ == "__main__":
    main()