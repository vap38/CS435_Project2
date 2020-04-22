from Node import Node

class DirectedGraph:
    def __init__(self):
        self.nodesList = []
        self.dicOfNodes = {}

    # adds a new node to the graph
    def addNode(self, name):
        self.nodesList.append(Node(name))
        self.dicOfNodes[name]= Node(name)

    #adds directed edge between first and second node
    def addDirectedEdge(self, first, second):
        if first in second.neighbors or first == None or second == None:
            return
        if second not in first.neighbors:
            first.neighbors.append(second)
            

    #removes undirected edge between first and second
    def removeDirectedEdge(self, first, second):
        if first in second.neighbors:
            first.neighbors.remove(second)
        else:
            return
        

    #returns a set of all nodes in the graph
    def getAllNodes(self):
        #return self.nodesList
        return self.dicOfNodes