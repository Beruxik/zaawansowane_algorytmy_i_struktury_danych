import numpy as np
import pandas as pd


def initialize_centroids(data, k):
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    return centroids


def assign_clusters(data, centroids):
    distances = np.sqrt(((data - centroids[:, np.newaxis]) ** 2).sum(axis=2))
    clusters = np.argmin(distances, axis=0)
    return clusters


def update_centroids(data, clusters, k):
    centroids = np.zeros((k, data.shape[1]))
    for i in range(k):
        centroids[i] = np.mean(data[clusters == i], axis=0)
    return centroids


def kmeans(data, k, max_iterations=10000):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, clusters, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return clusters


def main():
    # Load the iris dataset
    data = pd.read_csv("iris.csv")

    # Drop the target column if present
    if "variety" in data.columns:
        data = data.drop("variety", axis=1)

    # Convert the data to numpy array
    data = data.values
    # Perform k-means clustering
    k = 3  # Number of clusters
    clusters = kmeans(data, k)

    # Rename the clusters to iris species
    clusters = clusters.astype(str)  # Convert clusters to string type
    clusters[clusters == '0'] = "setosa"
    clusters[clusters == '1'] = "versicolor"
    clusters[clusters == '2'] = "virginica"

    print(clusters)


if __name__ == "__main__":
    main()
