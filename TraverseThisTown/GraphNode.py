class GraphNode:
    def __init__(self, name):
        self.neighbors = list()
        self.name = name
        self.visited = False