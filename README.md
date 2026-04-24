# TSP FunSearch Project
## FunSearch for the Traveling Salesman Problem

### 项目说明

实现 **FunSearch 风格的 TSP 优化算法**，结合经典最近邻（Nearest Neighbor）算法与自动化启发式设计。

目标：通过使用大型语言模型（LLM）自动生成和改进启发式函数，与baseline算法作比较。

### 功能

* **数据读取**：TSPLib 格式 `.tsp` 文件 → 距离矩阵
* **Baseline**：Nearest Neighbor, Greedy, OR-Tools 等算法
* **FunSearch 优化**：使用LLM生成初始启发式集合，迭代改进最佳启发式
* **实验对比**：显示 baseline 与 FunSearch 对比

### 代码说明

| 文件              | 功能                              |
| --------------- | ------------------------------- |
| `tsp_loader.py` | 读取 TSPLib 数据并生成距离矩阵             |
| `baseline.py`   | 各种baseline算法及路径长度计算                    |
| `funsearch.py`  | FunSearch 核心逻辑：LLM生成和修改启发式        |
| `main.py`       | 运行入口，展示 baseline 与 FunSearch 对比 |
| `data/`         | 存放 TSPLib 数据文件，如 `berlin52.tsp` |

### 运行

创建 `.env` 文件并设置API密钥：

```
QWEN_API_KEY=your-qwen-api-key-here
```

然后运行：

```bash
pip install ortools openai python-dotenv
python main.py
```

运行后输出：

* Baseline算法的结果
* FunSearch优化过程
* 最终最佳启发式代码

### 注意

- FunSearch使用Qwen3.6-Flash模型，需要有效的API密钥。
- 如果没有设置密钥或API调用失败，代码会回退到默认启发式。
- 迭代次数和初始启发式数量可在funsearch函数中调整。

Baseline： 在`berlin52.tsp`上的运行结果：

| Solver             | Length      | Time     |
|-------------------|------------|---------|
| nearest_neighbor   | 8980.9183  | 0.000s  |
| nn_best_start      | 8182.1916  | 0.023s  |
| greedy             | 9954.0627  | 0.001s  |
| ortools            | 7544.3659  | 30.275s |

### 参考

* [TSPLib](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
    * 这个链接我打不开，下载的数据集来自：https://github.com/mastqe/tsplib.git
* [Google OR-Tools TSP](https://developers.google.com/optimization/routing/tsp)
