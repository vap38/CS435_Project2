from Node import Node
from DirectedGraph import DirectedGraph
import random
class TopSortDFS:
    
    # Helper function for DFS recursive
    def mDFSRec(self, graphNode, lst):
        #update visited
        graphNode.visited = True
        #for node in graph.nodesList:
        # for neighbor in node.neighbors:
        #     if neighbor not in dic:
        #         neighborCopy = UndirectedGraphNode(neighbor.label)
        #         dic[neighbor] = neighborCopy
        #         dic[node].neighbors.append(neighborCopy)
        #         self.dfs(neighbor, dic)
        #     else:
        #         dic[node].neighbors.append(dic[neighbor])
        
        for i in range(0,len(graphNode.neighbors)):
            if not graphNode.neighbors[i].visited:
                #if node is visited, pass, else call fcn and pass it in the helper method
                self.mDFSRec(graphNode.neighbors[i], lst)
       #after going thru the list, append the node to stack
        lst.append(graphNode)
# Using mDFS topological sort on the graph
    def mDFS(self, graph):
        lst = []
        
        
        for i in range(0,len(graph.nodesList)):
            #if node is visited, pass, else call fcn and pass it in the helper method
            if  graph.nodesList[i].visited is False:
                TopSortDFS.mDFSRec(self,graph.nodesList[i], lst)

        # reverse the order
        topMDFS = lst[::-1]
      
        return topMDFS
