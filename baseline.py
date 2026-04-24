"""
baseline.py — Fast TSP baselines via Numba JIT
Used purely as comparison benchmarks against FunSearch results.

Algorithms
----------
nearest_neighbor           : single-start NN (dist_matrix)
nearest_neighbor_from_coords : single-start NN (coords only, no matrix)
nn_multi_start             : best of k random starts (small n only)
run_all_baselines          : unified runner → dict of results
"""

import time
import numpy as np
from numba import njit


# ──────────────────────────────────────────────────────────────
# Distance utilities (JIT-compiled)
# ──────────────────────────────────────────────────────────────

@njit
def route_length(route, dist_matrix):
    """
    Total tour length via a precomputed distance matrix.

    Parameters
    ----------
    route : int32 ndarray  ← must be ndarray, NOT a Python list.
                             Callers outside this module: np.array(route, np.int32)
    dist_matrix : 2-D float ndarray
    """
    total = 0.0
    n = len(route)
    for i in range(n):
        total += dist_matrix[route[i], route[(i + 1) % n]]
    return total


@njit
def route_length_coords(route, coords):
    """Total tour length computed on-the-fly from coordinates (no matrix needed)."""
    total = 0.0
    n = len(route)
    for i in range(n):
        a = route[i]
        b = route[(i + 1) % n]
        dx = coords[a, 0] - coords[b, 0]
        dy = coords[a, 1] - coords[b, 1]
        total += (dx * dx + dy * dy) ** 0.5
    return total


# ──────────────────────────────────────────────────────────────
# Nearest-neighbour heuristics (JIT-compiled)
# ──────────────────────────────────────────────────────────────

@njit
def nearest_neighbor(dist_matrix, start=0):
    """Single-start nearest-neighbour using a precomputed distance matrix."""
    n = dist_matrix.shape[0]
    visited = np.zeros(n, dtype=np.bool_)
    route   = np.empty(n, dtype=np.int32)

    route[0]       = start
    visited[start] = True
    current        = start

    for i in range(1, n):
        best_dist = 1e18
        next_city = -1
        row = dist_matrix[current]
        for j in range(n):
            if not visited[j] and row[j] < best_dist:
                best_dist = row[j]
                next_city = j
        route[i]           = next_city
        visited[next_city] = True
        current            = next_city

    return route


@njit
def nearest_neighbor_from_coords(coords, start=0):
    """
    Single-start nearest-neighbour using raw coordinates.
    Compares squared distances (no sqrt) — finds identical nearest city.
    """
    n = coords.shape[0]
    visited = np.zeros(n, dtype=np.bool_)
    route   = np.empty(n, dtype=np.int32)

    route[0]       = start
    visited[start] = True
    current        = start

    for i in range(1, n):
        best_dist = 1e18
        next_city = -1
        cx = coords[current, 0]
        cy = coords[current, 1]
        for j in range(n):
            if not visited[j]:
                dx = cx - coords[j, 0]
                dy = cy - coords[j, 1]
                d  = dx * dx + dy * dy
                if d < best_dist:
                    best_dist = d
                    next_city = j
        route[i]           = next_city
        visited[next_city] = True
        current            = next_city

    return route


def nn_multi_start(dist_matrix, k=None):
    """
    Multi-start nearest-neighbour: best of k random starts.
    Only called for small instances (n <= _MULTISTART_MAX_N).

    k defaults to min(20, n).
    """
    n = dist_matrix.shape[0]
    k = k or min(20, n)

    best_route = None
    best_len   = np.inf

    starts = np.random.choice(n, min(k, n), replace=False)
    for s in starts:
        r = nearest_neighbor(dist_matrix, int(s))
        l = route_length(r, dist_matrix)
        if l < best_len:
            best_len   = l
            best_route = r

    return best_route


# ──────────────────────────────────────────────────────────────
# Unified runner
# ──────────────────────────────────────────────────────────────

_MULTISTART_MAX_N = 2000   # multi-start only worthwhile for small instances


def run_all_baselines(dist_matrix=None, coords=None, verbose=True):
    """
    Run all applicable baselines and return a results dict.

    Accepts either:
      dist_matrix : (n, n) ndarray  — preferred
      coords      : (n, 2) ndarray  — fallback for large-n (no matrix)

    Returns
    -------
    dict  {name: {"route": ndarray, "length": float, "time": float}}
    """
    if dist_matrix is None and coords is None:
        raise ValueError("run_all_baselines requires dist_matrix or coords.")

    results = {}

    if dist_matrix is not None:
        n = dist_matrix.shape[0]

        def _run(name, fn):
            t0      = time.time()
            route   = fn(dist_matrix)
            elapsed = time.time() - t0
            length  = route_length(route, dist_matrix)
            results[name] = {"route": route, "length": float(length), "time": elapsed}
            if verbose:
                print(f"  [{name}] length={length:.2f}  ({elapsed:.3f}s)")

        _run("nearest_neighbor", nearest_neighbor)

        if n <= _MULTISTART_MAX_N:
            _run("nn_multi_start", nn_multi_start)

    else:  # coords-only path (large n, no matrix)
        def _run(name, fn):
            t0      = time.time()
            route   = fn(coords)
            elapsed = time.time() - t0
            length  = route_length_coords(route, coords)
            results[name] = {"route": route, "length": float(length), "time": elapsed}
            if verbose:
                print(f"  [{name}] length={length:.2f}  ({elapsed:.3f}s)")

        _run("nn_coords", nearest_neighbor_from_coords)

    return results