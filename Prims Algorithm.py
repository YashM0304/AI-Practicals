import heapq

class Prim:
    def __init__(self, graph):
        self.graph = graph

    def run(self, start_vertex):
        minimum_spanning_tree = []
        visited = set()
        heap = []

        # Start with the given start_vertex
        visited.add(start_vertex)
        self.add_edges_to_heap(start_vertex, heap)

        while heap:
            weight, vertex, neighbor = heapq.heappop(heap)

            if neighbor not in visited:
                visited.add(neighbor)
                minimum_spanning_tree.append((vertex, neighbor, weight))
                self.add_edges_to_heap(neighbor, heap)

        return minimum_spanning_tree

    def add_edges_to_heap(self, vertex, heap):
        for neighbor, weight in self.graph[vertex].items():
            heapq.heappush(heap, (weight, vertex, neighbor))
            
graph = {
    'A': {'B': 5, 'C': 9, 'F': 6},
    'B': {'A': 5, 'C': 2, 'D': 7},
    'C': {'A': 9, 'B': 2, 'D': 4, 'F': 3},
    'D': {'B': 7, 'C': 4, 'E': 8},
    'E': {'D': 8, 'F': 1},
    'F': {'A': 6, 'C': 3, 'E': 1}
}

prim = Prim(graph)

minimum_spanning_tree = prim.run('A')

for edge in minimum_spanning_tree:
    print(edge)
