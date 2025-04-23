import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components_ = None
        self.mean_ = None

    def fit(self, X):
        """
        Fits the PCA model to the data.

        Args:
            X (numpy.ndarray): Training data (n_samples, n_features).
        """
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

        # Calculate the covariance matrix
        covariance_matrix = np.cov(X_centered, rowvar=False)

        # Calculate the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

        # Sort the eigenvalues in descending order and get the corresponding eigenvectors
        sorted_indices = np.argsort(eigenvalues)[::-1]
        sorted_eigenvalues = eigenvalues[sorted_indices]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]

        # Select the top n_components eigenvectors
        self.components_ = sorted_eigenvectors[:, :self.n_components]

    def transform(self, X):
        """
        Applies dimensionality reduction to the input data.

        Args:
            X (numpy.ndarray): Input data (n_samples, n_features).

        Returns:
            numpy.ndarray: Transformed data (n_samples, n_components).
        """
        X_centered = X - self.mean_
        return np.dot(X_centered, self.components_)

    def fit_transform(self, X):
        """
        Fits the PCA model and then applies dimensionality reduction to the data.

        Args:
            X (numpy.ndarray): Training data (n_samples, n_features).

        Returns:
            numpy.ndarray: Transformed data (n_samples, n_components).
        """
        self.fit(X)
        return self.transform(X)

# Example Usage:
if __name__ == '__main__':
    # Generate some synthetic data with some correlation
    np.random.seed(0)
    X = np.random.rand(100, 2)
    X[:, 1] = 2 * X[:, 0] + 0.5 * np.random.randn(100)

    # Create and apply PCA to reduce to 1 component
    pca = PCA(n_components=1)
    X_reduced = pca.fit_transform(X)

    print("Original Data Shape:", X.shape)
    print("Reduced Data Shape:", X_reduced.shape)
    print("Principal Components:\n", pca.components_)
    print("Mean of Original Data:\n", pca.mean_)

    # You could then try to reconstruct the data (with loss of information)
    # X_reconstructed = np.dot(X_reduced, pca.components_.T) + pca.mean_