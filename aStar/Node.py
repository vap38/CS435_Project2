class Node:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.name = name
        self.vertices = []
        self.pNode = None