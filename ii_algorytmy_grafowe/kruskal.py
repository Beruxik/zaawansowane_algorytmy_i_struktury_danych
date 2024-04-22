class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] < rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    
    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        minimum_cost = 0
        print('Krawędzie minimalnego drzewa rozpinającego')
        for u, v, weight in result:
            minimum_cost += weight
            print(f'{chr(ord("a") + u)} --- {chr(ord("a") + v)} waga: {weight}')
        print(f'Koszt minimalnego drzewa rozpinającego: {minimum_cost}')

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

    g.kruskal()