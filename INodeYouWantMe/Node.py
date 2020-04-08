class Node:
  def __init__(self, name):
    self.name = name
    self.visitedNodes = False
    self.neighbors = []

class EdgeNode:
  def __init__(self, destination, weight):
    self.destination = destination
    self.weight = weight