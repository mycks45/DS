class Graph:
    def __init__(self):
        self.map = {}

    def addVertex(self, data):
        self.map[data] = []

    def insert(self, vertex, edge, isBidirectional = False):
        if vertex not in self.map:
            self.addVertex(vertex)
        
        if edge not in self.map:
            self.addVertex(edge)
        
        self.map[vertex].append(edge)
        if isBidirectional:
            self.map[edge].append(vertex)

    def display(self):
        for i in enumerate(self.map.items()):
            print (i)

g = Graph()

g.insert(4,5,True)
g.insert(4,8,True)
g.insert(7,5,True)
g.insert(3,5,True)
g.insert(8,5,True)
g.display()