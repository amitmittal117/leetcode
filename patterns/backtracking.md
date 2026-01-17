# Backtracking Pattern

## Core Concept
Explore all possibilities by making choices, then **undo** (backtrack) when a path doesn't lead to a solution. Think of it as building a decision tree.

---

## Template

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])  # found valid solution
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)      # make choice
            backtrack(path, choices) # explore
            path.pop()               # undo choice (backtrack)
```

---

## When to Use
- **Permutations** - All orderings of elements
- **Combinations** - All subsets of size k
- **Subsets** - All possible subsets (power set)
- **N-Queens** - Place pieces with constraints
- **Sudoku** - Fill grid satisfying rules
- **Word Search** - Find path in grid

---

## Key Problems

| Problem | Variant |
|---------|---------|
| [Permutations](../solutions/permutations.py) | All orderings |
| [Subsets](../solutions/subsets.py) | Power set |
| [Combination Sum](../solutions/combination-sum.py) | Target sum with reuse |
| [N-Queens](../solutions/n-queens.py) | Constraint satisfaction |
| [Word Search](../solutions/word-search.py) | Grid path finding |
| [Generate Parentheses](../solutions/generate-parentheses.py) | Valid combinations |
| [Letter Combinations](../solutions/letter-combinations-of-a-phone-number.py) | Cartesian product |

---

## Optimization Tips
1. **Prune early** - Skip invalid branches as soon as possible
2. **Sort first** - Can help with duplicate handling and pruning
3. **Use visited set** - For grid problems to avoid revisiting

---

## Complexity
- **Time:** O(k * n^k) where k = depth, n = branching factor
- **Space:** O(k) for recursion stack
