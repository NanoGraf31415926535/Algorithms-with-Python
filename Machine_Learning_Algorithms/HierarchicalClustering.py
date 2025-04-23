import numpy as np
from scipy.spatial.distance import pdist, squareform

class HierarchicalClustering:
    def __init__(self, n_clusters=None, linkage='single'):
        self.n_clusters = n_clusters
        self.linkage = linkage
        self.merges = []

    def _pairwise_distance(self, X):
        """Calculates the pairwise distance matrix."""
        return squareform(pdist(X))

    def _merge_clusters(self, clusters, distance_matrix, linkage='single'):
        """Finds the two closest clusters to merge."""
        min_distance = np.inf
        cluster_i = -1
        cluster_j = -1

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = self._calculate_linkage_distance(clusters[i], clusters[j], distance_matrix, linkage)
                if dist < min_distance:
                    min_distance = dist
                    cluster_i = i
                    cluster_j = j
        return cluster_i, cluster_j, min_distance

    def _calculate_linkage_distance(self, cluster1, cluster2, distance_matrix, linkage='single'):
        """Calculates the distance between two clusters based on the linkage method."""
        min_dist = np.inf
        max_dist = -np.inf
        avg_dist = 0
        count = 0

        for i in cluster1:
            for j in cluster2:
                dist = distance_matrix[i, j]
                min_dist = min(min_dist, dist)
                max_dist = max(max_dist, dist)
                avg_dist += dist
                count += 1

        if linkage == 'single':
            return min_dist
        elif linkage == 'complete':
            return max_dist
        elif linkage == 'average':
            return avg_dist / count if count > 0 else 0
        else:
            raise ValueError(f"Unknown linkage type: {linkage}")

    def fit(self, X):
        """Performs hierarchical clustering."""
        n_samples = X.shape[0]
        clusters = [[i] for i in range(n_samples)]
        distance_matrix = self._pairwise_distance(X)
        self.merges = []

        while len(clusters) > 1:
            if self.n_clusters is not None and len(clusters) <= self.n_clusters:
                break

            i, j, distance = self._merge_clusters(clusters, distance_matrix, self.linkage)
            merged_cluster = clusters[i] + clusters[j]
            self.merges.append((clusters[i], clusters[j], distance))

            # Remove the merged clusters (in reverse order to avoid index issues)
            if i < j:
                del clusters[j]
                del clusters[i]
            else:
                del clusters[i]
                del clusters[j]

            clusters.append(merged_cluster)

        self.labels_ = np.zeros(n_samples, dtype=int)
        if self.n_clusters is not None and len(clusters) == self.n_clusters:
            for idx, cluster in enumerate(clusters):
                for i in cluster:
                    self.labels_[i] = idx
        elif self.n_clusters == 1 and len(clusters) == 1:
            for i in clusters[0]:
                self.labels_[i] = 0
        else:
            # If n_clusters is not specified, the labels correspond to the final single cluster
            for i in clusters[0]:
                self.labels_[i] = 0

        return self

    def fit_predict(self, X):
        """Performs hierarchical clustering and returns cluster labels."""
        self.fit(X)
        return self.labels_

# Example Usage:
if __name__ == '__main__':
    # Simple dataset
    X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

    # Perform hierarchical clustering and get 2 clusters using single linkage
    hc = HierarchicalClustering(n_clusters=2, linkage='single')
    labels = hc.fit_predict(X)
    print("Cluster Labels (Single Linkage, 2 clusters):", labels)
    print("Merges (Single Linkage):", hc.merges)

    # Perform hierarchical clustering and get 3 clusters using complete linkage
    hc_complete = HierarchicalClustering(n_clusters=3, linkage='complete')
    labels_complete = hc_complete.fit_predict(X)
    print("Cluster Labels (Complete Linkage, 3 clusters):", labels_complete)
    print("Merges (Complete Linkage):", hc_complete.merges)