from Node import Node
from DirectedGraph import DirectedGraph
import random
class TopSort:
    def __init__(self):
        pass

    # implements Kahn's topological sort on graph
    def Kahns(self, graph):
        # lst for topological sort
        tSort = []
        #dict that stores vertex, degree pairs
        degreeList = {}
        # start with all 0s
        for i in range(0,len(graph.nodesList)):
            degreeList[graph.nodesList[i]] = 0
        #update w current neighbors
        for i in range(0,len(graph.nodesList)):
            for j in range(0,len(graph.nodesList[i].neighbors)):
                degreeList[graph.nodesList[i].neighbors[j]] = degreeList[graph.nodesList[i].neighbors[j]] + 1
        # lst2
        lst2 = []

        #lst2 only contains items w degree 0
        keys = list(degreeList.keys())
        for key in keys:
            #making a key search
            if degreeList[key] == 0:
                lst2.append(key)
                #reduce degree
                degreeList[key] = degreeList[key] - 1

        while lst2:
            # pop element from 
            temp = lst2.pop(0)
            # add to tSort list rhat will be returned
            tSort.append(temp)
            # Reduce degree of the neighbor by 1
            for i in range(0, len(temp.neighbors)):
                degreeList[temp.neighbors[i]] = degreeList[temp.neighbors[i]] - 1
            # add items to lst2 w updated degree of 0
            keys = list(degreeList.keys())
            for key in keys:
                #key Lookup
                if degreeList[key] == 0:
                    lst2.append(key)
                    degreeList[key] = degreeList[key] - 1
        #return lst
        return tSort

    # Using mDFS topological sort on the graph
    def mDFS(self, graph):
        lst = []

        
        for i in range(0,len(graph.nodesList)):
            #if node is visited, pass, else call fcn and pass it in the helper method
            if  graph.nodesList[i].visited is False:
                TopSort.mDFSRec(self,graph.nodesList[i], lst)

        # reverse the order
        topMDFS = lst[::-1]
      
        return topMDFS

    # Helper function for DFS recursive
    def mDFSRec(self, graphNode, lst):
        #update visited
        graphNode.visited = True

        
        for i in range(0,len(graphNode.neighbors)):
            if not graphNode.neighbors[i].visited:
                #if node is visited, pass, else call fcn and pass it in the helper method
                self.mDFSRec(graphNode.neighbors[i], lst)
       #after going thru the list, append the node to stack
        lst.append(graphNode)