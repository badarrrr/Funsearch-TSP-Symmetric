import numpy as np
import time
from numba import njit

# ──────────────────────────────────────────────
# Utility
# ──────────────────────────────────────────────

@njit
def route_length(route, dist_matrix):
    total = 0.0
    n = route.shape[0]
    for i in range(n):
        total += dist_matrix[route[i], route[(i + 1) % n]]
    return total


@njit
def route_length_coords(route, coords):
    total = 0.0
    n = route.shape[0]
    for i in range(n):
        a = route[i]
        b = route[(i + 1) % n]
        dx = coords[a, 0] - coords[b, 0]
        dy = coords[a, 1] - coords[b, 1]
        total += (dx * dx + dy * dy) ** 0.5
    return total


# ──────────────────────────────────────────────
# NN (matrix)
# ──────────────────────────────────────────────

@njit
def nearest_neighbor(dist_matrix, start=0):
    n = dist_matrix.shape[0]
    visited = np.zeros(n, dtype=np.bool_)
    route = np.empty(n, dtype=np.int32)

    route[0] = start
    visited[start] = True
    current = start

    for i in range(1, n):
        best_dist = 1e18
        next_city = -1

        row = dist_matrix[current]

        for j in range(n):
            if not visited[j]:
                d = row[j]
                if d < best_dist:
                    best_dist = d
                    next_city = j

        route[i] = next_city
        visited[next_city] = True
        current = next_city

    return route


# ──────────────────────────────────────────────
# NN (coords fallback)
# ──────────────────────────────────────────────

@njit
def nearest_neighbor_from_coords(coords, start=0):
    n = coords.shape[0]
    visited = np.zeros(n, dtype=np.bool_)
    route = np.empty(n, dtype=np.int32)

    route[0] = start
    visited[start] = True
    current = start

    for i in range(1, n):
        best_dist = 1e18
        next_city = -1

        cx = coords[current, 0]
        cy = coords[current, 1]

        for j in range(n):
            if not visited[j]:
                dx = cx - coords[j, 0]
                dy = cy - coords[j, 1]
                d = dx * dx + dy * dy

                if d < best_dist:
                    best_dist = d
                    next_city = j

        route[i] = next_city
        visited[next_city] = True
        current = next_city

    return route


# ──────────────────────────────────────────────
# Multi-start NN
# ──────────────────────────────────────────────

def nn_multi_start(dist_matrix, k=5):
    n = len(dist_matrix)
    best_route = None
    best_len = np.inf

    starts = np.random.choice(n, min(k, n), replace=False)

    for s in starts:
        r = nearest_neighbor(dist_matrix, int(s))
        l = route_length(r, dist_matrix)
        if l < best_len:
            best_len = l
            best_route = r

    return best_route


# ──────────────────────────────────────────────
# Runner（支持两种模式）
# ──────────────────────────────────────────────

def run_all_baselines(dist_matrix=None, coords=None, verbose=True):
    results = {}

    # ─────────────────────────────
    # CASE 1: 有 dist_matrix
    # ─────────────────────────────
    if dist_matrix is not None:
        n = len(dist_matrix)

        def _run(name, fn):
            t0 = time.time()
            route = fn(dist_matrix)
            elapsed = time.time() - t0
            length = route_length(route, dist_matrix)
            results[name] = {
                "route": route,
                "length": float(length),
                "time": elapsed
            }

        _run("nearest_neighbor", nearest_neighbor)

        if n >= 2000:
            _run("nn_multi", lambda dm: nn_multi_start(dm, 5))

        return results

    # ─────────────────────────────
    # CASE 2: coords-only
    # ─────────────────────────────
    elif coords is not None:
        def _run(name, fn):
            t0 = time.time()
            route = fn(coords)
            elapsed = time.time() - t0
            length = route_length_coords(route, coords)
            results[name] = {
                "route": route,
                "length": float(length),
                "time": elapsed
            }

        _run("nn_coords", nearest_neighbor_from_coords)
        return results

    else:
        raise ValueError("Need either dist_matrix or coords")