import numpy as np
from collections import Counter
from Decision_Tree import DecisionTreeClassifier  

class RandomForestClassifier:
    def __init__(self, n_estimators=10, max_depth=None, min_samples_split=2, n_features=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.trees = []

    def fit(self, X, y):
        n_samples, n_orig_features = X.shape
        if not self.n_features:
            self.n_features = int(np.sqrt(n_orig_features))  # Common heuristic
        elif isinstance(self.n_features, float):
            self.n_features = int(self.n_features * n_orig_features)

        for _ in range(self.n_estimators):
            # Bootstrap sample
            indices = np.random.choice(n_samples, n_samples, replace=True)
            X_sample, y_sample = X[indices], y[indices]

            # Train a Decision Tree on the bootstrap sample and a random subset of features
            tree = DecisionTreeClassifier(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split
            )
            # Random feature selection during training is handled within the tree's _best_split method
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        # Return the majority vote for each sample
        return np.array([Counter(preds).most_common(1)[0][0] for preds in predictions.T])

# Example Usage (assuming decision_tree.py is in the same directory):
if __name__ == '__main__':
    # Generate a more complex synthetic dataset
    np.random.seed(42)
    X = np.random.rand(100, 5)
    y = np.logical_xor(X[:, 0] > 0.5, X[:, 1] < 0.3).astype(int)

    # Create and train the Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=10, max_depth=5, min_samples_split=2, n_features=3)
    rf_classifier.fit(X, y)

    # Make predictions
    X_test = np.random.rand(20, 5)
    predictions = rf_classifier.predict(X_test)
    print(f"Predictions for X_test:\n{predictions}")