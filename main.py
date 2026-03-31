from tsp_loader import load_tsp
from funsearch import funsearch

from baseline import run_all_baselines
# 或单独调用
from baseline import ortools_solve, greedy, route_length

# 读取数据
coords, dist_matrix = load_tsp("data/berlin52.tsp")

results = run_all_baselines(dist_matrix, ortools_time_limit=30)


# FunSearch
best_route, best_score, history = funsearch(dist_matrix, iterations=100)

print("\nFunSearch Best:", best_score)