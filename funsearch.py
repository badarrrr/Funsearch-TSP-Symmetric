import random
import numpy as np
from baseline import route_length
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Qwen client
client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# Heuristic template
HEURISTIC_TEMPLATE = """
def heuristic(dist_matrix):
    import numpy as np
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    current = 0
    for _ in range(n - 1):
        scores = []
        for j in range(n):
            if not visited[j]:
                {score_calculation}
            else:
                score = np.inf
            scores.append(score)
        next_city = np.argmin(scores)
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route
"""

def generate_initial_heuristics(num_heuristics=10):
    """Generate initial set of heuristics using LLM."""
    heuristics = []
    for i in range(num_heuristics):
        prompt = """
        You are designing a heuristic for the Traveling Salesman Problem (TSP).
        The heuristic is a modification of the nearest neighbor algorithm.
        In the nearest neighbor, we choose the closest unvisited city.
        You need to modify the score calculation for selecting the next city.

        The template is:
        for j in range(n):
            if not visited[j]:
                score = {something involving dist_matrix[current][j]}
            else:
                score = np.inf

        Provide a Python expression for 'score' that estimates how good it is to go to city j from current.
        Make it creative and potentially better than just dist_matrix[current][j].
        Use only basic operations: +, -, *, /, **, np.inf, dist_matrix[current][j], dist_matrix[j][current], etc.
        Avoid using min(), max(), sum(), len(), or any functions that might fail on empty lists.
        For example: score = dist_matrix[current][j] * 1.1
        Or: score = dist_matrix[current][j] + dist_matrix[j][0] * 0.5
        Or: score = dist_matrix[current][j] ** 0.9

        Output only the Python code for the score calculation, nothing else.
        """
        try:
            response = client.chat.completions.create(
                model="qwen3.6-flash",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.7,
                extra_body={"enable_thinking": True}
            )
            score_calc = response.choices[0].message.content.strip()
            heuristic_code = HEURISTIC_TEMPLATE.format(score_calculation=score_calc)
            heuristics.append(heuristic_code)
        except Exception as e:
            print(f"Error generating heuristic {i}: {e}")
            # Fallback to default
            score_calc = "score = dist_matrix[current][j]"
            heuristic_code = HEURISTIC_TEMPLATE.format(score_calculation=score_calc)
            heuristics.append(heuristic_code)
    return heuristics

def evaluate_heuristic(heuristic_code, dist_matrix):
    """Evaluate a heuristic by executing it and computing route length."""
    try:
        local_vars = {}
        exec(heuristic_code, {"np": np, "dist_matrix": dist_matrix}, local_vars)
        heuristic_func = local_vars["heuristic"]
        route = heuristic_func(dist_matrix)
        
        # Validate route
        n = len(dist_matrix)
        if len(route) != n or len(set(route)) != n or not all(0 <= city < n for city in route):
            print(f"Invalid route generated: {route}")
            return np.inf, None
        
        length = route_length(route, dist_matrix)
        print(f"Evaluated route: {route[:5]}..., length: {length}")
        return length, route
    except Exception as e:
        print(f"Error evaluating heuristic: {e}")
        return np.inf, None

def modify_heuristic(heuristic_code, performance, dist_matrix_size):
    """Use LLM to modify a heuristic for better performance."""
    prompt = f"""
    The current heuristic code is:
    {heuristic_code}

    It achieved a route length of {performance} on a TSP instance with {dist_matrix_size} cities.

    Modify the score calculation to potentially improve the performance.
    Provide a new Python expression for 'score' in the loop.
    Use only basic operations: +, -, *, /, **, np.inf, dist_matrix[current][j], dist_matrix[j][current], etc.
    Avoid using min(), max(), sum(), len(), or any functions that might fail on empty lists.

    Output only the new score calculation code, nothing else.
    """
    try:
        response = client.chat.completions.create(
            model="qwen3.6-flash",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7,
            extra_body={"enable_thinking": True}
        )
        new_score_calc = response.choices[0].message.content.strip()
        new_heuristic_code = HEURISTIC_TEMPLATE.format(score_calculation=new_score_calc)
        return new_heuristic_code
    except Exception as e:
        print(f"Error modifying heuristic: {e}")
        return heuristic_code

def funsearch(dist_matrix, iterations=10, num_initial=5):
    """FunSearch for TSP heuristics."""
    # Generate initial heuristics
    heuristics = generate_initial_heuristics(num_initial)
    
    # Evaluate initial heuristics
    performances = []
    for code in heuristics:
        perf, route = evaluate_heuristic(code, dist_matrix)
        if perf != np.inf:  # Only add valid ones
            performances.append((perf, code, route))
    
    if not performances:
        # Fallback to default nearest neighbor
        from baseline import nearest_neighbor
        default_route = nearest_neighbor(dist_matrix)
        default_length = route_length(default_route, dist_matrix)
        default_code = HEURISTIC_TEMPLATE.format(score_calculation="score = dist_matrix[current][j]")
        performances = [(default_length, default_code, default_route)]
    
    # Sort by performance (lower is better)
    performances.sort(key=lambda x: x[0])
    best_perf, best_code, best_route = performances[0]
    
    history = [best_perf]
    
    for i in range(iterations):
        # Pick the best heuristic
        current_best_code = best_code
        
        # Modify it
        modified_code = modify_heuristic(current_best_code, best_perf, len(dist_matrix))
        
        # Evaluate modified
        mod_perf, mod_route = evaluate_heuristic(modified_code, dist_matrix)
        
        # If better and valid, replace
        if mod_perf < best_perf and mod_perf != np.inf:
            best_perf = mod_perf
            best_code = modified_code
            best_route = mod_route
            print(f"Iter {i}: Improved to {best_perf:.2f}")
        else:
            print(f"Iter {i}: No improvement, kept {best_perf:.2f}")
        
        history.append(best_perf)
    
    return best_route, best_perf, history, best_code 
