import random
import sys
from Graph import Graph
from Graph import GraphNode
from GraphSearch import GraphSearch
def createGraph(graph,n):
    for i in range(n):graph.addNode(i)
def createRandomUnweighterGraph(n):
    """creates a random graph"""
    graph = Graph()
    createGraph(graph,n)
    neighs = random.randrange(1,n//3)
    nodes = graph.getNodes()
    size = graph.getnodesListSize()-1
    for i in range(0,len(nodes)):
        x = nodes.index(nodes[i])
        suggested = random.sample(nodes[:x]+nodes[x+1:],neighs)
        for n in range(len(suggested)):
            graph.addUndirectedEdge(nodes[i],suggested[n])
            
    return graph

def createLinkedList(n):
    """for creating linked list"""
    graph = Graph()
    previous = None
    d ={}
    for i in range(0,n+1,1):
        graph.addNode(i)
        temp = graph.nodesList[graph.getnodesListSize()-1]
        if previous:
            graph.addUndirectedEdge(previous, temp)
        previous = temp
    return graph


def BFTIterLinkedList(graph):
    """returns linkedList"""
    return GraphSearch.BFTIter(graph)


def printNodeNames(lst):
    """print function for main"""
    for n in lst:print(n.name, end=" ")
    print()
    return 

def BFTRecLinkedList(graph):
  return GraphSearch.BFTRec(graph)

def makeNodesVisted(lst):
    for i in range(0,len(lst)): lst[i].visited = yes
    
#Main class testing
randGraph = createRandomUnweighterGraph(10)
allNodes = randGraph.getNodes()
for i in range(0,len(allNodes)):
    print(allNodes[i].name,"has", "edges ", sep = " ", end = ": ")
    printNodeNames(allNodes[i].neighbors)

print("DFS Iterative", end = ": ")   
traverse = GraphSearch.DFSIter(randGraph.getNodeName(0),randGraph.getNodeName(9))
traversed = GraphSearch.DFSRec(randGraph.getNodeName(0),randGraph.getNodeName(9))
if traverse:
    printNodeNames(traverse)
else:
    print("DFS ITERATIVE DID NOT WORK")
yes = False

print("DFS Recursive", end = ": ")

myNodes = randGraph.getNodes()
if traversed:
    printNodeNames(traversed)
else:
    print(" DFS RECURSIVE DID NOT WORK")    
    
myNodesCopy = randGraph.getNodes()
makeNodesVisted(myNodesCopy)

traversedPath = GraphSearch.BFTIter(randGraph)
traversedP = GraphSearch.BFTRec(randGraph)

print("BFT Iterative", end = ": ")
printNodeNames(traversedPath)

myNodesCopy = randGraph.getNodes()
makeNodesVisted(myNodesCopy)

print("BFT Recursive", end=": ")
myNodesCopy = randGraph.getNodes()
if not traversedP:
    print("BFT RECURSIVE DID NOT WORK")
else:
    printNodeNames(traversedP)
#creates a linkedList of size
graph2 = createLinkedList(10)

lstOfNodes = graph2.getNodes()
for i in range(len(allNodes)):
    print(allNodes[i].name, "has", "edges ", sep = " ", end = ": ")
    printNodeNames(allNodes[i].neighbors)

tenk = createLinkedList(10000)
bIt = BFTIterLinkedList(tenk)
print("BFT ITERATIVE LINKED LIST", end = ": ")
printNodeNames(bIt)
print()
print("DONE ITER")
print()
#does not work for 10000, 
#max length works for is 990
diff = createLinkedList(990)
bRec = BFTRecLinkedList(diff)
print("BFT RECURSIVE LINKEDLIST", end = ": ")
printNodeNames(bRec)
print()
print("DONE REC")
