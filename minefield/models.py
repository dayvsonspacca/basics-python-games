import pygame


class Cell:

    size = 50
    borderColor = (16, 16, 16)

    def __init__(self, posX: int, posY: int, hasBomb: bool):
        """
        Create an instance of cell.
        posX: An integer represetation of axis X.
        posY: An integer represetation of axis Y.
        hasBomb: A bool thats represents if the cell has bomb or not.
        """
        self.posX = posX
        self.posY = posY
        self.hasBomb = hasBomb
        self.color = (33, 33, 33)
        self.value = 0
        self.clicked = False
        self.friends = []
        self.numberOfFriends = 0

    def showCell(self):
        """
        Draw cell in screen.
        """
        if not self.clicked:
            display = pygame.display.get_surface()
            pygame.draw.rect(display, Cell.borderColor,  ((self.posX, self.posY),
                                                          (Cell.size, Cell.size)))
            pygame.draw.rect(display, self.color, ((self.posX+2, self.posY+2),
                                                   (Cell.size-4, Cell.size-4)))

    def showValue(self) -> bool:
        """
        Show the true value of cell.
        return: A bool thats represents if the player hit the bomb cell.
        """
        if self.hasBomb:
            return False
        font = pygame.font.SysFont("Arial", int(Cell.size/2))
        self.color = (75, 75, 75)
        display = pygame.display.get_surface()
        pygame.draw.rect(display, Cell.borderColor, ((self.posX, self.posY),
                                                     (Cell.size, Cell.size)))
        pygame.draw.rect(display, self.color, ((self.posX+2, self.posY+2),
                                               (Cell.size-4, Cell.size-4)))
        if not self.hasBomb and self.value != 0:
            colors = ((), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0),
                      (255, 255, 255), (0, 255, 255), (255, 0, 255), (255, 100, 100))
            text = font.render(f"{self.value}", True, colors[self.value])
            display.blit(text, (int((self.posX+Cell.size/2)-(text.get_width()/2)),
                                int((self.posY+Cell.size/2)-(text.get_height()/2))))

        self.clicked = True
        for friend in self.friends:
            if not friend.hasBomb and not friend.clicked:
                if self.value == 0:
                    friend.showValue()

        return True

    def updateValue(self, cellStructure: list):
        """
        Update de internal value of cell.
        dataStructure: A linear array to calc the nums of bombs near.
        """
        for friend in self.friends:
            if friend.hasBomb:
                self.value += 1

    def calcCellFriends(self, cellStructure: list):
        """
        cell: Root cell to define his number of friends.
        cellStructure: A cell array to find the root cell friends.
        """
        display = pygame.display.get_surface()
        if self.posX == 0 or self.posX == display.get_height()-Cell.size or self.posY == 0 or self.posY == display.get_height()-Cell.size:
            if self.posX == 0 and self.posY == 0 or self.posX == display.get_width()-Cell.size and self.posY == 0 or self.posX == 0 and self.posY == display.get_height()-Cell.size or self.posY == display.get_height()-Cell.size and self.posX == display.get_width()-Cell.size:
                self.numberOfFriends = 3
                if self.posX == 0 and self.posY == 0:
                    friendsDirections = (
                        1, int((display.get_width()/Cell.size))+1, int((display.get_width()/Cell.size)))
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
                elif self.posX == display.get_width()-Cell.size and self.posY == 0:
                    friendsDirections = (-1, int((display.get_width()/Cell.size)),
                                         int((display.get_width()/Cell.size))-1)
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
                elif self.posX == 0 and display.get_height()-Cell.size == self.posY:
                    friendsDirections = (
                        1, -int((display.get_width()/Cell.size)), -int((display.get_width()/Cell.size))+1)
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
                elif self.posX == display.get_width()-Cell.size and self.posY == display.get_height()-Cell.size:
                    friendsDirections = (-1, -int((display.get_width()/Cell.size)
                                                  ), -int((display.get_width()/Cell.size))-1)
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
            else:
                self.numberOfFriends = 5
                if self.posY == 0:  # UP WALL CELLS
                    friendsDirections = (-1, 1, int((display.get_width()/Cell.size)), int(
                        (display.get_width()/Cell.size))+1, int((display.get_width()/Cell.size)-1))
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
                elif self.posY == display.get_width()-Cell.size:  # BOTTOM WALL CELLS
                    friendsDirections = (-1, 1, -int((display.get_width()/Cell.size)), -int(
                        (display.get_width()/Cell.size))-1, -int((display.get_width()/Cell.size))+1)
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
                elif self.posX == 0:  # LEFT WALL CELLS
                    friendsDirections = (1, -int((display.get_width()/Cell.size)), int((display.get_width(
                    )/Cell.size)), -int((display.get_width()/Cell.size))+1, int((display.get_width()/Cell.size))+1)
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
                else:  # RIGHT WALL CELLS
                    friendsDirections = (-1, int((display.get_width()/Cell.size)), -int((display.get_width(
                    )/Cell.size)), -int((display.get_width()/Cell.size))-1, int((display.get_width()/Cell.size))-1)
                    self.numberOfFriends = getFriends(self,
                                                      friendsDirections, cellStructure)
        else:
            self.numberOfFriends = 8
            friendsDirections = (1, -1, int((display.get_width()/Cell.size)), -int((display.get_width()/Cell.size)), int((display.get_width()/Cell.size)) +
                                 1, int((display.get_width()/Cell.size))-1, -int((display.get_width()/Cell.size))-1, -int((display.get_width()/Cell.size))+1)
            self.numberOfFriends = getFriends(self,
                                              friendsDirections, cellStructure)


def getFriends(cell: Cell, friendsDirections: tuple, cellStructure: list) -> list:
    """
    cell: Root cell to define friends indexs.
    friendsDirections: A tuple thats contains the direction in a linear array.
    cellStructure: A linear arrau thats contains the cells informations.
    return: A list with root cell friends indexs.
    """
    myIndex = cellStructure.index(cell)
    for direction in friendsDirections:
        friend = cellStructure[myIndex+direction]
        cell.friends.append(friend)
