import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Isotopic data for each artifact
artifact_data = {
    'Artifact A': np.array([24.1, 32.6, 4.8]),
    'Artifact B': np.array([24.0, 32.9, 4.6]),
    'Artifact C': np.array([10.5, 15.2, 25.8]),
    'Artifact D': np.array([24.3, 32.5, 5.0])
}

# Artifact names and their corresponding data points
artifact_names = list(artifact_data.keys())
data_points = np.array(list(artifact_data.values()))

# Calculate Euclidean distances (same as before)
def calculate_euclidean_distance(profile1, profile2):
    return euclidean(profile1, profile2)

distances = {}
for i in range(len(artifact_names)):
    for j in range(i + 1, len(artifact_names)):
        name1 = artifact_names[i]
        name2 = artifact_names[j]
        distance = calculate_euclidean_distance(artifact_data[name1], artifact_data[name2])
        distances[(name1, name2)] = distance
        distances[(name2, name1)] = distance

print("Euclidean Distances between Artifact Isotopic Profiles:")
for (art1, art2), dist in distances.items():
    print(f"Distance between {art1} and {art2}: {dist:.3f}")

# --- Plotting in 3D ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the artifacts
scatter = ax.scatter(data_points[:, 0], data_points[:, 1], data_points[:, 2], s=100, c=['r', 'g', 'b', 'm'])

# Annotate each point with the artifact name
for i, name in enumerate(artifact_names):
    ax.text(data_points[i, 0], data_points[i, 1], data_points[i, 2], name)

# Draw lines connecting the most similar pair
most_similar_pair = None
min_distance = float('inf')
for pair, dist in distances.items():
    if dist < min_distance:
        min_distance = dist
        most_similar_pair = pair

if most_similar_pair:
    art1_name, art2_name = most_similar_pair
    art1_data = artifact_data[art1_name]
    art2_data = artifact_data[art2_name]
    ax.plot([art1_data[0], art2_data[0]], [art1_data[1], art2_data[1]], [art1_data[2], art2_data[2]], 'k--', linewidth=2, label=f'Most Similar (Dist: {min_distance:.3f})')
    ax.legend()

ax.set_xlabel('$^{118}$Sn Abundance (%)')
ax.set_ylabel('$^{120}$Sn Abundance (%)')
ax.set_zlabel('$^{122}$Sn Abundance (%)')
ax.set_title('3D Visualization of Tin Isotopic Profiles')

plt.show()

# --- Simple "Animation" - Highlighting the closest pair ---
if most_similar_pair:
    fig_anim, ax_anim = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})
    scatter_anim = ax_anim.scatter(data_points[:, 0], data_points[:, 1], data_points[:, 2], s=100, c=['lightgray'] * len(artifact_names))

    # Highlight the most similar pair with different colors
    idx1 = artifact_names.index(most_similar_pair[0])
    idx2 = artifact_names.index(most_similar_pair[1])
    colors = ['lightgray'] * len(artifact_names)
    colors[idx1] = 'red'
    colors[idx2] = 'red'
    scatter_anim._facecolors = plt.cm.viridis(np.array(colors) == 'red') # A bit of a hack to change colors
    scatter_anim._edgecolors = plt.cm.viridis(np.array(colors) == 'red')

    for i, name in enumerate(artifact_names):
        ax_anim.text(data_points[i, 0], data_points[i, 1], data_points[i, 2], name)

    ax_anim.plot([art1_data[0], art2_data[0]], [art1_data[1], art2_data[1]], [art1_data[2], art2_data[2]], 'k--', linewidth=2, label=f'Most Similar (Dist: {min_distance:.3f})')
    ax_anim.legend()
    ax_anim.set_xlabel('$^{118}$Sn Abundance (%)')
    ax_anim.set_ylabel('$^{120}$Sn Abundance (%)')
    ax_anim.set_zlabel('$^{122}$Sn Abundance (%)')
    ax_anim.set_title('Highlighting the Most Similar Artifacts')
    plt.show()