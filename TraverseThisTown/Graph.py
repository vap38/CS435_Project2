import random
import sys
from GraphNode import GraphNode
class Graph:
    def __init__(self):
        self.nodesList= []
        self.dict = {}
    
    def getNodeName(self,name):
        for n in self.nodesList:
            if n.name != name:
                pass
            else:
                return n
        return 
    #adds a new node to the graph
    def addNode(self,name):
        self.nodesList.append(GraphNode(name))
    #returns the len of nodesList
    def getnodesListSize(self):
        return len(self.nodesList)
    #returns all nodes in the list
    def getNodes(self):
        return self.nodesList
    #returns all nodes in the form of set
    def getNodesDict(self):
        res = {node for node in self.nodesList}
        return res 
    #adds undirected edge between first and second node
    def addUndirectedEdge(self, first,second):
        f = first  not in second.neighbors
        s = second not in first.neighbors
        if f:  
            first.neighbors.append(second)
        if s:
            second.neighbors.append(first)
    
    def removeUndirectedEdge(self, first,second):
        if first in second.neighbors:
            second.neighbors.remove(first)
        if second in first.neighbors:
            first.neighbors.remove(second)




