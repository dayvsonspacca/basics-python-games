

class Wall:
    
    wallSize = 10
    
    def __init__(self, posX:int, posY:int, walkable:bool, color:tuple, constant:bool, win:bool):
        
        self.posX = posX
        self.posY = posY
        self.walkable = walkable
        self.color = color
        self.constant = constant
        self.win = win
        
    def checkCollision(self, mousePos:tuple, mousePressed:tuple):

        posXrange = range(self.posX, self.posX+Wall.wallSize)
        posYrange = range(self.posY, self.posY+Wall.wallSize)
        if mousePos[0] in posXrange and mousePos[1] in posYrange and mousePressed[0] == 1 and not self.constant:
            #print(f'wallx = {self.posX}, wally = {self.posY}, mousepos = {mousePos}')
            self.color = (0, 0, 0)
            self.walkable = False
        elif mousePos[0] in posXrange and mousePos[1] in posYrange and mousePressed[2] == 1 and not self.constant:
            self.color = (255, 255, 255)
            self.walkable = True
        elif mousePos[0] in posXrange and mousePos[1] in posYrange and mousePressed[1] == 1 and not self.constant:
            self.color = (0, 255, 0)
            self.win = True
            self.walkable = True
            
            
class Player:
    color = (255, 0, 0)
    
    def __init__(self, posX, posY, index):
        self.posX = posX
        self.posY = posY
        self.index = index
        