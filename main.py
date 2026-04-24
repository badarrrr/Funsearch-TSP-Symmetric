import os
import time
from tsp_loader import load_tsp_auto
from baseline import run_all_baselines
from funsearch import funsearch

SMALL_N = 500
MEDIUM_N = 2000
LARGE_N = 5000

FUNSEARCH_SMALL = dict(iterations=5, num_initial=3)
FUNSEARCH_MEDIUM = dict(iterations=2, num_initial=2)

data_dir = "data"
tsp_files = sorted([f for f in os.listdir(data_dir) if f.endswith('.tsp')])

all_results = {}

for tsp_file in tsp_files:
    print(f"\nProcessing {tsp_file}...")

    file_path = os.path.join(data_dir, tsp_file)

    coords, dist_matrix = load_tsp_auto(file_path)
    n = len(coords)

    print(f"n = {n}")

    # ── baseline ──
    if dist_matrix is not None:
        results = run_all_baselines(dist_matrix=dist_matrix, verbose=False)
    else:
        results = run_all_baselines(coords=coords, verbose=False)

    # ── FunSearch（只在有矩阵 & 小规模）──
    if dist_matrix is not None and n < MEDIUM_N:
        cfg = FUNSEARCH_SMALL if n < SMALL_N else FUNSEARCH_MEDIUM

        t0 = time.time()
        fs_route, fs_length, fs_history, fs_code = funsearch(
            dist_matrix,
            iterations=cfg["iterations"],
            num_initial=cfg["num_initial"]
        )

        results["funsearch"] = {
            "route": fs_route,
            "length": fs_length,
            "time": time.time() - t0,
            "history": fs_history,
            "code": fs_code
        }

    all_results[tsp_file] = results


# ── save ──
with open('results.md', 'w', encoding='utf-8') as f:
    f.write("# TSP Results\n\n")

    algo_set = set()
    for r in all_results.values():
        algo_set.update(r.keys())
    algos = sorted(algo_set)

    f.write("| Problem | " + " | ".join(
        [f"{a} len | {a} time" for a in algos]
    ) + " |\n")

    f.write("|---|" + "---|---|" * len(algos) + "\n")

    for name, res in all_results.items():
        f.write(f"| {name} | ")
        for a in algos:
            if a in res:
                f.write(f"{res[a]['length']:.1f} | {res[a]['time']:.2f} | ")
            else:
                f.write("- | - | ")
        f.write("\n")