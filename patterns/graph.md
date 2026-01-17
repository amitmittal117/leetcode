# Graph Traversal Pattern

## Core Concept
Explore nodes and edges systematically using **BFS** (level-by-level) or **DFS** (depth-first).

---

## BFS Template (Shortest Path)

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    distance = 0
    
    while queue:
        for _ in range(len(queue)):  # process level
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        distance += 1
    return distance
```

## DFS Template (Explore All)

```python
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

---

## When to Use

| BFS | DFS |
|-----|-----|
| Shortest path (unweighted) | Detect cycles |
| Level-order traversal | Topological sort |
| Multi-source shortest path | Path existence |
| Finding connected components | All paths enumeration |

---

## Key Problems

| Problem | Pattern |
|---------|---------|
| [Number of Islands](../solutions/number-of-islands.py) | Grid DFS/BFS |
| [Course Schedule](../solutions/course-schedule.py) | Topological Sort |
| [Clone Graph](../solutions/clone-graph.py) | Graph copying |
| [Word Ladder](../solutions/open-the-lock.py) | BFS shortest path |
| [Pacific Atlantic Water Flow](../solutions/pacific-atlantic-water-flow.py) | Multi-source BFS |

---

## Complexity
- **Time:** O(V + E) for both BFS and DFS
- **Space:** O(V) for visited set + queue/stack
