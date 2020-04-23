import random
import heapq
import math
import sys
from Node import Node

class GridGraph:
    def __init__(self):
        self.adj_matrix = []
        self.edges = {}

    def addGridNode(self, x, y, name):
        """adds a node to the graph"""
        self.adj_matrix.append(Node(x, y, name))

    
    def addUndirectedEdge(self, first, second):
        """adds undirected edge between first and second node"""
        if second in first.vertices or first in second.vertices:
            return
        
        if not((first.x + 1 == second.x and first.y == second.y) or (first.x == second.x and first.y + 1 == second.y) or (first.x-1 == second.x and first.y == second.y) or (first.x == second.x and first.y - 1 == second.y)):
            first.vertices.append(second)
            second.vertices.append(first)
    
    def getNode(self,name):
        """gets node from the graph"""
        return self.adj_matrix[name]
    
    def isNeighbor(self,first, second):
        """checks if two nodes are neighbors"""
        firstX = first.x
        firstY = first.y
        secondX = second.x
        secondY = second.y

        if (firstX + 1 == secondX and firstY == secondY) or (firstX == secondX and firstY + 1 == secondY) or (firstX-1 == secondX and firstY == secondY) or (firstX == secondX and firstY - 1 == secondY):
            return True
        return False
    
    def removeUndirectedEdge(self,first,second):
        """removes an undirectedEdge"""
        if not((first.x + 1 == second.x and first.y == second.y) or (first.x == second.x and first.y + 1 == second.y) or (first.x-1 == second.x and first.y == second.y) or (first.x == second.x and first.y - 1 == second.y)):
            if second in first.vertices:
                first.vertices.remove(second)
            if first in second.vertices:
                second.vertices.remove(first)
        
    def getAllNodes(self):
        """returns the list of all nodes of graph"""
        return self.adj_matrix
            
    def getNeighborValidity(name,size):
        """checks the perimeters of being a neighbor"""
        if 0<= name and name < size:
            return True
        else:
            return False

            
    