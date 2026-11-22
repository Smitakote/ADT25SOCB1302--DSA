
# Assignment 8A: Graph using Adjacency List
# Implement Breadth First Search (BFS)

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # Add Vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add Edge
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Display Graph
    def display(self):
        print("\nAdjacency List:")
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    # BFS Traversal
    def bfs(self, start):
        if start not in self.graph:
            print("Starting vertex not found!")
            return

        visited = set()
        queue = deque([start])
        visited.add(start)

        print("\nBFS Traversal:")

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print()


# Main Program
g = Graph()

n = int(input("Enter number of vertices: "))

print("Enter vertex names:")
for i in range(n):
    vertex = input()
    g.add_vertex(vertex)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    g.add_edge(u, v)

g.display()

start = input("Enter starting vertex: ")
g.bfs(start)
