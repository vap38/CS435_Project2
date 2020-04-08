from Node import Node,EdgeNode
from WeightedGraph import WeightedGraph
import random
import sys

def createRandomCompleteWeightedGraph(n):
    randgraph = WeightedGraph()
    i=0
    while(i<n):
        randgraph.addNode(i)
        i+=1
    i = 0
    while(i<n):
        j = 0
        while(j<n):
            if i != j:
                x = randgraph.nodesList[i]
                y = randgraph.nodesList[j]
                z = random.randint(1, max(10,n/2))
                randgraph.addWeightedEdge(x,y,z)
            j+=1
        i+=1      
    return randgraph

def createLinkedList(n):
    linkedgraph = WeightedGraph()
    i = 0
    while(i<n):
        linkedgraph.addNode(i)
        i+=1
    j = 1
    while(j<(n)):
        linkedgraph.addWeightedEdge(linkedgraph.nodesList[j-1], linkedgraph.nodesList[j], 1)
        j+=1
    return linkedgraph

def minDistLst(dicOfDistances, visitedNodes):
    ans = None
    m = sys.maxsize
    lst = dicOfDistances.keys()
    for node in lst:
        if node not in visitedNodes and dicOfDistances[node] <=m:
            m = dicOfDistances[node]
            ans = node
    return ans

def dijkstras(start):
    dicOfDistances = {}
    dicOfDistances[start] = 0
    visitedNodes = set()
    node = start
    while node is not None and node in dicOfDistances:
        visitedNodes.add(node)
        for neighbor in node.neighbors:
            cnd2 = dicOfDistances[node] + neighbor.weight
            #cnd1 = dicOfDistances[neighbor.destination]
            if neighbor.destination not in dicOfDistances or  dicOfDistances[neighbor.destination] > cnd2:
                dicOfDistances[neighbor.destination] = cnd2
        node = minDistLst(dicOfDistances, visitedNodes)
    print("The finalized length:", len(visitedNodes))
    return dicOfDistances


graph1 = createRandomCompleteWeightedGraph(11)
nodes = graph1.getAllNodes()
lst = nodes.values()
for node in lst:
    print("\t-------",node.name,"-------",sep=" ")
    for edge in node.neighbors:
        name = edge.destination.name
        weight = edge.weight
        print("edge", name, "weight", weight,"" ,sep= "  :  ")

n = graph1.findNode(0)
dicOfDistances = dijkstras(n)
lst = list(dicOfDistances.keys())
print("******DIJKSTRAS ALGORITHM FOR RANDOM GRAPH******")
for item in lst:print("Node: ", item.name, "  :  Distance: ", dicOfDistances[item], sep = " ")
  
print()
linkedGraph = createLinkedList(11)
lst = linkedGraph.getAllNodes().values()
print("******LINKED LIST******")
for item in lst:
  print("\t-------",item.name,"-------",sep=" ")
  for e in item.neighbors:
        name = e.destination.name
        weight = e.weight
        print("edge", name, "weight", weight,"" ,sep= "  :  ")

print()
dicOfDistances = dijkstras(linkedGraph.findNode(0))
nodes = dicOfDistances.keys()
print("******DIJKSTRAS FOR LINKED LIST******")
for node in nodes:print("Node: ", node.name, "  :  Distance: ", dicOfDistances[node], sep = " ")
#extra credit #7

print()
linkedGraph = createLinkedList(10000)
lst = linkedGraph.getAllNodes().values()
print("******LINKED LIST EXTRA CREDIT******")
for item in lst:
  print("\t-------",item.name,"-------",sep=" ")
  for e in item.neighbors:
        name = e.destination.name
        weight = e.weight
        print("edge", name, "weight", weight,"" ,sep= "  :  ")

print()
dicOfDistances = dijkstras(linkedGraph.findNode(0))
nodes = dicOfDistances.keys()
print("******DIJKSTRAS FOR LINKED LIST EXTRA CREDIT******")
for node in nodes:print("Node: ", node.name, "  :  Distance: ", dicOfDistances[node], sep = " ")
print("Number of Nodes finalized in dijstras: ",len(nodes))
