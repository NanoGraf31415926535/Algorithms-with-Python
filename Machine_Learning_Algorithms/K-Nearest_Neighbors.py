import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        """
        Stores the training data.

        Args:
            X (numpy.ndarray): Training features (n_samples, n_features).
            y (numpy.ndarray): Target values (n_samples,).
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """
        Predicts the class labels for new data points.

        Args:
            X (numpy.ndarray): Test features (n_samples, n_features).

        Returns:
            numpy.ndarray: Predicted class labels (n_samples,).
        """
        predictions = [self._predict_single(x) for x in X]
        return np.array(predictions)

    def _predict_single(self, x):
        """
        Predicts the class label for a single data point.

        Args:
            x (numpy.ndarray): Single test feature vector (n_features,).

        Returns:
            int or float: Predicted class label.
        """
        # Calculate the Euclidean distances between the test point and all training points
        distances = np.sqrt(np.sum((self.X_train - x)**2, axis=1))

        # Get the indices of the k-nearest neighbors
        k_nearest_indices = np.argsort(distances)[:self.k]

        # Get the labels of the k-nearest neighbors
        k_nearest_labels = self.y_train[k_nearest_indices]

        # Return the most common class label among the neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# Example Usage:
if __name__ == '__main__':
    # Generate some synthetic classification data
    np.random.seed(0)
    X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    y = np.array([0, 0, 1, 1, 0, 1])

    # Create and train the model
    knn = KNN(k=3)
    knn.fit(X, y)

    # Make predictions
    X_test = np.array([[2, 2], [7, 8], [1, 1]])
    predictions = knn.predict(X_test)
    print(f"Predictions for X_test = {X_test}: {predictions}")