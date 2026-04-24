"""
tsp_loader.py — TSPLib .tsp file loader (EUC_2D format)
"""

import numpy as np


def load_tsp(file_path, build_matrix=True, dtype=np.float32):
    """
    Load a TSPLib .tsp file.

    Parameters
    ----------
    file_path : str
    build_matrix : bool
        Build full O(n^2) distance matrix when True.
    dtype : numpy dtype
        float32 saves memory vs float64 with negligible precision loss.

    Returns
    -------
    coords : (n, 2) ndarray
    dist_matrix : (n, n) ndarray  or  None
    """
    coords = []

    with open(file_path, 'r') as f:
        in_coord_section = False
        for line in f:
            line = line.strip()
            if "NODE_COORD_SECTION" in line:
                in_coord_section = True
                continue
            if line == "EOF":
                break
            if in_coord_section and line:
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        coords.append((float(parts[1]), float(parts[2])))
                    except ValueError:
                        continue  # skip malformed lines

    coords = np.array(coords, dtype=dtype)
    n = len(coords)

    if n == 0:
        return coords, None

    if build_matrix:
        # Vectorized — note: np.sqrt does NOT accept a dtype kwarg, use .astype()
        diff = coords[:, None, :] - coords[None, :, :]              # (n, n, 2)
        dist_matrix = np.sqrt((diff ** 2).sum(axis=2)).astype(dtype) # (n, n)
        return coords, dist_matrix

    return coords, None


def load_tsp_auto(file_path, threshold=5000, dtype=np.float32):
    """
    Auto-select strategy based on instance size.

    n <= threshold  →  build full dist_matrix  (threshold=5000 ≈ 100 MB @ float32)
    n >  threshold  →  return coords only
    """
    coords, _ = load_tsp(file_path, build_matrix=False, dtype=dtype)
    n = len(coords)

    if n == 0:
        return coords, None

    if n <= threshold:
        return load_tsp(file_path, build_matrix=True, dtype=dtype)
    else:
        return coords, None


def euclidean_distance(i, j, coords):
    """On-the-fly scalar distance. Replaces dist_matrix[i][j] for large n."""
    dx = coords[i, 0] - coords[j, 0]
    dy = coords[i, 1] - coords[j, 1]
    return float((dx * dx + dy * dy) ** 0.5)


def batch_distances_from(city, candidates, coords):
    """
    Vectorized distances from one city to many candidates.

    Returns
    -------
    (len(candidates),) ndarray
    """
    pts  = coords[np.asarray(candidates)]
    diff = pts - coords[city]
    return np.sqrt((diff ** 2).sum(axis=1))