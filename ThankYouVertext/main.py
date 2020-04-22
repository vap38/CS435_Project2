from Node import Node
from DirectedGraph import DirectedGraph
import random
from TopSortKahns import TopSortKahns
from TopSortDFS import TopSortDFS
def checkandCreate(g1,name,randName1,randName2,randList):
    size = len(g1.nodesList) - 1
    if name is not randName1 and randName1 not in randList:
        g1.addDirectedEdge(g1.nodesList[name], g1.nodesList[randName1])
        randList.append(randName1)
    if name is not randName2 and randName2 not in randList:
        g1.addDirectedEdge(g1.nodesList[name], g1.nodesList[randName2])
        randList.append(randName2)
        
def createRandomDAGIter(n):
    randGraph = DirectedGraph()
    i=0
    # Create n nodes
    while i<n:
        randGraph.addNode(i)
        i+=1

    # Assign each node 2 random nodesList (might assign 0, 1 or 2 nodesList)
    for i in range(len(randGraph.nodesList)):
        randList = []
        #retreive the length of nodesList
        size = len(randGraph.nodesList) - 1
        
        name = randGraph.nodesList[i].name
        #generate random number
        n1 = random.randint(name, size) #d2
        n2 = random.randint(name, size) #d1
        #if n1 generated is unique
        checkandCreate(randGraph,name,n1,n2,randList)
        
    return randGraph

#main
randG1 = createRandomDAGIter(1000)

if randG1:
    for i in range(0,len(randG1.nodesList)):
    #print edges and nodes in randG1.nodesList:
        print("Edge: ", randG1.nodesList[i].name, sep = " ", end = " ")
        print("\t has neighboring nodes:", end = " ")
        for j in range(len(randG1.nodesList[i].neighbors)):print("\t",randG1.nodesList[i].neighbors[j].name, end = " ")
        print()

    
secondSort = TopSortDFS()
mdfsSort = secondSort.mDFS(randG1)
topsort = TopSortKahns()
kahns = topsort.Kahns(randG1)
#mDFS
print("\t*****mDFS*****", end = " ")
print()
for node in mdfsSort: print(node.name, end = ",")
print()
#Kahns topological sort


print("\t*****Kahns:*****", end= " ")
print()
for i in range(0,len(kahns)):print(kahns[i].name, sep = ",",end=",")
print()
