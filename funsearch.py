import random
import numpy as np
from baseline import route_length

# 一个“策略函数模板”
def heuristic_nn(dist_matrix, alpha=1.0):
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True

    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                # 👇 关键：可调策略（FunSearch优化的对象）
                score = dist_matrix[current][j] ** alpha
            else:
                score = np.inf
            scores.append(score)

        next_city = np.argmin(scores)
        route.append(next_city)
        visited[next_city] = True
        current = next_city

    return route


# “进化搜索”
def funsearch(dist_matrix, iterations=50):
    best_alpha = random.uniform(0.5, 2.0)
    best_route = heuristic_nn(dist_matrix, best_alpha)
    best_score = route_length(best_route, dist_matrix)

    history = []

    for i in range(iterations):
        # 模拟 LLM 生成新策略（这里用随机扰动）
        new_alpha = best_alpha + random.uniform(-0.2, 0.2)

        route = heuristic_nn(dist_matrix, new_alpha)
        score = route_length(route, dist_matrix)

        if score < best_score:
            best_score = score
            best_alpha = new_alpha
            best_route = route

        history.append(best_score)

        print(f"Iter {i}: best = {best_score:.2f}, alpha = {best_alpha:.3f}")

    return best_route, best_score, history