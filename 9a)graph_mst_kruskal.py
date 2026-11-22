
# Assignment 9A: Minimum Spanning Tree
# Using Kruskal's Algorithm

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    # Add Edge
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # Find Parent
    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    # Union
    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)

        if root_u == root_v:
            return False

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    # Kruskal's Algorithm
    def kruskal(self):
        self.edges.sort()

        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        mst = []
        total_cost = 0

        for weight, u, v in self.edges:
            if self.union(parent, rank, u, v):
                mst.append((u, v, weight))
                total_cost += weight

        print("\nMinimum Spanning Tree:")
        for u, v, weight in mst:
            print(u, "-", v, ":", weight)

        print("Total MST Cost:", total_cost)


# Main Program
n = int(input("Enter number of vertices: "))
g = Graph(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, weight = map(
        int, input("Enter edge (u v weight): ").split()
    )
    g.add_edge(u, v, weight)

g.kruskal()
