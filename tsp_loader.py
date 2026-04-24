import numpy as np


def load_tsp(file_path, build_matrix=True, dtype=np.float32):
    """
    Load TSPLib .tsp file

    Parameters
    ----------
    file_path : str
    build_matrix : bool
        Whether to build full distance matrix (O(n^2))
    dtype : numpy dtype
        float32 is faster & saves memory

    Returns
    -------
    coords : (n, 2) array
    dist_matrix : (n, n) array or None
    """

    coords = []

    # ── 读取文件（流式，比 readlines 快且省内存）──
    with open(file_path, 'r') as f:
        start = False
        for line in f:
            if "NODE_COORD_SECTION" in line:
                start = True
                continue
            if "EOF" in line:
                break
            if start:
                parts = line.split()
                if len(parts) >= 3:
                    coords.append((float(parts[1]), float(parts[2])))

    coords = np.array(coords, dtype=dtype)
    n = len(coords)

    if n == 0:
        return coords, None

    # ──────────────────────────────────────────────
    # 小规模：构建完整距离矩阵（向量化）
    # ──────────────────────────────────────────────
    if build_matrix:
        # 🚀 向量化计算（比双循环快几十倍）
        diff = coords[:, None, :] - coords[None, :, :]
        dist_matrix = np.sqrt((diff ** 2).sum(axis=2), dtype=dtype)

        return coords, dist_matrix

    # ──────────────────────────────────────────────
    # 大规模：不建矩阵（避免 n^2 内存）
    # ──────────────────────────────────────────────
    return coords, None


# ──────────────────────────────────────────────
# 可选：按规模自动决定是否建矩阵（推荐🔥）
# ──────────────────────────────────────────────

def load_tsp_auto(file_path, threshold=5000):
    """
    自动根据规模决定是否构建距离矩阵

    threshold : int
        n > threshold 时不构建 dist_matrix
    """

    coords, _ = load_tsp(file_path, build_matrix=False)
    n = len(coords)

    if n <= threshold:
        return load_tsp(file_path, build_matrix=True)
    else:
        return coords, None


# ──────────────────────────────────────────────
# 可选：按需计算距离（用于超大规模）
# ──────────────────────────────────────────────

def euclidean_distance(i, j, coords):
    """
    On-the-fly distance (替代 dist_matrix[i][j])
    """
    dx = coords[i][0] - coords[j][0]
    dy = coords[i][1] - coords[j][1]
    return (dx * dx + dy * dy) ** 0.5