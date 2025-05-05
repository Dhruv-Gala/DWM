import random
import math

def kmeans():

    def distance(p1, p2):
        return abs(p1-p2)

    def mean(points):
        if not points:
            return 0

        sum = 0
        for p in points:
            sum = sum + p
        return round(sum / len(points), 2)
    
    n = int(input("Enter no.of points: "))
    points = []

    for i in range(n):
        x = float(input(f"Enter x{i+1}: "))
        points.append(x)

    k = int(input("Enter cluster size: "))

    centroids = [points[i] for i in random.sample(range(len(points)), k)]
    print(f"\nInitial Centroids: {centroids}")
    
    max_iter = 10

    for it in range(max_iter):
        clusters = [[] for _ in range(k)]

        print(f"--- Iteration {it+1} ---")

        for point in points:
            distances = [distance(point, centroid) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)

        for idx, cluster in enumerate(clusters):
            print(f"Cluster {idx+1}: {cluster}")

        new_centroids = [mean(cluster) for cluster in clusters]
        print(f"Updated Centroids: {new_centroids}")

        if new_centroids == centroids:
            print("Converged!")
            break
        
        centroids = new_centroids

if __name__ == "__main__":
    kmeans()
                                            
            
        
