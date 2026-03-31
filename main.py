from tsp_loader import load_tsp
from baseline import nearest_neighbor, route_length
from funsearch import funsearch

# 读取数据
coords, dist_matrix = load_tsp("data/berlin52.tsp")

# baseline
nn_route = nearest_neighbor(dist_matrix)
nn_score = route_length(nn_route, dist_matrix)
print("Nearest Neighbor:", nn_score)

# FunSearch
best_route, best_score, history = funsearch(dist_matrix, iterations=100)

print("\nFunSearch Best:", best_score)