

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]
    
    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        
    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for adjacent in self.adj[v]:
            if not visited[adjacent]:
                self.dfs(adjacent, visited)

    def dfs_traversal(self, s):
        visited = [False] * self.V
        self.dfs(s, visited)

# Create a graph
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)

# Perform DFS traversal starting from vertex 0
print("Following is Depth First Traversal (starting from vertex 0):")
g.dfs_traversal(0)
