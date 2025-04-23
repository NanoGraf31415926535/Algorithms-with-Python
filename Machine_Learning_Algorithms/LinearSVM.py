import numpy as np

class LinearSVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Ensure y is in {-1, 1}
        y_ = np.where(y <= 0, -1, 1)

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.weights) - self.bias) >= 1
                if condition:
                    self.weights -= self.lr * (2 * self.lambda_param * self.weights)
                else:
                    self.weights -= self.lr * (2 * self.lambda_param * self.weights - np.dot(x_i, y_[idx]))
                    self.bias -= self.lr * y_[idx]

    def predict(self, X):
        linear_output = np.dot(X, self.weights) - self.bias
        return np.sign(linear_output)

# Example Usage:
if __name__ == '__main__':
    # Generate some linearly separable data
    np.random.seed(0)
    X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
    y = np.concatenate([-np.ones(20), np.ones(20)])

    # Create and train the Linear SVM classifier
    svm = LinearSVM(learning_rate=0.001, lambda_param=0.01, n_iters=1000)
    svm.fit(X, y)

    # Make predictions
    X_test = np.array([[0, 0], [3, 3], [-3, -3]])
    predictions = svm.predict(X_test)
    print(f"Predictions for X_test = {X_test}: {predictions}")
    print(f"Learned weights: {svm.weights}, bias: {svm.bias}")

    # You could also try to visualize the decision boundary if you have matplotlib.
    # The decision boundary is where np.dot(X, svm.weights) - svm.bias = 0