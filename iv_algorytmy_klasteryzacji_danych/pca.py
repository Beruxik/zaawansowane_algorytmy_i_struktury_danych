import numpy as np


def pca(data: np.ndarray, n_components: int) -> np.ndarray:
    data_meaned = data - np.mean(data, axis=0)

    cov_matrix = np.cov(data_meaned, rowvar=False)

    eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)

    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvectors = eigen_vectors[:, sorted_index]

    eigenvector_subset = sorted_eigenvectors[:, 0:n_components]

    data_reduced = np.dot(
        eigenvector_subset.transpose(), data_meaned.transpose()
    ).transpose()

    return data_reduced


def main():
    X = np.random.randint(10, 50, 100).reshape(20, 5)

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Get the IRIS dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    data = pd.read_csv(
        url,
        names=["sepal length", "sepal width", "petal length", "petal width", "target"],
    )

    x = data.iloc[:, 0:4]

    target = data.iloc[:, 4]

    mat_reduced = pca(x, 2)

    principal_df = pd.DataFrame(mat_reduced, columns=["PC1", "PC2"])

    principal_df = pd.concat([principal_df, pd.DataFrame(target)], axis=1)

    plt.figure(figsize=(6, 6))
    sns.scatterplot(
        data=principal_df, x="PC1", y="PC2", hue="target", s=60, palette="icefire"
    )
    plt.show()


if __name__ == "__main__":
    main()
