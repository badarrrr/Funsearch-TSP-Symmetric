import numpy as np
import time
from numba import njit
# ──────────────────────────────────────────────
# Utility
# ──────────────────────────────────────────────

@njit
def route_length(route, dist_matrix):
    """Calculate total tour length (returns to start)."""
    total = 0
    n = len(route)
    for i in range(n):
        total += dist_matrix[route[i]][route[(i + 1) % n]]
    return total


# ──────────────────────────────────────────────
# 1. Nearest Neighbour Heuristic  (Constructive)
#    Ref: tsp_baseline.py – nearest_neighbor
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


def nearest_neighbor_best_of_all(dist_matrix):
    """
    Run nearest_neighbor from every possible start city and
    return the best tour found.  O(n³) but much better quality.
    """
    best_route = None
    best_len = np.inf
    n = len(dist_matrix)
    for start in range(n):
        r = nearest_neighbor(dist_matrix, start)
        l = route_length(r, dist_matrix)
        if l < best_len:
            best_len = l
            best_route = r
    return best_route


# ──────────────────────────────────────────────
# 2. Greedy Edge-Insertion Heuristic  (Constructive)
#    Ref: tsp_baseline.py – greedy
#    Sort all edges by weight; add edge if it does not
#    create a degree-3 node or a premature subtour.
# ──────────────────────────────────────────────

def greedy(dist_matrix):
    """
    Sort all O(n²) edges by length.  Greedily add each edge if:
      • neither endpoint has degree 2 already, AND
      • adding the edge does not close a cycle (unless it is the
        last edge that closes the Hamiltonian cycle).

    Time complexity: O(n² log n)
    Typically 15-20 % above optimal – better than pure NN.
    """
    n = len(dist_matrix)

    # Build sorted edge list (i < j only, undirected)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((dist_matrix[i][j], i, j))
    edges.sort()

    degree = [0] * n
    adj = [[] for _ in range(n)]          # adjacency list
    # Union-Find for cycle detection
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    edges_added = 0
    for dist, u, v in edges:
        if edges_added == n:
            break
        # Skip if either node already has degree 2
        if degree[u] >= 2 or degree[v] >= 2:
            continue
        # Skip if adding this edge would close a cycle prematurely
        if edges_added < n - 1 and find(u) == find(v):
            continue
        # Accept edge
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        union(u, v)
        edges_added += 1

    # Reconstruct tour from adjacency list
    # Find a degree-1 node to start (or any node if all degree-2)
    start = next((i for i in range(n) if degree[i] == 1), 0)
    route = [start]
    prev = -1
    current = start
    for _ in range(n - 1):
        for nb in adj[current]:
            if nb != prev:
                prev = current
                current = nb
                route.append(current)
                break

    return route


# ──────────────────────────────────────────────
# 3. Google OR-Tools  (Meta-heuristic / Local Search)
#    Ref: Google OR-Tools Routing Library
#    https://developers.google.com/optimization/routing/tsp
# ──────────────────────────────────────────────

def ortools_solve(dist_matrix, time_limit_seconds=30, first_solution_strategy="PATH_CHEAPEST_ARC"):
    """
    Solve TSP with Google OR-Tools Routing Solver.

    Parameters
    ----------
    dist_matrix : 2-D array-like of floats
        Symmetric distance matrix.
    time_limit_seconds : int
        Wall-clock budget for the local-search phase.
    first_solution_strategy : str
        One of: 'PATH_CHEAPEST_ARC', 'SAVINGS', 'CHRISTOFIDES',
                'PARALLEL_CHEAPEST_INSERTION', 'LOCAL_CHEAPEST_INSERTION'

    Returns
    -------
    route : list[int]   (0-indexed, does NOT repeat the start city)
    """
    try:
        from ortools.constraint_solver import routing_enums_pb2
        from ortools.constraint_solver import pywrapcp
    except ImportError:
        raise ImportError(
            "Google OR-Tools is not installed.\n"
            "Install it with:  pip install ortools"
        )

    n = len(dist_matrix)
    # OR-Tools requires integer distances
    scale = 1_000
    int_dist = [[int(dist_matrix[i][j] * scale) for j in range(n)] for i in range(n)]

    # ── Manager & Model ──────────────────────────────────────────
    manager = pywrapcp.RoutingIndexManager(n, 1, 0)   # n nodes, 1 vehicle, depot=0
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        i = manager.IndexToNode(from_index)
        j = manager.IndexToNode(to_index)
        return int_dist[i][j]

    transit_cb_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_cb_index)

    # ── Search Parameters ────────────────────────────────────────
    strategy_map = {
        "PATH_CHEAPEST_ARC":            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC,
        "SAVINGS":                      routing_enums_pb2.FirstSolutionStrategy.SAVINGS,
        "CHRISTOFIDES":                 routing_enums_pb2.FirstSolutionStrategy.CHRISTOFIDES,
        "PARALLEL_CHEAPEST_INSERTION":  routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION,
        "LOCAL_CHEAPEST_INSERTION":     routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_INSERTION,
    }

    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = strategy_map.get(
        first_solution_strategy,
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    # Enable guided local search (most effective metaheuristic for TSP)
    search_params.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_params.time_limit.seconds = time_limit_seconds
    search_params.log_search = False

    # ── Solve ────────────────────────────────────────────────────
    solution = routing.SolveWithParameters(search_params)

    if solution is None:
        raise RuntimeError("OR-Tools found no solution within the time limit.")

    # ── Extract route ────────────────────────────────────────────
    route = []
    index = routing.Start(0)
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))

    return route


# ──────────────────────────────────────────────
# Convenience runner (used by main.py)
# ──────────────────────────────────────────────

def run_all_baselines(dist_matrix, ortools_time_limit=30, verbose=True):
    """
    Run all baselines and return a dict with results.

    Returns
    -------
    dict with keys: 'nn', 'nn_best', 'greedy', 'ortools'
    Each value is a dict: {'route': [...], 'length': float, 'time': float}
    """
    results = {}

    def _run(name, fn, *args, **kwargs):
        t0 = time.time()
        route = fn(*args, **kwargs)
        elapsed = time.time() - t0
        length = route_length(route, dist_matrix)
        results[name] = {"route": route, "length": length, "time": elapsed}
        if verbose:
            print(f"[{name:18s}]  length = {length:10.4f}   time = {elapsed:.3f}s")
        return route

    if verbose:
        print("=" * 55)
        print("  Baseline Solver Results")
        print("=" * 55)

    _run("nearest_neighbor",      nearest_neighbor,              dist_matrix)
    _run("nn_best_start",         nearest_neighbor_best_of_all,  dist_matrix)
    _run("greedy",                greedy,                        dist_matrix)

    try:
        _run("ortools",           ortools_solve, dist_matrix,
             time_limit_seconds=ortools_time_limit)
    except ImportError as e:
        print(f"[ortools           ]  SKIPPED – {e}")
    except RuntimeError as e:
        print(f"[ortools           ]  FAILED  – {e}")

    if verbose:
        print("=" * 55)

    return results