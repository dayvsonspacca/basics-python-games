class Pixel_walkable(object):
    """
    Objeto que guarda as caracateristicas de pixel.
    Caracteristicas: Pos x, Pos y, Color, Size e Walkable.
    """
    def __init__(self, pos_x, pos_y, walkable = True):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = [pos_x, pos_y]
        self.size = (10, 10)
        self. walkable = walkable
        self.win_pixel = False
        if self.walkable:
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)



class Player(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = [pos_x, pos_y]
        self.size = (10, 10)
        self.color = (255, 0, 0)