from Node import Node
from DirectedGraph import DirectedGraph
import random
from TopSort import TopSort
def createRandomDAGIter(n):
    g1 = DirectedGraph()
    # Create n nodes
    for k in range(n):g1.addNode(k)

    # Assign each node 2 random nodesList (might assign 0, 1 or 2 nodesList)
    for i in range(len(g1.nodesList)):
        randList = []
        
        #retreive the length of nodesList
        size = len(g1.nodesList) - 1
        
        name = g1.nodesList[i].name
        #generate random number
        n1 = random.randint(name, size) #d2
        n2 = random.randint(name, size) #d1
        #if n1 generated is unique
        if name is not n1 and n1 not in randList:
            g1.addDirectedEdge(g1.nodesList[name], g1.nodesList[n1])
            randList.append(n1)
        # if n2 generated is unique
        if name is not n2 and n2 not in randList:
            g1.addDirectedEdge(g1.nodesList[name], g1.nodesList[n2])
            randList.append(n2)

    return g1

#main
randG1 = createRandomDAGIter(1000)
if not(randG1 is None):
    for i in range(0,len(randG1.nodesList)):
    #print edges and nodes in randG1.nodesList:
        print("Edge: ", randG1.nodesList[i].name, sep = " ", end = " ")
        print("\t has neighboring nodes:", end = " ")
        for j in range(len(randG1.nodesList[i].neighbors)):print("\t",randG1.nodesList[i].neighbors[j].name, end = " ")
        print()

#mDFS     
topsort = TopSort()
secondSort = TopSort()
mdfsSort = secondSort.mDFS(randG1)
print("\t*****mDFS*****", end = " ")
print()
for node in mdfsSort: print(node.name, end = ",")
print()
#Kahns topological sort
kahns = topsort.Kahns(randG1)

print("\t*****Kahns:*****", end= " ")
print()
for i in range(0,len(kahns)):print(kahns[i].name, sep = ",",end=",")
print()
