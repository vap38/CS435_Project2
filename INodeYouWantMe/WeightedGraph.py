from Node import Node, EdgeNode
class WeightedGraph:
    def __init__(self):
        self.dicOfNodes = {}
        self.nodesList = []
        
    def findNode(self, name):
        return self.dicOfNodes.get(name)

    def getAllNodes(self):
        return self.dicOfNodes
  
    def addWeightedEdge(self, first, second, weight):
        if (first is second) or (not first) or (not second):
            return
        
        #self.nodesList[first.name].neighbors.append(Edge(second,weight))
        self.dicOfNodes[first.name].neighbors.append(EdgeNode(second, weight))
    
    def addNode(self, nodeVal):
        node = Node(nodeVal)
        self.nodesList.append(node)
        self.dicOfNodes[nodeVal] = node
    def removeDirectedEdge(self, first, second):  
        if not first or not second :
            return
        self.nodesList[first].neighbors.pop(second)