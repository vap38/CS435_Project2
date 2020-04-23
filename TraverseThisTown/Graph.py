import random
import sys
from GraphNode import GraphNode
class Graph:
    def __init__(self):
        self.nodesList= []
        self.dicNodes = {}
    
    def getNodeName(self,name):
        """returns name of the node"""
        for n in self.nodesList:
            if n.name == name:
                return n
        return 
    def findNode(self, n):
        """checks if a node is in Graph"""
        return n in self.nodesList
    def addNode(self,name):
        """adds a new node to the graph"""
        self.nodesList.append(GraphNode(name))
        self.dicNodes[name] = GraphNode(name)
    
    def getnodesListSize(self):
        """returns the len of nodesList"""
        return len(self.nodesList)
    
    def getNodes(self):
        """returns all nodes in the list"""
        return self.nodesList
    
    def getNodesdic(self):
        """returns all nodes in the form of set"""
        return self.dicNodes
    
    def addUndirectedEdge(self, first,second):
        """adds undirected edge between first and second node"""
        if not self.findNode(first):
            self.addNode(first)
        if not self.findNode(second):
            self.addNode(second)
        if first  not in second.neighbors:  
            first.neighbors.append(second)
        if second not in first.neighbors:
            second.neighbors.append(first)
    
    def removeUndirectedEdge(self, first,second):
        """remove undirected edge from graph"""
        if self.findNode(first) and self.findNode(second) and second in self.nodesList[first]:
            if first in second.neighbors:
                second.neighbors.remove(first)
            if second in first.neighbors:
                first.neighbors.remove(second)

