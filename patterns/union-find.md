# Union-Find (Disjoint Set Union) Pattern

## Core Concept
Efficiently track **connected components** in a graph. Supports two operations:
- **Find** - Which group does an element belong to?
- **Union** - Merge two groups together

---

## Template

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected
        # union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

---

## When to Use
- **Connected Components** - Count/find groups
- **Cycle Detection** - In undirected graphs
- **Kruskal's MST** - Minimum spanning tree
- **Account Merge** - Group related items
- **Dynamic Connectivity** - Edges added over time

---

## Key Problems

| Problem | Variant |
|---------|---------|
| [Number of Islands](../solutions/number-of-islands.py) | Grid connectivity |
| [Accounts Merge](../solutions/accounts-merge.py) | Email grouping |
| [Redundant Connection](../solutions/redundant-connection.py) | Cycle detection |
| [Number of Provinces](../solutions/friend-circles.py) | Graph components |
| [Longest Consecutive Sequence](../solutions/longest-consecutive-sequence.py) | Value connectivity |

---

## Optimizations
1. **Path Compression** - Flatten tree during find()
2. **Union by Rank** - Attach smaller tree under larger

---

## Complexity
- **Time:** O(α(n)) per operation (nearly O(1))
- **Space:** O(n) for parent/rank arrays
