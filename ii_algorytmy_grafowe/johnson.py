from math import inf

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def johnsons_bellman_ford(self):
        dist_from_q_to_u = [inf for _ in range(self.V)]
        dist_from_q_to_u.append(0)

        for i in range(self.V):
            self.add_edge(self.V, i, 0)

        for _ in range(self.V - 1):
            for edge in self.graph:
                # if d[u] + w[u, v] < d[v]
                if dist_from_q_to_u[edge[0]] + edge[2] < dist_from_q_to_u[edge[1]]:
                    dist_from_q_to_u[edge[1]] = dist_from_q_to_u[edge[0]] + edge[2]
        
        dist_from_q_to_u.pop()
        return dist_from_q_to_u
    
    def remove_q(self):
        graph_wo_q = [edge for edge in self.graph if edge[0] != self.V]
        return graph_wo_q

    def change_edge_weights(self, dist_from_q_to_u):
        self.graph = self.remove_q()
        for edge in self.graph:
            edge[2] = dist_from_q_to_u[edge[0]] + edge[2] - dist_from_q_to_u[edge[1]]

    def dijkstra(self, start):
        distances = {i: (0 if i == start else inf) for i in range(self.V)}
        edges = {i: [] for i in range(self.V)}

        for i in range(self.V):
            for edge in self.graph:
                if edge[0] == i:
                    edges[i].append(edge)

        pred = [-1 for _ in range(self.V)]
        visited_nodes = []

        for _ in range(self.V):
            for node in sorted(distances.items(), key=lambda x:x[1]):
                if node[0] not in visited_nodes:
                    current_node = node[0]
                    visited_nodes.append(node[0])
                    break

            for edge in edges[current_node]:
                print(edges[current_node])
                if distances[edge[0]] + edge[2] < distances[edge[1]]:
                    distances[edge[1]] = distances[edge[0]] + edge[2]
                    pred[edge[1]] = edge[0]
        
        return (distances, pred)

    def johnson(self, start):
        self.change_edge_weights(self.johnsons_bellman_ford())
        return self.dijkstra(start)
            



def main():
    g = Graph(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 4, 1)
    g.add_edge(2, 1, 7)
    g.add_edge(2, 3, -2)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -5)
    distances, pred = g.johnson(0)
    print(f'Distances: {distances}')
    print(f'Pred: {pred}')
    

if __name__ == '__main__':
    main()