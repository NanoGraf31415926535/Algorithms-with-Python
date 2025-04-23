import numpy as np

class LinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None

    def fit(self, X, y, learning_rate=0.01, n_iterations=1000):
        """
        Fits the linear regression model to the training data using gradient descent.

        Args:
            X (numpy.ndarray): Training features (n_samples, n_features).
            y (numpy.ndarray): Target values (n_samples,).
            learning_rate (float): Step size for gradient descent.
            n_iterations (int): Number of iterations for gradient descent.
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(n_iterations):
            # Calculate predictions
            y_predicted = np.dot(X, self.weights) + self.bias

            # Calculate gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update weights and bias
            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db

    def predict(self, X):
        """
        Predicts target values for new data.

        Args:
            X (numpy.ndarray): Test features (n_samples, n_features).

        Returns:
            numpy.ndarray: Predicted target values (n_samples,).
        """
        return np.dot(X, self.weights) + self.bias

# Example Usage:
if __name__ == '__main__':
    # Generate some synthetic data
    X = np.array([[1], [2], [3], [4]], dtype=np.float32)
    y = np.array([2, 4, 6, 8], dtype=np.float32)

    # Create and train the model
    model = LinearRegression()
    model.fit(X, y, learning_rate=0.01, n_iterations=1000)

    # Make predictions
    X_test = np.array([[5], [6]], dtype=np.float32)
    predictions = model.predict(X_test)
    print(f"Predictions for X_test = {X_test}: {predictions}")
    print(f"Learned weights: {model.weights}, bias: {model.bias}")