class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.graph.append([v, u, w])
    
    def get_smallest_edge_from_vertex(self, vertex, visited):
        edges_to_use = []
        for edge in self.graph:
            if edge[1] not in visited and edge[0] == vertex:
                edges_to_use.append(edge)
        
        edges_to_use.sort(key=lambda x: x[2])
        return edges_to_use[0] if len(edges_to_use) != 0 else -1
    
    def nearest_neighbour(self, starting_vertex):
        visited = [starting_vertex]
        result = [self.get_smallest_edge_from_vertex(starting_vertex, visited)]
        for _ in range(self.V - 2):
            visited.append(result[len(result) - 1][1])
            result.append(self.get_smallest_edge_from_vertex(result[len(result) - 1][1], visited))
            if -1 in result:
                print(f'Can\'t build hamiltionian cycle using this algorithm.')
                return
        
        sum = 0
        path = f'{result[0][0]}'
        for edge in result:
            sum += edge[2]
            path += f' -> {edge[1]}'
        
        print(f'Length of path: {sum}')
        print(f'Path: {path}')
            
    



if __name__ == '__main__':
    g = Graph(7)
    g.add_edge(0, 1, 7)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 4, 7)
    g.add_edge(2, 4, 5)
    g.add_edge(3, 4, 15)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 8)
    g.add_edge(4, 6, 9)
    g.add_edge(5, 6, 11)
    g.nearest_neighbour(0)

    g1 = Graph(4)
    g1.add_edge(0, 1, 7)
    g1.add_edge(0, 2, 5)
    g1.add_edge(0, 3, 16)
    g1.add_edge(1, 2, 8)
    g1.add_edge(1, 3, 7)
    g1.add_edge(2, 3, 3)
    g1.nearest_neighbour(0)


