import numpy as np
from collections import Counter

class DecisionTreeClassifier:
    def __init__(self, min_samples_split=2, max_depth=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_nodes = 0  # For tracking the number of nodes in the tree
        self.tree = None

    def _gini(self, y):
        """Calculates the Gini impurity of a set of labels."""
        if len(y) == 0:
            return 0
        counts = Counter(y)
        impurity = 1.0
        for label in counts:
            prob = counts[label] / len(y)
            impurity -= prob**2
        return impurity

    def _split(self, X, y, feature_index, threshold):
        """Splits the dataset based on a feature and a threshold."""
        left_indices = np.where(X[:, feature_index] <= threshold)[0]
        right_indices = np.where(X[:, feature_index] > threshold)[0]
        X_left, y_left = X[left_indices], y[left_indices]
        X_right, y_right = X[right_indices], y[right_indices]
        return X_left, y_left, X_right, y_right

    def _best_split(self, X, y):
        """Finds the best split for the current node."""
        best_gini = 1.0
        best_feature_index = None
        best_threshold = None
        n_samples, n_features = X.shape

        if n_samples < self.min_samples_split:
            return None, None

        for feature_index in range(n_features):
            # Consider unique values as potential thresholds
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                X_left, y_left, X_right, y_right = self._split(X, y, feature_index, threshold)
                if len(y_left) > 0 and len(y_right) > 0:
                    gini_left = self._gini(y_left)
                    gini_right = self._gini(y_right)
                    gini = (len(y_left) / n_samples) * gini_left + (len(y_right) / n_samples) * gini_right
                    if gini < best_gini:
                        best_gini = gini
                        best_feature_index = feature_index
                        best_threshold = threshold
        return best_feature_index, best_threshold

    def _build_tree(self, X, y, depth=0):
        """Recursively builds the decision tree."""
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Stopping conditions
        if (self.max_depth is not None and depth >= self.max_depth) or \
           n_labels == 1 or n_samples < self.min_samples_split:
            self.n_nodes += 1
            return Counter(y).most_common(1)[0][0]  # Return the majority class

        best_feature_index, best_threshold = self._best_split(X, y)

        if best_feature_index is not None:
            X_left, y_left, X_right, y_right = self._split(X, y, best_feature_index, best_threshold)
            self.n_nodes += 1
            return (best_feature_index,
                    best_threshold,
                    self._build_tree(X_left, y_left, depth + 1),
                    self._build_tree(X_right, y_right, depth + 1))
        else:
            # No good split found (e.g., all samples have the same features)
            self.n_nodes += 1
            return Counter(y).most_common(1)[0][0]

    def fit(self, X, y):
        """Builds the decision tree from the training data."""
        self.tree = self._build_tree(X, y)
        return self

    def predict(self, X):
        """Predicts the class labels for new data points."""
        return np.array([self._predict_single(x, self.tree) for x in X])

    def _predict_single(self, x, node):
        """Predicts the class label for a single data point using the learned tree."""
        if not isinstance(node, tuple):  # Leaf node
            return node

        feature_index, threshold, left_child, right_child = node

        if x[feature_index] <= threshold:
            return self._predict_single(x, left_child)
        else:
            return self._predict_single(x, right_child)

# Example Usage:
if __name__ == '__main__':
    # Generate a simple dataset
    X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    y = np.array([0, 0, 1, 1, 0, 1])

    # Create and train the Decision Tree classifier
    dt_classifier = DecisionTreeClassifier(min_samples_split=2, max_depth=3)
    dt_classifier.fit(X, y)

    # Make predictions
    X_test = np.array([[2, 2], [7, 8], [1, 1]])
    predictions = dt_classifier.predict(X_test)
    print(f"Predictions for X_test = {X_test}: {predictions}")
    print(f"Number of nodes in the tree: {dt_classifier.n_nodes}")

    # You can try with a deeper tree or different data
    dt_classifier_deep = DecisionTreeClassifier(min_samples_split=1, max_depth=None)
    dt_classifier_deep.fit(X, y)
    print(f"Number of nodes in the deeper tree: {dt_classifier_deep.n_nodes}")