import numpy as np
from scipy.optimize import minimize

class LogisticRegression:
    def __init__(self):
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        """
        Sigmoid activation function.
        """
        return 1 / (1 + np.exp(-z))

    def _cost_function(self, params, X, y):
        """
        Logistic regression cost function (cross-entropy).
        """
        m = len(y)
        weights = params[:-1]
        bias = params[-1]
        z = np.dot(X, weights) + bias
        h = self._sigmoid(z)
        cost = (-1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
        return cost

    def _gradient(self, params, X, y):
        """
        Gradient of the cost function.
        """
        m = len(y)
        weights = params[:-1]
        bias = params[-1]
        z = np.dot(X, weights) + bias
        h = self._sigmoid(z)
        dw = (1 / m) * np.dot(X.T, (h - y))
        db = (1 / m) * np.sum(h - y)
        return np.concatenate((dw, [db]))

    def fit(self, X, y):
        """
        Fits the logistic regression model to the training data using optimization.

        Args:
            X (numpy.ndarray): Training features (n_samples, n_features).
            y (numpy.ndarray): Binary target values (n_samples,).
        """
        initial_params = np.zeros(X.shape[1] + 1)  # Initialize weights and bias
        result = minimize(self._cost_function, initial_params, args=(X, y),
                          method='BFGS', jac=self._gradient)
        self.weights = result.x[:-1]
        self.bias = result.x[-1]

    def predict_proba(self, X):
        """
        Predicts the probability of the positive class for new data.

        Args:
            X (numpy.ndarray): Test features (n_samples, n_features).

        Returns:
            numpy.ndarray: Probabilities of the positive class (n_samples,).
        """
        z = np.dot(X, self.weights) + self.bias
        return self._sigmoid(z)

    def predict(self, X, threshold=0.5):
        """
        Predicts the class labels for new data based on a threshold.

        Args:
            X (numpy.ndarray): Test features (n_samples, n_features).
            threshold (float): Probability threshold for classification.

        Returns:
            numpy.ndarray: Predicted class labels (0 or 1) (n_samples,).
        """
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)

# Example Usage:
if __name__ == '__main__':
    # Generate some synthetic binary classification data
    np.random.seed(0)
    X = np.random.rand(100, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)

    # Create and train the model
    model = LogisticRegression()
    model.fit(X, y)

    # Make predictions
    X_test = np.array([[0.5, 0.5], [1.5, 1.5]])
    probabilities = model.predict_proba(X_test)
    predictions = model.predict(X_test)
    print(f"Probabilities for X_test = {X_test}: {probabilities}")
    print(f"Predictions for X_test = {X_test}: {predictions}")
    print(f"Learned weights: {model.weights}, bias: {model.bias}")