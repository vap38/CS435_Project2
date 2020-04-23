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
    s = n//3
    neighs = random.randrange(1,s)
    nodes = graph.getNodesList()
    size = graph.getNodesListSize()-1
    for i in range(0,len(nodes)):
        x = nodes.index(nodes[i])
        lst = nodes[:x]+nodes[x+1:]
        suggested = random.sample(lst,neighs)
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
        temp = graph.nodesList[graph.getNodesListSize()-1]
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
allNodes = randGraph.getNodesList()
for i in range(0,len(allNodes)):
    print(allNodes[i].name,"has", "edges ", sep = " ", end = ": ")
    printNodeNames(allNodes[i].neighbors)

print("DFS Iterative", end = ": ")   
dfsIter = GraphSearch.DFSIter(randGraph.getNodeName(0),randGraph.getNodeName(9))
dfsRecGraph = GraphSearch.DFSRec(randGraph.getNodeName(0),randGraph.getNodeName(9))

if dfsIter:
    printNodeNames(dfsIter)
else:
    print("DFS ITERATIVE DID NOT WORK")
yes = False
print("DFS Recursive", end = ": ")
myNodes = randGraph.getNodesList()
if dfsRecGraph:
    printNodeNames(dfsRecGraph)
else:
    print(" DFS RECURSIVE DID NOT WORK")     
bftIterGraph = GraphSearch.BFTIter(randGraph)
bftRecGraph = GraphSearch.BFTRec(randGraph)
print("BFT Iterative", end = ": ")
printNodeNames(bftIterGraph)
print("BFT Recursive", end=": ")
if bftRecGraph:
    printNodeNames(bftRecGraph)
else:
    print("BFT RECURSIVE DID NOT WORK")

#creates a linkedList of size
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
