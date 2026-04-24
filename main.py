"""
main.py — TSP benchmark runner

For each .tsp file:
  1. Load instance  (auto-selects dist_matrix vs coords-only by size)
  2. Run baselines  (nearest-neighbour variants, comparison only)
  3. Run FunSearch  (only when dist_matrix is available and n < MEDIUM_N)
  4. Print summary table
  5. Save results_summary.json and funsearch_best_codes.py to OUTPUT_DIR
"""

import os
import time
import json
import numpy as np

from tsp_loader import load_tsp_auto
from baseline   import run_all_baselines
from funsearch  import funsearch

# ──────────────────────────────────────────────────────────────
# Config
# ──────────────────────────────────────────────────────────────

SMALL_N  = 500
MEDIUM_N = 2000

FUNSEARCH_CFG = {
    "small":  dict(iterations=5, num_initial=5, top_k=3),
    "medium": dict(iterations=2, num_initial=3, top_k=2),
}

DATA_DIR   = "data"
OUTPUT_DIR = "outputs"
MAX_FILES  = None     # set to None to process all

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ──────────────────────────────────────────────────────────────
# File discovery
# ──────────────────────────────────────────────────────────────

tsp_files = sorted(f for f in os.listdir(DATA_DIR) if f.endswith(".tsp"))
if MAX_FILES is not None:
    tsp_files = tsp_files[:MAX_FILES]

print(f"Found {len(tsp_files)} .tsp file(s) to process.\n")

# ──────────────────────────────────────────────────────────────
# Main loop
# ──────────────────────────────────────────────────────────────

all_results: dict = {}

for tsp_file in tsp_files:
    print(f"\n{'='*60}")
    print(f"  {tsp_file}")
    print(f"{'='*60}")

    file_path = os.path.join(DATA_DIR, tsp_file)

    # ── Load ──────────────────────────────────────────────────
    try:
        coords, dist_matrix = load_tsp_auto(file_path)
    except Exception as e:
        print(f"  [load] Error: {e} — skipping")
        continue

    n          = len(coords)
    has_matrix = dist_matrix is not None
    print(f"  n={n}  dist_matrix={'built' if has_matrix else 'skipped (large n)'}")

    results: dict = {}

    # ── Baselines (comparison only) ───────────────────────────
    try:
        if has_matrix:
            results = run_all_baselines(dist_matrix=dist_matrix, verbose=False)
        else:
            results = run_all_baselines(coords=coords, verbose=False)

        for alg, data in results.items():
            print(f"  [baseline/{alg}] length={data['length']:.2f}  "
                  f"time={data['time']:.3f}s")
    except Exception as e:
        print(f"  [baseline] Error: {e}")

    # ── FunSearch ─────────────────────────────────────────────
    if has_matrix and n < MEDIUM_N:
        cfg_key = "small" if n < SMALL_N else "medium"
        cfg     = FUNSEARCH_CFG[cfg_key]

        print(f"\n  Running FunSearch ({cfg_key}: {cfg})...")
        t0 = time.time()
        try:
            fs_route, fs_length, fs_history, fs_code = funsearch(
                dist_matrix, **cfg
            )
            elapsed = time.time() - t0

            baseline_best = min(
                (v["length"] for v in results.values() if "length" in v),
                default=np.inf,
            )
            gap = (fs_length - baseline_best) / baseline_best * 100

            print(f"\n  FunSearch best : {fs_length:.2f}  ({elapsed:.1f}s)")
            print(f"  Baseline best  : {baseline_best:.2f}")
            print(f"  Gap            : {gap:+.2f}%")

            results["funsearch"] = {
                "length":  fs_length,
                "time":    round(elapsed, 2),
                "history": fs_history,
                "code":    fs_code,
                "route":   fs_route.tolist(),
            }
        except Exception as e:
            print(f"  [funsearch] Error: {e}")
    else:
        reason = "no dist_matrix" if not has_matrix else f"n={n} >= MEDIUM_N"
        print(f"\n  Skipping FunSearch ({reason})")

    all_results[tsp_file] = results

# ──────────────────────────────────────────────────────────────
# Summary table
# ──────────────────────────────────────────────────────────────

print(f"\n\n{'='*70}")
print("RESULTS SUMMARY")
print(f"{'='*70}")
print(f"{'File':<26} {'Algorithm':<22} {'Length':>12} {'Time(s)':>10}")
print("-" * 72)

for fname, res in all_results.items():
    for alg, data in res.items():
        if isinstance(data, dict) and "length" in data:
            length = data.get("length", np.inf)
            t      = data.get("time", 0.0)
            ls     = f"{length:.2f}" if (length is not None and length != np.inf) else "inf"
            print(f"{fname:<26} {alg:<22} {ls:>12} {t:>10.2f}")

# ──────────────────────────────────────────────────────────────
# Persist results
# ──────────────────────────────────────────────────────────────

def _serializable(obj):
    """Recursively convert results to JSON-safe types. Drops 'route' (large)."""
    if isinstance(obj, dict):
        return {k: _serializable(v) for k, v in obj.items() if k != "route"}
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if obj is np.inf or obj == np.inf:
        return None
    if isinstance(obj, list):
        return [_serializable(x) for x in obj]
    return obj


summary_path = os.path.join(OUTPUT_DIR, "results_summary.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(_serializable(all_results), f, indent=2, ensure_ascii=False)
print(f"\nSummary saved  → {summary_path}")

codes_path = os.path.join(OUTPUT_DIR, "funsearch_best_codes.py")
with open(codes_path, "w", encoding="utf-8") as f:
    f.write("# Auto-generated: best FunSearch heuristic per instance\n\n")
    for fname, res in all_results.items():
        if "funsearch" in res and "code" in res["funsearch"]:
            length = res["funsearch"]["length"]
            f.write(f"# {'─'*54}\n")
            f.write(f"# {fname}  length={length:.2f}\n")
            f.write(f"# {'─'*54}\n")
            f.write(res["funsearch"]["code"])
            f.write("\n\n")
print(f"Best codes saved → {codes_path}")