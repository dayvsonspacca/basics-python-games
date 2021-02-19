
class Drop(object):
    
    def __init__(self, speed:int , positionX:int, positionY:int, lenght:int):
        self.speed:int = speed
        self.positionX:int = positionX
        self.positionY:int = positionY
        self.lenght:int = lenght
        self.acceleration:float = 0

    def fall(self) -> None:
        self.acceleration += 0.2
        self.positionY += self.speed + self.acceleration

    def isOutOfWindow(self, height: int) -> None:
        if self.positionY >= height:
            self.acceleration = 0
            self.positionY = -20

        
