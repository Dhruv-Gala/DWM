import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Linkage distance functions
def single_linkage_distance(cluster1, cluster2):
    return min(euclidean(p1, p2) for p1 in cluster1 for p2 in cluster2)

def complete_linkage_distance(cluster1, cluster2):
    return max(euclidean(p1, p2) for p1 in cluster1 for p2 in cluster2)

def average_linkage_distance(cluster1, cluster2):
    distances = [euclidean(p1, p2) for p1 in cluster1 for p2 in cluster2]
    return sum(distances) / len(distances)

def agglomerative_clustering(points, method="single"):
    distance_func = {
        "single": single_linkage_distance,
        "complete": complete_linkage_distance,
        "average": average_linkage_distance
    }.get(method)

    clusters = [[p] for p in points]
    step = 1

    print("Initial Clusters:")
    z = 0
    for cluster in clusters:
      print(f"Cluster {z+1}: {cluster}")
      z = z+1

    while len(clusters) > 1:
        min_dist = float('inf')
        to_merge = (0, 1)

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = distance_func(clusters[i], clusters[j])
                if dist < min_dist:
                    min_dist = dist
                    to_merge = (i, j)
        

        i, j = to_merge
        print(f"\nStep {step}: Merging Cluster {i+1} and Cluster {j+1} (Distance = {min_dist:.2f})")
        clusters[i].extend(clusters[j])
        del clusters[j]

        for idx, cluster in enumerate(clusters):
            print(f"Cluster {idx + 1}: {cluster}")

        step += 1

def get_user_points():
    n = int(input("Enter number of 2D points: "))
    points = []
    for i in range(n):
        x = float(input(f"Enter x for point {i+1}: "))
        y = float(input(f"Enter y for point {i+1}: "))
        points.append([x, y])
    return points

def main():
    points = get_user_points()

    print("\nChoose linkage method:")
    print("1. single")
    print("2. complete")
    print("3. average")
    method_input = input("Enter method name (single/complete/average): ").strip().lower()

    if method_input not in ['single', 'complete', 'average']:
        print("Invalid choice. Defaulting to 'single'")
        method_input = 'single'

    print(f"\n--- Agglomerative Clustering (Linkage: {method_input}) ---")
    agglomerative_clustering(points, method_input)

    Z = linkage(points, method=method_input)

    plt.figure(figsize=(10, 5))
    dendrogram(Z, labels=[f"P{i+1}" for i in range(len(points))])
    plt.title(f"Dendrogram - Agglomerative Clustering ({method_input.title()} Linkage)")
    plt.xlabel("Points")
    plt.ylabel("Distance")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
