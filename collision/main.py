import pygame
from pygame.locals import *
from block import Block, Pixel
from random import randint, choice

def main():
    width = 500
    heigth = 500
    blockSize = 5
    sizes = width, heigth
    display = createDisplay(sizes)
    clock = pygame.time.Clock()
    allPixels = createPixelsStructure(width, heigth, blockSize)
    allBlocks = createBlocksStructure(display, width, heigth, blockSize, allPixels)

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        moveBlocks(display, allBlocks, width, heigth, allPixels)
        drawBlocks(display, allBlocks)
        clock.tick(20)
        pygame.display.update()



def createDisplay(sizes):
    display = pygame.display.set_mode(sizes)
    pygame.display.set_caption('Collision')
    display.fill((255, 255, 255))
    return display

def createBlocksStructure(display, width, heigth, blockSize, allPixels):
    numberOfBlocks = 1000#int((width + heigth) / 2)
    numberOfPixels = int((width / blockSize) * (heigth / blockSize))
    allBlocks = []
    for block in range(numberOfBlocks):
        pixelChoiced = randint(0, numberOfPixels)
        #see pixelChoiced coords
        #print(f'positionX = {allPixels[pixelChoiced].positionX} positionY = {allPixels[pixelChoiced].positionY}')
        color = (randint(0,255), randint(0, 255) ,randint(0, 255))
        newBlock = Block(allPixels[pixelChoiced].positionX, allPixels[pixelChoiced].positionY, choice(('RIGHT', 'LEFT')), choice(('UP', 'DOWN')), color, blockSize, block)
        allBlocks.append(newBlock)
    return allBlocks

def createPixelsStructure(width, heigth, blockSize):
    numberOfPixels = int((width/blockSize) * (heigth / blockSize))
    positionX = positionY = 0
    allPixels = []
    for pixel in range(numberOfPixels):
        if positionX == width:
            positionX = 0
            positionY += blockSize
        walkable = True
        newPixel = Pixel(pixel, walkable, positionX, positionY)
        positionX += blockSize
        allPixels.append(newPixel)

    return allPixels

def moveBlocks(display, allBlocks, width, heigth, allPixels):
    for block in allBlocks:
        #see blocks coords and directions \/
        #print(f'positonX = {block.positionX} postionY = {block.positionY} xDirection = {block.xDirection} yDiretion = {block.yDirection}')
        if block.xDirection == 'RIGHT' and allPixels[block.index].walkable == True:
            block.positionX += block.speed
            if block.positionX == width - block.size[0]:
                block.xDirection = 'LEFT'
            if block.yDirection == 'UP':
                block.positionY -= block.speed
                if block.positionY == 0:
                    block.yDirection = 'DOWN'
            else:
                block.positionY += block.speed   
                if block.positionY == heigth - block.size[1]:
                    block.yDirection = 'UP'        
        else:
            block.positionX -= block.speed
            if block.positionX == 0:
                block.xDirection = 'RIGHT'
            if block.yDirection == 'UP':
                block.positionY -= block.speed
                if block.positionY == 0:
                    block.yDirection = 'DOWN'
            else:
                block.positionY += block.speed    
                if block.positionY == heigth - block.size[1]:
                    block.yDirection = 'UP'

def drawBlocks(display, allBlocks):
    display.fill((255, 255, 255))
    for block in allBlocks:
        pygame.draw.rect(display, (block.color),((block.positionX, block.positionY),(block.size)))
main()
