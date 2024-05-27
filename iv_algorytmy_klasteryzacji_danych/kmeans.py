import csv
import random
import math

def load_iris_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([float(x) for x in row])
    return data

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def initialize_centroids(data, k):
    centroids = random.sample(data, k)
    return centroids

def assign_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    return clusters

def update_centroids(clusters):
    centroids = []
    for cluster in clusters:
        centroid = [sum(x) / len(cluster) for x in zip(*cluster)]
        centroids.append(centroid)
    return centroids

def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if centroids == new_centroids:
            break
        centroids = new_centroids
    return clusters

# Usage example
data = load_iris_data('iris.csv')
clusters = kmeans(data, k=3)
for i, cluster in enumerate(clusters):
    print(f'Cluster {i+1}:')
    for point in cluster:
        print(point)
    print()