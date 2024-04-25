from sklearn import datasets
import pandas as pd
import numpy as np

class KNN():
    def __init__(self, n: int = 3) -> None:
        self.n = n

    def fit(self, train_samples: pd.core.frame.DataFrame, train_labels: np.ndarray):
        self._classes = np.unique(train_labels)
        self.train_samples = train_samples
        self.train_labels = train_labels

    def predict(self, test_samples: pd.core.frame.DataFrame):
        pass

def main() -> None:
    iris = datasets.load_iris()
    iris = pd.DataFrame(
        data=np.c_[iris["data"], iris["target"]], columns=iris["feature_names"] + ["target"]
    )
    labels = iris['target'].values
    print(iris.shape[0])

if __name__ == '__main__':
    main()