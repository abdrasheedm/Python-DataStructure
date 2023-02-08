# Adjacency Matrix representaion in Python

class Graph(object):
    # initializing the matrix
    def __init__(self, size):
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    # Print the matrix
    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print('{:4}'.format(val)),
            print

graph = Graph(5)

graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(4, 2)
graph.print_matrix()


