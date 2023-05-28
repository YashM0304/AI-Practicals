class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def graph_coloring(self):
        result = [-1] * self.vertices  # Stores the assigned colors for vertices
        result[0] = 0  # Assign the first color to the first vertex

        available_colors = [False] * self.vertices  # Track the availability of colors

        for u in range(1, self.vertices):
            for v in range(self.vertices):
                if self.adj_matrix[u][v] == 1 and result[v] != -1:
                    available_colors[result[v]] = True

            # Find the first available color
            color = 0
            while available_colors[color]:
                color += 1

            result[u] = color  # Assign the found color to the current vertex

            # Reset the availability for the next vertex
            available_colors = [False] * self.vertices

        return result


# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

colors = g.graph_coloring()
print("Assigned Colors:", colors)
