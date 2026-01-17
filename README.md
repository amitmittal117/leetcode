# LeetCode Patterns & Solutions

[![Language](https://img.shields.io/badge/language-Python-orange.svg)](https://leetcode.com/problemset/all/)&nbsp;
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)&nbsp;

A progression-based guide to mastering algorithm patterns through [LeetCode](https://leetcode.com/problemset/all/) solutions.

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

| # | Pattern | Description | Detailed Guide |
|---|---------|-------------|----------------|
| 1 | Binary Search 🔍 | Eliminate half each iteration | [Guide](./patterns/binary-search.md) |
| 2 | Two Pointers 👆 | Reduce O(n²) to O(n) | [Guide](./patterns/two-pointers.md) |
| 3 | Sliding Window 🪟 | Incremental window updates | [Guide](./patterns/sliding-window.md) |
| 4 | Linked List 🔗 | Pointer manipulation | [Guide](./patterns/linked-list.md) |
| 5 | Stack 📚 | LIFO for matching/nesting | - |
| 6 | DFS/BFS 🌳 | Tree/graph traversal | - |
| 7 | Dynamic Programming 📊 | Overlapping subproblems | [Guide](./patterns/dynamic-programming.md) |
| 8 | Backtracking 🔄 | Explore all possibilities | - |

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

## Progress: 123 / 3056 files ✅

---

## Repository Structure

- [**solutions/**](./solutions/) - Comprehensive LeetCode solutions in Python.
- [**patterns/**](./patterns/) - Detailed algorithm pattern guides and mind maps.
- [**PROGRESS.md**](./patterns/PROGRESS.md) - Tracked history of processed problems.

---

## About
Solving Leetcode Solutions as I go. Each enhanced solution includes an **INTUITION** section explaining the technical "WHY" behind the logic.

---

## Commands Reference

| Command | What it does |
|---------|--------------|
| `Continue` | Process next batch of files |
| `Resume from progress tracker` | Pick up where we left off |
| `Create mind map: [Name]` | Create new company/topic mind map |
| `git push` | Upload progress to GitHub |
