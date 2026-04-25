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
# ali535.tsp  length=2568.08
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / 2
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
# att532.tsp  length=108593.49
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
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
# ch130.tsp  length=7338.32
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
                score = dist_matrix[current][j] + dist_matrix[j][0] * 0.5
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# ch150.tsp  length=7988.13
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / 10
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
# d198.tsp  length=18374.01
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d493.tsp  length=42802.15
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
                score = 0.7 * dist_matrix[current][j] + 0.3 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# d657.tsp  length=61214.40
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
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
# eil76.tsp  length=662.44
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
                score = dist_matrix[current][j] + dist_matrix[j][current] + dist_matrix[j][0]
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
# fl1577.tsp  length=27152.72
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# fl417.tsp  length=15073.82
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
                score = dist_matrix[current][j] + dist_matrix[j][current] + dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gil262.tsp  length=3064.73
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr137.tsp  length=937.12
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
                score = (dist_matrix[current][j] + dist_matrix[j][0]) ** 0.5
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr202.tsp  length=568.42
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
                score = dist_matrix[current][j] ** 1.3 + 0.4 * dist_matrix[j][0] - 0.2 * dist_matrix[j][current]
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
# gr431.tsp  length=2420.55
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
                score = dist_matrix[current][j] + dist_matrix[j][0] * 0.5
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr666.tsp  length=3886.13
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
                score = dist_matrix[current][j] ** 0.7 / (dist_matrix[j][0] + 1)
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# gr96.tsp  length=635.68
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
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
# kroB100.tsp  length=28588.73
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
                score = dist_matrix[current][j] + dist_matrix[j][current] + dist_matrix[j][0]
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
# kroD100.tsp  length=26392.48
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
                score = 3.0 * dist_matrix[current][j] + 1.0 * dist_matrix[j][0]
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
# lin105.tsp  length=17757.94
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
                score = dist_matrix[current][j] / dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# lin318.tsp  length=53523.35
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
                score = dist_matrix[current][j] * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# linhp318.tsp  length=51566.55
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
                score = (dist_matrix[current][j] ** 0.5) / (dist_matrix[j][0] ** 0.5)
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
# pcb442.tsp  length=59726.28
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / n
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
# pr152.tsp  length=82690.80
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
                score = 0.7 * dist_matrix[current][j] + 0.3 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# pr226.tsp  length=94166.33
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / n
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
# pr299.tsp  length=59013.74
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
                score = dist_matrix[current][j] / 1.5 + dist_matrix[j][0] ** 0.7
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
# pr76.tsp  length=142519.92
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
                score = dist_matrix[current][j] * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat195.tsp  length=2681.56
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
                score = dist_matrix[current][j] / (dist_matrix[j][0] + 1)
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat575.tsp  length=8335.39
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
                score = dist_matrix[current][j] + 0.5 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat783.tsp  length=10840.75
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
                score = dist_matrix[current][j] ** 0.5 + dist_matrix[j][0] ** 0.5
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rat99.tsp  length=1433.48
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
                score = (dist_matrix[current][j] + dist_matrix[j][current]) / dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rd100.tsp  length=9310.94
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / 2
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
# rl1304.tsp  length=332006.83
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / 2
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# rl1323.tsp  length=330903.20
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / n
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
# ts225.tsp  length=145470.35
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
                score = dist_matrix[current][j] ** 1.2 + dist_matrix[j][0] / 3.0
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
# u1060.tsp  length=289666.37
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / n
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u1432.tsp  length=185267.13
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
                score = dist_matrix[current][j] ** 0.5 + dist_matrix[j][0] ** 0.5
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u159.tsp  length=52205.46
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
                score = 0.7 * dist_matrix[current][j] + 0.2 * dist_matrix[j][current] + 0.1 * dist_matrix[j][0]
            else:
                score = np.inf
            scores.append(score)
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route


# ──────────────────────────────────────────────────────
# u1817.tsp  length=69292.25
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
                score = dist_matrix[current][j] + dist_matrix[j][0] / n
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
# ulysses16.tsp  length=88.72
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
                score = 0.7 * dist_matrix[current][j] + 0.3 * dist_matrix[j][0]
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


