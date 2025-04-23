import numpy as np

class GaussianNaiveBayes:
    def fit(self, X, y):
        """
        Fits the Gaussian Naive Bayes model to the training data.

        Args:
            X (numpy.ndarray): Training features (n_samples, n_features).
            y (numpy.ndarray): Target values (n_samples,).
        """
        self.classes = np.unique(y)
        self.mean = {}
        self.variance = {}
        self.prior = {}

        for c in self.classes:
            X_c = X[y == c]
            self.mean[c] = np.mean(X_c, axis=0)
            self.variance[c] = np.var(X_c, axis=0)
            self.prior[c] = len(X_c) / len(y)

    def _pdf(self, x, mean, variance):
        """
        Calculates the probability density function of the Gaussian distribution.
        """
        numerator = np.exp(-((x - mean)**2) / (2 * variance + 1e-9)) # Adding a small constant for numerical stability
        denominator = np.sqrt(2 * np.pi * variance + 1e-9)
        return numerator / denominator

    def predict_proba(self, X):
        """
        Calculates the posterior probabilities for each class.

        Args:
            X (numpy.ndarray): Test features (n_samples, n_features).

        Returns:
            numpy.ndarray: Probability of each class for each sample (n_samples, n_classes).
        """
        n_samples = X.shape[0]
        n_classes = len(self.classes)
        probabilities = np.zeros((n_samples, n_classes))

        for i, x in enumerate(X):
            for j, c in enumerate(self.classes):
                prior_prob = self.prior[c]
                likelihood = np.prod(self._pdf(x, self.mean[c], self.variance[c]))
                posterior_prob = prior_prob * likelihood
                probabilities[i, j] = posterior_prob

            # Normalize probabilities to sum to 1 (though not strictly necessary for prediction)
            probabilities[i, :] /= np.sum(probabilities[i, :])

        return probabilities

    def predict(self, X):
        """
        Predicts the class labels for new data points.

        Args:
            X (numpy.ndarray): Test features (n_samples, n_features).

        Returns:
            numpy.ndarray: Predicted class labels (n_samples,).
        """
        probabilities = self.predict_proba(X)
        return self.classes[np.argmax(probabilities, axis=1)]

# Example Usage:
if __name__ == '__main__':
    # Generate some synthetic data with two classes
    np.random.seed(0)
    X = np.concatenate([np.random.randn(50, 2) + [2, 2],
                        np.random.randn(50, 2) + [-2, -2]])
    y = np.concatenate([np.zeros(50), np.ones(50)])

    # Create and train the Gaussian Naive Bayes classifier
    gnb = GaussianNaiveBayes()
    gnb.fit(X, y)

    # Make predictions
    X_test = np.array([[1, 1], [-1, -1], [3, 3]])
    predictions = gnb.predict(X_test)
    probabilities = gnb.predict_proba(X_test)
    print(f"Predictions for X_test = {X_test}: {predictions}")
    print(f"Probabilities for X_test = {X_test}:\n{probabilities}")
    print("Class Priors:", gnb.prior)
    print("Class Means:\n", gnb.mean)
    print("Class Variances:\n", gnb.variance)