import numpy as np

def load_tsp(file_path):
    coords = []
    with open(file_path, 'r') as f:
        lines = f.readlines()

    start = False
    for line in lines:
        if "NODE_COORD_SECTION" in line:
            start = True
            continue
        if "EOF" in line:
            break
        if start:
            parts = line.strip().split()
            coords.append((float(parts[1]), float(parts[2])))

    coords = np.array(coords)

    # 距离矩阵
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = np.linalg.norm(coords[i] - coords[j])

    return coords, dist_matrix