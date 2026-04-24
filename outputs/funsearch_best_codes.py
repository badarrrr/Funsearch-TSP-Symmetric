# Auto-generated: best FunSearch heuristic per instance

# ──────────────────────────────────────────────────────
# a280.tsp  length=3148.11
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ali535.tsp  length=2671.07
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# att48.tsp  length=40526.42
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# att532.tsp  length=112099.45
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# berlin52.tsp  length=8980.92
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# bier127.tsp  length=135751.78
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# burma14.tsp  length=38.69
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ch130.tsp  length=7575.29
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ch150.tsp  length=8194.61
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d1291.tsp  length=60996.35
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d1655.tsp  length=73939.42
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d198.tsp  length=18655.49
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d493.tsp  length=43646.37
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d657.tsp  length=61874.12
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# dsj1000.tsp  length=24630960.09
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# eil101.tsp  length=825.24
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# eil51.tsp  length=513.61
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# eil76.tsp  length=711.99
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# fl1400.tsp  length=27061.37
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# fl1577.tsp  length=29186.23
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# fl417.tsp  length=15737.09
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gil262.tsp  length=3241.47
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr137.tsp  length=1022.22
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr202.tsp  length=619.40
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr229.tsp  length=2014.71
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr431.tsp  length=2516.25
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr666.tsp  length=4110.90
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr96.tsp  length=707.09
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroA100.tsp  length=26856.39
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroA150.tsp  length=33609.87
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroA200.tsp  length=35798.41
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroB100.tsp  length=29155.04
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroB150.tsp  length=32825.75
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroB200.tsp  length=36981.59
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroC100.tsp  length=26327.36
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroD100.tsp  length=26950.46
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# kroE100.tsp  length=27587.19
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# lin105.tsp  length=20362.76
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# lin318.tsp  length=54033.58
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# linhp318.tsp  length=54033.58
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# nrw1379.tsp  length=70015.46
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# p654.tsp  length=43411.56
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pcb1173.tsp  length=70277.94
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pcb442.tsp  length=61984.05
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr1002.tsp  length=315596.59
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr107.tsp  length=46678.15
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr124.tsp  length=69299.43
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr136.tsp  length=120777.86
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr144.tsp  length=61650.72
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr152.tsp  length=85702.95
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr226.tsp  length=94685.45
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr264.tsp  length=58022.86
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr299.tsp  length=59899.01
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr439.tsp  length=131282.09
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr76.tsp  length=153461.92
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat195.tsp  length=2761.96
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat575.tsp  length=8449.32
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat783.tsp  length=11255.07
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat99.tsp  length=1564.72
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rd100.tsp  length=9941.16
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rd400.tsp  length=19168.05
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rl1304.tsp  length=339797.47
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rl1323.tsp  length=332094.97
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rl1889.tsp  length=400684.64
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# st70.tsp  length=805.53
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ts225.tsp  length=152493.55
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# tsp225.tsp  length=4829.00
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u1060.tsp  length=296543.89
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u1432.tsp  length=188815.01
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u159.tsp  length=54669.03
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u1817.tsp  length=71691.24
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u574.tsp  length=46881.87
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u724.tsp  length=52994.58
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ulysses16.tsp  length=104.73
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ulysses22.tsp  length=89.64
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# vm1084.tsp  length=301469.23
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# vm1748.tsp  length=408089.19
# ──────────────────────────────────────────────────────
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                score = dist_matrix[current][j]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


