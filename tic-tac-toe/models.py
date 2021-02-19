import pygame


class Cell:
    size = 200

    def __init__(self, x: int, y: int):
        """
        x: Start x position of cell.
        y: Start y position of cell.
        """
        self.x = x
        self.y = y
        self.value = None
        self.reveal = False

    def mark(self, color: tuple):
        """
        color: A tuple thats contains the RGB value.
        """
        font = pygame.font.SysFont("arial", int(Cell.size/2))
        text = font.render(f"{self.value}", True, color)
        pygame.display.get_surface().blit(text, (int((self.x+Cell.size/2)-(text.get_width()/2)),
                                                 int((self.y+Cell.size/2)-(text.get_height()/2))))
        self.reveal = True
