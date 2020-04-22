from Node import Node
from DirectedGraph import DirectedGraph
import random
class TopSortDFS:
    # Helper function for DFS recursive
    def mDFSRec(self, graphNode, lst):
        #update visited
        graphNode.visited = True
        for i in range(0,len(graphNode.neighbors)):
            if not graphNode.neighbors[i].visited:
                self.mDFSRec(graphNode.neighbors[i], lst)
        lst.append(graphNode)

    def mDFS(self, graph):
        lst = []
        for i in range(0,len(graph.nodesList)):
            if  graph.nodesList[i].visited is False:
                TopSortDFS.mDFSRec(self,graph.nodesList[i], lst)
        topMDFS = lst[::-1]
        return topMDFS
