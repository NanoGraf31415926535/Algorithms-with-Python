import numpy as np

class KMeans:
    def __init__(self, n_clusters=2, max_iterations=100):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.centroids = None

    def fit(self, X):
        """
        Fits the K-Means model to the data.

        Args:
            X (numpy.ndarray): Training data (n_samples, n_features).
        """
        n_samples, n_features = X.shape

        # Initialize centroids randomly
        random_indices = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_indices]

        for _ in range(self.max_iterations):
            # Assign each data point to the closest centroid
            distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
            labels = np.argmin(distances, axis=0)

            # Update centroids
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])

            # Check for convergence
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids

        self.labels_ = labels
        return self

    def predict(self, X):
        """
        Predicts the cluster for new data points.

        Args:
            X (numpy.ndarray): New data (n_samples, n_features).

        Returns:
            numpy.ndarray: Cluster labels for each data point.
        """
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

# Example Usage:
if __name__ == '__main__':
    # Generate some synthetic data
    np.random.seed(0)
    X = np.concatenate([np.random.randn(50, 2) + [2, 2],
                        np.random.randn(50, 2) + [-2, -2]], axis=0)

    # Create and train the model
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    labels = kmeans.labels_
    centroids = kmeans.centroids

    print("Cluster Labels:", labels)
    print("Centroids:", centroids)

    # You could then visualize the clusters using matplotlib if you have it installed.