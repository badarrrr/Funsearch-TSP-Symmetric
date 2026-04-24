"""
funsearch.py — LLM-guided heuristic search for TSP

FunSearch loop
--------------
1. Generate diverse initial population via LLM
2. Evaluate each heuristic on dist_matrix
3. Iteratively mutate top-k parents, keep improvements
4. Return best route, length, structured history, winning code

Design notes
------------
- LLM output sanitised before exec  (strips <think>, markdown fences, multi-line)
- Top-k parent sampling for population diversity
- Stagnation counter escalates mutation temperature automatically
- exec sandbox exposes only {np}  — no builtins, no dist_matrix in globals
- route converted to np.int32 ndarray before calling Numba route_length
"""

import re
import random
import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv

from baseline import route_length   # Numba JIT — requires np.int32 ndarray input

load_dotenv()

client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# ──────────────────────────────────────────────────────────────
# Heuristic code template
# LLM fills in {score_calculation}: one "score = ..." line.
# ──────────────────────────────────────────────────────────────

_TEMPLATE = """\
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
        next_city = int(np.argmin(scores))
        route.append(next_city)
        visited[next_city] = True
        current = next_city
    return route
"""

_DEFAULT_EXPR = "score = dist_matrix[current][j]"

_AVOID = (
    "Use ONLY: +, -, *, /, **, numeric literals, np.inf, "
    "dist_matrix[current][j], dist_matrix[j][current], dist_matrix[j][0]. "
    "Do NOT call min(), max(), sum(), len(), or any other function."
)

# Style hints ensure the initial population is diverse
_STYLE_HINTS = [
    "Use only the direct distance to the next city.",
    "Combine direct distance with a fraction of the return-to-depot distance.",
    "Apply a power < 1 to shrink large distances less aggressively.",
    "Apply a power > 1 to penalise distant cities more strongly.",
    "Blend forward and backward distance with asymmetric weights.",
    "Reward proximity to the depot (city 0) alongside direct distance.",
    "Use the ratio of direct distance to return-to-depot distance.",
    "Add a small perturbation scalar to diversify tie-breaking.",
    "Combine direct distance with the average of forward and backward costs.",
    "Use a logarithm-like transformation to flatten selection pressure.",
]


# ──────────────────────────────────────────────────────────────
# Internal helpers
# ──────────────────────────────────────────────────────────────

def _make_code(expr: str) -> str:
    return _TEMPLATE.format(score_calculation=expr)


def _default_code() -> str:
    return _make_code(_DEFAULT_EXPR)


def _clean_llm_output(raw: str) -> str:
    """
    Sanitise raw LLM text into a single valid 'score = ...' line.

    Strips:
      <think>...</think> blocks  (Qwen thinking mode)
      ```python ... ``` fences
      Leading/trailing whitespace and comment lines
    Ensures output starts with 'score ='.
    """
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL)
    raw = re.sub(r"```[a-zA-Z]*", "", raw).replace("```", "").strip()

    lines = [
        l.strip()
        for l in raw.splitlines()
        if l.strip() and not l.strip().startswith("#")
    ]

    if not lines:
        return _DEFAULT_EXPR

    expr = lines[0]
    if not expr.startswith("score"):
        expr = f"score = {expr}"
    return expr


def _call_llm(prompt: str, temperature: float = 0.8) -> str:
    response = client.chat.completions.create(
        model="qwen3-6b-flash",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120,
        temperature=temperature,
        extra_body={"enable_thinking": True},
    )
    return response.choices[0].message.content


# ──────────────────────────────────────────────────────────────
# Evaluation
# ──────────────────────────────────────────────────────────────

def evaluate_heuristic(code: str, dist_matrix: np.ndarray):
    """
    Execute heuristic code in a restricted sandbox and return (length, route).
    Returns (np.inf, None) on any failure.

    Converts route list → np.int32 ndarray before calling Numba route_length.
    """
    assert dist_matrix is not None, "dist_matrix must not be None"
    n = len(dist_matrix)

    try:
        local_vars: dict = {}
        exec(
            compile(code, "<heuristic>", "exec"),
            {"np": np},   # minimal sandbox — no builtins, no dist_matrix leak
            local_vars,
        )
        fn = local_vars.get("heuristic")
        if fn is None:
            raise ValueError("No 'heuristic' function defined")

        route_list = fn(dist_matrix)

        # Validate tour
        if (
            len(route_list) != n
            or len(set(route_list)) != n
            or not all(0 <= c < n for c in route_list)
        ):
            print(f"    [eval] Invalid tour  len={len(route_list)}  "
                  f"unique={len(set(route_list))}")
            return np.inf, None

        # Numba route_length requires int32 ndarray
        route_arr = np.array(route_list, dtype=np.int32)
        length    = float(route_length(route_arr, dist_matrix))
        return length, route_arr

    except Exception as e:
        print(f"    [eval] Error: {e}")
        return np.inf, None


# ──────────────────────────────────────────────────────────────
# LLM generation
# ──────────────────────────────────────────────────────────────

def generate_initial_heuristics(num: int) -> list:
    """Generate `num` diverse heuristic code strings via LLM."""
    heuristics = []

    for i in range(num):
        hint = _STYLE_HINTS[i % len(_STYLE_HINTS)]
        prompt = f"""
You are designing heuristic #{i + 1} for the Traveling Salesman Problem.
The heuristic selects the next unvisited city by scoring each candidate j.

Style directive: {hint}

Variables available inside the scoring loop:
  dist_matrix[current][j]  – distance from current city to candidate j
  dist_matrix[j][current]  – same (symmetric matrix)
  dist_matrix[j][0]        – distance from j back to depot (city 0)
  current                  – index of the current city (int)
  j                        – index of the candidate city (int)
  n                        – total number of cities (int)
  np                       – numpy module

{_AVOID}

Lower score = more preferred.
Output ONLY a single Python assignment line, exactly like:
  score = <expression>
No explanation, no markdown, no extra lines.
"""
        try:
            raw  = _call_llm(prompt, temperature=0.85)
            expr = _clean_llm_output(raw)
            print(f"  [init {i+1}/{num}] {expr}")
            heuristics.append(_make_code(expr))
        except Exception as e:
            print(f"  [init {i+1}] LLM error ({e}), using default")
            heuristics.append(_default_code())

    return heuristics


def mutate_heuristic(code: str, perf: float, n_cities: int, attempt: int = 0) -> str:
    """Ask the LLM to improve an existing heuristic score expression."""

    # Extract current score line for a concise prompt
    score_line = _DEFAULT_EXPR
    for line in code.splitlines():
        stripped = line.strip()
        if stripped.startswith("score =") and "np.inf" not in stripped:
            score_line = stripped
            break

    nudge = (
        "Try a structurally different expression."
        if attempt > 1 else
        "Make a targeted improvement to the existing expression."
    )

    prompt = f"""
The current TSP score calculation is:
  {score_line}

It achieved a tour length of {perf:.2f} on a {n_cities}-city instance. {nudge}

{_AVOID}

Output ONLY the new assignment line:
  score = <expression>
"""
    try:
        temp = min(0.75 + 0.1 * attempt, 1.2)
        raw  = _call_llm(prompt, temperature=temp)
        expr = _clean_llm_output(raw)
        print(f"  [mutate] {expr}")
        return _make_code(expr)
    except Exception as e:
        print(f"  [mutate] LLM error ({e}), keeping parent")
        return code


# ──────────────────────────────────────────────────────────────
# Main FunSearch loop
# ──────────────────────────────────────────────────────────────

def funsearch(
    dist_matrix: np.ndarray,
    iterations: int = 10,
    num_initial: int = 5,
    top_k: int = 3,
    stagnation_limit: int = 3,
):
    """
    LLM-guided heuristic evolution for TSP.

    Parameters
    ----------
    dist_matrix     : (n, n) float ndarray — must not be None
    iterations      : number of mutation steps
    num_initial     : initial population size
    top_k           : sample parent from top-k pool each iteration
    stagnation_limit: consecutive non-improvements before escalating temperature

    Returns
    -------
    best_route  : int32 ndarray
    best_length : float
    history     : list of {"iter", "best", "tried"} dicts
    best_code   : str
    """
    assert dist_matrix is not None, "funsearch requires a precomputed dist_matrix"
    n = len(dist_matrix)
    print(f"\n[funsearch] n={n}  iterations={iterations}  num_initial={num_initial}")

    # ── Phase 1: initial population ──────────────────────────
    print("[funsearch] Generating initial population...")
    codes = generate_initial_heuristics(num_initial)

    pool: list = []   # entries: (length, code, route_ndarray)
    for idx, code in enumerate(codes):
        length, route = evaluate_heuristic(code, dist_matrix)
        tag = f"{length:.2f}" if length != np.inf else "invalid"
        print(f"  [init eval {idx+1}/{num_initial}] {tag}")
        if length != np.inf:
            pool.append((length, code, route))

    # Fallback: plain nearest-neighbour if every initial heuristic fails
    if not pool:
        print("[funsearch] All initial heuristics failed — falling back to default NN")
        fallback = _default_code()
        length, route = evaluate_heuristic(fallback, dist_matrix)
        if length == np.inf:
            raise RuntimeError(
                "Default nearest-neighbour heuristic also failed. "
                "Check dist_matrix validity."
            )
        pool.append((length, fallback, route))

    pool.sort(key=lambda x: x[0])
    best_length, best_code, best_route = pool[0]
    print(f"[funsearch] Initial best: {best_length:.2f}")

    history    = [{"iter": 0, "best": best_length, "tried": best_length}]
    stagnation = 0

    # ── Phase 2: evolution ───────────────────────────────────
    for i in range(1, iterations + 1):
        print(f"\n[funsearch] Iter {i}/{iterations}  "
              f"best={best_length:.2f}  stagnation={stagnation}")

        # Sample parent from top-k for diversity
        k = min(top_k, len(pool))
        parent_length, parent_code, _ = random.choice(pool[:k])

        attempt      = min(stagnation, 3)
        mutated_code = mutate_heuristic(parent_code, parent_length, n, attempt=attempt)

        mut_length, mut_route = evaluate_heuristic(mutated_code, dist_matrix)

        if mut_length < best_length:
            best_length = mut_length
            best_code   = mutated_code
            best_route  = mut_route
            stagnation  = 0
            print(f"  ✅ Improved → {best_length:.2f}")

            pool.append((mut_length, mutated_code, mut_route))
            pool.sort(key=lambda x: x[0])
            pool = pool[:max(top_k * 2, 6)]   # keep pool bounded
        else:
            stagnation += 1
            tried_str = f"{mut_length:.2f}" if mut_length != np.inf else "invalid"
            print(f"  ❌ No improvement  tried={tried_str}")

        history.append({"iter": i, "best": best_length, "tried": mut_length})

    print(f"\n[funsearch] Done. Best length: {best_length:.2f}")
    return best_route, best_length, history, best_code