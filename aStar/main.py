import random
import math
import sys
from Node import Node
from GridGraph import GridGraph

n = 100
g = GridGraph.createRandomGridGraph(n)
lst = g.matrix
size = len(lst)
print("\t*****Grid*****")
path = GridGraph.astar(g.matrix[0],g.matrix[9999])
for item in lst: print("GRID[ ",item.x, " , ",item.y, " ]  =   ",item.name, sep = "")
print("\t*****AStar on grid with ",size," [X,Y] matrix*****")
print("AStar path: ")
if len(path): 
    print("\t ~> \t".join("[" + str(node.x) + " , " + str(node.y) + "]" for node in path))
    #7 extra credit for astar
    print("Number of Nodes finalized in A Star: ", len(path))
else:
    print("Error in finding path")
