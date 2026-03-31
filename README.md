---

# TSP FunSearch Project
## FunSearch for the Traveling Salesman Problem

## 简介

本项目实现了一个 **FunSearch 风格的 TSP 优化算法**，结合经典最近邻（Nearest Neighbor）算法与简单进化搜索策略。
目标：通过自动调整启发式策略参数，寻找更短的旅行路径。

---

## 功能

* **数据读取**：TSPLib 格式 `.tsp` 文件 → 距离矩阵
* **Baseline**：Nearest Neighbor 算法（应该还需要增加其他baseline进行对比）
* **FunSearch 优化**：模拟 LLM 生成策略 + 进化搜索优化路径长度
* **实验对比**：显示 baseline 与优化后的路径长度

---

## 文件说明

| 文件              | 功能                              |
| --------------- | ------------------------------- |
| `tsp_loader.py` | 读取 TSPLib 数据并生成距离矩阵             |
| `baseline.py`   | 最近邻算法及路径长度计算                    |
| `funsearch.py`  | FunSearch 核心优化逻辑                |
| `main.py`       | 运行入口，展示 baseline 与 FunSearch 对比 |
| `data/`         | 存放 TSPLib 数据文件，如 `berlin52.tsp` |

---

## 运行方法

```bash
python main.py
```

运行后会显示：

* Nearest Neighbor 的路径长度
* 每轮 FunSearch 优化的结果
* 最终最佳路径长度

---

## 后续工作

* 接 **LLM API** 自动生成更复杂策略
* 需对比更多 baseline（如 OR-Tools、LKH）

---

## 参考

* [TSPLib](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
    * 这个链接我打不开，下载的数据集来自：https://github.com/mastqe/tsplib.git
* [Google OR-Tools TSP](https://developers.google.com/optimization/routing/tsp)

---
