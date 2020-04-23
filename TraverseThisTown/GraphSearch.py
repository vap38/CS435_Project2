import random,sys
from GraphNode import GraphNode
from Graph import Graph

class GraphSearch:
    def __init(self):
        pass
    
    def DFSIter(start,end):
        """returns traversal using Depth First Search iteratively"""
        stack = []
        traversalPath = []
        stack.append(start)
            
        if not start or not end:
            return None

        while(stack):
            temp = stack.pop()
            traversalPath.append(temp)
            if temp.name == end.name:
                return traversalPath
            
            for node in temp.neighbors:
                if not node.visited:
                    temp.visited = True
                    stack.append(node)
                
    def DFSRec(start,end):
        """returns traversal using Depth First Search recursively"""
        if start and end:
            #passed into the helper function
            newLst = []
            return GraphSearch.DFSRecurHelper(start,end,newLst)
        return None
    
    def DFSRecurHelper(start,end,traversalPath):
        traversalPath.append(start)
        start.visited = True
        if start.name == end.name:
            return traversalPath
        for i in range(0,len(start.neighbors)):
            if start.neighbors[i] not in traversalPath:
                addedPath = GraphSearch.DFSRecurHelper(start.neighbors[i],end,traversalPath)
                if  addedPath:
                    return traversalPath
        return None
    
    def BFTIter(graph):
        """returns traversal using Breadth first search iteratively"""
        queue = []
        traversalPath = []
        gNodes = graph.getAllNodes()
        for curr in gNodes.values():
            if not curr.visited:
                curr.visited = True
                queue.append(curr)
                #keeps track of lst
                #length = len(queue)
                while queue:
                    #removes from lst
                    temp = queue.pop(0)
                    #update len
                    #length-=1
                    #removedNode is added to the path
                    traversalPath.append(temp)
                    #iterate through the nodes in temp.neighbors
                    nodes = temp.neighbors
                    for i in range(0,len(nodes)):
                        
                    #for n in nodes:
                        #mark them visited
                        if not gNodes[nodes[i].name].visited:
                            gNodes[nodes[i].name].visited = True
                            queue.append(nodes[i])
                            #length+=1
        return traversalPath
    # def BFTRec(graph):
    #     bftTraversal = []
    #     visited = []
    #     nodes = graph.getAllNodes()
    #     for node in nodes.values():
    #         if not node.visited:
    #             node.visited = True
    #             visited.append(node)
    #             GraphSearch.myBFTRec(graph, visited, bftTraversal)
    #     return bftTraversal

    # def myBFTRec(graph, visited, bftTraversal):
    #     if len(visited) == 0:
    #         return
    #     temp = visited.pop(0)
    #     bftTraversal.append(temp)
    #     nodes = temp.neighbors
    #     for i in range(0,len(nodes)):
    #         if not nodes[i].visited:
    #             nodes[i].visited = True
    #             visited.append(nodes[i])
    #     GraphSearch.myBFTRec(graph, visited, bftTraversal)
    
    #method, however it had some issue, though when traced on paper it works fine
    #my method using nodesList, works and prints it prints a little extra nodes 
    # and does not perfectly match bfsIter traversal's answer
    def BFTRec(graph):
        """returns traversal using Breadth First Search recursively"""
        bftTraversal=list()
        nodes = graph.nodesList
        for i in range(len(nodes)):
            visited = []
            if nodes[i] not in visited:
                visited.append(nodes[i])
                GraphSearch.bftRecHelper(graph,bftTraversal,visited)
        return bftTraversal

    def bftRecHelper(graph,bftTraversal,queue):
        #length = len(queue)
        if not queue:
            return bftTraversal
        else:
            temp = queue.pop(0)
            #length-=1
            stack=[temp]
            bftTraversal.append(temp)
            nodes = temp.neighbors
        for i in range(0,len(nodes)):
            if nodes[i] not in bftTraversal:
                queue.append(nodes[i])
        return GraphSearch.bftRecHelper(graph,bftTraversal,queue)
