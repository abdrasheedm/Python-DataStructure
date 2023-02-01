class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


costomDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f", "c"],
    "f": ["d", "e"]
}

graph = Graph(costomDict)
print(graph.gdict)

graph.addEdge("f", "z")
print(graph.gdict)