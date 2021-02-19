import pygame
from pygame.locals import *
from firepixel import Firepixel
from random import randint, choice
def main():
    # ORIGINAL PALLETE
    colorPallete =[(7, 7, 7), (31, 7, 7), (47, 15, 7), (71, 15, 7), (87, 23,  7), (103, 31,  7), (119, 31,  7),(143, 39,  7),
          (159, 47, 7), (175, 63, 7), (191, 71, 7), (199, 71, 7), (223, 79,  7), (223, 87,  7), (223, 87,  7), (215, 95,  7),
          (215, 95, 7), (215,103, 15), (207,111, 15), (207,119, 15), (207,127, 15), (207,135, 23), (199,135, 23), (199,143, 23),
          (199,151, 31), (191,159, 31), (191,159, 31), (191,167, 39), (191,167, 39), (191,175, 47), (183,175, 47), (183,183, 47),
         (183,183, 55), (207,207,111), (223,223,159), (239,239,199), (255,255,255)]
    """
    PERSONAL PALLETE
    colorPallete = [(0, 0, 0)]
    for color in range(36):
        colorPallete.append((0+color*4, 0+color*4, 0+color*4))
    """
    fireWidth = fireHeigth = 40
    sizes = fireWidth, fireHeigth
    display = createDisplay(sizes)
    canvas = createCanvas(display, colorPallete, sizes)
    clock = pygame.time.Clock()
    while True:
        updateCanvas(canvas, display, colorPallete, sizes)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        clock.tick(2000)
def createDisplay(sizes):
    pygame.init()
    display = pygame.display.set_mode((sizes[0]*10, sizes[1]*10))
    pygame.display.set_caption('doomfirev2')
    return display
def createCanvas(display, colorPallete, sizes):
    canvas = []
    numberofPixels = int((sizes[0]*10/5)*(sizes[0]*10/5))
    x = y = power = 0
    for pixel in range(numberofPixels):
        if pixel >= numberofPixels - sizes[0]*2:
            power = 36
        color = colorPallete[power]
        newPixel = Firepixel(x, y, color, pixel, power)
        x += 5
        if x == sizes[0]*10:
            y+= 5
            x = 0
        canvas.append(newPixel)
    return canvas
def updateCanvas(canvas, display, colorPallete, sizes):  
    numberofPixels = int((sizes[0]*10/5)*(sizes[0]*10/5)) 
    for pixel in canvas:
        if pixel.pos <= numberofPixels - (sizes[0]*2+1):
            decay = 1
            pixelBelow = int(sizes[0]*10/5)
            newPower = choice((canvas[pixel.pos+pixelBelow - decay].power - decay, canvas[pixel.pos+pixelBelow].power - 1, pixel.power-decay, pixel.power))
            if newPower < 0 or  newPower > 36:
                pixel.power = 0
            else:
                pixel.power = newPower
            pixel.color = colorPallete[pixel.power]  
    for pixel in canvas:
        pygame.draw.rect(display, pixel.color,((pixel.x, pixel.y), (5, 5))) 
    pygame.display.update()
main()