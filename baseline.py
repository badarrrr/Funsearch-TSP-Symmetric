import numpy as np

def nearest_neighbor(dist_matrix, start=0):
    n = len(dist_matrix)
    visited = [False] * n
    route = [start]
    visited[start] = True

    current = start
    for _ in range(n - 1):
        next_city = np.argmin([
            dist_matrix[current][j] if not visited[j] else np.inf
            for j in range(n)
        ])
        route.append(next_city)
        visited[next_city] = True
        current = next_city

    return route

def route_length(route, dist_matrix):
    total = 0
    for i in range(len(route)):
        total += dist_matrix[route[i]][route[(i + 1) % len(route)]]
    return total