# TSP FunSearch Project
## FunSearch for the Traveling Salesman Problem

### 项目说明

实现 **FunSearch 风格的 TSP 优化算法**，结合经典最近邻（Nearest Neighbor）算法与简单进化搜索策略。

目标：通过自动调整启发式策略参数，寻找更短的旅行路径，与baseline算法作比较。


### 功能

* **数据读取**：TSPLib 格式 `.tsp` 文件 → 距离矩阵
* **Baseline**：Nearest Neighbor 算法（应该还需要增加其他baseline进行对比）
* **FunSearch 优化**：模拟 LLM 生成策略 + 进化搜索优化路径长度
* **实验对比**：显示 baseline 与优化后的路径长度


### 代码说明
dataset：TSPLIB 是一个经典的旅行商问题（TSP）数据集库，Symmetric TSP 部分指的是“对称旅行商问题”，即城市之间的距离是对称的，也就是说从城市 A 到城市 B 的距离等于从城市 B 到城市 A 的距离。

| 文件              | 功能                              |
| --------------- | ------------------------------- |
| `tsp_loader.py` | 读取 TSPLib 数据并生成距离矩阵             |
| `baseline.py`   | 最近邻算法及路径长度计算                    |
| `funsearch.py`  | FunSearch 核心优化逻辑                |
| `main.py`       | 运行入口，展示 baseline 与 FunSearch 对比 |
| `data/`         | 存放 TSPLib 数据文件，如 `berlin52.tsp` |


### 运行
baseline 里的 ortools 方法要安装一下

```bash
pip install ortools
python main.py
```

运行后输出：

* Nearest Neighbor 的路径长度
* 每轮 FunSearch 优化的结果
* 最终最佳路径长度

Baseline： 在`berlin52.tsp`上的运行结果：

| Solver             | Length      | Time     |
|-------------------|------------|---------|
| nearest_neighbor   | 8980.9183  | 0.000s  |
| nn_best_start      | 8182.1916  | 0.023s  |
| greedy             | 9954.0627  | 0.001s  |
| ortools            | 7544.3659  | 30.275s |

### 后续工作

* 接 **LLM API** 自动生成更复杂策略
* 需对比更多 baseline（如 OR-Tools、LKH）


### 参考

* [TSPLib](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
    * 这个链接我打不开，下载的数据集来自：https://github.com/mastqe/tsplib.git
* [Google OR-Tools TSP](https://developers.google.com/optimization/routing/tsp)

---
