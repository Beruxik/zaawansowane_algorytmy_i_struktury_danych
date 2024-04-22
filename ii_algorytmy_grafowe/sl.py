from math import inf

def sl(graph):
    degrees = {i: 0 for i in range(len(graph))}
    neighbours = {i: [] for i in range(len(graph))}

    for i, row in enumerate(graph):
        degree = 0
        for j, weight in enumerate(row):
            if weight not in (0, inf):
                degree += 1
                neighbours[i].append(j)

        degrees[i] = degree
    
    degrees = dict(sorted(degrees.items(), key=lambda x: (x[1], x[0])))
    vertices_sorted_by_degrees = list(degrees.keys())

    colors = {}
    
    while vertices_sorted_by_degrees:
        vertice = vertices_sorted_by_degrees.pop()
        color = 0
        for v in colors:
            if colors[v] == color and v in neighbours[vertice]:
                color += 1
        
        colors[vertice] = color
    
    colors_translated = {}
    for color in colors:
        colors_translated[chr(ord('a') + color)] = colors[color]

    return colors_translated

graph = [
    [0, 4, inf, inf, 1, 2],
    [4, 0, 2, inf, 2, inf],
    [inf, 2, 0, 8, inf, inf],
    [inf, inf, 8, 0, 3, 6],
    [1, 2, inf, 3, 0, 7],
    [2, inf, inf, 6, 7, 0],
]

graph2 = [
    [0, 7, inf, 5, inf, inf, inf],
    [7, 0, 8, 9, 7, inf, inf],
    [inf, 8, 0, inf, 5, inf, inf],
    [5, 9, inf, 0, 15, 6, inf],
    [inf, 7, 5, 15, 0, 8, 9],
    [inf, inf, inf, 6, 8, 0, 11],
    [inf, inf, inf, inf, 9, 11, 0],
]

print(sl(graph))
print(sl(graph2))