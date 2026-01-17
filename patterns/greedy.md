# Greedy Pattern

## Core Concept
Make the **locally optimal choice** at each step, hoping it leads to a global optimum. Works when the problem has **optimal substructure** and **greedy choice property**.

---

## Template Approach

```python
def greedy_solution(items):
    # 1. Sort by some criteria (often key to greedy)
    items.sort(key=lambda x: x.some_property)
    
    result = 0
    for item in items:
        # 2. Make locally optimal choice
        if can_include(item):
            result += item.value
    
    return result
```

---

## When to Use
- **Interval Scheduling** - Max non-overlapping intervals
- **Activity Selection** - Choose most activities
- **Huffman Coding** - Optimal prefix codes
- **Fractional Knapsack** - Take fractions of items
- **Jump Game** - Reach the end with min jumps

---

## Key Problems

| Problem | Strategy |
|---------|----------|
| [Jump Game](../solutions/jump-game.py) | Track max reachable |
| [Gas Station](../solutions/gas-station.py) | Reset at deficit |
| [Assign Cookies](../solutions/assign-cookies.py) | Sort both, match smallest first |
| [Non-overlapping Intervals](../solutions/non-overlapping-intervals.py) | Sort by end time |
| [Merge Intervals](../solutions/merge-intervals.py) | Sort by start time |
| [Task Scheduler](../solutions/lemonade-change.py) | Process greedily |

---

## When NOT to Use
- **0/1 Knapsack** - Need DP (can't take fractions)
- **Longest Path** - Need DP or backtracking
- Problems without greedy choice property

---

## Complexity
- **Time:** Usually O(n log n) due to sorting
- **Space:** O(1) to O(n) depending on problem
