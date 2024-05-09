from sklearn import datasets
import pandas as pd
import numpy as np

def split_data_into_train_and_test(data: pd.DataFrame, test_ratio: float = 0.2) -> tuple:
    test_size = int(len(data) * test_ratio)
    shuffled_indices = np.random.permutation(len(data))
    test_indices = shuffled_indices[:test_size]
    train_indices = shuffled_indices[test_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def split_data_into_features_and_labels(data: pd.DataFrame, label_class: str) -> tuple:
    features = data.drop(label_class, axis=1)
    labels = data[label_class]
    return features, labels

def minkowski(v1: pd.Series, v2: pd.Series, m: int = 2) -> np.float64:
    distance = 0
    for feature in v1.index:
        distance += abs(v1[feature] - v2[feature]) ** m
    return distance ** (1 / m)

def get_nearest_neighbors(train_features: pd.DataFrame, test_instance: pd.Series, k: int) -> pd.DataFrame:
    distances = train_features.apply(lambda x: minkowski(x, test_instance), axis=1)
    return distances.nsmallest(k)

def predict(nearest_neighbors: pd.DataFrame, train_labels: pd.Series) -> str:
    return train_labels.loc[nearest_neighbors.index].mode()[0]

def accuracy(predictions: pd.Series, test_labels: pd.Series) -> float:
    return (predictions == test_labels).sum() / len(test_labels)

def main() -> None:
    iris = pd.read_csv('iris.csv')
    train_set, test_set = split_data_into_train_and_test(iris, 0.2)
    train_features, train_labels = split_data_into_features_and_labels(train_set, 'variety')
    test_features, test_labels = split_data_into_features_and_labels(test_set, 'variety')
    
    k = 3
    predictions = pd.Series()
    for i in range(len(test_features)):
        nearest_neighbors = get_nearest_neighbors(train_features, test_features.iloc[i], k)
        predictions = pd.concat([predictions, pd.Series(predict(nearest_neighbors, train_labels))])
    
    
    predictions = predictions.reset_index(drop=True)
    test_labels = test_labels.reset_index(drop=True)
    print(f'Accuracy: {accuracy(predictions, test_labels) * 100}%')
    

if __name__ == '__main__':
    main()