class Block(object):
    def __init__(self, positionX, positionY, xDirection, yDirection, color, blockSize, index):
        self.positionX = positionX
        self.positionY = positionY
        self.xDirection = xDirection
        self.yDirection = yDirection
        self.size = (blockSize, blockSize)
        self.color = color
        self.speed = blockSize
        self.index = index

class Pixel(object):
    def __init__(self, index, walkable, positionX, positionY):
        self.index = index
        self.walkable = walkable
        self.positionX = positionX
        self.positionY = positionY