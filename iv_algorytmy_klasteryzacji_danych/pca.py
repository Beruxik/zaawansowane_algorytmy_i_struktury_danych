import pandas as pd
import numpy as np

def cluster_iris_data():
    # Load the iris dataset using pandas
    data = pd.read_csv('iris.csv')

    # Extract the features from the dataset
    features = data.iloc[:, :-1].values

    # Normalize the features
    normalized_features = (features - np.mean(features, axis=0)) / np.std(features, axis=0)

    # Calculate the covariance matrix
    covariance_matrix = np.cov(normalized_features.T)

    # Perform eigen decomposition on the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # Sort the eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Select the top k eigenvectors based on the explained variance
    k = 2
    selected_eigenvectors = sorted_eigenvectors[:, :k]

    # Project the data onto the selected eigenvectors
    projected_data = np.dot(normalized_features, selected_eigenvectors)

    # Perform clustering on the projected data (e.g., using k-means algorithm)

    # Return the clustered data
    return projected_data

def main():
    # Cluster the iris dataset using PCA
    clustered_data = cluster_iris_data()

    # Plot the data using matplotlib
    import matplotlib.pyplot as plt
    plt.scatter(clustered_data[:, 0], clustered_data[:, 1])
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Iris Dataset')
    plt.show()

    # Display the clustered data
    print(clustered_data)

if __name__ == '__main__':
    main()