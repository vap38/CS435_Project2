import random
import math
import sys
from GridGraph import GridGraph
from Node import Node

def heuristic(tempNode, destination):
    """returns the multiplied distance in steps by the minimum cost for a step"""
    start = tempNode
    dest = destination
    nameidPath = []
    while (nameidPath):
        if nameidPath < 1:
            nameidPath.append(start)
    deltaX = abs(dest.x - start.x)
    deltaY = abs(dest.y - start.y)
    return deltaX+deltaY
    
    # def checkLeft(node,nodeList,n,move):
    #     x = node.x
    #     #name = node.name
    #     size = n*n
    #     if 0<move<size:
    #         if x is not nodeList[move].x:
    #             return False
    #         elif x is nodeList[move].x:
    #             return True
    
    # def checkRight(node,nodeList,n,move):
    #     x = node.x
    #     #name = node.name
    #     size = n*n
    #     if 0<move<size:
    #         if x is not nodeList[move].x:
    #             return False
    #         elif x is nodeList[move].x:
    #             return True
    
    # def checkUp(node,nodeList,n,move):
    #     y = node.y
    #     #name = node.name
    #     size = n*n
    #     if 0<move<size:
    #         if y is not nodeList[move].y:
    #             return False
    #         elif y is nodeList[move].y:
    #             return True
        
    # def checkDown(node,nodeList,n,move):
    #     y = node.y
    #     #name = node.name
    #     size = n*n
    #     if 0<move<size:
    #         if y is not nodeList[move].y:
    #             return False
    #         elif y is nodeList[move].y:
    #             return True
def getNextNeighbor(name, value,n):
    """returns value for a neighbor"""
    if value == "-1":
        return name-1
    if value == "1":
        return name+1
    if value == "-n":
        return name-n
    if value == "n":
        return name+n

def createRandomGridGraph(n):
    """creates a graph with random neighbors, at most 4"""
    length = index = 0
    graph = GridGraph()
        
    for i in range(0,n,1):
        for j in range(0,n,1):
            graph.addGridNode(j,i, index)
            index += 1
    lst = graph.adj_matrix
    
    for graphNode in lst:
        x = graphNode.x
        y = graphNode.y
        lstOfALLvertices = []
        
        name = graphNode.name
        size = n * n
        #since the possible neighbors are only 4
        #it checks accordingly with the helper of other helper methods 
        #to find 
        n1 = getNextNeighbor(name, "-1",n)        
        if GridGraph.getNeighborValidity(n1,size):
            checkY = lst[n1].y
            if y is checkY:
                lstOfALLvertices.append(n1)
                length+=1
        n2 = getNextNeighbor(name, "1",n)
        if GridGraph.getNeighborValidity(n2,size):
            checkY = lst[n2].y
            if y is checkY:
                lstOfALLvertices.append(n2)
                length+=1
        n3 = getNextNeighbor(name, "n",n)
        if GridGraph.getNeighborValidity(n3,size):
            checkX = lst[n3].x
            if x is checkX:
                lstOfALLvertices.append(n3)
                length+=1
        n4 = getNextNeighbor(name, "-n",n)
        if GridGraph.getNeighborValidity(n4,size):
            checkX = lst[n4].x
            if x is checkX:
                lstOfALLvertices.append(n4)
                length+=1

        for v in lstOfALLvertices:
            #acoord = lst[v] 
            #if acoord not in lst[v].vertices:
            if lst[v] not in graphNode.vertices and graphNode not in lst[v].vertices:
                randname = random.randint(0, 1)
                if randname <= 0:
                    pass
                else:
                    c1 = lst[v]
                    graphNode.vertices.append(c1)
                    lst[v].vertices.append(graphNode)
    graph.adj_matrix = lst
    return graph

def astar(sourceNode, destNode):
    """returns shortest possible path between two nodes in a graph"""
    dicOfDistances = {}
    checkVisited = set()
    tempNode = sourceNode
    closeList = []
    dicOfDistances[sourceNode] = 0
    optimalPath = []
    openList = []
    #edgesOfDistances = {}
    
    while tempNode:
        #tempNode = min(notVisited, key=lambda x: x.f)
        if tempNode is destNode:
            optimalPath.insert(0,tempNode)
            pNode = tempNode.pNode
            while pNode:
                optimalPath.insert(0, pNode)
                pNode = pNode.pNode
                #     for v in tempNode.vertices:
                        # cnd2 = 1+dicOfDistances[tempNode] + heuristic(v, destNode)
                        # #if vertice is not in dicOfDistances or it is greate that the calculated amount
                        # if not(v in dicOfDistances) or (dicOfDistances[v] > cnd2):  
                #     dicOfDistances[v] = cnd2
                #     v.pNode = tempNode
            break
        checkVisited.add(tempNode)
        #checks every vertice content
        for v in tempNode.vertices:
            cnd2 = 1+dicOfDistances[tempNode] + heuristic(v, destNode)
            #if vertice is not in dicOfDistances or it is greate that the calculated amount
            if not(v in dicOfDistances) or (cnd2 <dicOfDistances[v]):  
                #that vertice now gets assigned
                dicOfDistances[v] = cnd2
                v.pNode = tempNode
        answer = None
        m = sys.maxsize
        lst = dicOfDistances.keys()
        for node in lst:
            if node not in checkVisited and dicOfDistances[node] <= m:
                m = dicOfDistances[node]
                answer= node
        tempNode= answer
    return optimalPath

n = 100
g = createRandomGridGraph(n)
lst = g.adj_matrix
size = len(lst)
print("\t*****Grid*****")
path = astar(g.adj_matrix[0],g.adj_matrix[9999])
for item in lst: 
    print("GRID[ ",item.x, " , ",item.y, " ]  =   ",item.name, sep = "")
print()
print("\t*****AStar on grid with ",size," [X,Y] matrix*****")
print("AStar path: ")
if len(path):
    for i in range(len(path)):
        if i == len(path)-1:
            print(" [ " , path[i].x , " , ",path[i].y," ] ")
        else:
            print(" [ " , path[i].x , " , ",path[i].y," ] ",end="\t  ~>  \t")
    print("Number of Nodes finalized in A Star: ", len(path))
else:
    print("Error in finding path")
