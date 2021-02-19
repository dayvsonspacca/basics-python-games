from classes import Wall, Player
import pygame
from pygame.locals import *
from os import getcwd

def main():
    
    display = createDisplay()
    _map = createMap()
    player = createPlayer()
    key = 'STAY'
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                key = event.key
        clock.tick(7)
        player = movePlayer(player, key, _map)
        pygame.display.update()
    
    
    
def createDisplay()-> pygame.Surface:
    
    pygame.init()
    pygame.display.init()
    display = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('mapwalkv2')
    
    return display


def createMap()-> list:
    currentFolder = getcwd()
    _map = open(f'{currentFolder}\map1.txt', 'r')
    mapStructure = []
    for line in _map:
        wallData = lineData(line)
        newWall = Wall(wallData[0], wallData[1], wallData[2], wallData[3], wallData[4], wallData[5])
        mapStructure.append(newWall)
    drawMap(mapStructure)
    return mapStructure
def drawMap(mapStructure):
    
    display = pygame.display.get_surface()
    for wall in mapStructure:
        pygame.draw.rect(display, wall.color, ((wall.posX, wall.posY), (Wall.wallSize, Wall.wallSize)))

def createPlayer()-> Player:
    display = pygame.display.get_surface()
    displayWidth:int = display.get_width()
    displayHeight:int = display.get_height()
    posX:int = Wall.wallSize
    posY:int = displayHeight-Wall.wallSize*2
    numberOfWalls = int(displayWidth/Wall.wallSize * displayHeight/Wall.wallSize)
    index = numberOfWalls - (int(displayWidth/Wall.wallSize)*2)+1
    player = Player(posX, posY, index)
    return player

def movePlayer(player:Player, key, _map:list)->Player:
    
    display = pygame.display.get_surface()
    displayWidth = display.get_width()
    wallsPerWidth = int(displayWidth/Wall.wallSize)
    direction = 'STAY'    
    
    if key == K_RIGHT and _map[player.index+1].walkable == True:
        player.index += 1
        pygame.draw.rect(display, (255, 255, 255), ((player.posX, player.posY),
                                                    (Wall.wallSize, Wall.wallSize)))
        player.posX += Wall.wallSize
    elif key == K_LEFT and _map[player.index-1].walkable == True:
        player.index -=1
        pygame.draw.rect(display, (255, 255, 255), ((player.posX, player.posY),
                                                    (Wall.wallSize, Wall.wallSize)))
        player.posX -= Wall.wallSize
    elif key == K_DOWN and _map[player.index+wallsPerWidth].walkable == True:
        player.index += wallsPerWidth
        pygame.draw.rect(display, (255, 255, 255), ((player.posX, player.posY),
                                                    (Wall.wallSize, Wall.wallSize)))
        player.posY += Wall.wallSize
    elif key == K_UP and _map[player.index-wallsPerWidth].walkable == True:
        player.index -= wallsPerWidth
        pygame.draw.rect(display, (255, 255, 255), ((player.posX, player.posY),
                                                    (Wall.wallSize, Wall.wallSize)))
        player.posY -= Wall.wallSize
        
    pygame.draw.rect(display, Player.color, ((player.posX, player.posY),
                                             (Wall.wallSize, Wall.wallSize)))
    checkWin(player.index, _map)
    return player


def checkWin(index:int, _map:list):
    winWalls = 0
    for wall in _map:
        if wall.win:
            winWalls+=1
    if _map[index].win == True:
        _map[index].win = False
        _map[index].color = (255, 255, 255)

    if winWalls == 0:
        pygame.display.quit()
        pygame.quit()
        print('Paraben vc ganhou :)')
        exit_ = str(input('Press ENTER for exit.'))
        exit()
    
    
    
def lineData(line:str)-> list:

    wallData = []
    for data in range(6):
        index = line.find('-')
        value = line[:index]
        line = line[index+1:]
        wallData.append(value)
    wallData = [int(wallData[0]), int(wallData[1]), eval(wallData[2].capitalize()),
                       eval(wallData[3].capitalize()), eval(wallData[4].capitalize()),
                       eval(wallData[5])]
    return wallData
if __name__ == "__main__":
    main()