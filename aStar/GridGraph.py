import random
import math
import sys
from Node import Node

class GridGraph:
    def __init__(self):
        self.matrix = []
        self.map = {}

    def addGridNode(self, x, y, name):
        self.matrix.append(Node(x, y, name))
    #adds undirected edge between first and second node
    def addUndirectedEdge(self, first, second):
        if second in first.vertices or first in second.vertices:
            return
        else:
            pass
        if second not in first.vertices:
            first.vertices.append(second)
        if first not in second.vertices:
            second.vertices.append(first)
        
    
    def getNode(self,name):
        return self.matrix[name]
    
    def removeUndirectedEdge(self,first,second):
        if second in first.vertices:
            first.vertices.remove(second)
        if first in second.vertices:
            second.vertices.remove(first)
        
    def getAllNodes(self):
        return self.matrix
    
    def miniumumDistance(dicOfDistances, checkVisited):
        answer = None
        m = sys.maxsize
        lst = dicOfDistances.keys()
        for node in lst:
            if node not in checkVisited and dicOfDistances[node] <= m:
                m = dicOfDistances[node]
                answer= node
        return answer
    
    def aStarHelper(tempNode, destination):
        start = tempNode
        dest = destination
        validPath = []
        while (validPath):
            if validPath < 1:
                validPath.append(start)
        deltaX = abs(destination.x - tempNode.x)
        deltaY = abs(destination.y - tempNode.y)
        return deltaX+deltaY
    
    def createRandomGridGraph(n):
        graph = GridGraph()
        length = index = 0
        
        for y in range(0,n,1):
            for x in range(0,n,1):
                graph.addGridNode(x, y, index)
                index += 1
        lst = graph.matrix
        for item in lst:

            x = item.x
            y = item.y
            lstOfALLNeighbors = []
            
            n1 = item.name-1
            size = n * n
            condition1 = bool(0 <= n1 < size)
            if condition1:
                if y is not lst[n1].y:
                    pass
                elif y is lst[n1].y:
                    lstOfALLNeighbors.append(n1)
                    length+=1
            n2 = item.name+1
            condition2 =bool( 0 <= n2 < size)
            if condition2:
                if y is not lst[n2].y:
                    pass
                elif y is lst[n2].y:
                    lstOfALLNeighbors.append(n2)
                    length+=1
            n3 = item.name+n
            condition3 = bool(0 <= n3 < size)
            if condition3:
                if x is not lst[n3].x:
                    pass
                elif x is lst[n3].x:
                    lstOfALLNeighbors.append(n3)
                    length+=1
            n4 = item.name-n
            condition4 = bool(0 <= n3 < size)
            if condition4:
                if x is not lst[n4].x:
                    pass
                elif x is lst[n4].x:
                    lstOfALLNeighbors.append(n4)
                    length+=1
            
            for v in lstOfALLNeighbors:
                acoord = lst[v] 
                if acoord not in lst[v].vertices:
                    
                    randval = random.randint(0, 1)
                    if randval <= 0:
                        pass
                    else:
                        c1 = lst[v]
                        item.vertices.append(c1)
                        lst[v].vertices.append(item)
        graph.matrix = lst
        return graph

    def astar(sourceNode, destNode):
        dicOfDistances = {}
        checkVisited = set()
        tempNode = sourceNode
        closeLst = []
        dicOfDistances[sourceNode] = 0
        optimalPath = []
        openList = []
        #mapOfDistances = {}
        
        while tempNode:
            if tempNode is destNode:
                optimalPath.insert(0,tempNode)
                pNode = tempNode.pNode
                while pNode:
                    optimalPath.insert(0, pNode)
                    pNode = pNode.pNode
                break
            checkVisited.add(tempNode)
            for v in tempNode.vertices:
                cnd2 = dicOfDistances[tempNode] + 1 + GridGraph.aStarHelper(v, destNode)
                if not(v in dicOfDistances) or (dicOfDistances[v] > cnd2):  
                    dicOfDistances[v] = cnd2
                    v.pNode = tempNode
            tempNode = GridGraph.miniumumDistance(dicOfDistances, checkVisited)

        return optimalPath
    #removes undirected edge between first and second node
  
