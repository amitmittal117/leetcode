# LeetCode Patterns Mind Map

A progression-based guide to mastering algorithm patterns.

---

## Pattern Progression

```
┌─────────────────────────────────────────────────────────────┐
│                    LEARNING PATH                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Binary Search ──► 2. Two Pointers ──► 3. Sliding Window │
│                                                             │
│  4. Linked List ──► 5. Stack/Queue ──► 6. DFS/BFS           │
│                              │              │               │
│                              ▼              ├──► 8. Backtrack│
│                         7. DP               │               │
│                                             ▼               │
│                         9. Greedy      10. Graph            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Pattern Index

| # | Pattern | Description | Files |
|---|---------|-------------|-------|
| 1 | [Binary Search](./binary-search.md) 🔍 | Eliminate half each iteration | 2 |
| 2 | [Two Pointers](./two-pointers.md) 👆 | Reduce O(n²) to O(n) | 2 |
| 3 | [Sliding Window](./sliding-window.md) 🪟 | Incremental window updates | 1 |
| 4 | [Linked List](./linked-list.md) 🔗 | Pointer manipulation | 3 |
| 5 | Stack 📚 | LIFO for matching/nesting | 1 |
| 6 | DFS/BFS 🌳 | Tree/graph traversal | 1 |
| 7 | [Dynamic Programming](./dynamic-programming.md) 📊 | Overlapping subproblems | 4 |
| 8 | Backtracking 🔄 | Explore all possibilities | 1 |

---

## Quick Reference

| Pattern | Template Snippet |
|---------|-----------------|
| Binary Search | `while left <= right: mid = (left+right)//2` |
| Two Pointers | `while left < right: # compare and move` |
| Sliding Window | `for right: expand; while invalid: shrink` |
| Linked List | `dummy = Node(0); dummy.next = head` |
| Stack | `if open: push; if close: pop and match` |
| DFS | `mark visited; for neighbors: recurse` |
| DP | `dp[i] = f(dp[i-1], ...)` |
| Backtracking | `choose; explore; unchoose` |

---

## Progress: 23 / 3056 files ✅



