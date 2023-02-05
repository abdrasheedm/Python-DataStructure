class Graph:
    def __init__(self,  gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        if vertex in self.gdict and edge in self.gdict:
            self.gdict[vertex].append(edge)
        else:
            print("there no vertex")

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.gdict[pop_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
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
graph.add_edge("a", "g")
print(graph.gdict)
graph.dfs("a")