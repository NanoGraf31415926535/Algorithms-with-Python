import numpy as np
from scipy.spatial.distance import euclidean

# Isotopic data for each artifact
artifact_data = {
    'Artifact A': np.array([24.1, 32.6, 4.8]),
    'Artifact B': np.array([24.0, 32.9, 4.6]),
    'Artifact C': np.array([10.5, 15.2, 25.8]),
    'Artifact D': np.array([24.3, 32.5, 5.0])
}

def calculate_euclidean_distance(profile1, profile2):
    """Calculates the Euclidean distance between two isotopic profiles."""
    return euclidean(profile1, profile2)

# Calculate the distance matrix
distances = {}
artifacts = list(artifact_data.keys())

for i in range(len(artifacts)):
    for j in range(i + 1, len(artifacts)):
        artifact1 = artifacts[i]
        artifact2 = artifacts[j]
        distance = calculate_euclidean_distance(artifact_data[artifact1], artifact_data[artifact2])
        distances[(artifact1, artifact2)] = distance
        distances[(artifact2, artifact1)] = distance # Distance is symmetric

print("Euclidean Distances between Artifact Isotopic Profiles:")
for (art1, art2), dist in distances.items():
    print(f"Distance between {art1} and {art2}: {dist:.3f}")

# Analyze the distances to find the most similar artifacts
print("\nAnalysis of Similarities:")

# Find the pair with the smallest distance
most_similar_pair = None
min_distance = float('inf')
for pair, dist in distances.items():
    if dist < min_distance:
        min_distance = dist
        most_similar_pair = pair

if most_similar_pair:
    print(f"The artifacts with the most similar Tin isotopic profiles are {most_similar_pair[0]} and {most_similar_pair[1]} with a distance of {min_distance:.3f}.")

# Identify artifacts that are significantly different
average_distance = np.mean(list(distances.values()))
distance_threshold_multiplier = 2 # A heuristic threshold - can be adjusted
significant_difference_threshold = average_distance * distance_threshold_multiplier

print(f"\nAverage distance: {average_distance:.3f}")
print(f"Threshold for significant difference (heuristic): {significant_difference_threshold:.3f}")

for artifact1 in artifacts:
    for artifact2 in artifacts:
        if artifact1 != artifact2 and distances[(artifact1, artifact2)] > significant_difference_threshold:
            print(f"{artifact1} and {artifact2} have a significantly different Tin isotopic profile (distance: {distances[(artifact1, artifact2)]:.3f}).")

# Conclusion based on the smallest distance
print("\nConclusion:")
if most_similar_pair:
    print(f"Based on the smallest Euclidean distance, {most_similar_pair[0]} and {most_similar_pair[1]} are the most likely to have originated from the same source based on their Tin isotopic composition.")
    # Further analysis could involve comparing the distances of other pairs to this minimum.
    # For example, if the next smallest distance is significantly larger, it strengthens this conclusion.

    other_artifacts = [art for art in artifacts if art not in most_similar_pair]
    for art in other_artifacts:
        dist_to_pair1 = distances.get((art, most_similar_pair[0]))
        dist_to_pair2 = distances.get((art, most_similar_pair[1]))
        if dist_to_pair1 is not None and dist_to_pair2 is not None and (dist_to_pair1 > min_distance * 2 or dist_to_pair2 > min_distance * 2):
            print(f"{art}'s Tin isotopic profile appears different from the likely source of {most_similar_pair[0]} and {most_similar_pair[1]}.")
else:
    print("Could not determine the most similar pair.")