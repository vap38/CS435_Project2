from Node import Node
from DirectedGraph import DirectedGraph
import random

import heapq
class TopSortKahns:
    def Kahns(self, graph):
        tSort = []
        degreeList = {}
        for i in range(0,len(graph.nodesList)):
            degreeList[graph.nodesList[i]] = 0
        for i in range(0,len(graph.nodesList)):
            for j in range(0,len(graph.nodesList[i].neighbors)):
                degreeList[graph.nodesList[i].neighbors[j]] = degreeList[graph.nodesList[i].neighbors[j]] + 1
        lst2 = []

        keys = list(degreeList.keys())
        for key in keys:
            if degreeList[key] == 0:
                lst2.append(key)
                degreeList[key] = degreeList[key] - 1

        while lst2:
            temp = lst2.pop(0)
            tSort.append(temp)
            for i in range(0, len(temp.neighbors)):
                degreeList[temp.neighbors[i]] = degreeList[temp.neighbors[i]] - 1
            keys = list(degreeList.keys())
            for key in keys:
                if degreeList[key] == 0:
                    lst2.append(key)
                    degreeList[key] = degreeList[key] - 1
        return tSort