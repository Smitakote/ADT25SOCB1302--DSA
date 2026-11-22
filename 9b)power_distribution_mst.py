
# Assignment 9B: Power Distribution Network Optimization
# Minimum Spanning Tree using Kruskal's Algorithm

class PowerNetwork:
    def __init__(self, substations):
        self.substations = substations
        self.edges = []

    # Add Connection Between Substations
    def add_connection(self, u, v, cost):
        self.edges.append((cost, u, v))

    # Find Parent
    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(
                parent, parent[vertex]
            )
        return parent[vertex]

    # Union Operation
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

        parent = list(range(self.substations))
        rank = [0] * self.substations

        mst = []
        total_cost = 0

        for cost, u, v in self.edges:
            if self.union(parent, rank, u, v):
                mst.append((u, v, cost))
                total_cost += cost

        print("\nMinimum Spanning Tree:")

        if len(mst) != self.substations - 1:
            print("Network is disconnected!")
            return

        for u, v, cost in mst:
            print("Substation", u, "- Substation", v,
                  "Cost:", cost)

        print("\nMinimum Wiring Cost:", total_cost)


# Main Program
n = int(input("Enter number of substations: "))

network = PowerNetwork(n)

e = int(input("Enter number of connections: "))

for i in range(e):
    u, v, cost = map(
        int, input("Enter connection (u v cost): ").split()
    )

    network.add_connection(u, v, cost)

network.kruskal()
