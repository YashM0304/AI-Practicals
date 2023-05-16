Kruskal Algorithm

class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def run(self):
        self.graph.sort(key=lambda x: x[2])
        union_find = UnionFind(self.vertices)
        mst = []

        for edge in self.graph:
            u, v, weight = edge
            root1 = union_find.find(u)
            root2 = union_find.find(v)
            if root1 != root2:
                mst.append(edge)
                union_find.union(root1, root2)

        return mst


vertices = ['A', 'B', 'C', 'D', 'E', 'F']
kruskal = Kruskal(vertices)


# Adding edges to the graph
kruskal.add_edge('A', 'B', 5)
kruskal.add_edge('A', 'C', 9)
kruskal.add_edge('A', 'F', 6)
kruskal.add_edge('B', 'C', 2)
kruskal.add_edge('B', 'D', 7)
kruskal.add_edge('C', 'D', 4)
kruskal.add_edge('C', 'F', 3)
kruskal.add_edge('D', 'E', 8)
kruskal.add_edge('E', 'F', 1)

# Running Kruskal's algorithm
minimum_spanning_tree = kruskal.run()

# Printing the minimum spanning tree
for edge in minimum_spanning_tree:
    print(edge)