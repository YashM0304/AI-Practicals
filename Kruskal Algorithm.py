class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        self.graph.sort(key=lambda x: x[2])  # Sort edges by weight
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        minimumCost = 0

        for u, v, w in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)
                minimumCost += w

        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree Cost:", minimumCost)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()
