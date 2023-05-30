from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]
    
    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def bfs(self, s):
        visited = [False] * self.V
        queue = deque()

        visited[s] = True
        queue.append(s)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for adjacent in self.adj[vertex]:
                if not visited[adjacent]:
                    visited[adjacent] = True
                    queue.append(adjacent)
                    
                    # Create a graph
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform BFS traversal starting from vertex 2
print("Following is Breadth First Traversal (starting from vertex 2):")
g.bfs(2)

# O(n^d) O(n)
