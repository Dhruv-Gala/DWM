import random
import math

def kmeans():

    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def mean(points):
        if not points:
            return [0, 0]
        sum_x = sum(p[0] for p in points)
        sum_y = sum(p[1] for p in points)

        return [round(sum_x / len(points), 2), round(sum_y / len(points), 2)]

    n = int(input("Enter no.of points: "))
    points = []
    for i in range(n):
        x = float(input(f"Enter x{i+1}: "))
        y = float(input(f"Enter y{i+1}: "))
        points.append([x, y])

    k = int(input("\nEnter cluster size: "))

    centroids = [points[i] for i in random.sample(range(len(points)), k)]
    print("\nInitial Centroids: ")
    print(centroids)

    max_iter = 10

    for it in range(max_iter):
        print(f"\n--- Iteration {it+1} ---")

        clusters = [[] for _ in range(k)]
        
        for point in points:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = distances.index((min(distances)))
            clusters[cluster_index].append(point)

        for idx, cluster in enumerate(clusters):
            print(f"Cluster {idx+1}: {cluster}")

        new_centroids = [mean(cluster) for cluster in clusters]
        print(f"New Centroids: {new_centroids}")

        if centroids == new_centroids:
            print("\nConverged!")

            print("Final Clusters")
            z = 0
            for cluster in clusters:
                print(f"\tCluster {z+1}: {cluster}")
                z=z+1
            print(f"Final Centroids: {new_centroids}")
            break
        centroids = new_centroids
    
