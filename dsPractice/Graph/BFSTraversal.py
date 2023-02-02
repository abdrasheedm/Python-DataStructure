class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            de_vertext = queue.pop(0)
            print(de_vertext)
            for adjacent_vertex in self.gdict[de_vertext]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    visited.append(adjacent_vertex)


costomDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f", "c"],
    "f": ["d", "e"]
}

graph = Graph(costomDict)
graph.add_edge("a", "f")
print(graph.gdict)
graph.bfs("a")