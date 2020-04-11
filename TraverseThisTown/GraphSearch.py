import random,sys
from GraphNode import GraphNode
from Graph import Graph

class GraphSearch:
    def __init(self):
        pass
    def DFSIter(start,end):
        stack = []
        traversalPath = []
        stack.append(start)
        if not start or not end:
            return None
        while(stack):
            temp = stack.pop()
            traversalPath.append(temp)
            temp.visited = True
            
            for node in temp.neighbors:
                if node.visited is not True:
                    stack.append(node)
            if temp == end: 
                return traversalPath
        return None
    
    def DFSRec(start,end):
        if start and end:
            #passed into the helper function
            newLst = []
            return GraphSearch.DFSRecurHelper(start,end,newLst)
        return None
    
    def DFSRecurHelper(start,end,traversalPath):
        #s = 0
        yes = True
        start.visited = yes
        traversalPath.append(start)
        s = start.name
        f = end.name
        if s == f:
            return traversalPath
        for i in range(0,len(start.neighbors)):
            if start.neighbors[i] not in traversalPath:
                addedPath = GraphSearch.DFSRecurHelper(start.neighbors[i],end,traversalPath)
                if  addedPath:
                    return traversalPath
        return None
    
    def BFTIter(graph):
        q = []
        yes = True
        traversalPath = []
        gNodes = graph.getNodes()
        for i in range(0,len(gNodes)):
            if not gNodes[i].visited:
                gNodes[i].visited = yes
                q.append(gNodes[i])
                #keeps track of lst
                length = len(q)
                while length>0:
                    #removes from lst
                    temp = q.pop(0)
                    #update len
                    length-=1
                    #removedNode is added to the path
                    traversalPath.append(temp)
                    #iterate through the nodes in temp.neighbors
                    nodes = temp.neighbors
                    for i in range(0,len(nodes)):
                    #for n in nodes:
                        #mark them visited
                        if not nodes[i].visited:
                            nodes[i].visited = yes
                            q.append(nodes[i])
                            length+=1
        return traversalPath
    
    def BFTRec(graph):
        bftTraversal=list()
        nodes = graph.nodesList
        for i in range(len(nodes)):
            visited = []
            
            if nodes[i] not in visited:
                
                visited.append(nodes[i])
                GraphSearch.bftRecHelper(graph,bftTraversal,visited)
        return bftTraversal
    def bftRecHelper(graph,bftTraversal,q):
        length = len(q)
        if length == 0:
            return bftTraversal
        else:
            temp = q.pop(0)
            length-=1
            stack=[temp]
            bftTraversal.append(temp)
            nodes = temp.neighbors
        for i in range(0,len(nodes)):
            if nodes[i] not in bftTraversal:
                q.append(nodes[i])
        return GraphSearch.bftRecHelper(graph,bftTraversal,q)
    


    
dfsTraversal = []
bftTraversal = []
found = []                 