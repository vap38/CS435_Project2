from Node import Node

class DirectedGraph:
    def __init__(self):
        self.nodesList = []

    # adds a new node to the graph
    def addNode(self, name):
        self.nodesList.append(Node(name))

    #adds directed edge between first and second node
    def addDirectedEdge(self, first, second):
        if first in second.neighbors:
            return
        first.neighbors.append(second)

    #removes undirected edge between first and second
    def removeDirectedEdge(self, first, second):
        try:
            first.neighbors.remove(second)
        except:
            return

    #returns a set of all nodes in the graph
    def getAllNodes(self):
        return self.nodesList