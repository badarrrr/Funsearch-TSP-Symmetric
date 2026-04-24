import os
import time
from tsp_loader import load_tsp

from baseline import run_all_baselines
# 或单独调用
from baseline import ortools_solve, greedy, route_length
from funsearch import funsearch

# 挑选了十来个比较小的TSP实例进行测试，结果以Markdown表格的形式保存到results.md文件中
data_dir = "data"
tsp_files = sorted([f for f in os.listdir(data_dir) if f.endswith('.tsp')])  # 只取前15个

# 收集所有结果
all_results = {}

for tsp_file in tsp_files:
    print(f"Processing {tsp_file}...")
    file_path = os.path.join(data_dir, tsp_file)
    try:
        coords, dist_matrix = load_tsp(file_path)
        if len(dist_matrix) == 0:
            continue
    except Exception as e:
        continue
    
    # baseline
    try:
        results = run_all_baselines(dist_matrix, ortools_time_limit=30, verbose=False)
        
        # Run FunSearch
        t0 = time.time()
        fs_route, fs_length, fs_history, fs_code = funsearch(dist_matrix, iterations=5, num_initial=3)
        fs_time = time.time() - t0
        results["funsearch"] = {"route": fs_route, "length": fs_length, "time": fs_time, "history": fs_history, "code": fs_code}
        
        all_results[tsp_file] = results
    except Exception as e:
        continue

# 保存为Markdown表格格式
with open('results.md', 'w', encoding='utf-8') as f:
    f.write("# TSP Benchmark Results\n\n")
    
    # 获取所有算法名称
    algorithms = list(all_results[tsp_files[0]].keys()) if tsp_files and tsp_files[0] in all_results else []
    
    # 写表头
    f.write("| Problem | ")
    for algo in algorithms:
        f.write(f"{algo} (Length) | {algo} (Time) | ")
    f.write("\n")
    
    f.write("|---------|")
    for algo in algorithms:
        f.write("---------|---------|")
    f.write("\n")
    
    # 写数据
    for tsp_file in tsp_files:
        if tsp_file not in all_results:
            continue
        f.write(f"| {tsp_file} | ")
        results = all_results[tsp_file]
        for algo in algorithms:
            if algo in results:
                length = results[algo]['length']
                time_val = results[algo]['time']
                f.write(f"{length:.2f} | {time_val:.3f}s | ")
        f.write("\n")
    
    # Add FunSearch details
    f.write("\n## FunSearch Details\n\n")
    for tsp_file in tsp_files:
        if tsp_file not in all_results or "funsearch" not in all_results[tsp_file]:
            continue
        fs = all_results[tsp_file]["funsearch"]
        f.write(f"### {tsp_file}\n")
        f.write(f"- Final Length: {fs['length']:.2f}\n")
        f.write(f"- Time: {fs['time']:.3f}s\n")
        f.write(f"- History: {fs['history']}\n")
        f.write(f"- Best Code:\n```\n{fs['code']}\n```\n\n")

