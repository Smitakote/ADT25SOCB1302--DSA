
# Assignment 7A: Graph using Adjacency Matrix
# Implement Depth First Search (DFS)

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0 for i in range(vertices)]
                       for j in range(vertices)]

    # Add Edge
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    # Display Adjacency Matrix
    def display(self):
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)

    # DFS Traversal
    def dfs(self, start):
        visited = [False] * self.vertices
        print("\nDFS Traversal:")

        self.dfs_recursive(start, visited)
        print()

    def dfs_recursive(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for i in range(self.vertices):
            if self.matrix[vertex][i] == 1 and not visited[i]:
                self.dfs_recursive(i, visited)


# Main Program
n = int(input("Enter number of vertices: "))
g = Graph(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

g.display()

start = int(input("Enter starting vertex: "))
g.dfs(start)
